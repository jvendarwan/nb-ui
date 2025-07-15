# Contributing to nb-ui

Thank you for your interest in contributing to nb-ui! This document provides guidelines for contributing to the project.

## Development Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/nb-ui.git
cd nb-ui
```

2. Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

3. Install the package in development mode:

```bash
pip install -e .
```

## Development Workflow

1. Create a new branch for your feature:

```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and test them in a Jupyter notebook

3. Run tests (when available):

```bash
pytest
```

4. Format your code:

```bash
black nb_ui/
```

5. Commit your changes with a descriptive message:

```bash
git commit -m "Add new component: YourComponent"
```

6. Push your branch and create a pull request

## Code Style

- Use Black for code formatting
- Follow PEP 8 guidelines
- Add type hints where appropriate
- Write descriptive docstrings for all public functions and classes

## Component Guidelines

When creating new components:

1. Inherit from `ComponentBase`
2. Implement the `render()` method
3. Support theming through the theme system
4. Include proper documentation and examples
5. Follow MaterialUI/AntUI naming conventions where applicable

## Testing

- Test components in different themes
- Verify responsive behavior
- Check browser compatibility in Jupyter environments

## Documentation

- Update README.md for new features
- Add examples to demo notebooks
- Document API changes in CHANGELOG.md
