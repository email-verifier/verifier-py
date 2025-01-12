import setuptools

install_requires = [
    'requests>=2.21.0',
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="verifier",
    version="1.0.0",
    author="Meet Chopra",
    author_email="meet@verifyright.co",
    description="Offical Library for VerifyRight",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/email-verifier/verifier-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
