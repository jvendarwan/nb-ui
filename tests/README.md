# Testing Strategy for nb-ui Components

## Overview

This document outlines the comprehensive testing strategy for the nb-ui component library. Testing UI components that generate HTML/CSS requires specific approaches to ensure reliability, maintainability, and user experience.

## Why Unit Tests Are Essential

### 1. **HTML Generation Validation**

Components generate complex HTML strings with embedded CSS. Tests ensure:

- Correct HTML structure and elements
- Proper CSS class generation
- Valid HTML attributes
- Component content inclusion

### 2. **Parameter Handling & API Validation**

Components accept numerous parameters that affect rendering:

- Different variants (contained, outlined, text)
- Color schemes (primary, secondary, success, error, etc.)
- Size options (small, medium, large)
- Boolean properties (disabled, fullWidth, etc.)
- Icon handling (startIcon, endIcon)

### 3. **Theme System Integration**

Components must properly integrate with the theme system:

- Color value extraction from themes
- Spacing system utilization
- Typography integration
- Theme switching support

### 4. **Component Uniqueness & Isolation**

Each component instance should be unique:

- Unique component IDs for CSS scoping
- No style bleeding between components
- Proper CSS encapsulation

### 5. **Regression Prevention**

Tests catch breaking changes when:

- Refactoring component code
- Updating theme values
- Modifying CSS generation logic
- Adding new features

## Testing Structure

```
tests/
├── conftest.py              # Shared fixtures and utilities
├── requirements.txt         # Testing dependencies
├── test_*.py               # Component-specific tests
├── integration/            # Integration tests
└── performance/            # Performance tests
```

## Testing Categories

### 1. **Unit Tests (Primary Focus)**

#### Basic Component Tests

- Component creation and instantiation
- HTML structure validation
- Content rendering
- CSS generation

#### Parameter Testing

- All parameter combinations
- Invalid parameter handling
- Default value behavior
- Edge cases (empty strings, None values)

#### Styling Tests

- CSS property generation
- Theme integration
- Responsive behavior
- Hover/focus states

#### Uniqueness Tests

- Component ID generation
- CSS class uniqueness
- Multiple instance isolation

### 2. **Integration Tests**

#### Component Interaction

- Components working together in layouts
- Nested component behavior
- Theme consistency across components

#### Layout System Integration

- Components in Grid/Stack/Row/Col
- Responsive behavior in layouts
- Spacing and alignment

### 3. **Parametrized Tests**

Use pytest parametrization for comprehensive coverage:

- All variant × color combinations
- Size × state combinations
- Theme × component combinations

### 4. **Error Handling Tests**

Test resilience with:

- Invalid parameters
- Empty/None inputs
- Special characters
- Very long content

## Testing Utilities

### HTML/CSS Parsing

```python
def parse_html(html_string: str) -> BeautifulSoup:
    """Parse HTML for element validation"""

def extract_css_styles(html_string: str) -> Dict[str, str]:
    """Extract CSS properties for testing"""

def assert_css_property(html: str, property_name: str, expected_value: str = None):
    """Assert CSS property exists with optional value check"""
```

### Component Testing Utilities

```python
class ComponentTestUtils:
    @staticmethod
    def assert_basic_structure(component, expected_tag: str, expected_text: str = None):
        """Test basic component structure"""

    @staticmethod
    def assert_theme_integration(component, theme_property: str, expected_theme_value: str):
        """Test theme integration"""

    @staticmethod
    def assert_responsive_behavior(component, min_css_rules: int = 1):
        """Test responsive CSS generation"""
```

## Component-Specific Testing Examples

### Button Component Tests

- ✅ Variants: contained, outlined, text
- ✅ Colors: primary, secondary, success, error, warning, info
- ✅ Sizes: small, medium, large
- ✅ States: enabled, disabled
- ✅ Icons: startIcon, endIcon, both
- ✅ Layout: fullWidth option
- ✅ Accessibility: proper button semantics

### Alert Component Tests

- ✅ Severities: error, warning, info, success
- ✅ Variants: standard, filled, outlined
- ✅ Interactivity: closeable alerts
- ✅ Content: HTML content support
- ✅ Icons: severity-specific icons

### Layout Component Tests

- ✅ Stack: vertical layout, spacing, alignment
- ✅ Row/Col: horizontal layout, responsive behavior
- ✅ Grid: responsive grid system, breakpoints
- ✅ Container: content width control

### Typography Component Tests

- ✅ Variants: h1-h6, body1/body2, subtitle1/subtitle2
- ✅ Colors: theme color integration
- ✅ Alignment: left, center, right, justify

## Test Execution

### Setup

```bash
# Install testing dependencies
pip install -r tests/requirements.txt

# Install package in development mode
pip install -e .
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific component tests
pytest tests/test_button.py

# Run with coverage
pytest --cov=nb_ui

# Run parametrized tests only
pytest -k "parametrize"

# Verbose output
pytest -v
```

### Continuous Integration

```yaml
# Example GitHub Actions workflow
- name: Test Components
  run: |
    pytest tests/ --cov=nb_ui --cov-report=xml

- name: Upload Coverage
  uses: codecov/codecov-action@v1
```

## Testing Best Practices

### 1. **Test Structure**

- Use descriptive test names
- Group related tests in classes
- Use fixtures for common setup
- Parametrize for comprehensive coverage

### 2. **Assertions**

- Test specific behavior, not implementation
- Use meaningful assertion messages
- Test both positive and negative cases
- Validate complete component output

### 3. **Maintainability**

- Keep tests simple and focused
- Use utilities for common operations
- Document complex test scenarios
- Regular test review and cleanup

### 4. **Performance**

- Mock external dependencies
- Use fixtures for expensive setup
- Parallel test execution where possible
- Profile slow tests

## Coverage Goals

### Minimum Coverage Targets

- **Overall Code Coverage**: 90%+
- **Component Coverage**: 95%+
- **Critical Path Coverage**: 100%

### Coverage Areas

- ✅ All public methods
- ✅ All parameter combinations
- ✅ Error handling paths
- ✅ Theme integration
- ✅ CSS generation
- ✅ HTML structure

## Testing Tools & Dependencies

### Core Testing

- **pytest**: Testing framework
- **pytest-cov**: Coverage reporting
- **beautifulsoup4**: HTML parsing
- **lxml**: XML/HTML parser

### Optional Enhancements

- **pytest-xdist**: Parallel test execution
- **pytest-mock**: Mocking utilities
- **pytest-benchmark**: Performance testing
- **html5lib**: Additional HTML parsing

## Component Testing Checklist

For each new component, ensure tests cover:

- [ ] Basic instantiation and rendering
- [ ] All parameter variations
- [ ] Theme integration
- [ ] CSS structure and properties
- [ ] Component ID uniqueness
- [ ] Responsive behavior
- [ ] Error handling
- [ ] Integration with other components
- [ ] Accessibility features
- [ ] Performance (for complex components)

## Future Testing Enhancements

### Visual Regression Testing

- Screenshot comparison for UI changes
- Browser-based testing with Selenium
- Cross-browser compatibility

### Performance Testing

- Component rendering performance
- Memory usage testing
- Large dataset handling

### Integration Testing

- End-to-end notebook testing
- Jupyter environment testing
- Real-world usage scenarios

## Conclusion

Comprehensive testing ensures the nb-ui library provides reliable, consistent components for data scientists building professional Jupyter notebooks. The testing strategy balances thoroughness with maintainability, providing confidence in component behavior while enabling rapid development.
