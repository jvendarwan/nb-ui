# Getting Started

## Installation

### Using pip (Recommended)

```bash
pip install nb-ui
```

### Development Installation

If you want to use the latest development version:

```bash
git clone https://github.com/username/nb-ui.git
cd nb-ui
pip install -e .
```

### Verify Installation

Test that nb-ui is working correctly:

```python
from nb_ui import Header, success, list_themes

# Check available themes
print("Available themes:", list_themes())

# Create a test component (auto-renders!)
Header("Welcome to nb-ui!", subtitle="Installation successful")
success("🎉 nb-ui is ready to use!")
```

## Basic Usage

### 1. Import Essential Components

```python
# Import core components
from nb_ui import Header, Card, Alert, CodeBlock, Typography, Container

# Import utility functions (most commonly used)
from nb_ui import success, error, warning, info

# Import theme functions
from nb_ui import set_theme, get_theme, list_themes
```

### 2. Set Your Theme

Choose from 3 beautiful themes:

```python
# Clean Material Design (default)
set_theme("material")

# Professional Ant Design
set_theme("antd")

# Dark theme for presentations
set_theme("dark")
```

### 3. Create Your First Components

**Auto-Rendering**: Components display automatically like pandas DataFrames - no `.display()` needed!

```python
# Section headers
Header("Data Analysis Report", subtitle="Customer Segmentation Study")

# Key findings in cards
Card("""
Our analysis revealed 3 distinct customer segments:
- **Premium** (15%): High value, low churn risk
- **Standard** (60%): Medium value, moderate risk
- **Budget** (25%): Price-sensitive, high churn risk
""", title="🎯 Key Findings")

# Status updates during analysis
success("✅ Data preprocessing completed")
warning("⚠️ Class imbalance detected in target variable")
info("ℹ️ Model training started with Random Forest")

# Document your code
CodeBlock("""
def segment_customers(df):
    # Apply K-means clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['segment'] = kmeans.fit_predict(df[features])
    return df
""", language="python", title="Customer Segmentation")

# Professional text styling
Typography("Statistical significance: p < 0.001",
           variant="caption", style="italic")
```

## Essential Workflow

### Data Science Report Structure

```python
from nb_ui import Header, Card, CodeBlock, Typography
from nb_ui import success, warning, info, set_theme

# 1. Set theme
set_theme("material")

# 2. Title section
Header("Customer Churn Prediction",
       subtitle="Machine Learning Analysis")

# 3. Executive summary
Card("""
**Key Results:**
- Model Accuracy: 94.2%
- Top Feature: Monthly Charges (importance: 0.31)
- Identified 847 high-risk customers
- Estimated savings: $2.3M annually
""", title="📊 Executive Summary")

# 4. Methodology
Header("Methodology", level=2)
CodeBlock("""
# Data preprocessing pipeline
def preprocess_data(df):
    # Handle missing values
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

    # Feature engineering
    df['charges_per_month'] = df['TotalCharges'] / df['tenure']
    return df

# Model training
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
""", language="python", title="Model Pipeline")

# 5. Progress updates
success("✅ Model training completed successfully")
info("💾 Model saved to: models/churn_model_v1.pkl")

# 6. Conclusions
Header("Conclusions", level=2)
Typography("The Random Forest model demonstrates strong predictive performance "
          "and provides actionable insights for customer retention strategies.",
          variant="body1")
```

### Quick Status Updates

Perfect for long-running analyses:

```python
# At the start
info("🚀 Starting customer analysis pipeline...")

# During processing
success("✅ Data loaded - 10,000 customer records")
success("✅ Feature engineering completed")
warning("⚠️ Detected 15% missing values in TotalCharges")
success("✅ Missing values handled with median imputation")

# Model training updates
info("🤖 Training Random Forest model...")
success("✅ Model training completed - Accuracy: 94.2%")
info("💾 Model saved to disk")

# Final results
success("🎉 Analysis complete! Check results above.")
```

## Next Steps

1. **Explore Components**: Check out each component's documentation
2. **Try Different Themes**: Test `material`, `antd`, and `dark` themes
3. **Create Your First Report**: Use the workflow example above
4. **Advanced Usage**: Check the API reference for all options

Ready to transform your notebooks? Let's dive into the components! 🚀

```{admonition} Pro Tip
:class: tip
Start each notebook with your theme choice: `set_theme("material")`. All subsequent components will use this theme automatically.
```
