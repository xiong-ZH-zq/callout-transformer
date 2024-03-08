import pathlib
import setuptools

setuptools.setup(
    name="callout-transformer",
    version="0.1.0",
    description="A simple markdown admonition transformer",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="xzqbear",
    author_email="xzqbear@outlook.com",
    license="MIT License",
    project_urls={
        "Source": "https://github.com/xiong-ZH-zq/callout-transformer",
        "Documentation": "https://github.com/xiong-ZH-zq/callout-transformer/blob/main/README.md"
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.10"
    ],
    python_requires=">=3.9",
    install_requires=["markdown"],
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={"console_scripts": ["callout_transformer = callout_transformer.cli:main"]},
)