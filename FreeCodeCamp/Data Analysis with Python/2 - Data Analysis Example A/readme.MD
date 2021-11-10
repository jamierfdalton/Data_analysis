# Notes for Learn Data Analysis Example A

### Import python libraries
* Numpy as np
* pandas as pd
* matplotlib.pyplot as plt

### Loading Data

* Not sure I understand what the !head in !head data/sales_data.csv is
data/sales_data.csv is the location of our data.

* Then assign the csv to a variable called sales using pandas
* sales = pd.read_csv(
    'data/sales_data.csv',
    parse_dates=['Date'])

### Understanding the data without a visual representation of all lines

* sales.head() gives the top 5 rows and the headers of the dataset.
* sales.shape() gives us the number of rows and columns of the dataset.
* sales.info() returns information about the columns of the dataset. Their indexes, titles, datatypes, etc.
* sales.describe() returns information about the contents of the columns such as the total number of entries, the mean, min, max and various percentages.
* you can get the same information for a single column with sales['Unit_Cost'].describe() or more generally datasetVariable['columnName'].describe()

### Analysing a single column

* Whilst "sales.descibe()" describes the whole dataframe, "sales['Unit_Cost'].describe()" describes only the column designated. (In this case Unit_Cost)
* You can do a similar thing with .mean or .median to get the mean or median of that column
* .value_counts returns the number of occurences of values in a dataset. (Can also be applied to a single column in the normal way)
* You can create a plot using matplotlib with the .plot method. (See the Pandas and Matplotlib lessons for more information)
* Examples of chart types:
    * box: kind='box'
    * density: kind='density'
    * histogram: kind='hist'
    * pie chart: kind='pie'
    * bar chart: kind='bar'
    * scatter chart: kind='scatter'
* Correlation analysis can be done with sales.corr() which returns a value between 0 and 1 for how strongly correlated the values in the columns are.
* Correlation analysis can be output to a matrix for visualisation using matplotlib. (More in depth in the data visualisation section)
