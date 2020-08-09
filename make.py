from subprocess import run
from typing import List
from pathlib import Path


def stale(input_file: str, files_to_compare: List[str] = None) -> bool:
    target = Path(input_file)
    if not target.exists():
        return True
    for file in files_to_compare or []:
        source = Path(file)
        if source.stat().st_mtime > target.stat().st_mtime:
            return True
    return False


if stale('env/bin/pip-compile'):
    run(['env/bin/pip', 'install', 'pip-tools'])

if stale('env/bin/pip-compile'):
    run(['env/bin/pip', 'install', 'pytest-cov'])

if stale('env/bin/pip-compile'):
    run(['env/bin/pip', 'install', 'pytest-mock'])

if stale('requirements-dev.txt', ['requirements-dev.in']):
    run(['env/bin/pip-compile', 'requirements-dev.in'])


if stale('env/ready', ['requirements-dev.txt']):
    run(['env/bin/pip', 'install', '-r', 'requirements-dev.txt'])
    Path('env/ready').touch()
