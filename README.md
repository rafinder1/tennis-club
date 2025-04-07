# tennis-club
Basic App For Learning Deployment To AWS


## Linting Tools

The following tools are used to lint and format the code in this project:

### 1. **Black**
   - **Purpose**: A code formatter that automatically formats Python code to conform to the PEP 8 style guide with some extra flexibility.
   - **Configuration**: The line length is set to 88 characters, and the target Python version is set to `py312` (Python 3.12).

### 2. **isort**
   - **Purpose**: A tool to sort imports in Python files according to a consistent style.
   - **Configuration**: The sorting style follows the `black` profile to maintain uniformity with the `black` code formatter.

### 3. **Flake8**
   - **Purpose**: A linting tool for Python that checks for coding style violations, errors, and potential issues in the codebase.
   - **Configuration**: The maximum line length is set to 88 characters. Warnings `E203` (whitespace before a colon) and `W503` (line break before binary operator) are ignored to avoid conflicts with `black`'s formatting style.

### 4. **Mypy**
   - **Purpose**: A static type checker for Python. It helps ensure that the code adheres to type hints and can catch type-related bugs early.
   - **Configuration**: Mypy is configured to ignore missing imports and uses Python 3.12 for type checking.

## Pre-commit Hooks

### What is pre-commit?

**pre-commit** is a framework for managing and maintaining multi-language pre-commit hooks. These hooks run automatically before a commit is made, ensuring that code is properly formatted and meets certain quality standards. The benefit of using **pre-commit** is that it enforces consistent code formatting and error checking without requiring manual intervention.

### How to Use pre-commit in This Project

1. **Install pre-commit**: First, you need to install the `pre-commit` package:
   ```bash
   pip install pre-commit
   ```
2. **Install the Hooks**: Run the following command to set up the hooks in your project:
   ```bash
   pre-commit install
   ```
3. **Run pre-commit Manually**: You can manually trigger the pre-commit hooks on all files with:
   ```bash
   pre-commit run --all-files
   ```
