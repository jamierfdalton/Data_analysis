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
