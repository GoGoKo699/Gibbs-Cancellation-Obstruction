#!/usr/bin/env python3
"""Check conservative publication numbers against the stored ball certificates."""
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from flint import arb, ctx

HERE = Path(__file__).resolve().parent
ctx.prec = 256


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def point(filename, lower, upper, normalized):
    data = json.loads((HERE/filename).read_text())
    require(data['passed'], filename+' did not pass')
    for key, value in lower.items():
        require(arb(data[key]) > arb(value), filename+' lower bound '+key)
    for key, value in upper.items():
        require(arb(data[key]) < arb(value), filename+' upper bound '+key)
    delta = Fraction(lower['coercivity_lower'])
    eta = Fraction(lower['eta_max_for_error_bound'])
    slope = Fraction(upper['half_trace_error_slope_upper'])
    strength = Fraction(upper['generator_norm_for_eta_le_one_upper'])
    require(delta/(strength*slope) >= Fraction(normalized['gap_coefficient']),
            filename+' normalized gap coefficient')
    require(Fraction(normalized['epsilon_max']) <= eta*slope,
            filename+' normalized error range')
    return {'certificate': filename, 'lower_bounds': lower, 'upper_bounds': upper,
            'normalized_strength_one': normalized}


def main():
    points = [
        point('construction_beta003_certificate.json', {
            'cp_margin_lower': '0.7234', 'coercivity_lower': '13.900',
            'eta_max_for_error_bound': '0.000548',
        }, {
            'dissipator_norm_upper': '75.580',
            'drift_hilbert_schmidt_upper': '0.014963',
            'half_trace_error_slope_upper': '1.022',
            'generator_norm_for_eta_le_one_upper': '142.470',
        }, {'gap_coefficient': '0.0954', 'epsilon_max': '0.00056'}),
        point('construction_beta001_certificate.json', {
            'cp_margin_lower': '0.2019', 'coercivity_lower': '8.859',
            'eta_max_for_error_bound': '0.000205',
        }, {
            'dissipator_norm_upper': '102.952',
            'drift_hilbert_schmidt_upper': '0.174897',
            'half_trace_error_slope_upper': '23.411',
            'generator_norm_for_eta_le_one_upper': '169.843',
        }, {'gap_coefficient': '0.0022', 'epsilon_max': '0.00479'}),
    ]
    interval = json.loads((HERE/'construction_interval_certificate.json').read_text())
    require(interval['passed'], 'The interval certificate did not pass.')
    require(interval['cells'] == 128 and len(interval['records']) == 128,
            'The interval does not have the expected 128 cells.')
    for i, cell in enumerate(interval['records']):
        require(cell['passed'], 'A cell failed.')
        require(Fraction(cell['beta_lower_rational']) == Fraction(i, 12800),
                'Incorrect lower cell endpoint.')
        require(Fraction(cell['beta_upper_rational']) == Fraction(i+1, 12800),
                'Incorrect upper cell endpoint.')
        require(arb(cell['cp_margin_lower']) > arb('0.0512'), 'Uniform positivity bound.')
        require(arb(cell['coercivity_lower']) > arb('4.12'), 'Uniform coercivity bound.')
        require(arb(cell['dissipator_norm_upper']) < arb('109.645'), 'Uniform norm bound.')
        require(arb(cell['balance_inverse_frobenius_upper']).is_finite(),
                'Nonfinite inverse norm enclosure.')
    names = ['README.md', 'requirements.txt', 'hamiltonian.json', 'design_witness.json',
             'certify_construction.py', 'certify_interval.py', 'make_summary.py',
             'construction_beta003_certificate.json', 'construction_beta001_certificate.json',
             'construction_interval_certificate.json']
    output = {
        'scope': 'Constructive certificates; the continuous interval is not a Gibbs-rank certificate.',
        'point_bounds': points,
        'interval_bounds': {'beta_min': '0', 'beta_max': '1/100', 'cells': 128,
                            'cp_margin_lower': '0.0512', 'coercivity_lower': '4.12',
                            'dissipator_norm_upper': '109.645'},
        'dependencies': {'Python': '3', 'NumPy': '>=1.23', 'python-flint': '0.9.0'},
        'precision_bits': 256,
        'checks_passed': True,
        'sha256': {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in names},
    }
    (HERE/'summary.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k != 'sha256'}, indent=2))


if __name__ == '__main__':
    main()
