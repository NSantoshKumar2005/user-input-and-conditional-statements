'''
Data Analysis:
-------------------
-->Data Analysis is the process of inspecting,cleaning,transforming,modeling data to discover useful insights,
support decision-making..
1.Descriptive Analysis:
------------------------------
Summarizing Data
2.Diagnostic Analysis:
-----------------------------
-->Understanding causes such as sales dropped.

3.Predictive Analysis:
----------------------------
-->Foyrecasting future outcomes

4.Prescriptive Analysis:
-------------------------------
-->Suggesting actions based on data (Marketing).

Why?
Numpy(ndarray):
-----------------------
-->Numerical Python (Numpy).
-->It provides support for multi-dimensional arrays.

Creating Numpy arrays:
-------------------------------
Example:'''
if __name__=="__main__":
    app.run(debug=True)
'''
1D array:
------------
Example:'''
import numpy as np
arr_1=np.array([1,2,3,4,5])
print(arr_1)
'''
2D array:
------------
Example:'''
import numpy as np
arr_1=np.array([[1,2,3,4,5],[1,2,3]])
print(arr_1)
'''
3D array:
------------
Example:'''
import numpy as np
arr_1=np.array([[[1,2,3,4,5],[1,2,3]]])
print(arr_1)
'''
arange:
----------
Example:'''
import numpy as np
arr_1=np.arange(1,20,2)
print(arr_1)
'''
reshape:
-----------
Example:'''
import numpy as np
arr_1=np.array([[1,2,3],[4,5,6]])
reshap=arr_1.reshape(3,2)
print(reshap)
'''
shallow copy:
------------------
Example:'''
import numpy as np
arr_1=np.array([10,20,301])
arr_view=arr_1.view()
arr_view[0]=40
print(arr_view)
print(arr_1)
'''
deep copy:
---------------
Example:'''
arr_copy=arr_1.copy()
arr_copy[0]=50
print(arr_copy)
print(arr_1)
'''
Pandas:
-----------
-->Pandas is  a powerful data manipulation and analysis library,built on top of numpy.
-->It provided data structure like series and data frames for efficient data handling
.mean()
.sum()
.max()
.min()
.head()
.tail()
Example:'''
import pandas as pd
price=pd.series([67,90,45,20],index=["apple","Banana","curd","dal"])
print(price)




























































