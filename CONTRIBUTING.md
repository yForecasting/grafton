# Contributing

The developer guide is for anyone wanting to contribute directly to the grafton project. 


## Open an issue

grafton is an open source project maintained by [Vives AI lab](https://yforecasting.github.io/index). This is an open-source project we work on in our free time. We are open to new content and adding more features. If you have a bug or an idea, start by opening an issue. Try to make it as descriptive as possible. 

## Developing and contributing code

We would be delighted to have your contribution and look at your code. Here are a few guidelines we follow. Hopefully, these will ensure your contribution could quickly be added to the project. 

### Work locally

Most grafton users run their own local instances of grafton after install via pip. As grafton is a non-intrusive library we recommend developing against a local repository and ensuring you are 
able to add your contributions successfully on your local fork/repo. 

If you are developing against remote libraries or repositories - that's great! We'd love to hear how you're doing with it. In the meantime, before you open a pull request, deploy and test your contributions locally.

### Keep your fork in sync

grafton is usually updated on a weekly basis. Syncing your fork weekly ensures you are working on an updated version that will not break your pull request.  

### Rationalize your commits

Try to work on structured and well-defined contributions. If you are building a new feature try to build a unified feature block that can be easily reviewed and tested.

If you are fixing or patching changing existing code break changes into logical blocks which individually make sense and in aggregate solve a broader issue. 

### Test where it matters

1. Unit: Unit tests, including check tests, are stored in grafton/tests/. 
2. E2E: End-to-end tests will help us establish if the feature is in high readiness. They are not required for simple or straight forward features but will help us in evaluating the pull request.

#### Tests for new checks

When you add a new check, please write a test for it. 

#### Running tests

Continuous integration will run these tests either as pre-submits on pull requests and post-submits against main branch. Results will appear under [actions](https://github.com/yForecasting/grafton/actions).

To run tests locally use the following commands (install dev dependencies, run tests and compute tests coverage):
If you are using conda, create a new environment with Python 3.7.10 version:
```sh
conda create -n python37 --m python=3.7.10
conda activate python37
```
Then, we need pipenv installation and run the tests and coverage modules 
```sh
pip install pipenv
pipenv install --dev
pipenv run python -m coverage run -m pytest tests
```

### Build package locally
Change the version number on the file with your version : `<grafton>/grafton/version.py`
To build package locally run the following on `<grafton>` root folder:

```sh
pipenv run python setup.py sdist bdist_wheel
```
- This will create a `*.whl` package under a new folder named `dist`

To install package from local directory, update the release version value and run the installation:
```sh
RELEASE_VERSION='xxx'
pip install dist/grafton-${RELEASE_VERSION}-py3-none-any.whl
```

### Test the package
First verify you have the right version installed:
```sh
grafton --version
```
Then, optionally, you can run on a terraform file/directory with your success and failure test scenarios.

### Documentation is awesome

Contributing to the documentation is not mandatory but it will ensure people are aware of your important contribution. The best way to add documentation is by including suggestions to the the feature list. 

## Creating a pull-request

If a trivial fix such as a broken link, typo or grammar mistake, review the entire document for other potential mistakes. 
Try not to open multiple pull requests for small fixes in the same document.
Reference any issues related to your pull request, or issues that pull request may solve.
Comment on your own pull request where you believe something may need further explanation.
No need to assign explicit reviewers. We have maintainers reviewing contributions on a regular basis.
If your pull request is considered a "Work in progress" prefix the name with [WIP] or use the /hold command. This will prevent the pull request from being merged till the [WIP] or hold is lifted.
If your pull request isn't getting enough attention, don't hesitate to ping one of the maintainers to find additional reviewers.
