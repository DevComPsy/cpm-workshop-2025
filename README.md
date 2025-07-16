# WORKSHOP: theory-driven computational modeling in computational psychiatry with `cpm`

## Preparations

Please make sure to have a completely set-up python environment. If you are new to python, we recommend you check out the [Python documentation](https://docs.python.org/3/tutorial/index.html) or [Anaconda](https://www.anaconda.com/docs/getting-started/getting-started) for a more comprehensive guide.

However, we recommend you simply use Google Colab, which is a free Jupyter notebook environment that runs in the cloud and requires no setup. You can access it [here](https://colab.research.google.com/). The advantage of using Google Colab is that it comes with many pre-installed packages, and you can install `cpm` by simply including an extra line at the beginning of your notebook, see below.

### Installing `cpm`

To install the `cpm` package, you can use the following command in your terminal:

```bash
pip install cpm-toolbox
```

### Installing dependencies

There is no need to install any additional dependencies, as the required should be installed alongside `cpm`.

### Installing `cpm` via Anaconda

If you prefer to use Anaconda, I recommend you create a new environment and install `cpm` there. You can do this with the following commands:

```bash
conda create -n cpm python=3.12.4
conda activate cpm
pip install cpm-toolbox
```

### Installing `cpm` in JupyterLab or Google Colab

If you want to use `cpm` in JupyterLab or Google Colab, you can install it directly in the notebook by running the following command in a code cell:

```python
!pip install git+https://github.com/DevComPsy/cpm.git
```

## Running the workshop

To run the workshop, you can either clone the repository or download the files directly from GitHub.
The exercises are designed to be run in a Jupyter notebook, but you can also run them in any Python environment that supports the `cpm` package.
Uncompleted exercises are in the `exercises` folder, and completed exercises are in the `solutions` folder.

### Jupyter Notebook Exercises

Exercise 1: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lenarddome/cpm-workshop-2025/blob/main/exercises/01-model-building.ipynb)
Exercise 2: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lenarddome/cpm-workshop-2025/blob/main/exercises/02-model-parameter-recovery.ipynb)
Exercise 3: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]()
