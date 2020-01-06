import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-package",
    version="1.0.0",
    author="Example Author",
    author_email="example@example.com",
    description="Does cool stuff.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/example/example",
    packages=['example_package'],
    package_data={'example_package': ['data/']},
    keywords=['parser', 'file-parser',
              'packages', 'example', 'numbers'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    entry_points={
        'console_scripts': [
            'parser=example_package.parser:main'
        ]
    },
    python_requires='>=3.6',
)
