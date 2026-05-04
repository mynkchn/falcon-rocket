# Copied From @rajiv0801

# Falcon Rocket — SpaceX Falcon 9 First Stage Landing Prediction

> *Can we predict whether a SpaceX Falcon 9 booster will land successfully — and estimate the cost of a launch before it even lifts off?*

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=flat-square&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Dashboard-3F4F75?style=flat-square&logo=plotly&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML%20Models-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)

---

## Overview

SpaceX has disrupted the aerospace industry by reusing Falcon 9 rocket boosters — cutting launch costs from ~$165M (competitors) down to ~$62M. The key to that saving? A successful first-stage landing.

**Falcon Rocket** is an end-to-end data science project that:

- Collects real SpaceX launch data via REST API and web scraping
- Cleans and engineers features from raw JSON and HTML sources
- Performs exploratory data analysis (EDA) with SQL and visualizations
- Builds an interactive Plotly Dash dashboard for business intelligence
- Trains and evaluates multiple classification models to **predict landing success**

If we can predict whether a booster lands, we can predict the launch cost — a critical advantage for any company bidding against SpaceX.

---

## Project Structure

```
falcon-rocket/

 Data/                          # Raw and processed datasets (CSV)

 Data Wrangling/                # Cleaning, feature engineering, label creation

 Exploratory Data Analysis/     # EDA via SQL queries and Python visualizations

 DashBoard/                     # Interactive Plotly Dash web application

 Model/                         # ML model training, evaluation, and comparison

 data.ipynb                     # Entry-point notebook: data collection via SpaceX API
```

---

## Methodology

The project follows a complete data science lifecycle:

### 1. Data Collection
- **SpaceX REST API** — Fetches structured launch data: rocket version, payload mass, orbit type, launch site, landing outcome, and more
- **Wikipedia Web Scraping** — Collects historical Falcon 9 launch records using `BeautifulSoup`
- Data is normalized and stored as structured CSV files

### 2. Data Wrangling
- Handles missing values and inconsistent formats
- Encodes categorical features (orbit types, launch sites, booster versions) as dummy variables
- Creates the binary target label: **Class = 1 (successful landing)** or **Class = 0 (failed/no attempt)**

### 3. Exploratory Data Analysis (EDA)
- SQL-based analysis to identify patterns across launch sites, orbits, and payloads
- Visualizations with **Matplotlib** and **Seaborn**:
  - Launch success rate over time
  - Payload mass vs. landing outcome
  - Success rate by orbit type and launch site
  - Booster reuse trends

### 4. Interactive Dashboard
- Built with **Plotly Dash**
- Features a dropdown for filtering by launch site
- Pie charts for success vs. failure ratios
- Scatter plot: Payload Mass vs. Launch Outcome (with booster version color coding)

### 5. Machine Learning Models
Four classification algorithms are trained and compared:

| Model | Description |
|---|---|
| Logistic Regression | Baseline linear classifier |
| Support Vector Machine (SVM) | Hyperplane-based classification |
| Decision Tree | Rule-based, interpretable model |
| K-Nearest Neighbors (KNN) | Instance-based learning |

Models are evaluated using **accuracy**, **F1-score**, and **confusion matrices**. Hyperparameter tuning is performed via `GridSearchCV`.

---

## Key Features & Dataset Columns

| Feature | Description |
|---|---|
| `FlightNumber` | Sequential launch number |
| `Date` | Launch date |
| `BoosterVersion` | Falcon 9 variant (v1.0, v1.1, FT, Block 5) |
| `PayloadMass` | Payload in kg |
| `Orbit` | Target orbit (LEO, GTO, ISS, SSO, etc.) |
| `LaunchSite` | CCAFS LC-40, KSC LC-39A, VAFB SLC-4E |
| `Outcome` | Landing attempt result |
| `GridFins` | Whether grid fins were deployed |
| `Reused` | Whether the booster was reused |
| `Legs` | Whether landing legs were deployed |
| `LandingPad` | Target landing pad (if applicable) |
| `Block` | Booster block version |
| `ReusedCount` | Number of previous booster flights |
| `Class` | **Target variable** — 1 = success, 0 = failure |

---

## Key Insights

- **Launch success rate has improved dramatically** — from ~20% in early flights to near 100% after flight 80
- **Payload mass matters** — heavier payloads correlate with lower landing success rates
- **Launch site influences outcome** — KSC LC-39A has among the highest success rates
- **Booster reuse is a strong positive signal** — reused boosters tend to land more reliably
- **Block 5 boosters** (latest variant) achieve the highest consistency

---

## Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.8+ |
| Data Manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Dashboard | Plotly Dash |
| Machine Learning | scikit-learn |
| Data Collection | Requests, BeautifulSoup4 |
| Database / SQL | SQLite / IBM Db2 (via ipython-sql) |
| Environment | Jupyter Notebook |

---

## Getting Started

### Prerequisites

```bash
pip install pandas numpy matplotlib seaborn plotly dash scikit-learn requests beautifulsoup4
```

### Run the Notebooks

Clone the repository and open notebooks in order:

```bash
git clone https://github.com/mynkchn/falcon-rocket.git
cd falcon-rocket
jupyter notebook
```

Recommended execution order:

1. `data.ipynb` — Data collection from SpaceX API
2. `Data Wrangling/` — Clean and prepare the dataset
3. `Exploratory Data Analysis/` — Analyze patterns with SQL and plots
4. `DashBoard/` — Launch the interactive Plotly Dash app
5. `Model/` — Train and evaluate classification models

### Launch the Dashboard

```bash
cd DashBoard
python app.py
```

Open your browser at `http://127.0.0.1:8050`

---

## Business Problem

> *An aerospace startup wants to bid against SpaceX for a rocket launch contract. To price competitively, they need to estimate SpaceX's actual cost — which depends entirely on whether the Falcon 9 booster can be recovered.*

This project provides that capability. By predicting landing success from known pre-launch variables (payload mass, orbit, launch site, booster reuse history), companies can estimate whether SpaceX will incur booster manufacturing costs (~$50M) — and bid accordingly.

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgements

- [SpaceX REST API](https://github.com/r-spacex/SpaceX-API) — Open source community-maintained launch data
- [Wikipedia — List of Falcon 9 and Falcon Heavy Launches](https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches)
- IBM Data Science Professional Certificate — Capstone Project framework

---

<div align="center">
  <sub>Built by <a href="https://github.com/mynkchn">mynkchn</a></sub>
</div>
