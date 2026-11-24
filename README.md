# Physical Activity and Public Health in Europe

## Project Overview

This project investigates the relationship between physical inactivity, obesity prevalence, and economic development across European countries.

The analysis focuses on 2022 and combines data from two independent sources: the World Health Organization (WHO) and Eurostat.

The project uses statistical analysis and data visualization to explore relationships between these indicators. The analysis is observational and focuses on country-level comparisons; it does not attempt to establish causal relationships.

## Research Questions

1. Is physical inactivity associated with obesity prevalence?
2. Is GDP per capita associated with physical inactivity?
3. Is GDP per capita associated with obesity prevalence?

## Data Sources

The project uses the following datasets:

- **WHO – Physical inactivity:** Prevalence of insufficient physical activity among adults, age-standardized estimates.
  - Indicator code: `NCD_PAA`
  - [WHO indicator documentation](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/prevalence-of-insufficient-physical-activity-among-adults-aged-18-years-%28age-standardized-estimate%29-%28-%29)

- **Eurostat – Obesity prevalence:** Adult obesity prevalence (BMI ≥ 30).
  - Dataset: `sdg_02_10`

- **Eurostat – GDP per capita:** GDP per capita at current market prices, expressed in EUR per inhabitant.
  - Dataset: `nama_10_pc`

The analysis uses 2022 as its reference year. Raw datasets may contain observations from additional years.

## Project Structure

```text
physical-activity-public-health/
│
├── data/
│   ├── raw/                 # Original datasets tracked with DVC
│   └── processed/           # Cleaned and transformed datasets
│
├── notebooks/               # Jupyter notebooks
│   └── data_exploartion.ipynb
├── scripts/                 # Reusable Python scripts
│   └── download_data.py
│
├── .dvc/                    # DVC configuration
├── .dvcignore
├── .gitignore
├── README.md
└── requirements.txt
```

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git and GitHub
- DVC (Data Version Control)
- DagsHub (DVC remote storage)

## Setup and Reproducing the Project

### 1. Prerequisites

- Python
- Git

### 2. Clone the repository

```bash
git clone https://github.com/Edgybug/european-physical-activity-and-public-health.git
cd european-physical-activity-and-public-health
```

### 3. Create a virtual environment

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
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

### 5. Download the datasets

The original datasets can be retrieved directly from their respective public sources using the provided download script.

Run:

```bash
python scripts/download_data.py
```

The script downloads the WHO physical inactivity data and both Eurostat datasets into `data/raw/`.

Existing files are not overwritten by default. To download the datasets again and replace existing files, use:

```bash
python scripts/download_data.py --force
```

DagsHub credentials are not required to retrieve the original datasets.

### 6. Run the notebooks

Start Jupyter:

```bash
jupyter notebook
```

Open the notebooks in the `notebooks/` directory and execute them in the intended order.

## Data Management

- Git tracks source code, notebooks, documentation, and DVC metadata.
- DVC tracks the raw datasets and their versions.
- DagsHub provides remote storage for the datasets used during project development.

The original public data sources and download script provide an alternative way to retrieve the raw datasets without requiring access to the DagsHub remote.

This separation keeps the Git repository lightweight while supporting data versioning and reproducibility.

## Project Status

The project is currently in the data exploration and preparation phase. Further analysis, statistical methods, and visualizations will be added as the project develops.