
# AtmoSync Duplicate Record Handling

## Purpose

This document describes how duplicate records are identified and handled in the AtmoSync micro-climate dataset.

## 1. Duplicate Record Check

The dataset should be checked for completely duplicated rows.

The duplicate check helps identify repeated weather observations that may affect analysis results.

## 2. Identification

Duplicate records can be identified using the Pandas `duplicated()` function.

Example:

```python
df.duplicated().sum()
````

This returns the number of duplicate records.

## 3. Removing Duplicates

Duplicate records can be removed using:

```python
df = df.drop_duplicates()
```

The original raw dataset should not be modified directly.

## 4. Before and After Check

The number of duplicate records should be checked before and after removal.

Example:

```python
duplicates_before = df.duplicated().sum()

df = df.drop_duplicates()

duplicates_after = df.duplicated().sum()
```

## 5. Dataset Verification

After removing duplicates, verify:

* Number of remaining records
* Number of duplicate records
* Dataset shape
* Important columns are still present

## 6. Processed Dataset

The cleaned dataset should be saved in:

```text
dataset/processed/
```

The original raw dataset should remain unchanged in:

```text
dataset/raw/
```

## Final Objective

The duplicate handling process ensures that repeated records do not unnecessarily affect the AtmoSync analysis.


