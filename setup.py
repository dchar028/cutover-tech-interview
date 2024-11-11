from setuptools import setup, find_packages

setup(
    name="project_name",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "redis",
        "python-dotenv"
    ],
    entry_points={
        'console_scripts': [
            'run-project=project_name.main:main'
        ]
    },
)
