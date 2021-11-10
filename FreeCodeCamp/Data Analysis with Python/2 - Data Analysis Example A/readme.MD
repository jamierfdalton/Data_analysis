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

### Creating a new column from Existing columns

* In order to make a Calculated Revenue column from the existing Cost column and Profit Column, the syntax is very straight forward:
    * sales['Calulated_Revenue'] = sales['Cost'] + sales['Profit'] (Revenue = Cost + Profit) where Calulated_Revenue is the name of the new column and Cost and Profit are both existing columns
    * You can then display the top 5 results from the new column with sales['Calculated_Revenue'].head() as normal.
    * As there is an pre-existing sales['Revenue'] column, it is easy for us to check mistakes in data entry by using the following comparison
        * sales['Calculated_Revenue'] != sales['Revenue'].sum()
        * This returns the number of rows in which Calculated_Revenue is different to 'Revenue'
        * If you don't use .sum() the output is is the True/False value for the comparison on each row. Therefore if you sum them (because False = 0 and True = 1) you return the actual number of rows where you have a discrepancy.
* Similarly to make a 'Revenue_per_Age' column the syntax would be:
    * sales['Revenue_per_Age'] = sales['Revenue'] / sales['Customer_Age']

### Manipulating Existing columns

* If for instance you needed to update the unit price of all the rows by 3% you can use the following syntax
    * sales['Unit_Price'] *= 1.03

### Filtering

* To filter you can use .loc[]
    * sales.loc[sales['State'] == 'Kentucky']
    * sales.loc[sales[Age_Group] == 'Adults (35-64)']
    * DataFrame.loc[DataFrame[Column_Name] == 'Value']
* You can also use .loc to return the output of pandas operations on a filter like so:
    * sales.loc[sales['Age_Group'] == 'Adults (35-64)', 'Revenue'].mean()
    * sales.loc[sales['Age_Group'] == 'Adults (35-64)', 'Revenue'].sum()

* More data is available on the relevant modules.

### Working with Databases

* As before we import:
    * Numpy as np
    * pandas as pd
    * matplotlib.pyplot as plt
* But we also need the sqlite3 module:
    * import sqlite3

* Next we need to connect to our database.
    * conn = sqlite3.connect('data/sakila.db')
    * data/sakila.db is the location of our database (obviously)

* Next we can use sql commands to create our DataFrame which we are calling df like so:
    * df = pd.read_sql('''INSERT SQL COMMANDS HERE''')

* Now df is a dataframe we can use pandas methods to help us analyse the data just like when we were working from CSV
    * df.head() returns the top 5 rows and the headers for our new dataframe.
