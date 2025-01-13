import sys ## The sys module is used for interacting with the Python runtime environment. Here it’s used to exit the process if certain conditions are met.

from setuptools import setup ## This is a Python tool to help package and distribute Python projects. The setup function from setuptools is used to define the package metadata, dependencies, and other configurations.

from setuptools.command.bdist_egg import bdist_egg ## bdist_egg is a command in setuptools for creating a distribution in the .egg format, which was an older distribution format for Python packages. .egg is now largely deprecated, but this setup script customizes its behavior.


class bdist_egg_disabled(bdist_egg): ## The bdist_egg_disabled class inherits from bdist_egg and overrides the run method. This is done to disable the .egg building behavior entirely when the bdist_egg command is called.
    """Disabled version of bdist_egg

    Prevents setup.py install from performing setuptools' default easy_install,
    which it should never ever do.
    """

    def run(self):
        sys.exit(
            "Aborting implicit building of eggs."
            "Use `pip install .` to install from source."
        )


cmdclass = {
    "bdist_egg": bdist_egg if "bdist_egg" in sys.argv else bdist_egg_disabled,
} ## If the bdist_egg command is in the command-line arguments (sys.argv), the original bdist_egg class is used. Otherwise, the bdist_egg_disabled class is used, effectively disabling .egg distribution by default.

with open("README.md") as f:
    readme = f.read() ## This block reads the contents of the README.md file, which will later be used as the long description for the package.

setup(
    name="chartpress",
    version="2.2.1.dev",
    py_modules=["chartpress"], ## Specifies the Python modules to be included in the package. In this case, there’s just one module called chartpress.
    cmdclass=cmdclass,
    entry_points={
        "console_scripts": [
            "chartpress = chartpress:main",
        ],
    }, ## Defines the entry points for the package. In this case, it adds a command-line script called chartpress, which runs the main function from the chartpress module.
    description="ChartPress: render and publish helm charts and images",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Jupyter Development Team",
    author_email="jupyter@googlegroups.com",
    url="https://github.com/jupyterhub/chartpress",
    license="BSD",
    platforms="Linux, Mac OS X",
    keywords=["helm", "kubernetes"],
    python_requires=">=3.7", ## Specifies the minimum required Python version (3.7 or higher).
    install_requires=[
        "ruamel.yaml>=0.15.44",
        # Bug in 5.0.0: https://github.com/docker/docker-py/pull/2844
        "docker>=3.2.0,!=5.0.0",
    ], ## A list of dependencies that the package requires. For this package, it requires ruamel.yaml and docker.
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
