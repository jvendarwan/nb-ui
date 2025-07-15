# Utility Functions API Reference

Quick and convenient utility functions for common tasks.

## Alert Utility Functions

Simple functions for creating alerts without specifying severity.

### success()

```python
success(message: str, **kwargs) -> Alert
```

Creates a success alert with green styling.

**Parameters:**

- **message** (`str`): Success message to display
- **kwargs**: Additional parameters passed to Alert component

**Example:**

```python
from nb_ui import success

success("✅ Model training completed successfully!")
success("Data processing finished", variant="filled")
```

---

### warning()

```python
warning(message: str, **kwargs) -> Alert
```

Creates a warning alert with orange styling.

**Parameters:**

- **message** (`str`): Warning message to display
- **kwargs**: Additional parameters passed to Alert component

**Example:**

```python
from nb_ui import warning

warning("⚠️ Low memory detected")
warning("Class imbalance found", onClose=True)
```

---

### error()

```python
error(message: str, **kwargs) -> Alert
```

Creates an error alert with red styling.

**Parameters:**

- **message** (`str`): Error message to display
- **kwargs**: Additional parameters passed to Alert component

**Example:**

```python
from nb_ui import error

error("❌ Database connection failed")
error("Model validation error", variant="outlined")
```

---

### info()

```python
info(message: str, **kwargs) -> Alert
```

Creates an info alert with blue styling.

**Parameters:**

- **message** (`str`): Information message to display
- **kwargs**: Additional parameters passed to Alert component

**Example:**

```python
from nb_ui import info

info("ℹ️ Model saved to disk")
info("Processing 1,000 records", variant="filled")
```

## Theme Management

Functions for managing the global theme system.

### set_theme()

```python
set_theme(theme_name: str) -> None
```

Sets the global theme for all components.

**Parameters:**

- **theme_name** (`str`): Theme name ("material", "antd", "dark")

**Example:**

```python
from nb_ui import set_theme

set_theme("material")  # Clean Material Design
set_theme("antd")      # Professional Ant Design
set_theme("dark")      # Dark mode theme
```

---

### get_theme()

```python
get_theme() -> Theme
```

Returns the current active theme object.

**Returns:**

- **Theme**: Current theme configuration

**Example:**

```python
from nb_ui import get_theme

current_theme = get_theme()
print(f"Primary color: {current_theme.colors.primary}")
```

---

### list_themes()

```python
list_themes() -> List[str]
```

Returns a list of available theme names.

**Returns:**

- **List[str]**: Available theme names

**Example:**

```python
from nb_ui import list_themes

available = list_themes()
print(f"Available themes: {available}")
# Output: ['material', 'antd', 'dark']
```

## Usage Patterns

### Quick Status Updates

Perfect for Jupyter notebooks and data science workflows:

```python
from nb_ui import success, warning, error, info, set_theme

# Set preferred theme
set_theme("material")

# Model training pipeline
info("🚀 Starting model training...")
success("✅ Data preprocessing completed")
warning("⚠️ Class imbalance detected - applying SMOTE")
success("✅ Model training completed")
error("❌ Validation failed - retrying...")
success("🎉 Model deployment successful!")
```

### Theme Switching

```python
from nb_ui import set_theme, Header, Card

# Try different themes
for theme in ["material", "antd", "dark"]:
    set_theme(theme)
    Header(f"Preview of {theme.title()} Theme")
    Card("This is how content looks in this theme")
```
