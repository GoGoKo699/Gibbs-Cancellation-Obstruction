#!/usr/bin/env python3
"""A construction-only temperature interval certificate.

Precontracts Taylor coefficients with the rational right inverse before
interval evaluation. This sharply reduces dependency inflation compared with
passing an interval beta directly to a dense matrix exponential. It does not
certify the rank of the separate 923-dimensional Gibbs evaluation minor.
"""
from __future__ import annotations
import argparse
import json
import math
import time
from fractions import Fraction
from certify_construction import (Model, arb, arb_mat, acb_mat, fmpq,
                                  frob, out, certified_hermitian_norm, HERE)


class TaylorBalance:
    def __init__(self, model, order=20, beta_max=arb('1/100')):
        self.model = model
        self.order = order
        self.beta_max = beta_max
        self.Ms, self.qs = [], []
        y = arb_mat(51, 1, model.y)
        power = model.I
        previous_A = None
        for k in range(order+1):
            A, f = model.balance(power)
            self.Ms.append((A*model.R)/math.factorial(k))
            q = f/math.factorial(k)
            if k:
                q += (previous_A*y)/(64*math.factorial(k-1))
            self.qs.append(q)
            previous_A = A
            power = (-model.H*power)/64
        # x_lin=t*y/64: the highest term has degree order+1.
        self.qs.append((previous_A*y)/(64*math.factorial(order)))
        self.hnorm = certified_hermitian_norm(model.H)
        z = beta_max*self.hnorm
        self.tail = (arb(32).sqrt()*z.exp()*z**(order+1)
                     /math.factorial(order+1)).upper()
        self.Bnorms = [frob(B).upper() for B in model.Bs]
        self.Rcols = [sum((abs(model.R[a, j]) for a in range(51)), arb(0)).upper()
                      for j in range(31)]
        self.yone = sum(abs(y) for y in model.y)

    @staticmethod
    def horner(coefficients, t):
        result = coefficients[-1]
        for value in reversed(coefficients[:-1]):
            result = result*t+value
        return result

    def certify(self, beta):
        m = self.model
        t = 64*beta
        M = self.horner(self.Ms, t)
        q = self.horner(self.qs, t)
        # Each delta_a has induced HS norm <=1. D0 has norm64.
        # These independent entrywise radii cover the common exponential tail.
        for i in range(31):
            for j in range(31):
                radius = (self.Bnorms[i]*self.Rcols[j]*self.tail).upper()
                M[i, j] += arb(0, radius)
            radius = (self.Bnorms[i]*(64+self.beta_max*self.yone)*self.tail).upper()
            q[i, 0] += arb(0, radius)
        correction = M.solve(-q, algorithm='precond')
        x = arb_mat(51, 1, [beta*y for y in m.y])+m.R*correction
        result, bounds = m.coefficient_bounds(x)
        inverse = M.solve(arb_mat([[int(i == j) for j in range(31)] for i in range(31)]),
                          algorithm='precond')
        if not all(inverse[i, j].is_finite() for i in range(31) for j in range(31)):
            raise ArithmeticError('The balance inverse was not certified finite.')
        result.update({'beta_ball': out(beta),
                       'balance_inverse_frobenius_upper': out(frob(inverse).upper())})
        # All coefficient balls are kept, so positivity may be independently
        # rechecked without reconstructing the Taylor coefficient contraction.
        return result, bounds


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--beta-max', default='1/100')
    parser.add_argument('--cells', type=int, default=128)
    parser.add_argument('--order', type=int, default=20)
    parser.add_argument('--precision', type=int, default=256)
    parser.add_argument('--output', default='construction_interval_certificate.json')
    args = parser.parse_args()
    start = time.time()
    model = Model(args.precision)
    bmax = arb(args.beta_max)
    taylor = TaylorBalance(model, args.order, bmax)
    records = []
    passed = True
    exact_max = Fraction(args.beta_max)
    for j in range(args.cells):
        midpoint = bmax*arb(fmpq(2*j+1, 2*args.cells))
        radius = (bmax/(2*args.cells)).upper()
        beta = arb(midpoint, radius)
        exact_lower = exact_max*j/args.cells
        exact_upper = exact_max*(j+1)/args.cells
        if not beta.contains(arb(fmpq(exact_lower.numerator, exact_lower.denominator))):
            raise ArithmeticError('The beta ball does not contain the exact lower endpoint.')
        if not beta.contains(arb(fmpq(exact_upper.numerator, exact_upper.denominator))):
            raise ArithmeticError('The beta ball does not contain the exact upper endpoint.')
        try:
            r, _ = taylor.certify(beta)
        except (ZeroDivisionError, ArithmeticError) as error:
            r = {'beta_ball': out(beta), 'passed': False,
                 'failure': type(error).__name__+': '+str(error)}
        r['cell'] = j
        r['beta_lower_rational'] = str(exact_lower)
        r['beta_upper_rational'] = str(exact_upper)
        records.append(r)
        print(json.dumps({k:v for k,v in r.items() if k != 'coefficients'}), flush=True)
        if not r['passed']:
            passed = False
            break
    output = {
        'scope': 'Construction and coercivity only; not a Gibbs evaluation-rank interval.',
        'beta_max': args.beta_max, 'cells': args.cells, 'taylor_order': args.order,
        'precision_bits': args.precision, 'passed': passed,
        'exp_tail_hilbert_schmidt_upper': out(taylor.tail),
        'hamiltonian_norm_upper': out(taylor.hnorm), 'records': records,
        'nodes': model.nodes, 'right_inverse_denominator': model.r_den,
        'right_inverse_numerators': model.r_nums,
        'elapsed_seconds': time.time()-start,
    }
    (HERE/args.output).write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k not in
                    {'records','nodes','right_inverse_numerators'}}), flush=True)


if __name__ == '__main__':
    main()
