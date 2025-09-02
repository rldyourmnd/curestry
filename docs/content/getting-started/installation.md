# Installation Guide

## Prerequisites
- Python 3.9 or above
- pip, Conda, or Pipenv (latest version recommended)

## Quick Installation
```bash
pip install curestry
```

## Platform-Specific Installation

### Windows
```bash
# Create virtual environment
python -m venv curestry-env
curestry-env\Scripts\activate

# Install Curestry
pip install curestry
```

### macOS/Linux
```bash
# Create virtual environment
python -m venv curestry-env
source curestry-env/bin/activate

# Install Curestry
pip install curestry
```

### Using Conda
```bash
# Create conda environment
conda create --name curestry-env python=3.10
conda activate curestry-env

# Install Curestry
pip install curestry
```

## Verification
Verify your installation:
```python
python -c "import curestry; print(curestry.__version__)"
```

## Development Installation
For contributing or development:
```bash
git clone git@github.com:rldyourmnd/curestry.git
cd curestry
pip install -e ".[dev]"
```

## Next Steps
- [Quick Start Guide](quick-start.md)
- [Basic Usage](../core-concepts/basic-usage.md)