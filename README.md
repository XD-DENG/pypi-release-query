# Query for the Latest Release of Python Packages

This mini project is to provide a tool to query for the latest release of Python packages.

It may be helpful when your project is broken due to some dependency update breaks backward
compatibility or conflicts with other packages in you dependencies.

The result is sorted using *package upload time* on PyPi (latest release first). By comparing
with your build/test history, you may identify which package is more likely to have led to
the build/test failures.


## Usage

1. List the packages you would like to check in a file, say `packages_to_check.txt`, in the working dir.

    You can run `pip freeze > packages_to_check.txt` to prepare it as well.
    
    Each row inside this file should be in format `<package name>` or `<package name>==<version>`

2. Run `python main.py packages_to_check.txt`.

## Note

- The version and upload date returned here are the latest information on PyPi,
    rather than the version in your environment.
    
## Scrrenshot

![screenshot_1](https://raw.githubusercontent.com/XD-DENG/pypi-release-query/master/screenshots/screenshot-1.png)