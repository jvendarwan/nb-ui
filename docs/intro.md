# Welcome to nb-ui 🎨

**Essential UI Components for Data Science Notebooks**

> **Zero HTML/CSS Required** - Professional presentations with simple Python function calls

## What is nb-ui?

**nb-ui** is a streamlined Python package that brings essential UI components directly into Jupyter notebooks. Designed specifically for data scientists, it provides exactly what you need to create professional reports and presentations without the complexity of full web frameworks.

```{admonition} Built for Data Scientists
:class: tip
Focus on your analysis, not on styling. nb-ui provides just the essential components data scientists actually use - no bloat, just clean, professional presentation tools.
```

## ✨ Key Features

- **🎯 Essential Components**: Header, Card, Alert, CodeBlock, Typography, Container
- **🎨 3 Beautiful Themes**: Material UI, Ant Design, and Dark themes
- **🚀 Auto-Rendering**: Components display automatically like pandas DataFrames
- **📦 Simple Installation**: One pip install, zero configuration required
- **🔧 Clean API**: Intuitive functions with sensible defaults
- **📱 Professional Look**: Consistent, responsive design out of the box

## Essential Components

### Core Components

- **Header** - Section titles and subtitles with decorative dividers
- **Card** - Content containers for key findings and results
- **Alert** - Status messages with success/warning/error/info styling
- **CodeBlock** - Syntax-highlighted code with language support
- **Typography** - Professional text styling with weight and emphasis
- **Container** - Centered layout wrapper with consistent margins

### Quick Utilities

- **success()** - Green success messages
- **warning()** - Orange warning alerts
- **error()** - Red error notifications
- **info()** - Blue informational messages

## Quick Preview

```python
from nb_ui import Header, Card, CodeBlock, Typography, Container
from nb_ui import success, warning, error, info, set_theme

# Set your preferred theme
set_theme("material")  # or "antd", "dark"

# Create professional notebook sections
Header("Customer Churn Analysis", subtitle="Predictive Modeling Results")

Card("""
Our Random Forest model achieved 94.2% accuracy. Key predictors:
- Monthly charges (importance: 0.31)
- Tenure (importance: 0.28)
- Contract type (importance: 0.22)
""", title="🎯 Model Performance")

# Status updates during analysis
success("✅ Data preprocessing completed")
warning("⚠️ Class imbalance detected")
info("ℹ️ Model saved to disk")

# Document your code
CodeBlock("""
def preprocess_data(df):
    return df.dropna().reset_index()
""", language="python", title="Data Processing")
```

## Perfect For

- **📊 Data Analysis Reports** - Professional presentation of findings
- **🤖 Model Documentation** - Clear explanation of ML pipelines
- **📈 Executive Summaries** - Stakeholder-ready insights
- **🔬 Research Papers** - Academic-quality formatting
- **🎯 Model Training Logs** - Real-time status updates

## Why nb-ui?

| **Before nb-ui**           | **With nb-ui**                |
| -------------------------- | ----------------------------- |
| ❌ Plain text outputs      | ✅ Professional styling       |
| ❌ Inconsistent formatting | ✅ Cohesive design system     |
| ❌ Hard to read code dumps | ✅ Syntax-highlighted blocks  |
| ❌ No status indicators    | ✅ Clear success/error alerts |
| ❌ Boring presentations    | ✅ Engaging visual reports    |

## Three Beautiful Themes

```python
set_theme("material")  # Clean Google Material Design
set_theme("antd")      # Professional Ant Design
set_theme("dark")      # Perfect for presentations
```

## Get Started

```{panels}
:card: + intro-card text-center
:column: col-lg-6 col-md-6 col-sm-6 col-xs-12 d-flex

---
**🚀 Quick Start**
^^^
Jump right in with examples

+++
{doc}`quick-start`

---
**📚 Essential Components**
^^^
Explore all 6 core components

+++
{doc}`components/headers`

---
**🎨 Theme Gallery**
^^^
See all 3 themes in action

+++
{doc}`themes/overview`

---
**⚡ API Reference**
^^^
Complete function documentation

+++
{doc}`api/components`
```

## Community & Support

- **GitHub**: [github.com/username/nb-ui](https://github.com/username/nb-ui)
- **Issues**: Report bugs and request features
- **Discussions**: Get help and share examples
- **Contributing**: Help improve nb-ui for everyone

Transform your notebooks from code dumps to professional reports! 🚀
