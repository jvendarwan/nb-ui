"""
Pytest configuration and shared fixtures for nb-ui tests
"""

import pytest
import re
from typing import Dict, Any, Optional

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None  # type: ignore


@pytest.fixture
def light_theme():
    """Light theme fixture for testing"""
    from nb_ui.theme import create_material_theme
    return create_material_theme()


@pytest.fixture
def dark_theme():
    """Dark theme fixture for testing"""
    from nb_ui.theme import create_dark_theme
    return create_dark_theme()


def parse_html(html_string: str):  # type: ignore
    """Parse HTML string into BeautifulSoup object for testing"""
    return BeautifulSoup(html_string, 'html.parser')  # type: ignore


def extract_css_styles(html_string: str) -> Dict[str, str]:
    """Extract CSS styles from HTML string for testing"""
    soup = parse_html(html_string)
    styles = {}
    
    # Extract inline styles
    for element in soup.find_all(style=True):  # type: ignore
        styles.update(parse_inline_styles(element.get('style', '')))  # type: ignore
    
    # Extract styles from <style> tags
    for style_tag in soup.find_all('style'):
        css_text = style_tag.get_text()
        styles.update(parse_css_rules(css_text))
    
    return styles


def parse_inline_styles(style_attr: str) -> Dict[str, str]:
    """Parse inline CSS styles into dictionary"""
    styles = {}
    if style_attr:
        for declaration in style_attr.split(';'):
            if ':' in declaration:
                property_name, value = declaration.split(':', 1)
                styles[property_name.strip()] = value.strip()
    return styles


def parse_css_rules(css_text: str) -> Dict[str, str]:
    """Extract CSS properties from CSS text"""
    styles = {}
    # Simple regex to extract property: value pairs
    pattern = r'([a-z-]+)\s*:\s*([^;]+)'
    matches = re.findall(pattern, css_text, re.IGNORECASE)
    for prop, value in matches:
        styles[prop.strip()] = value.strip()
    return styles


def assert_html_contains_element(html: str, tag: str, **attributes):
    """Assert that HTML contains an element with specific attributes"""
    soup = parse_html(html)
    elements = soup.find_all(tag, **attributes)
    assert len(elements) > 0, f"Expected to find <{tag}> with attributes {attributes}"
    return elements[0]


def assert_css_property(html: str, property_name: str, expected_value: Optional[str] = None):
    """Assert that HTML contains CSS property with optional value check"""
    styles = extract_css_styles(html)
    assert property_name in styles, f"Expected CSS property '{property_name}' not found"
    
    if expected_value:
        actual_value = styles[property_name]
        assert expected_value in actual_value, f"Expected '{expected_value}' in '{actual_value}'"


def assert_contains_text(html: str, text: str):
    """Assert that HTML contains specific text content"""
    soup = parse_html(html)
    assert text in soup.get_text(), f"Expected text '{text}' not found in HTML"


def assert_component_id_present(html: str):
    """Assert that component has a unique ID for CSS classes"""
    assert re.search(r'class="[^"]*-\w+', html), "Component should have unique ID in CSS class"


# Test utilities for common assertions
class ComponentTestUtils:
    """Utility class for common component testing patterns"""
    
    @staticmethod
    def assert_basic_structure(component, expected_tag: str, expected_text: Optional[str] = None):
        """Test basic component structure"""
        html = component.render()
        
        # Should have HTML content
        assert html.strip(), "Component should render non-empty HTML"
        
        # Should have expected tag
        assert_html_contains_element(html, expected_tag)
        
        # Should have nb-component class
        assert 'class="nb-component' in html, "Component should have nb-component class"
        
        # Should have unique component ID
        assert_component_id_present(html)
        
        # Should contain expected text if provided
        if expected_text:
            assert_contains_text(html, expected_text)
    
    @staticmethod
    def assert_theme_integration(component, theme_property: str, expected_theme_value: str):
        """Test that component properly integrates with theme"""
        html = component.render()
        styles = extract_css_styles(html)
        
        # Should use theme values
        found_theme_value = False
        for prop, value in styles.items():
            if expected_theme_value in value:
                found_theme_value = True
                break
        
        assert found_theme_value, f"Expected theme value '{expected_theme_value}' not found in styles"
    
    @staticmethod
    def assert_responsive_behavior(component, min_css_rules: int = 1):
        """Test that component includes responsive CSS"""
        html = component.render()
        
        # Should have CSS styles
        soup = parse_html(html)
        style_tags = soup.find_all('style')
        assert len(style_tags) > 0, "Component should include CSS styles"
        
        # Count CSS rules
        css_rules = 0
        for style_tag in style_tags:
            css_text = style_tag.get_text()
            css_rules += len(re.findall(r'{[^}]+}', css_text))
        
        assert css_rules >= min_css_rules, f"Expected at least {min_css_rules} CSS rules"


@pytest.fixture
def component_utils():
    """Fixture providing component testing utilities"""
    return ComponentTestUtils


# Parametrized fixtures for common test scenarios
@pytest.fixture(params=['light', 'dark'])
def theme_variant(request):
    """Parametrized fixture for testing both themes"""
    if request.param == 'light':
        from nb_ui.theme import create_material_theme
        return create_material_theme()
    else:
        from nb_ui.theme import create_dark_theme
        return create_dark_theme()


@pytest.fixture(params=['xs', 'sm', 'md', 'lg', 'xl'])
def spacing_size(request):
    """Parametrized fixture for testing different spacing sizes"""
    return request.param


@pytest.fixture(params=['primary', 'secondary', 'success', 'error', 'warning', 'info'])
def color_variant(request):
    """Parametrized fixture for testing different color variants"""
    return request.param 