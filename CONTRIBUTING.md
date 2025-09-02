# Contributing to Curestry

Thank you for considering contributing to Curestry! We welcome contributions from everyone.

## How to Contribute

### Reporting Issues

- Search existing issues before creating a new one
- Provide a clear title and detailed description
- Include steps to reproduce the issue
- Add relevant code samples or screenshots

### Suggesting Features

- Open an issue with a clear title and detailed description
- Explain why this feature would be useful for Curestry users

### Pull Requests

1. Fork the repository
2. Create a feature branch from `main`
3. Make your changes with clear commit messages
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## Development Setup

1. Ensure you have Python 3.9 or higher installed
2. Fork the Curestry repository on GitHub
3. Clone your fork locally:
   ```bash
   git clone https://github.com/yourusername/curestry.git
   cd curestry
   ```
4. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
5. Install in development mode:
   ```bash
   pip install -e ".[dev]"
   ```

## Code Standards

- Follow Python PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings for new functions and classes
- Keep functions focused and small
- Add type hints where appropriate

## Testing

Run the test suite before submitting changes:
```bash
python -m pytest tests/
```

## Questions?

Feel free to open an issue for any questions about contributing.

Thank you for contributing to Curestry!