# Weather History Analysis

A small exploratory data analysis project using historical weather data.

**Repository Structure**
- **Files:** [requirments.txt](requirments.txt) — Python dependencies (note: filename contains a typo).
- **Notebook:** [weather analysis.ipynb](weather%20analysis.ipynb) — main analysis and visualizations.
- **Data:** [data/weatherHistory.csv](data/weatherHistory.csv) — dataset used for the analysis.
- **Visuals:** [visualizations/](visualizations/) — output plots and images.

**Overview**
This repository contains a Jupyter Notebook that performs EDA and creates visualizations from the `weatherHistory.csv` dataset. The notebook demonstrates data cleaning, feature exploration, and example plots useful for weather pattern analysis.

**Getting Started**
1. Install Python (3.8+ recommended).
2. Create and activate a virtual environment.

Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirments.txt
jupyter notebook "weather analysis.ipynb"
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirments.txt
jupyter notebook "weather analysis.ipynb"
```

**What to look at**
- Open the notebook `[weather analysis.ipynb](weather%20analysis.ipynb)` to step through the analysis and regenerable plots.
- Data is loaded from `[data/weatherHistory.csv](data/weatherHistory.csv)`; adapt the path if you move the file.
- Generated figures are stored in the `[visualizations/](visualizations/)` folder.

**Notes & Tips**
- The dependency file is named `requirments.txt` (contains a spelling error). If you prefer, rename it to `requirements.txt` and update commands accordingly.
- If you encounter memory issues loading the full CSV, consider sampling or using chunked reads in the notebook.

**Next steps**
- Add a `requirements-dev.txt` or `environment.yml` for reproducible environments.
- Add a short script to export cleaned datasets and regenerate visualizations automatically.


