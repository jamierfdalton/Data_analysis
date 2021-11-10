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
