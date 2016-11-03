from invoke import task


@task
def create_requirements(c):
    c.run('pip freeze > requirements.txt')


@task(pre=[create_requirements])
def build(c):
    print('build finished')
