# Data Cleaning with Pandas
### 6 Step Process for Cleaning Data

1. Remove irrelevant data.
2. Deduplicate your data.
3. Fix structural errors.
4. Deal with missing data.
5. Filter out data outliers.
6. Validate your data.

FreeCodeCamp's tutorial only talks about a 4 step process in high level terms. I like this 6 step process because it includes Removing irrelevant data and deduplicating data. The rest of the tutorial is mostly focused on dealing with missing data and invalid data (either by domain or structural errors)

### Pandas Utility functions
As we already know, Pandas is built on top of numpy so they share some of the same elements that are can be useful for dealing with missing data.

NumPy has an object called nan (not a number) which is used to identify null values. It is similar to Python's None value but obviously numpy has some major memory usage and speed benefits over vanilla Python.
