from invoke import task


@task
def create_requirements(c):
    c.run('pip freeze > requirements.txt')


@task
def collectstatic(c):
    c.run('./manage.py collectstatic')


@task(pre=[create_requirements, collectstatic])
def build(c):
    print('build finished')
