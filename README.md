# Physical Activity and Public Health in Europe

## Project Overview

This project examines country-level associations between physical inactivity, obesity prevalence, and GDP per capita across countries in the WHO European Region.

The analysis uses 2022 data from the World Health Organization (WHO) and Eurostat. It combines data preparation, exploratory data analysis, correlation analysis, statistical hypothesis testing, and data visualisation.

The final analytical dataset contains **35 countries** with complete observations for all three indicators. The project is observational and cross-sectional; it investigates associations and does not establish causal relationships.

## Research Questions

The main research question is:

**How are physical inactivity, obesity prevalence, and GDP per capita associated across European countries?**

The analysis addresses three specific questions:

1. Is physical inactivity associated with obesity prevalence?
2. Is GDP per capita associated with physical inactivity?
3. Is GDP per capita associated with obesity prevalence?

## Data Sources

The project uses three indicators from two independent public data sources.

### World Health Organization (WHO)

- **Indicator:** Prevalence of insufficient physical activity among adults aged 18 years and over (age-standardized estimate).
- **Indicator code:** `NCD_PAA`
- **Measure:** Percentage of adults with insufficient physical activity.
- **Source:** [WHO indicator documentation](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/prevalence-of-insufficient-physical-activity-among-adults-aged-18-years-%28age-standardized-estimate%29-%28-%29)

### Eurostat

- **Obesity prevalence:** Adult obesity prevalence (BMI ≥ 30).
  - Dataset: `sdg_02_10`
  - [Eurostat dataset](https://ec.europa.eu/eurostat/databrowser/view/sdg_02_10/default/table?lang=en)
- **GDP per capita:** GDP at current market prices, expressed in euros per inhabitant.
  - Dataset: `nama_10_pc`
  - [Eurostat dataset](https://ec.europa.eu/eurostat/databrowser/view/nama_10_pc/default/table?lang=en)

All three indicators refer to **2022**. GDP per capita is expressed in current euros and is not adjusted for purchasing power standards (PPS).

## Methodology and Analysis

The project is organised into two Jupyter notebooks:

1. **`01_data_preparation.ipynb`** — explores the raw WHO and Eurostat datasets, extracts the relevant 2022 observations, examines data quality and geographical coverage, standardises country identifiers, validates the analytical variables, establishes the common 35-country sample, and integrates the datasets into a processed analytical dataset.
2. **`02_statistical_analysis.ipynb`** — performs exploratory data analysis, examines distributions and potential outliers, calculates Pearson and Spearman correlations, conducts correlation hypothesis tests, applies Holm's correction for multiple testing, visualises the relationships, and discusses the conclusions and limitations.

Spearman correlation is treated as the primary correlation measure in the interpretation, with Pearson correlation used as a complementary analysis. Statistical significance is assessed at the 0.05 level, with Holm correction applied to the three primary Spearman tests.

## Main Findings

The analysis identifies a moderate negative monotonic association between GDP per capita and physical inactivity across the 35 countries. This association remains statistically significant after Holm correction (Spearman's ρ ≈ -0.41; adjusted p-value ≈ 0.043).

The analysis does not find statistically significant evidence of an association between physical inactivity and obesity prevalence, or between GDP per capita and obesity prevalence, after correction for multiple testing.

These are country-level associations and should not be interpreted as evidence of individual-level relationships or causation.

## Project Structure

```text
physical-activity-public-health/
│
├── data/
│   ├── raw/
│   │   ├── who/                 # WHO source data (tracked with DVC)
│   │   └── eurostat/            # Eurostat source data (tracked with DVC)
│   └── processed/
│       └── analysis_dataset.csv # Integrated 35-country analytical dataset
│
├── notebooks/
│   ├── 01_data_preparation.ipynb
│   └── 02_statistical_analysis.ipynb
│
├── scripts/
│   └── download_data.py         # Downloads the original public datasets
│
├── .dvcignore
├── .gitignore
├── README.md
└── requirements.txt
```

The raw datasets and processed analytical CSV are managed with DVC. The `.dvc` directory contains local DVC configuration and is not required when retrieving the source data using the download script.

## Technologies

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- SciPy and Statsmodels
- PyCountry
- Jupyter Notebook
- Git and GitHub
- DVC

## Setup and Reproducing the Project

### 1. Prerequisites

- Python (the project has been developed with Python 3.x)
- Git

### 2. Clone the repository

```bash
git clone https://github.com/Edgybug/european-physical-activity-and-public-health.git
cd european-physical-activity-and-public-health
```

### 3. Create and activate a virtual environment

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Download the raw datasets

The original WHO and Eurostat datasets can be downloaded from their public sources using the provided script:

```bash
python scripts/download_data.py
```

The script saves the datasets in the appropriate subdirectories under `data/raw/`. Existing files are not overwritten by default. To download the datasets again and replace existing files, run:

```bash
python scripts/download_data.py --force
```

This source-download workflow does not require DagsHub credentials.

### 6. Run the notebooks

Start Jupyter:

```bash
jupyter notebook
```

Run the notebooks in this order:

1. `notebooks/01_data_preparation.ipynb`
2. `notebooks/02_statistical_analysis.ipynb`

The first notebook creates `data/processed/analysis_dataset.csv`, which is loaded by the second notebook.

## Data and Version Control

- Git tracks the notebooks, scripts, documentation, dependency list, and DVC metadata.
- DVC tracks the raw datasets and the processed analytical dataset.
- DagsHub is used as the DVC remote for project data versioning.
- Alternatively, the public-source download script can retrieve the original raw datasets without DagsHub access.

## Limitations

- The final analysis uses 35 countries with complete observations across all three indicators; this is not the full set of countries in the WHO European Region.
- The data represent a single year (2022), so the analysis cannot establish trends over time.
- Country-level results cannot be assumed to describe relationships between individuals (ecological fallacy).
- Correlation does not establish causation, and other factors may influence the observed relationships.
- GDP per capita is measured in current euros and is not adjusted for differences in purchasing power between countries.

## Project Status

The data preparation, integration, exploratory analysis, statistical testing, visualisations, conclusions, and limitations are documented in the two notebooks. The project is in its final review and submission-preparation stage.