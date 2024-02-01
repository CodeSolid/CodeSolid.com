# JohnLockwood.com 

This can be run as a codespace on GitHub, as a .devcontainer in VS Code (run using ```code .```), or using a virtual environment, as follows:

```
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r .devcontainer/packages.txt
```

To run or build the site locally, use ```./scripts/serve``` or ```./scripts/build```, respectively.

Note that the site must be built to the doc directory before a push.