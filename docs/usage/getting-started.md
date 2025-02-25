# Getting started

## Importing EasyPeasy

To start using EasyPeasy, first import the package in your Python
script or Jupyter Notebook:
```python
import easypeasy as ep
```

## Creating a job object

The **Job** object is central to EasyPeasy, storing all necessary
information for performing diffraction calculations. Below is an example of how
to create a Job object:
```python
job = ep.Job()
```

This object serves as a container for **model definitions**,
**experimental data**, and **analysis settings**.

## Data analysis workflow

Once the Job object is created, you can proceed with the
**data analysis workflow**, which is described in detail in the
[Workflow steps](workflow-steps/index.md) section of the documentation.
