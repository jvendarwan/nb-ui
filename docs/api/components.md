# Component API Reference

Complete API documentation for all nb-ui components.

## Header

Creates beautiful section headers with optional subtitles and dividers.

```python
Header(
    title: str,
    subtitle: str = "",
    level: int = 1,
    align: str = "center",
    divider: bool = True,
    theme: Optional[str] = None
)
```

### Parameters

- **title** (`str`): Main header text
- **subtitle** (`str`, optional): Secondary text below the title
- **level** (`int`, default=1): Header level (1-6, maps to h1-h6 tags)
- **align** (`str`, default="center"): Text alignment ("left", "center", "right")
- **divider** (`bool`, default=True): Whether to show decorative line below header
- **theme** (`Optional[str]`): Override default theme

### Example

```python
from nb_ui import Header

# Basic header
Header("Data Analysis Report")

# Header with subtitle
Header("Model Results", subtitle="Random Forest Classification", level=2)

# Left-aligned header without divider
Header("Introduction", align="left", divider=False)
```

---

## Card

Content containers with optional titles and consistent styling.

```python
Card(
    children: str = "",
    title: Optional[str] = None,
    variant: str = "elevation",
    elevation: int = 1,
    theme: Optional[str] = None
)
```

### Parameters

- **children** (`str`): HTML content to display inside the card
- **title** (`Optional[str]`): Optional title header for the card
- **variant** (`str`, default="elevation"): Card style variant
- **elevation** (`int`, default=1): Shadow depth (1-5)
- **theme** (`Optional[str]`): Override default theme

### Example

```python
from nb_ui import Card

# Basic card
Card("Simple content here")

# Card with title
Card("Our model achieved 94.2% accuracy", title="Results Summary")

# Custom elevation
Card("Important findings", title="Key Insights", elevation=3)
```

---

## Alert

Status messages with severity levels and consistent styling.

```python
Alert(
    message: str,
    severity: str = "info",
    variant: str = "standard",
    onClose: bool = False,
    theme: Optional[str] = None
)
```

### Parameters

- **message** (`str`): Alert message text
- **severity** (`str`, default="info"): Alert type ("success", "warning", "error", "info")
- **variant** (`str`, default="standard"): Style variant ("standard", "filled", "outlined")
- **onClose** (`bool`, default=False): Whether to show close button
- **theme** (`Optional[str]`): Override default theme

### Example

```python
from nb_ui import Alert

# Different severities
Alert("Process completed!", severity="success")
Alert("Low disk space", severity="warning")
Alert("Connection failed", severity="error")
Alert("Model training started", severity="info")

# Filled variant with close button
Alert("Important notice", severity="warning", variant="filled", onClose=True)
```

---

## CodeBlock

Syntax-highlighted code display with language support.

```python
CodeBlock(
    code: str,
    language: str = "python",
    title: Optional[str] = None,
    lineNumbers: bool = False,
    theme: Optional[str] = None
)
```

### Parameters

- **code** (`str`): Code content to display
- **language** (`str`, default="python"): Programming language for syntax highlighting
- **title** (`Optional[str]`): Optional title for the code block
- **lineNumbers** (`bool`, default=False): Whether to show line numbers
- **theme** (`Optional[str]`): Override default theme

### Example

```python
from nb_ui import CodeBlock

# Python code
CodeBlock("""
def process_data(df):
    return df.dropna()
""", language="python", title="Data Processing")

# JavaScript with line numbers
CodeBlock("""
function hello() {
    console.log("Hello World!");
}
""", language="javascript", lineNumbers=True)
```

---

## Typography

Professional text styling with Material UI variants.

```python
Typography(
    text: str,
    variant: str = "body1",
    color: str = "text",
    align: str = "left",
    weight: Optional[str] = None,
    style: Optional[str] = None,
    gutterBottom: bool = False,
    theme: Optional[str] = None
)
```

### Parameters

- **text** (`str`): Text content to display
- **variant** (`str`, default="body1"): Typography variant ("h1"-"h6", "body1", "body2", "caption")
- **color** (`str`, default="text"): Text color from theme
- **align** (`str`, default="left"): Text alignment
- **weight** (`Optional[str]`): Font weight ("bold", "normal", "light")
- **style** (`Optional[str]`): Font style ("italic", "normal")
- **gutterBottom** (`bool`, default=False): Add bottom margin
- **theme** (`Optional[str]`): Override default theme

### Example

```python
from nb_ui import Typography

# Different variants
Typography("Main Title", variant="h1")
Typography("Section heading", variant="h3")
Typography("Regular paragraph text", variant="body1")
Typography("Small caption text", variant="caption")

# Styled text
Typography("Bold important text", variant="body1", weight="bold")
Typography("Italic emphasis", variant="body2", style="italic")
```

---

## Container

Responsive content wrapper with consistent margins and max-width.

```python
Container(
    children: str = "",
    maxWidth: str = "lg",
    fixed: bool = False,
    disableGutters: bool = False,
    theme: Optional[str] = None
)
```

### Parameters

- **children** (`str`): HTML content to wrap
- **maxWidth** (`str`, default="lg"): Maximum width ("xs", "sm", "md", "lg", "xl")
- **fixed** (`bool`, default=False): Use fixed width instead of responsive
- **disableGutters** (`bool`, default=False): Remove horizontal padding
- **theme** (`Optional[str]`): Override default theme

### Example

```python
from nb_ui import Container

# Basic container
Container("<h3>Centered Content</h3><p>This is automatically centered.</p>")

# Small container without gutters
Container("<div>Compact layout</div>", maxWidth="sm", disableGutters=True)
```
