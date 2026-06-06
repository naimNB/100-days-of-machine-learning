# 100 Days of Machine Learning

A curated collection of notes, Jupyter notebooks, and small projects created while following the CampusX "100 Days of ML" learning path. The repository is intended as a personal learning log and lightweight demos of common ML concepts.

Table of contents

- Project overview
- Repository structure
- Quick setup
- Running notebooks
- Running the placement demo
- Data description
- Suggestions & contributions

Repository structure

- `Basic ML/` — Jupyter notebooks, learning notes, and experiment files. Notebooks may include exploratory code, visualizations, and short writeups.
- `placement problem/` — A small Flask demo app demonstrating a placement prediction flow. Contains `app.py`, `Placement.csv`, and `templates/`.

Quick setup (recommended)

1. Create a Python virtual environment and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

1. Install common data-science packages (create `requirements.txt` if the project doesn't provide one):

```bash
pip install --upgrade pip
pip install jupyterlab numpy pandas scikit-learn matplotlib seaborn flask
```

Running the notebooks

- Start Jupyter Lab (recommended) or Notebook in the repository root and open files under `Basic ML/`:

```bash
jupyter lab
# or
jupyter notebook
```

- Notes: Some notebooks are exploratory or duplicated (e.g., `day_1.ipynb`, `day1.ipynb`). Use the most recent or best-formatted file when following a lesson.

Running the placement demo app

1. Change into the app directory and (optionally) create a virtualenv there:

```bash
cd "placement problem"
python3 -m venv .venv
source .venv/bin/activate
```

1. If a `requirements.txt` is present install it; otherwise install `flask`:

```bash
pip install -r requirements.txt  # if provided
# or
pip install flask pandas scikit-learn
```

1. Run the app:

```bash
python3 app.py
```

1. Open `http://127.0.0.1:5000` in your browser to use the demo.

Data description

- `placement problem/Placement.csv`: tabular dataset used by the Flask demo. Typical columns include student features (scores, internships, etc.) and a target indicating placement outcome. Inspect the CSV header to confirm available fields.

Contributing & suggestions

- This repository is a personal learning log. If you want a clearer structure, reproducible requirements, or a cleaned set of notebooks, I can:
 	- Add a `requirements.txt` and a minimal `setup.sh` or `Makefile`.
 	- Standardize notebook filenames and remove duplicates.
 	- Add short READMEs inside each subfolder with per-project usage steps.

License

- Add a license file if you want to share these examples publicly (MIT, Apache-2.0, etc.).

Questions or next steps

- Tell me which sections you'd like expanded (installation, dataset schema, examples), and I will update the README or add supporting files.
