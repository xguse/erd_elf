"""Install setup."""
import setuptools

setuptools.setup(
    name="erd_elf",
    version="0.0.1",
    url="git@github.com:xguse/erd_elf.git",

    author="Gus Dunn",
    author_email="w.gus.dunn@gmail.com",

    description="Script to draw Entity-Relationship Diagrams from simple definition files.",
    # long_description=open('README.rst').read(),

    packages=setuptools.find_packages('src'),
    package_dir={"": "src"},

    package_data={
        # Include any *.yaml files found in the 'configs' subdirectory
        # of the 'mypkg' package, also:
        'erd_elf': ['configs/*.yaml'],
    },

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    entry_points={
    "console_scripts": [
        "erd_elf = erd_elf.cli.main:run",
        ]
    },
)
