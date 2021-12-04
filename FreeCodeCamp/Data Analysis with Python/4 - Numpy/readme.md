# Data Analysis with NumPy

One of the most important libraries in data processing on Python.

It is a numeric computing library. It has a purposefully limited scope.
In python numeric processing is relatively slow, especially when working with larger datasets.

NumPy solves this issue by being an efficient numeric processing library that sits on top of Python and allows you to take advantage of the benefits of Python with the speed of more efficient numeric processing tools.

It lacks popularity because we don't often use NumPy itself very often. Normally you will be using other libraries such as matplotlib and pandas which both take advantage of NumPy.


### Low level explanation of how NumPy works

Back to basics of computers and numbers.

Computers don't work with decimal numbers directly. They are stored in memory as a combination of 1s and 0s (binary.)
Each 1 or 0 is a single bit.
8 bits is a single byte.
In order to store a decimal number you need to know the binary representation of that number.
So the question becomes how many decimal numbers can you store per a certain number of bits.
For example from 0 to 7 can be stored with 3 bits.

2**bits = number of decimal number you can store.

eg. 2**3 bits = 8 numbers (from 0 to 7)  

### How to use NumPy

NumPy only has a few objects; numbers, floats, integer floats, arrays and that's it.

#### Basic NumPy arrays:

To create a NumPy Array:
a = np.array([1,2,3,4,5]) - usually the contents between the brackets would be read from an external source.

Accessing elements in a NumPy Array is pretty similar to accessing elements in a Python array:
* individual element:
  * a[0] == 1
  * a[3] == 4
* slices:
  * a[1:3] == array(2,3)
  * a[::2] == array[1,2,5]
* multi-indexing (returns another numpy array):
  * a[[1,2,-1]] == array([1, 3, 5])

#### Array Types:
Numpy arrays need to have a datatype in order to take advantage of the speed optimisations that numpy provides over regular python arrays. (Due to efficiencies in memory allocation for numbers)

By default using whole numbers, numpy arrays are 'int64' - 64 bit integers.
If your array has decimals, numpy will automatically give the numbers the datatype of float64.
You can print the datatype of your array with a.dtype

You can force datatypes for your array with "dtype=":
* b = np.array([1,2,3,4,5], dtype=np.int8)
  * b.dtype == dtype('int8')
  * 'b' will be more efficient than 'a' due to the smaller size (int8 vs. int64)

You can also store strings (dtype('<U1')) in numpy but it doesn't have an advantage over storing them in regular python arrays

### Dimensions and shapes
#### Multidimensional arrays
Like in Python, Numpy arrays can store arrays within arrays. These are called multidimensional arrays.

* A = np.array([
    [1,2,3],
    [7,8,9]
  ])
* B = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
  ])
* C = np.array([
    [
      [1,2,3],
      [4,5,6]  
    ],
    [
      [7,8,9],
      [10,11,12]
    ]
  ])

To describe the shape of the array, we can use shape:
* A.shape == (2,3)
  * This is 2 rows and 3 cols
* B.shape == (3,4)
  * 3 rows and 4 cols.
* C.shape == (2,2,3)
  * 2 lists, 2 rows, 3 columns

To display the number of dimensions you can use ndim:
* A.ndim == 2
* B.ndim == 2
* C.ndim == 3

To get the total number of elements in the array we can use size:
* A.size == 6
* B.size == 12
* C.size == 12

Multidimensional arrays must be consistent in shape. If they are not, then the array will be created in datatype object.

Indexing and slicing multidimensional arrays works in the way you would expect:
* B[0] == array([1,2,3,4])
* B[0][1] == 2

You can also use the multidimensional selection from numpy to achieve the same result:
* B[0,1] == 2
* C[1,0,2] == 9

One advantage of this notation is the ability for us to use slicing:
* B[0:2] == array([[1,2,3,4],[5,6,7,8]])
  * Note: Remember that this does not return the array at the 2nd index because python slicing only goes to the upper limit, but does not include it!
* B[:, :2] == array([[1,2],[5,6],[9,10]])
  * This selects from every row, the elements at the 0th and 1st positions.
* B[:2, 1:3] == array([[2,3],[6,7]])
  * This selects from the first 2 rows, the elements at positions 1 and 2

To modify multidimensional arrays:
* B[1] = np.array([10,10,10,10])
  * this replaces the existing array at the 1st position in B with [10,10,10]
  * therefore we end up with: B = np.array([
      [1,2,3,4],
      [10,10,10,10],
      [9,10,11,12]
    ])
You can also do this with expansion operations like so:
* B[2] = 99
  * B = np.array([
      [1,2,3,4],
      [10,10,10,10],
      [99,99,99,99]
    ])

### NumPy Array Operations
NumPy has a large number of built-in operations that can be applied to numpy arrays.
These include:
* a.sum => returns the sum of an array
* a.mean => returns the mean of an array
* a.std => returns the standard deviation of an array
* a.var => returns the variance of an array

These operations can be applied per axis like so in multidimensional arrays:
* B.sum(axis=0) => returns the sum of the vertical axes of a multidimensional array as a new array
* B.mean(axis=0) => returns the mean of vertical axis of a multidimensional array as a new array
* B.std(axis=0) => returns the standard deviation of the vertical axis of a multidimensional array as a new array
* B.var(axis=0) => returns the variance of the vertical axis of a multidimensional array as a new array

axis=1 will do the same thing but horizontally. For arrays with more than 2 dimensions you can just continue to increase the y in axis=y

### Broadcasting and Vectorized operations
So everything we've seen so far can be done in Python arrays and you might think, why do I need a whole new library to work do this. Broadcasting and Vectorized operations are a (or maybe 'the') fundamental advantage of NumPy over standard python array operations.

These broadcast operations apply the same operation to the whole array. So, for example;
* a = np.arange(4) == array[0,1,2,3]
* a + 10 == array[10,11,12,13]
  * as you can see, this broadcast operation added 10 every element in the array 'a'
* a * 10 == array[0, 10, 20 , 30]
  * Similarly, this broadcast operation multiplied every element by 10.

These broadcast operations are extremely well optimised, so they are very useful for high performance work.
It is useful to note here that these operations return new arrays. 'a' still returns array([0,1,2,3]). The broadcast operations haven't changed the original array but are returning new arrays.
If you want to override this behaviour you can use +=, *=, etc.
* a *= 100 = array([0, 100, 200, 300])
  * so now: a == array([0, 100, 200, 300])

These operations are not limited to integers or floats, but can also apply an array of operations to another array. < That's horribly written, but I know what I mean. Do you???
Here's an example of vectorized operations:
* a = arange(4)
* a == array[0,1,2,3]
* b = np.array[(10,10,10,10)]
* a + b == array[(10,11,12,13)]
  * as you can see, when we add a and b together, the first element of each array are added together, the second element of each array is added together and so on and so forth.

You can do the same thing with multiplication:
* Using the same a and b arrays
* a * b == array[(0, 10, 20, 30)]

NOTE: in order to do vectorized operations, the two relevant arrays must line up. For example, you can't multiply a 7 item array by a 25 item array. It returns "ValueError: operands could not be broadcast together with shapes (7,) (25,)"

### Boolean Arrays (aka masks)
Another way to select elements from an array is to use a boolean array:
* a = np.arange(5)
  * a == array([0,1,2,3,4])
If we wanted to select the first, second and fourth elements, we could do the following:
* a[[True, True, False, True, False]] == array([0,1,3])  
This is the same as doing a[[0,1,3]]

So why would this be useful? Boolean arrays are the output of some array operations in NumPy.
For example:
* a >= 2 == array([False, False, True, True, True])
Obviously this is really useful because you can pick out elements of an array that have certain conditions.
An easy way to do this is by combining the Boolean operation with the Boolean element selection described above. This will look like this:
* a[a>=2]
  * expanding this out step by step:
  * a[array([False, False, True, True, True])] == array([2,3,4])

This means that you 
