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

NumPy has an object called np.nan (not a number) which is used to identify null values. It is similar to Python's None value but obviously numpy has some major memory usage and speed benefits over vanilla Python.

There are 2 synonymous functions for evaluating if a value is a null value. They can be used interchangeably:
* pd.isnull(np.nan) == True
* pd.isna(np.nan) == True

For evaluating if an value is not a null value we have the equivalent opposites to;
* pd.notnull(np.nan) == False
* pd.notna(np.nan) == False

We can pass either Series or DataFrames to these null evaluation functions. They will return a new Series or DataFrame with boolean values:

* pd.isnull(pd.Series([1,2,None,3])) ==
  * 0    False
    1    False
    2     True
    3    False
    dtype: bool

* pd.notnull(pd.DataFrame({
    'Column A': [1,2,None,4],
    'Column B': [None,2,8,4],
    'Column C': [1,2,'A string',4],
    'Column D': [None,4, np.nan, 9],
    }))
  * ==    Column A  Column B  Column C  Column D
      0      True     False      True     False
      1      True      True      True      True
      2     False      True      True     False
      3      True      True      True      True

  A particularly useful operation to do on an null evaluation is to sum up its values, because that can show how many null values we have to deal with in our dataset.

  * eg = pd.Series(['a','b',2,None,None,5])
  * pd.isnull(eg) ==
    * 0    False
      1    False
      2    False
      3     True
      4     True
      5    False
      dtype: bool
  * pd.isnull(eg).sum() == 2

You can also use these evaluations to filter a series. In order to get all the values that are not-null you might do this:

* eg[pd.notnull(s)] ==
  * 0    a
    1    b
    2    2
    5    5
    dtype: object

Finally these evaluation functions can be used as methods which simplifies writing them:

* eg.isnull() == pd.isnull(eg)
* eg.notnull() == pd.notnull(eg)
* etc.

Another way to get all a series or DataFrame wihout the null values is .dropna()
* eg.dropna() == eg[eg.notnull()]

Finally remember that all of these functions and methods are immutable. We are not changing the underlying data, but instead returning a new Series or DataFrame!
