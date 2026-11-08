#!/usr/bin/env python3
"""Run the finite and interval certificates; retain actual reports and logs."""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path,
                        default=ROOT / 'verification' / 'local-output')
    args = parser.parse_args()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    inputs = [ROOT / 'verification' / 'data' / 'hamiltonian.json',
              ROOT / 'verification' / 'gap' / 'data' / 'hamiltonian.json',
              ROOT / 'verification' / 'construction' / 'hamiltonian.json']
    values = [json.loads(p.read_text()) for p in inputs]
    if any(v != values[0] for v in values[1:]):
        raise RuntimeError('Hamiltonian inputs disagree')
    commands = [
        ('exact', ['verification/exact_certificate.py']),
        ('ground-thermal', ['verification/ground-thermal/certify_ground_thermal.py']),
        ('gap-beta003', ['verification/gap/verify_gap_bound.py', '--beta', '3/1000']),
        ('gap-beta01', ['verification/gap/verify_gap_bound.py', '--beta', '1/100']),
        ('construction-beta003', ['verification/construction/certify_construction.py', '--beta', '3/1000']),
        ('construction-beta01', ['verification/construction/certify_construction.py', '--beta', '1/100']),
        ('construction-interval', ['verification/construction/certify_interval.py', '--cells', '128']),
    ]
    source_files = [p for p in ROOT.rglob('*') if p.is_file()
                    and not any(x in p.parts for x in ('.git', '__pycache__', '.venv', 'local-output'))
                    and output not in p.parents]
    source_hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in sorted(source_files)}
    report = {
        'status': 'running', 'python': sys.version,
        'packages': {name: importlib.metadata.version(name)
                     for name in ['numpy', 'sympy', 'python-flint']},
        'source_sha256': source_hashes, 'checks': [],
    }
    environment = dict(os.environ)
    environment.setdefault('OPENBLAS_NUM_THREADS', '1')
    start = time.monotonic()
    try:
        for name, arguments in commands:
            target = output / (name + '.json')
            command = [sys.executable, *arguments]
            if name != 'exact':
                command += ['--output', str(target)]
            print(f'Running {name}', flush=True)
            began = time.monotonic()
            result = subprocess.run(command, cwd=ROOT, env=environment,
                                    text=True, capture_output=True)
            (output / (name + '.log')).write_text(result.stdout + result.stderr)
            if result.returncode:
                raise RuntimeError(f'{name} exited {result.returncode}; inspect {name}.log')
            if name == 'exact':
                target.write_text(result.stdout)
            payload = json.loads(target.read_text())
            if name.startswith('construction') and payload.get('passed') is not True:
                raise RuntimeError(f'{name} did not certify every required bound')
            if name.startswith('gap') and payload.get('inverse_certified') is not True:
                raise RuntimeError(f'{name} did not certify its inverse')
            if name == 'ground-thermal':
                required = {
                    'all_32_energy_balls_disjoint',
                    'normalized_ground_eigenvector_enclosed',
                    'all_nine_ground_marginals_positive_definite',
                    'mu_and_ratio_minimizing_supports_certified',
                    'thermal_crossing_brackets_certified',
                    'all_four_population_forms_strictly_negative',
                }
                accepted = payload.get('accepted_checks', {})
                if set(accepted) != required or any(value is not True for value in accepted.values()):
                    raise RuntimeError('ground-thermal did not certify every required inequality')
                if payload.get('hamiltonian_sha256') != source_hashes['verification/data/hamiltonian.json']:
                    raise RuntimeError('ground-thermal used an unexpected Hamiltonian input')
            report['checks'].append({'name': name, 'status': 'pass',
                                     'command': command[1:],
                                     'seconds': time.monotonic() - began,
                                     'report_sha256': hashlib.sha256(target.read_bytes()).hexdigest()})
        report['status'] = 'pass'
    except Exception as error:
        report['status'] = 'fail'
        report['error'] = str(error)
        raise
    finally:
        report['seconds'] = time.monotonic() - start
        (output / 'verification-report.json').write_text(json.dumps(report, indent=2) + '\n')
    print(f'All {len(commands)} certificate checks passed. Reports: {output}', flush=True)


if __name__ == '__main__':
    main()
