# Working with CSV Files - Day 15

## Import Library

```python
import pandas as pd
```

## Opening a Local CSV File

```python
df = pd.read_csv('aug_train.csv')
df
```

## Opening a CSV File from a URL

```python
import pandas as pd
import requests
from io import StringIO

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

response = requests.get(url)

df = pd.read_csv(StringIO(response.text))

print(df.head())
```

## sep Parameter

Used to specify the delimiter in the CSV file. For example, using tab separator:

```python
pd.read_csv('movie_titles_metadata.tsv', sep='\t', names=['sno', 'name', 'release_year', 'ratings', 'votes', 'generes'])
```

## Index_col Parameter

Specify which column to use as the index:

```python
pd.read_csv('aug_train.csv', index_col='enrollee_id')
```

## Header Parameter

Specify which row to use as column headers (0-indexed):

```python
pd.read_csv('aug_train.csv', header=1)
```

## Usecols Parameter

Select only specific columns to read:

```python
pd.read_csv('aug_train.csv', usecols=['enrollee_id', 'city', 'gender', 'education_level'])
```

## Squeeze Parameter

Convert a single column DataFrame into a Series:

```python
gender = pd.read_csv('aug_train.csv', usecols=['gender']).squeeze()
gender
```

## Skip Rows / Nrows Parameter

Skip specific rows during reading:

```python
pd.read_csv('aug_train.csv', skiprows=[0, 5])
```

## Encoding Parameter

Specify the file encoding (useful for non-ASCII characters):

```python
pd.read_csv('zomato.csv', encoding='latin-1')
```

## Skip Bad Lines

Handle malformed rows in the CSV file:

```python
pd.read_csv('BX-Books.csv', sep=';', encoding='latin-1', on_bad_lines='skip')
```

**Note:** `on_bad_lines='skip'` ignores malformed rows. Other valid values:

- `'error'` — stop on bad lines
- `'warn'` — skip and warn

## Dtypes Parameter

Specify data types for columns:

```python
pd.read_csv('aug_train.csv', dtype={'target': int})

# Verify data types
pd.read_csv('aug_train.csv', dtype={'target': int}).info()
```

## Handling Dates

Parse date columns using `parse_dates`:

```python
# Without parsing dates
pd.read_csv('IPL.csv').info()

# With parsing dates
pd.read_csv('IPL.csv', parse_dates=['date']).info()
```

## Converters

Apply custom functions to columns while reading:

```python
def rename(name):
    if name == "Royal Challengers Bangalore":
        return "RBC"
    else:
        return name

# Apply the converter function
pd.read_csv('IPL.csv', converters={'bowling_team': rename})
```

## na_values Parameter

Specify which values should be treated as NaN/missing:

```python
pd.read_csv('aug_train.csv', na_values=['Male'])
```

## Loading Large Datasets in Chunks

Read huge CSV files in smaller chunks to manage memory:

```python
dfs = pd.read_csv('aug_train.csv', chunksize=5000)

for chunks in dfs:
    print(chunks.shape)
```

---

## Summary of Key Parameters

| Parameter | Purpose |
|-----------|---------|
| `sep` | Specify delimiter/separator |
| `index_col` | Set a column as index |
| `header` | Specify header row |
| `usecols` | Select specific columns |
| `squeeze` | Convert single column to Series |
| `skiprows` | Skip specific rows |
| `encoding` | Specify file encoding |
| `on_bad_lines` | Handle malformed rows |
| `dtype` | Specify data types |
| `parse_dates` | Parse date columns |
| `converters` | Apply custom functions |
| `na_values` | Define missing values |
| `chunksize` | Read data in chunks |
