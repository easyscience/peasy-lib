---
icon: material/cog-box
---

# :material-cog-box: Installation & Setup

## Requirements

EasyPeasy is a cross-platform Python library compatible with
**Python 3.11 through 3.13**.
Make sure Python is installed on your system before proceeding with the
installation.

Below, we outline two installation methods: using **Pixi** (recommended for
ease of use) and the **classical approach** (for advanced users).

## Installing with Pixi <small>recommended</small> { #installing-with-pixi data-toc-label="Installing with Pixi" }

This section describes the most simple way to set up EasyDiffraction using
[Pixi](https://pixi.sh), an advanced package and environment manager for Python
and Conda-compatible packages.

It requires installing Pixi first, but then it automates the creation of an
isolated environment with all dependencies, which is especially useful for
non-expert Python users.

<!-- prettier-ignore-start -->

- Install Pixi by following the instructions on the
  [official Pixi Installation Guide](https://pixi.sh/latest/installation).
- Initialize a new Pixi project and navigate into it:
  ```bash
  pixi init easydiffraction
  cd easydiffraction
  ```
- Set the Python version for the Pixi environment (e.g., 3.14):
  ```bash
  pixi add python=3.14
  ```
- Add the GNU Scientific Library (GSL) dependency:
  ```bash
  pixi add gsl
  ```
- Add EasyDiffraction with the `visualization` extras:
  ```bash
  pixi add --pypi "easydiffraction[visualization]"
  ```
- Add a Pixi task to run EasyDiffraction commands easily:
  ```bash
  pixi task add easydiffraction "python -m easydiffraction"
  ```

<!-- prettier-ignore-end -->

## Classical Installation <small>advanced</small> { #classical-installation data-toc-label="Classical Installation" }

### Environment Setup <small>optional</small> { #environment-setup data-toc-label="Environment Setup" }

We recommend using a **virtual environment** to isolate dependencies and avoid
conflicts with system-wide packages. If any issues arise, you can simply delete
and recreate the environment.

#### Creating and Activating a Virtual Environment:

<!-- prettier-ignore-start -->

- Create a new virtual environment:
  ```bash
  python3 -m venv venv
  ```
- Activate the environment:

    === ":material-apple: macOS"
        ```bash
        . venv/bin/activate
        ```
    === ":material-linux: Linux"
        ```bash
        . venv/bin/activate
        ```
    === ":fontawesome-brands-windows: Windows"
        ```bash
        . venv/Scripts/activate      # Windows with Unix-like shells
        .\venv\Scripts\activate.bat  # Windows with CMD
        .\venv\Scripts\activate.ps1  # Windows with PowerShell
        ```

- The terminal should now show `(venv)`, indicating that the virtual environment
  is active.

<!-- prettier-ignore-end -->

#### Deactivating and Removing the Virtual Environment:

<!-- prettier-ignore-start -->

- Exit the environment:
  ```bash
  deactivate
  ```
- If this environment is no longer needed, delete it:

    === ":material-apple: macOS"
        ```bash
        rm -rf venv
        ```
    === ":material-linux: Linux"
        ```bash
        rm -rf venv
        ```
    === ":fontawesome-brands-windows: Windows"
        ```bash
        rmdir /s /q venv
        ```

<!-- prettier-ignore-end -->

### Installing from PyPI <small>recommended</small> { #from-pypi data-toc-label="Installing from PyPI" }

EasyDiffraction is available on **PyPI (Python Package Index)** and can be
installed using `pip`. We strongly recommend installing it within a virtual
environment, as described in the [Environment Setup](#environment-setup)
section.

We recommend installing the latest release of EasyDiffraction with the
`visualization` extras, which include optional dependencies used for simplified
visualization of charts and tables. This can be especially useful for running
the Jupyter Notebook examples. To do so, use the following command:

```bash
pip install 'easypeasy[visualization]'
```

If only the core functionality is needed, the library can be installed simply
with:

```bash
pip install easypeasy
```

To install a specific version of EasyDiffraction, e.g., 1.0.3:

```bash
pip install 'easypeasy==1.0.3'
```

To upgrade to the latest version:

```bash
pip install --upgrade easypeasy
```
To upgrade to the latest version and force reinstallation of all
dependencies (useful if files are corrupted):

```bash
pip install --upgrade --force-reinstall easypeasy
```

To check the installed version:

```bash
pip show easypeasy
```

### Installing from PyPI <small>alternative</small> { #from-github data-toc-label="Installing from GitHub" }

Installing unreleased versions is generally not recommended but may be useful
for testing.

To install EasyDiffraction from, e.g., the `develop` branch of GitHub:

```bash
pip install git+https://github.com/easyscience/diffraction-lib@develop
```

To include extra dependencies (e.g., visualization):

```bash
pip install 'easypeasy[visualization] @ git+https://github.com/easyscience/diffraction-lib@develop'
```

## How to Run Tutorials

EasyDiffraction includes a collection of **Jupyter Notebook examples** that
demonstrate key functionality. These tutorials serve as **step-by-step guides**
to help users understand the diffraction data analysis workflow.

They are available as **static HTML pages** in the
[:material-school: Tutorials](../tutorials/index.md) section. You can also run
them interactively in two ways:

- **Run Locally** – Download the notebook via the :material-download:
  **Download** button and run it on your computer.
- **Run Online** – Use the :google-colab: **Open in Google Colab** button to run
  the tutorial directly in your browser (no setup required).

!!! note

    You can also download all Jupyter notebooks at once as a zip archive from the
    [EasyDiffraction Releases](https://github.com/easyscience/diffraction-lib/releases/latest).

### Run Tutorials Locally

To run tutorials locally, install **Jupyter Notebook** or **JupyterLab**.

Below, we outline the steps to run the tutorials using either **Pixi** (recommended)
or the classical method (advanced users).

#### Running with Pixi <small>recommended</small> { #running-with-pixi data-toc-label="Running with Pixi" }

Here are the steps to follow using **JupyterLab** with Pixi:

- Navigate to your existing Pixi project, as described in the
  [Installing with Pixi](#installing-with-pixi) section.
- Add JupyterLab and the Pixi kernel for Jupyter:
  ```bash
  pixi add --pypi jupyterlab pixi-kernel
  ```
- Download all the EasyDiffraction tutorials to the `tutorials/` directory:
  ```bash
  pixi run easydiffraction download-all-tutorials
  ```
- Start JupyterLab in the `tutorials/` directory to access the notebooks:
  ```bash
  pixi run jupyter lab tutorials/
  ```
- Your web browser should open automatically. Click on one of the `*.ipynb`
  files and select the `Python (Pixi)` kernel to get started and select the
  tutorial you want to run.

#### Classical Approach <small>advanced</small> { #classical-approach data-toc-label="Classical Approach" }

Here are the steps to follow in the case of **Jupyter Notebook**:

- Install Jupyter Notebook and IPython kernel:
  ```bash
  pip install notebook ipykernel
  ```
- Add the virtual environment as a Jupyter kernel
  ```bash
  python -m ipykernel install --user --name=venv --display-name "EasyDiffraction Python kernel"
  ```
- Download all the EasyDiffraction tutorials to the `tutorials/` directory:
  ```bash
  python -m easydiffraction download-all-tutorials
  ```
- Launch the Jupyter Notebook server in the `tutorials/` directory:
  ```bash
  jupyter notebook tutorials/
  ```
- In your web browser, go to:
  ```bash
  http://localhost:8888/
  ```
- Open one of the `*.ipynb` files and select the `EasyDiffraction Python kernel`
  to get started.

### Run Tutorials via Google Colab

**Google Colab** lets you run Jupyter Notebooks in the cloud without any local
installation.

To use Google Colab:

- Ensure you have a **Google account**.
- Go to the **[:material-school: Tutorials](../tutorials/index.md)** section.
- Click the :google-colab: **Open in Google Colab** button on any tutorial.

This is the fastest way to start experimenting with EasyDiffraction, without
setting up Python on your system.
