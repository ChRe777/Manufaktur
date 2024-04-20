# How create python packages

Creating Python packages involves organizing your Python code into a directory structure that can be distributed and installed using Python's packaging tools. Here's a step-by-step guide on how to create a Python package:

## 1. Directory Structure

Start by creating a directory structure for your package. A typical structure might look like this:

```
my_package/
    my_package/
        __init__.py
        module1.py
        module2.py
    setup.py
    README.md
    LICENSE
```

- The outer my_package/ directory is the root directory of your package.
- Inside my_package/, create another my_package/ directory which will serve as the Python package directory.
- **init**.py: This file turns the directory into a Python package.
- module1.py, module2.py: Python modules containing your code.
- setup.py: Script for package distribution and installation.
- README.md: Description and usage instructions.
- LICENSE: License file (e.g., MIT, GPL). 2. Define Package Code

## 2. Define Package Code

Inside my_package/my_package/, create Python modules (module1.py, module2.py, etc.) that contain your code. For example:

```python
# module1.py

def hello():
print("Hello from module1!")
```

```python
# module2.py

def goodbye():
print("Goodbye from module2!")
```

## 3. **init**.py File

Inside my_package/my_package/, create an **init**.py file. This file can be empty or used to import functions/classes from your modules for convenience:

```python
# __init__.py

from .module1 import hello
from .module2 import goodbye
```

## 4. setup.py File

Create setup.py in the root of your package directory (my_package/setup.py). This file defines metadata about your package and how to distribute it:

```python
from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='A simple Python package',
    long_description=open('README.md').read(),
    install_requires=[], # List any dependencies
)
```

## 5. Packaging and Distribution

To build your package, run the following command in the root of your package directory:

```bash
python setup.py sdist bdist*wheel
```

This command creates a dist/ directory containing a source distribution (\*.tar.gz) and a built distribution (\_.whl).

## 6. Installation

You can install your package locally using pip:

```bash
pip install ./dist/my_package-0.1.tar.gz
```

## 7. Usage

You can now use your package in Python scripts or interactive sessions:

```python
import my_package

my_package.module1.hello() # Outputs: Hello from module1!
my_package.module2.goodbye() # Outputs: Goodbye from module2!
```

## 8. Distribution

To distribute your package on PyPI (Python Package Index), consider registering an account on PyPI and following the steps for uploading your package.

By following these steps, you've created a simple Python package that can be installed and used by others using standard Python packaging tools. You can extend this example by adding more modules, defining additional metadata in setup.py, and implementing more complex package functionality.

# Develop mode

It looks like you're asking about how to work in "development mode" or how to develop Python packages effectively while continuously making changes and testing them without needing to reinstall the package each time. Development mode allows you to work on your package code and immediately see the changes reflected without having to reinstall the package repeatedly.

To work effectively in development mode for a Python package, you can use a combination of virtual environments, editable installs (pip install -e), and development workflows. Here's how you can set this up:

## 1. Virtual Environment

First, create a virtual environment to isolate your package development environment from the system Python installation and other projects.

```bash

# Create a virtual environment (replace 'venv' with your preferred name)

python -m venv venv

# Activate the virtual environment (Windows)

venv\Scripts\activate

# Activate the virtual environment (Mac/Linux)

source venv/bin/activate
```

## 2. Package Setup

Assuming you have the directory structure as described previously:

```
my_package/
    my_package/
        **init**.py
        module1.py
        module2.py
    setup.py
    README.md
    LICENSE
```

## 3. Install in Editable Mode

Navigate to the root directory of your package (my_package/) and use pip to install your package in editable mode (-e option). This installs your package in "editable" mode, where changes to the source code are immediately reflected without reinstalling the package.

```bash

cd my_package

# Install the package in editable mode

pip install -e .
```

## 4. Development Workflow

Now you can start editing your package code using your favorite text editor or IDE. As you make changes to your code, these changes will be immediately visible without reinstalling the package.

For example, if you modify module1.py:

```python

# my_package/module1.py

def hello():
print("Modified Hello from module1!")
```

You can then test these changes immediately in a Python environment without reinstalling the package:

```python

import my_package

my_package.module1.hello() # Outputs: Modified Hello from module1!
```

## 5. Testing

During development, it's a good practice to write unit tests to validate the behavior of your package. You can run tests using tools like pytest within your virtual environment.

## 6. Version Control

Use version control (e.g., Git) to track changes to your package code. Commit your changes regularly and use branches to isolate features or bug fixes.

## 7. Cleaning Up

When you're done working on your package, deactivate the virtual environment:

```bash
deactivate
```

## Recap

Working in development mode with Python packages involves creating a virtual environment, installing your package in editable mode, and continuously testing and iterating on your code within the virtual environment. This setup allows for an efficient and isolated development environment where changes to your package code are immediately reflected in your development environment.
