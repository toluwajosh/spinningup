import sys
from os.path import join

from setuptools import setup

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, (
    "The Spinning Up repo is designed to work with Python 3.6 and greater."
    + "Please install it before proceeding."
)

with open(join("spinup", "version.py")) as version_file:
    exec(version_file.read())

setup(
    name="spinup",
    py_modules=["spinup"],
    version=__version__,  #'0.1',
    install_requires=[
        "cloudpickle",
        "gym[atari,box2d,classic_control]",  # OR
        # 'gymnasium[atari,box2d,classic_control]', # drop-in replacement for gym
        "ipython",
        "joblib",
        "matplotlib",
        "numpy",
        "pandas",
        "pytest",
        "psutil",
        "scipy",
        "seaborn",
        "tensorflow",
        "tqdm"
        # 'mpi4py',
        # 'torch==1.13.1',
    ],
    description="Teaching tools for introducing people to deep RL.",
    author="Joshua Achiam",
)
