from fabric.api import local, task


BANNER = """

    ____     __  __   ____ ___     _____
   / __ \   / / / /  / __ `__ \   / ___/
  / /_/ /  / /_/ /  / / / / / /  / /
 / .___/   \__, /  /_/ /_/ /_/  /_/
/_/       /____/

"""


@task
def setup_env():
    local('mkdir -p ~/.virtual_envs')
    local('virtualenv .pymr')
    local('. ./.pymr/bin/activate && pip install -r requirements.txt')


@task
def flake8():
    local('flake8 --config .flake8rc *.py **/*.py --verbose')


@task
def unit_test():
    local('nosetests --verbose')


@task
def test():
    print(BANNER)
    flake8()
    unit_test()


@task
def bump_patch():
    local('bumpversion patch')


@task
def bump_minor():
    local('bumpversion minor')


@task
def bump_major():
    local('bumpversion major')


@task
def pypi_register():
    local('python setup.py register')


@task
def pypi_upload():
    local('python setup.py bdist_wheel upload')
