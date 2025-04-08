# 🎾 My Tennis Club – Django 

A Django project managed with [Poetry](https://python-poetry.org/).  
This file contains a complete guide to installing, running, and linting.

---

## 📦 Requirements

- Python 3.12
- Poetry – dependency and virtual environment manager

### Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Check that it works:
```bash
poetry --version
```

## 🚀 Getting Started

1. Clone the Repository
```bash
git clone https://github.com/rafinder1/tennis-club
cd my-tennis-club
```
2. Install Dependencies
```bash
poetry install
```
3. (Optional) Activate the Virtual Environment
```bash
poetry shell
```


## 🧪 Pre-commit & Pylint Setup (Development Tools)

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

## Linting Tools

The following tools are used to lint and format the code in this project:

### 1. **Black**
   - **Purpose**: A code formatter that automatically formats Python code to conform to the PEP 8 style guide with some extra flexibility.

### 2. **isort**
   - **Purpose**: A tool to sort imports in Python files according to a consistent style.

### 3. **Flake8**
   - **Purpose**: A linting tool for Python that checks for coding style violations, errors, and potential issues in the codebase.

### 4. **Mypy**
   - **Purpose**: A static type checker for Python. It helps ensure that the code adheres to type hints and can catch type-related bugs early.

