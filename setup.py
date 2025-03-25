from setuptools import setup, find_packages

setup(
    name="jamal_batcher",
    version="1.0.1",
    packages=find_packages(),
    install_requires=[
        "paramiko",
        "psycopg2-binary",
        "python-dotenv",
        "setuptools"
    ],
    author="Norden",
    description="Remote access to stones' db",
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
)