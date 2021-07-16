#!/usr/bin/env python3
'''
Dafault: create wheel
'''
import glob
from doit.tools import create_folder

DOIT_CONFIG = {'default_tasks': ['all']}


def task_gitclean():
    """Clean all generated files not tracked by GIT."""
    return {
            'actions': ['git clean -xdf'],
           }


def task_html():
    """Make HTML documentationi."""
    return {
            'actions': ['sphinx-build -M html docs build'],
           }


def task_test():
    """Preform tests."""
    yield {'actions': ['coverage run -m unittest -v'], 'name': "run"}
    yield {'actions': ['coverage report'], 'verbosity': 2, 'name': "report"}


def task_pot():
    """Re-create .pot ."""
    return {
            'actions': ['pybabel extract -o DateTime.pot AppBase'],
            'file_dep': glob.glob('AppBase/*.py'),
            'targets': ['DateTime.pot'],
           }


def task_po():
    """Update translations."""
    return {
            'actions': ['pybabel update -D DateTime -d po -i DateTime.pot'],
            'file_dep': ['DateTime.pot'],
            'targets': ['po/ru/LC_MESSAGES/DateTime.po'],
           }


def task_mo():
    """Compile translations."""
    return {
            'actions': [
                (create_folder, ['AppBase/ru/LC_MESSAGES']),
                'pybabel compile -D DateTime -l ru -i po/ru/LC_MESSAGES/DateTime.po -d AppBase'
                       ],
            'file_dep': ['po/ru/LC_MESSAGES/DateTime.po'],
            'targets': ['AppBase/ru/LC_MESSAGES/DateTime.mo'],
           }


def task_sdist():
    """Create source distribution."""
    return {
            'actions': ['python -m build -s'],
            'task_dep': ['gitclean'],
           }


def task_wheel():
    """Create binary wheel distribution."""
    return {
            'actions': ['python -m build -w'],
            'task_dep': ['mo'],
           }


def task_app():
    """Run application."""
    return {
            'actions': ['python -m AppBase'],
            'task_dep': ['mo'],
           }


def task_style():
    """Check style against flake8."""
    return {
            'actions': ['flake8 AppBase']
           }


def task_docstyle():
    """Check docstrings against pydocstyle."""
    return {
            'actions': ['pydocstyle AppBase']
           }


def task_check():
    """Perform all checks."""
    return {
            'actions': None,
            'task_dep': ['style', 'docstyle', 'test']
           }


def task_all():
    """Perform all build task."""
    return {
            'actions': None,
            'task_dep': ['check', 'html', 'wheel', 'req']
           }


def task_req():
    """Try to calculate runtime requirements."""
    return {
            'actions': ['pymin_reqs -d AppBase'],
            'verbosity': 2
           }


def task_buildreq():
    """Try to calculate build requirements."""
    return {
            'actions': ['python BuildReq.py doit all'],
            'task_dep': ['gitclean']
           }


def task_publish():
    """Publish distros on test.pypi.org"""
    return {
            'task_dep': ['sdist', 'wheel'],
            'actions': ['twine upload -u __token__ --repository testpypi dist/*'],
            'verbosity': 2
           }
