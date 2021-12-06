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

### Pandas Dataframes
Wildly innacurrately but useful in terms of learning, a dataframe is kinda like an excel table. In fact dataframes are often created from .csv files.

A dataframe column is basically made up of pandas series. This means that dataframes have indices like a python list.

df = pd.DataFrame({
  'Population': [35.333, 63.345, 80.94, 60.2123, 127.998, 64.123, 318.666],
  'GDP' : [17173664,12321345,12334555,11334343,555545456,213123123,56564565],
  'Continent': ['America', 'Europe', 'Europe', 'Europe', 'Asia', 'Europe', 'America']
  }, columns=['Population', 'GDP', 'Continent']
)
Note that DataFrame has a capital D and a capital F!

You can name the indexes in the same way as you can in a Series
* df.index = ['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom', 'United States']

#### Commonly used DataFrame Methods
* df.info
  * Gives information on structure of the DataFrame including memory usage
* df.size
  * Gives the number of elements in the DataFrame
* df.shape
  * Gives the number of rows and columns in the DataFrame
* df.describe
  * Gives the result of some basic mathematical operations on numeric columns (i.e. not objects!) in the DataFrame
* df.dtypes
  * Returns the type of the columns of the columns

#### Indexes, Selections and Slicing data in a DataFrame
* df.loc['Canada']
  * select the row by its text index
* df.iloc[0]
  * select the row by its numeric index (position)
* df['Population']
  * Select the relevant column
All of the above methods for selecting data from a DataFrame returns a Series!

Slicing works in the same way as above with the same caveat as for Series in that a slice in Pandas includes the Upper Limit (unlike a python list)

* df.loc['France':'Italy'] ==          
                 Population       GDP Continent
        France      63.3450  12321345    Europe
        Germany     80.9400  12334555    Europe
        Italy       60.2123  11334343    Europe

* df.loc['France':'Italy', 'Population'] ==
        France     63.3450
        Germany    80.9400
        Italy      60.2123
        Name: Population, dtype: float64
* df.loc['France':'Italy', ['Population', 'GDP']] ==
                 Population       GDP
        France      63.3450  12321345
        Germany     80.9400  12334555
        Italy       60.2123  11334343

iloc is very similar to multi-indexing in Series.
* df.iloc[[0, 2, 3] ==
                 Population       GDP Continent
        Canada      35.3330  17173664   America
        Germany     80.9400  12334555    Europe
        Italy       60.2123  11334343    Europe

The tutorial recommends always using loc and iloc to select rows and the nake dataframe to select columns in order to reduce ambiguity in your code

#### Conditional Selection
Conditional selection works in a similar way to series.

For example if we wanted to select data for all the countries that have a population greater than 70 (in mySQL this would look something like SELECT * WHERE 'Population' > 70)

First of all, we create a boolean series that checks that conditional:
* df['Population'] > 70 ==
    Canada            False
    France            False
    Germany            True
    Italy             False
    Japan              True
    United Kingdom    False
    United States      True
    Name: Population, dtype: bool

We can use this boolean series in a .loc selection to get the data for the rows that fulfil the conditional.
* df.loc[df['Population'] > 70] ==
                   Population        GDP Continent
    Germany            80.940   12334555    Europe
    Japan             127.998  555545456      Asia
    United States     318.666   56564565   America

If you just want certain columns, you can do this in the way you normally would using .loc
* df.loc[df['Population'] > 70, ['Population', 'GDP']] ==
                   Population        GDP
    Germany            80.940   12334555
    Japan             127.998  555545456
    United States     318.666   56564565

#### Dropping
The opposite of selection is to drop. Instead of looking for a certain row, you can ask pandas to return to you all the rows except the ones you specify. This is down with the .drop method.

* df.drop('Canada') ==
                    Population        GDP Continent
    France             63.3450   12321345    Europe
    Germany            80.9400   12334555    Europe
    Italy              60.2123   11334343    Europe
    Japan             127.9980  555545456      Asia
    United Kingdom     64.1230  213123123    Europe
    United States     318.6660   56564565   America

#### Operations in series
Operations in series work at a column level, broadcasting down the rows.

In this example we are creating a new series called 'crisis'
* crisis = pd.Series([-20,-1000000], index=['Population', 'GDP'])

Currently our dataframe for those two columns looks like this:
* df[['Population', 'GDP']] ==
                      Population        GDP
      Canada             35.3330   17173664
      France             63.3450   12321345
      Germany            80.9400   12334555
      Italy              60.2123   11334343
      Japan             127.9980  555545456
      United Kingdom     64.1230  213123123
      United States     318.6660   56564565

Now let us apply crisis to the DataFrame above:
* df[['Population', 'GDP']] + crisis ==
                      Population        GDP
      Canada             15.3330   16173664
      France             43.3450   11321345
      Germany            60.9400   11334555
      Italy              40.2123   10334343
      Japan             107.9980  554545456
      United Kingdom     44.1230  212123123
      United States     298.6660   55564565

We can see that the GDP column have been decreased by 1,000,000 and the population column have all decreased by 20!

### Modifying DataFrames
None of the operations that we've done so far have had any effect on the underlying DataFrames. They are returning new DataFrames. This is because these operations are 'immutable'

One quick way to modify a DataFrame is simply to save the results of your operation in a variable. If you want to get rid of the old data and just use the new DataFrame you can always use your original variable name.
* df2 = df + crisis ==  
                     Continent          GDP  Population
      Canada               NaN   16173664.0     15.3330
      France               NaN   11321345.0     43.3450
      Germany              NaN   11334555.0     60.9400
      Italy                NaN   10334343.0     40.2123
      Japan                NaN  554545456.0    107.9980
      United Kingdom       NaN  212123123.0     44.1230
      United States        NaN   55564565.0    298.6660

#### Explicit Modification
Say we wanted to add a column to df. We can create a series for the new column like normal:
* lang = pd.Series(['French','German','Italian'], index=['France', 'Germany', 'Italy'], name='Language')
  * lang ==
        France      French
        Germany     German
        Italy      Italian
        Name: Language, dtype: object

We can simply add this series to df with the following syntax:
* df['Language'] = lang
  * now df ==
                      Population        GDP Continent Language
      Canada             35.3330   17173664   America      NaN
      France             63.3450   12321345    Europe   French
      Germany            80.9400   12334555    Europe   German
      Italy              60.2123   11334343    Europe  Italian
      Japan             127.9980  555545456      Asia      NaN
      United Kingdom     64.1230  213123123    Europe      NaN
      United States     318.6660   56564565   America      NaN

Note that the lang series did not have indexes that matched every row in the DataFrame, but this did not matter. Pandas was smart enough to apply the contents in the relevant rows.

If you want to change all the values in a column, the syntax is similar to adding the series above:
* df['Language'] = 'English'
  * df ==
                      Population        GDP Continent Language
      Canada             35.3330   17173664   America  English
      France             63.3450   12321345    Europe  English
      Germany            80.9400   12334555    Europe  English
      Italy              60.2123   11334343    Europe  English
      Japan             127.9980  555545456      Asia  English
      United Kingdom     64.1230  213123123    Europe  English
      United States     318.6660   56564565   America  English

##### Usually if there is an '=' symbol you are changing the underlying data not creating a new DataFrame as when you broadcast an operation.

To rename a column you can use the Pandas .rename method. Remember that the rename method is immutable so it doesn't change the underlying DataFrame but returns a new one instead.

* df.rename(
    columns={'GDP': 'Gross Domestic Product', 'HDI': 'Human Development Index'},
    index={'United States': 'US', 'United Kingdom': 'UK', 'Neverland':'Was never here'}
    )
    * This returns a new DataFrame that looks like this:
               Population  Gross Domestic Product Continent Language
      Canada      35.3330                17173664   America  English
      France      63.3450                12321345    Europe  English
      Germany     80.9400                12334555    Europe  English
      Italy       60.2123                11334343    Europe  English
      Japan      127.9980               555545456      Asia  English
      UK          64.1230               213123123    Europe  English
      US         318.6660                56564565   America  English

Note that even where we try to rename columns or indexes that do not exist in the original DataFrame, this doesn't throw a error, it just continues on. 
