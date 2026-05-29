## Appartments - Project Overview
A real estate price prediction and analytics platform. The project aims to provide insights into the real estate market, predict property prices, and offer recommendations based on user preferences. The below are the four important featues of the project:
1. Analytics Module : Give insights about the selected city and its real estate market. The insights include:
    a. Spatial Analysis : Price distribution across sectors.
    b. Price Distribution across sectors : Price distribution across sectors using Box Plot
    c. Price Vs Square Foot Analysis : Price Vs Square Foot Analysis using Scatter Plot for whole or specific sectors.
    d. Number of rooms Pie Chart : Number of rooms distribution across the city using Pie Chart fpr whole city or specific sectors.
    e. Top Feature Word Cloud : 
2. Price prediction Module : ML model for price range prediction based on user input features.
3. Recommender System Module : ML model for recommending properties based on selected property.
4. Insights Module : ML regression model for feature selection and tell which features are more important for price prediction and how much.

## Project Workflow
- Data Gathering
    - Web Scraping from 99acres.com
- Data Preprocessing
    - CSV cleaning mannual
    - Flats and Independent house data cleaning
    - combine Flats and Independent house data and cleaning
- Feature Engineering
    - creating new features
- EDA
    - Univariate Analysis
    - Bivariate Analysis
    - Multivariate Analysis
- Feature Selection
- Model Building

## Points of Improvement
1. Add more analytics
2. Build for any other city
3. Add Independent Floors and Residential Plots
4. Add Commercial Properties
5. Improvement of Predictive Modules with better Algorithms like XGBoost, LightGBM, CatBoost and Deep Learning Models etc.
6. Add more features

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         appartments and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── appartments   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes appartments a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── src                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

