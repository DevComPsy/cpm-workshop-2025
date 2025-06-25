# WORKSHOP: theory-driven computational modeling in computational psychiatry with `cpm`

## Preparations

### Installing `cpm`

To install the `cpm` package, you can use the following command in your terminal:

```bash
pip install git+https://github.com/DevComPsy/cpm.git
```

Or alternatively, you can clone the repository and install it locally:

```bash
git clone https://github.com/DevComPsy/cpm.git
cd cpm
pip install -e .
```

### Installing dependencies

There is no need to install any additional dependencies, as the required should be installed alongside `cpm`. However, if you want a more comprehensive environment, I recommend you install either [Spyder](https://www.spyder-ide.org) or [JupyterLab](https://jupyter.org/), or use your favorite IDE.

### Installing `cpm` via Anaconda

If you prefer to use Anaconda, we recommend you create a new environment and install `cpm` there. You can do this with the following commands:

```bash
conda create -n cpm python=3.12.4
conda activate cpm
pip install git+https://github.com/DevComPsy/cpm.git
```

### Installing `cpm` in JupyterLab or Google Colab

If you want to use `cpm` in JupyterLab or Google Colab, you can install it directly in the notebook by running the following command in a code cell:

```python
!pip install git+https://github.com/DevComPsy/cpm.git
```
