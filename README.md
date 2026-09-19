## Appartments - Project Overview
A real estate price prediction and analytics platform. The project aims to provide insights into the real estate market, predict property prices, and offer recommendations based on user preferences. The below are the four important featues of the project:

1. **Analytics Module**: Give insights about the selected city and its real estate market. The insights include:

- **Spatial Analysis with area and price per sq ft**: It is useful to decide which `sector` to invest as per Average Price per Sq ft `color` and Average Area `size` requirements on **Scatter Plot on Map** or **Spatial Analysis**.
![alt text](/reports/figures/image-4.png)

- **Distribution of Bedrooms for each Sector**: `Bedrooms` distribution for specific sectors using **Pie Chart**. It tells the `number of bedrooms` distribution for the selected **sector**.
![alt text](/reports/figures/image-7.png)

- **Distribution of Price for Different Property Types**: It is useful to decide which `property type` to invest in using **Histogram with KDE**.
![alt text](/reports/figures/image-8.png)

- **Price Vs Built Up Area Analysis**: Price Vs Built Up Area Analysis using ***Scatter Plot** for whole or specific sectors. It is useful to find the `Built Up Area` will customer get for the price for the selected **property type**.
![alt text](/reports/figures/image-9.png)

- **Price Distribution for Bedroom**: Price distribution for different number of bedrooms using **Box Plot**. It is useful to decide right `price` range for the selected `number of bedrooms`.
![alt text](/reports/figures/image-6.png)

- **Top Feature Word Cloud**: It shows **word cloud** of `top features` or `amenities` that are generally provided, the bigger the size the higher the frequency of occurrence of the feature or amenities in a property.
![alt text](/reports/figures/image-5.png)

2. **Price prediction Module**: ML model for price range prediction based on user input features.
![alt text](/reports/figures/image-2.png)
- This can be used to predict the price range of a property based on user input features like location, number of rooms, square footage, etc.

3. **Recommender System Module**: ML model for recommending properties based on selected property.
![alt text](/reports/figures/image-3.png)
![alt text](/reports/figures/image.png)
- This can be used to tell nearest popular places with distance.
![alt text](/reports/figures/image-1.png)
- This can be used to recommend similar properties based on selected property like recommending or listing similar properties below the current property the user is viewing in a website or app.

4. Insights Module : ML regression model for feature selection and tell which features are more important for price prediction and how much.

## EDA
![alt text](/reports/figures/Pandas_Profiling_Report.png)

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