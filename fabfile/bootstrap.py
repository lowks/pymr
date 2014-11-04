from fabric.api import local, task, execute


@task(default=True)
def all():
    execute(install_venv)
    execute(create_venv)
    execute(install_requirements)


@task
def install_venv():
    """
    installs virtualenv in the currently activated python environment
    """
    cmd = 'pip install virtualenv'
    local(cmd)


@task
def create_venv():
    """
    creates a new virtualenv (.pymr) in the current directory
    """
    cmd = 'virtualenv .pymr'
    local(cmd)


@task
def install_requirements():
    """
    installs requirements.txt in the .pyrm virtualenv
    """
    cmd = '. .pymr/bin/activate && '
    cmd += 'pip install -r requirements.txt'
    local(cmd)