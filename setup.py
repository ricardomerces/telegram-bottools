import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bottools",
    version="0.1.0",
    author="Ricardo Merces",
    author_email="ricardo.merces@gmail.com",
    description="Tools for Telegram Bots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ricardomerces/telegram-bottools.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['requests>=2.20', 'lxml>=4.5']
)