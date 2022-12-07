# Build guidelines


In order to re-build the static homepage from the reStructuredText source files, you will
need to install the following Python packages:

```bash
pip install -U sphinx sphinx_bootstrap_theme sphinx_togglebutton
```

or, if it fails

```bash
python3 -m pip install -U sphinx sphinx_bootstrap_theme sphinx_togglebutton
```

## Linux

```
cd docs
make html
```

## Windows

```
cd docs
sphinx-build -b html source build/html
```
