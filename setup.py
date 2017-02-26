from setuptools import setup, find_packages

setup(
    name='prejus',
    version='0.1',
    description='Cliente para consumir dados do Portal de ' +
                'Transparência do Judiciário Brasileiro',
    long_description=open("README.rst").read(),
    author='Thiago Curvelo',
    author_email='tcurvelo@gmail.com',
    url='https://github.com/tcurvelo/prejus',
    py_modules=['prejus'],
    install_requires=[
        'setuptools',
        'requests',
    ],
    entry_points="""
    """,
)
