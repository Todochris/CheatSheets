# Python Libraries CheatSheet
Cheat Sheet for Python libraries, taken from multiple sources.
Modified by Christian Toderascu.

**last update: 20231017**

last update available on [GitHub - Python libs CheatSheet.md](https://github.com/Todochris/CheatSheets/blob/main/Python%20libs%20CheatSheet.md)


## NumPy

[NumPy](http://www.numpy.org) is the fundamental package for scientific computing with Python. Here are the [official docs](https://docs.scipy.org/doc/numpy/).

If you don't already have it **installed**, you can do so using Pip:
```
$ pip install numpy
```

### Basics

One of the most commonly used functions of NumPy are *NumPy arrays*: The essential difference between *lists* and *NumPy arrays* is functionality and speed. *lists* give you basic operation, but *NumPy* adds FFTs, convolutions, fast searching, basic statistics, linear algebra, histograms, etc.</br>
The most important difference for data science is the ability to do **element-wise calculations** with *NumPy arrays*.

`axis 0` always refers to row </br>
`axis 1` always refers to column

| Operator     | Description   
| :------------- | :------------- |
|`np.array([1,2,3])`|1d array
|`np.array([(1,2,3),(4,5,6)])`|2d array
|`np.arange(start,stop,step)`|range array

#### Placeholders
| Operators | Description 
| :------------- | :------------- |
|`np.linspace(0,2,9)`|Add evenly spaced values btw interval to array of length 
|`np.zeros((1,2))`|Create and array filled with zeros
|`np.ones((1,2))`|Creates an array filled with ones
|`np.random.random((5,5))`|Creates random array
|`np.empty((2,2))`|Creates an empty array

#### Examples

```python
import numpy as np

# 1 dimensional
x = np.array([1,2,3])
# 2 dimensional
y = np.array([(1,2,3),(4,5,6)])

x = np.arange(3)
>>> array([0, 1, 2])

y = np.arange(3.0)
>>> array([ 0.,  1.,  2.])

x = np.arange(3,7)
>>> array([3, 4, 5, 6])

y = np.arange(3,7,2)
>>> array([3, 5])
```

</br>

### Array
#### Array Properties
|Syntax|Description
|:-------------|:-------------|
|`array.shape`|Dimensions (Rows,Columns)
|`len(array)`|Length of Array
|`array.ndim`|Number of Array Dimensions
|`array.size`|Number of Array Elements
|`array.dtype`|Data Type
|`array.astype(type)`|Converts to Data Type
|`type(array)`|Type of Array

#### Copying/Sorting <a name="gops"></a>
| Operators | Descriptions     | Documentation |
| :------------- | :------------- | :----------- |
|`np.copy(array)`|Creates copy of array
|`other = array.copy()`|Creates deep copy of array
|`array.sort()`|Sorts an array
|`array.sort(axis=0)`|Sorts axis of array

##### Examples <a name="array-example"></a>
```python
import numpy as np
# Sort sorts in ascending order
y = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
y.sort()
print(y)
>>> [ 1  2  3  4  5  6  7  8  9  10]
```

### Array Manipulation Routines

#### Adding or Removing Elements
|Operator|Description|
|:-----------|:--------|
|`np.append(a,b)`|Append items to array
|`np.insert(array, 1, 2, axis)`|Insert items into array at axis 0 or 1
|`np.resize((2,4))`|Resize array to shape(2,4)
|`np.delete(array,1,axis)`|Deletes items from array

##### Example
```python
import numpy as np
# Append items to array
a = np.array([(1, 2, 3),(4, 5, 6)])
b = np.append(a, [(7, 8, 9)])
print(b)
>>> [1 2 3 4 5 6 7 8 9]

# Remove index 2 from previous array
print(np.delete(b, 2))
>>> [1 2 4 5 6 7 8 9]
```

#### Combining Arrays
|Operator|Description|
|:---------|:-------|
|`np.concatenate((a,b),axis=0)`|Concatenates 2 arrays, adds to end
|`np.vstack((a,b))`|Stack array row-wise
|`np.hstack((a,b))`|Stack array column wise

##### Example
```python
import numpy as np
a = np.array([1, 3, 5])
b = np.array([2, 4, 6])

# Stack two arrays row-wise
print(np.vstack((a,b)))
>>> [[1 3 5]
     [2 4 6]]

# Stack two arrays column-wise
print(np.hstack((a,b)))
>>> [1 3 5 2 4 6]
```

#### Splitting Arrays <a name="split"></a>
|Operator|Description|
|:---------|:-------|
|`numpy.split()`|
|`np.array_split(array, 3)`|Split an array in sub-arrays of (nearly) identical size
|`numpy.hsplit(array, 3)`|Split the array horizontally at 3rd index

##### Example
```python
# Split array into groups of ~3
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(np.array_split(a, 3))
>>> [array([1, 2, 3]), array([4, 5, 6]), array([7, 8])]
```
#### Shaping Arrays
|Operator|Description|
|:---------|:-------|
|`other = ndarray.flatten()`|Flattens a 2d array to 1d
|numpy.flip()|Flips order of elements in 1D array|
|np.ndarray[::-1]|Same as above|
|reshape|
|squeeze|
|expand_dims|

#### Misc
|Operator|Description|Documentation|
|:--------|:--------|:--------|
|`other = ndarray.flatten()`|Flattens a 2d array to 1d
|`array = np.transpose(other)`</br> `array.T` |Transpose array
|`inverse = np.linalg.inv(matrix)`|Inverse of a given matrix
</br>

##### Example
```python
# Find inverse of a given matrix
>>> np.linalg.inv([[3,1],[2,4]])
array([[ 0.4, -0.1],
       [-0.2,  0.3]])
```

### Mathematics

#### Operations
| Operator | Description     |
| :------------- | :------------- |
|`np.add(x,y)`<br/>`x + y`|Addition
|`np.substract(x,y)`<br/>`x - y`|Subtraction
|`np.divide(x,y)`<br/>`x / y`|Division
|`np.multiply(x,y)`<br/>`x @ y`|Multiplication
|`np.sqrt(x)`|Square Root
|`np.sin(x)`|Element-wise sine
|`np.cos(x)`|Element-wise cosine
|`np.log(x)`|Element-wise natural log
|`np.dot(x,y)`|Dot product
|`np.roots([1,0,-4])`|Roots of a given polynomial coefficients

Remember: NumPy array operations work element-wise.

##### Example
```python
# If a 1d array is added to a 2d array (or the other way), NumPy
# chooses the array with smaller dimension and adds it to the one
# with bigger dimension
a = np.array([1, 2, 3])
b = np.array([(1, 2, 3), (4, 5, 6)])
print(np.add(a, b))
>>> [[2 4 6]
     [5 7 9]]
     
# Example of np.roots
# Consider a polynomial function (x-1)^2 = x^2 - 2*x + 1
# Whose roots are 1,1
>>> np.roots([1,-2,1])
array([1., 1.])
# Similarly x^2 - 4 = 0 has roots as x=±2
>>> np.roots([1,0,-4])
array([-2.,  2.])
```

#### Comparison
| Operator | Description | Documentation |
| :------------- | :------------- |:---------|
|`==`|Equal
|`!=`|Not equal
|`<`|Smaller than
|`>`|Greater than
|`<=`|Smaller than or equal
|`>=`|Greater than or equal
|`np.array_equal(x,y)`|Array-wise comparison

##### Example
```python
# Using comparison operators will create boolean NumPy arrays
z = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
c = z < 6
print(c)
>>> [ True  True  True  True  True False False False False False]
```
#### Basic Statistics
| Operator | Description    |
| :------------- | :------------- |
|`np.mean(array)`|Mean
|`np.median(array)`|Median
|`array.corrcoef()`|Correlation Coefficient
|`np.std(array)`|Standard Deviation

##### Example <a name="stats-examples"></a>
```python
# Statistics of an array
a = np.array([1, 1, 2, 5, 8, 10, 11, 12])

# Standard deviation
print(np.std(a))
>>> 4.2938910093294167

# Median
print(np.median(a))
>>> 6.5
```


#### More <a name="more"></a>
| Operator | Description    |
| :------------- | :------------- |
|`array.sum()`|Array-wise sum
|`array.min()`|Array-wise minimum value
|`array.max(axis=0)`|Maximum value of specified axis
|`array.cumsum(axis=0)`|Cumulative sum of specified axis

### Slicing and Subsetting <a name="ss"></a>
|Operator|Description|Documentation|
| :------------- | :------------- | :------------- |
|`array[i]`|1d array at index i|[link](https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html)|
|`array[i,j]`|2d array at index[i][j]|see above|
|`array[i<4]`|Boolean Indexing, see [Tricks](#tricks)|see above|
|`array[0:3]`|Select items of index 0, 1 and 2|see above|
|`array[0:2,1]`|Select items of rows 0 and 1 at column 1|see above|
|`array[:1]`|Select items of row 0 (equals array[0:1, :])|see above|
|`array[1:2, :]`|Select items of row 1|see above|
[comment]: <> (|`array[1,...]`|equals array[1,:,:]|see above|)
|`array[ : :-1]`|Reverses `array`|see above|


##### Examples
```python
b = np.array([(1, 2, 3), (4, 5, 6)])

# The index *before* the comma refers to *rows*,
# the index *after* the comma refers to *columns*
print(b[0:1, 2])
>>> [3]

print(b[:len(b), 2])
>>> [3 6]

print(b[0, :])
>>> [1 2 3]

print(b[0, 2:])
>>> [3]

print(b[:, 0])
>>> [1 4]

c = np.array([(1, 2, 3), (4, 5, 6)])
d = c[1:2, 0:2]
print(d)
>>> [[4 5]]

```

### Tricks
This is a growing list of examples. Know a good trick? Let me know in a issue or fork it and create a pull request.

*boolean indexing* (available as separate `.py` file [here](https://github.com/JulianGaal/python-cheat-sheet/blob/master/code/boolean-indexing.py)
```python
# Index trick when working with two np-arrays
a = np.array([1,2,3,6,1,4,1])
b = np.array([5,6,7,8,3,1,2])

# Only saves a at index where b == 1
other_a = a[b == 1]
#Saves every spot in a except at index where b != 1
other_other_a = a[b != 1]
```

```python
import numpy as np
x = np.array([4,6,8,1,2,6,9])
y = x > 5
print(x[y])
>>> [6 8 6 9]

# Even shorter
x = np.array([1, 2, 3, 4, 4, 35, 212, 5, 5, 6])
print(x[x < 5])
>>> [1 2 3 4 4]

```


#### Credits
[Datacamp](https://www.datacamp.com/home),
[Quandl](https://s3.amazonaws.com/quandl-static-content/Documents/Quandl+-+Pandas,+SciPy,+NumPy+Cheat+Sheet.pdf),



## Matplotlib

Original maker of this section : [Julian Gaal](https://github.com/juliangaal/python-cheat-sheet.git). Modified by Christian Toderascu.

This serves as a cheat sheet for Matplotlib, a 2d plotting library for Python here is the [officila api references](https://matplotlib.org/stable/api/index.html)

If you don't already have it **installed**, do so using Pip:
```
$ pip install matplotlib
```

### Creating plots

*Figure*

| Operator    | Description     |
| :------------- | :------------- |
| `fig = plt.figures()`      | a container that contains all plot elements

*Axes*

| Operator    | Description     | 
| :------------- | :------------- | 
| `fig.add_axes()`<br/>`a = fig.add_subplot(222)` |Initializes subplot <br/> A subplot is an axes on a grid system <br/> row-col-num, see [examples](#examples)
| `fig, b = plt.subplots(nrows=3, nclos=2)`|Adds subplot
|`ax = plt.subplots(2, 2)`|Creates subplot

Axes are very useful for subplots. See example [here](#sub)

**After configuring your plot, you must use `plt.show()` to make it visible**

### Plotting

*1D Data*

| Operator    | Description     | Documentation |
| :------------- | :------------- | :----------- |
| `lines = plt.plot(x,y)`|Plot data connected by lines|
| `plt.scatter(x,y)`|Creates a scatterplot, unconnected data points
| `plt.bar(xvalue, data , width, color...)`|simple vertical bar chart||
| `plt.barh(yvalue, data, width, color...)`|simple horizontal bar||
|`plt.hist(x, y)`|Plots a histogram|
|`plt.boxplot(x,y)`|Box and Whisker plot
|`plt.violinplot(x, y)`| Creates violin plot
|`ax.fill(x, y, color='lightblue')`<br/>`ax.fill_between(x,y,color='yellow')`|Fill area under/between plots

For more advanced box plots, start [here](http://matplotlib.org/api/pyplot_api.html?highlight=bar#matplotlib.pyplot.boxplot)

*2D Data*

| Operator    | Description     |
| :------------- | :------------- |
|`fig, ax = plt.subplots()`</br>`im = ax.imshow(img, cmap, vmin...)`|Colormapped or RGB arrays

Suggestions?

*Saving plots*>

| Operator    | Description     |
| :------------- | :------------- |
|`plt.savefig('pic.png')`|Saves plot/figure to image
|`plt.savefig('transparentback.png', transparent=True)`|Saves transparent plot/figure to image|see above|


### Customization

*Color*

| Operator    | Description     |
| :------------- | :------------- |
| `plt.plot(x, y, color='lightblue')`<br/>`plt.plot(x, y, alpha = 0.4)`|colors plot to color blue
|`plt.colorbar(mappable, orientation='horizontal')`|`mappable`: the Image, Contourset etc to which colorbar applies

*Markers* 

| Operator    | Description     |
| :------------- | :------------- |
| `plt.plot(x, y, marker='*')`|adds `*` for every data point
| `plt.scatter(x, y, marker='.')` |adds . for every data point

*Lines*

| Operator    | Description     |
| :------------- | :------------- |
|`plt.plot(x, y, linewidth=2)`|Sets line width
|`plt.plot(x, y, ls='solid')`|Sets linestyle, `ls` can be ommitted, see 2 below|see above|
|`plt.plot(x, y, ls='--')`|Sets linestyle, `ls` can be ommitted, see below|see above|
|`plt.plot(x,y,'--', x**2, y**2, '-.')`|Lines are '--' and '_.', see [example](#crazylines)|see above|
|`plt.setp(lines,color='red',linewidth=2)`|Sets properties of plot `lines`|[link](http://matplotlib.org/api/pyplot_api.html?highlight=setp#matplotlib.pyplot.setp)|

*Text*

| Operator    | Description     |
| :------------- | :------------- |
|`plt.text(1, 1,'Example Text',style='italic')`|Places text at coordinates 1/1
|`ax.annotate('some annotation', xy=(10, 10))`|Annotate the point with coordinates`xy` with text `s`
|`plt.title(r'$delta_i=20$', fontsize=10)`|Mathtext

*Limits, Legends/Labels , Layout*

*Limits*

| Operator    | Description     |
| :------------- | :------------- |
|`plt.xlim(0, 7)`|Sets x-axis to display 0 - 7 
|`plt.ylim(-0.5, 9)`|Sets y-axis to display -0.5 - 9
|`ax.set(xlim=[0, 7], ylim=[-0.5, 9])`<br/>`ax.set_xlim(0, 7)`
|`plt.margins(x=1.0, y=1.0)`|Set margins: add padding to a plot, values 0 - 1
|`plt.axis('equal')`|Set the aspect ratio of the plot to 1

*Legends/Labels*

| Operator    | Description     |
| :------------- | :------------- |
|`plt.title('just a title')`|Sets title of plot
|`plt.xlabel('x-axis')`|Sets label next to x-axis
|`plt.ylabel('y-axis')`|Sets label next to y-axis
|`ax.set(title='axis', ylabel='Y-Axis', xlabel='X-Axis')`|Set title and axis labels
|`ax.legend(loc='best')`|No overlapping plot elements

*Ticks*

| Operator    | Description     | 
| :------------- | :------------- |
|`plt.xticks(x, labels, rotation='vertical')`|Set ticks, [example](#ticks)
|`ax.xaxis.set(ticks=range(1,5), ticklabels=[3,100,-12,"foo"])`|Set x-ticks
|`ax.tick_params(axis='y', direction='inout', length=10)`|Make y-ticks longer and go in and out

### Examples

#### Basics

```python
import matplotlib.pyplot as plt

x = [1, 2.1, 0.4, 8.9, 7.1, 0.1, 3, 5.1, 6.1, 3.4, 2.9, 9]
y = [1, 3.4, 0.7, 1.3, 9, 0.4, 4, 1.9, 9, 0.3, 4.0, 2.9]
plt.scatter(x,y, color='red')

w = [0.1, 0.2, 0.4, 0.8, 1.6, 2.1, 2.5, 4, 6.5, 8, 10]
z = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.plot(z, w, color='lightblue', linewidth=2)

c = [0,1,2,3,4, 5, 6, 7, 8, 9, 10]
plt.plot(c)

plt.ylabel('some numbers')
plt.xlabel('some more numbers')
plt.show()
```
![alt-text](/img/plot.png)

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(10)
y = np.random.rand(10)

plt.plot(x,y,'--', x**2, y**2,'-.')
plt.savefig('lines.png')
plt.show()
```
![alt-text](/img/lines.png)


```python
import matplotlib.pyplot as plt


x = [1, 2, 3, 4]
y = [1, 4, 9, 6]
labels = ['Frogs', 'Hogs', 'Bogs', 'Slogs']

plt.plot(x, y, 'ro')
# You can specify a rotation for the tick labels in degrees or with keywords.
plt.xticks(x, labels, rotation='vertical')
# Pad margins so that markers don't get clipped by the axes
plt.margins(0.2)
plt.savefig('ticks.png')
plt.show()
```
![alt-text](/img/ticks.png)

#### Subplotting Examples
```python
import matplotlib.pyplot as plt

x = [0.5, 0.6, 0.8, 1.2, 2.0, 3.0]
y = [10, 15, 20, 25, 30, 35]
z = [1, 2, 3, 4]
w = [10, 20, 30, 40]

fig = plt.figure()
ax =  fig.add_subplot(111)
ax.plot(x, y, color='lightblue', linewidth=3)
ax.scatter([2,3.4,4, 5.5],
               [5,10,12, 15],
               color='black',
               marker='^')
ax.set_xlim(0, 6.5)

ax2 =  fig.add_subplot(222)
ax2.plot(z, w, color='lightgreen', linewidth=3)
ax2.scatter([3,5,7],
               [5,15,25],
               color='red',
               marker='*')
ax2.set_xlim(1, 7.5)

plt.savefig('mediumplot.png')
plt.show()
```
![alt-text](/img/medium.png)

Thanks to this guy for this [good example](http://stackoverflow.com/questions/37970424/what-is-the-difference-between-drawing-plots-using-plot-axes-or-figure-in-matpl)
```python
import numpy as np
import matplotlib.pyplot as plt

# First way #

x = np.random.rand(10)
y = np.random.rand(10)

figure1 = plt.plot(x,y)

# Second way #

x1 = np.random.rand(10)
x2 = np.random.rand(10)
x3 = np.random.rand(10)
x4 = np.random.rand(10)
y1 = np.random.rand(10)
y2 = np.random.rand(10)
y3 = np.random.rand(10)
y4 = np.random.rand(10)

figure2, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.plot(x1,y1)
ax2.plot(x2,y2)
ax3.plot(x3,y3)
ax4.plot(x4,y4)

plt.show()
```

![alt-text](/img/axes.png)

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 500)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)

fig, ax = plt.subplots()

ax.fill(x, y, color='lightblue')
plt.show()
```
![alt-text](/img/fill.png)

[source](http://matplotlib.org/api/pyplot_api.html?highlight=fill#matplotlib.pyplot.fill)

#### Advanced

Taken from [official docs](http://matplotlib.org/api/pyplot_api.html)
```python
import matplotlib.pyplot as plt
import numpy as np


np.random.seed(0)

x, y = np.random.randn(2, 100)
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
ax1.grid(True)
ax1.axhline(0, color='black', lw=2)

ax2 = fig.add_subplot(212, sharex=ax1)
ax2.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
ax2.grid(True)
ax2.axhline(0, color='black', lw=2)

plt.show()
```
![alt-text](/img/advanced.png)

#### Credit
[Datacamp](https://www.datacamp.com/),
[Official Docs](http://matplotlib.org/api/),
[Quandl](https://s3.amazonaws.com/quandl-static-content/Documents/Quandl+-+Pandas,+SciPy,+NumPy+Cheat+Sheet.pdf),
[Julian Gaal](https://github.com/juliangaal/python-cheat-sheet.git)



