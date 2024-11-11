from setuptools import setup, find_packages

# Read the requirements.txt file
def parse_requirements(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()

setup(
    name="top_track_in_space",
    version="1.0",
    packages=find_packages(),
    install_requires=parse_requirements("requirements.txt"),  # Dynamically load requirements
    entry_points={
        'console_scripts': [
            'top-track-in-space=top_track_in_space.main:main'
        ]
    },
)
