# Notes for the Python for Data Analysis
#### by Wes McKinney

## 1. Preliminaries
### Essential Libraries
#### 1. NumPy
Contains a fast multidimensional array object *ndarray*
For numerical data, NumPy arrays are much more efficient ways of storing and manipulating data. It also contains a number of tools for common data wrangling and processing tasks (linear algebra, random number gen, etc.) It also integrates nicely with FORTRAN, C and C++ which are commonly used languages for fast processing due to their compiled nature and lack of a GCL.
#### 2. pandas
This is the primary tool that will be used in this book. It contains a useful 2d dimensional array data structure called a DataFrame that combines the speed of NumPy with the flexible data manipulation.
Has some additional benefits for financial data and is based on the R data.frame
#### 3. matplotlib
Helps the user to easily produce interactive plots and charts from data.
#### 4. IPython
An enhance python shell that is highly recommended by the author of this book. I might try and stick with my current workflow, but if it becomes difficult I will move to that instead.
#### 5. SciPy
A collection of packages for addressing common problems in scientific computing.
Combined with NumPy this package makes a reasonable replacement for MATLAB.
