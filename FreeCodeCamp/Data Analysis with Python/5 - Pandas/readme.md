# Data Analysis with pandas

pandas is a very important library for python data analysis.

The elements of data analysis are something like this:
1. Get data from source
2. Clean data if necessary
3. Processing data
4. Visualising Data
5. Create reports
6. Statistical Analysis
pandas is useful in all the areas above.

Before starting with pandas it is important to import numpy as pandas is built on top of it.
* import pandas as pd
* import numpy as np

### Pandas Series
In general pandas has two main data structures; the series and the dataframe. We are going to start with the series.
The concept of a series is an ordered sequence of elements, indexed.
* g7_pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])
   * g7_pop ==
      0     35.467
      1     63.951
      2     80.940
      3     60.665
      4    127.061
      5     64.511
      6    318.523
      dtype: float64

As you can see this series has an associated datatype. We saw these datatypes when looking at numpy arrays and this is because the underlying datastructure that pandas is using to create a series is a numpy array.

However, a pandas series has a few more features than a numpy array. For example it can be named:
* g7_pop.name = 'G7 Population in Millions'
  * g7_pop ==
      0     35.467
      1     63.951
      2     80.940
      3     60.665
      4    127.061
      5     64.511
      6    318.523
      Name: G7 Population in Millions, dtype: float64

You can return the datatype with
* g7_pop.dtype == dtype('float64')

You can return the values of the series with:
* g7_pop.values == array([ 35.467,  63.951,  80.94 ,  60.665, 127.061,  64.511, 318.523])

 You can select elements as you would in a list (or numpy array) because pandas series have indexes.
 * g7_pop[0] == 35.467

However, there is a big difference between a pd.Series and a python list: we can arbitrarily assign indexes.
So for example:
* g7_pop.index = ['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom', 'United States']
  * >>> g7_pop ==
          Canada             35.467
          France             63.951
          Germany            80.940
          Italy              60.665
          Japan             127.061
          United Kingdom     64.511
          United States     318.523
          Name: G7 Population in Millions, dtype: float64
So now you can use g7_pop['Canada'] to get the Canada indexed element from the series like so:
* g7_pop['Canada'] == 35.467

So now a series is kinda like a dictionary in that they have named indexes which are very similar to keys, but they are ordered like a python list so you can still work with them sequentially.

#### Pandas Series Indexing

You can use .iloc to locate by sequential position in the Series:
* g7_pop.iloc[2] == 80.940
* g7_pop.iloc[-1] == 318.523

Series also supports multi-indexing (returns a new series):
* g7_pop[['Germany', 'France', 'Italy']] == Germany    80.940
                                            France     63.951
                                            Italy      60.665
                                            Name: G7 Population in Millions, dtype: float64


Pandas Series also support slicing, BUT the UPPER LIMIT IS INCLUDED (unlike Python or NumPy slicing):
* g7_pop['Canada':'Italy'] == Canada     35.467
                              France     63.951
                              Germany    80.940
                              Italy      60.665
                              Name: G7 Population in Millions, dtype: float64

#### Pandas Boolean Series
In the same way as broadcasting to NumPy arrays, you can apply both mathematical and boolean operations to Pandas Series.
For instance:
* g7_pop * 100000 ==  Canada             3546700.0
                      France             6395100.0
                      Germany            8094000.0
                      Italy              6066500.0
                      Japan             12706100.0
                      United Kingdom     6451100.0
                      United States     31852300.0
                      Name: G7 Population in Millions, dtype: float64

* g7_pop > 70 ==  Canada            False
                  France            False
                  Germany            True
                  Italy             False
                  Japan              True
                  United Kingdom    False
                  United States      True
                  Name: G7 Population in Millions, dtype: bool

* g7_pop.mean() == 107.30257142857144

* g7_pop[g7_pop > g7_pop.mean()] == Japan            127.061
                                    United States    318.523
                                    Name: G7 Population in Millions, dtype: float64

You can also use logical operators such as '&' and '|' to create more sophisticated filtering.
There are some inbuilt mathematical operations such as .mean and .log (THIS SECTION CAN BE EXPANDED)

#### Modifying series
Modifying series uses a familiar syntax:
* g7_pop['Canada'] = 40.5
  * g7_pop == Canada             40.500
              France             63.951
              Germany            80.940
              Italy              60.665
              Japan             127.061
              United Kingdom     64.511
              United States     318.523
              Name: G7 Population in Millions, dtype: float64
  * You can do the same operation with iloc or boolean indexing
* g7_pop[g7_pop > 70] = 278
  * This says wherever an element is greater than 70, modify that element to 278.
  * g7_pop == Canada             40.500
              France             63.951
              Germany           278.000
              Italy              60.665
              Japan             278.000
              United Kingdom     64.511
              United States     278.000
              Name: G7 Population in Millions, dtype: float64