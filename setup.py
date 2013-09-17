from setuptools import setup, find_packages

version = '0.2dev'

setup(name='br.jus.portaltransparencia',
    version=version,
    description="Cliente para consumir dados do Portal de " +
                "Transparencia do Judiciario Brasileiro",
    long_description=open("README.rst").read(),
    classifiers = [
        "Intended Audience :: Developers",
        "Intended Audience :: Telecommunications Industry",
        "Natural Language :: Portuguese (Brazilian)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='brasil brazil judiciario transparencia',
    author='Thiago Curvelo',
    author_email='tcurvelo@gmail.com',
    url='https://github.com/tcurvelo/br.jus.portaltransparencia',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['br'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    extras_require={
    },
    entry_points="""
    """,
)
