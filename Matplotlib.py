'''
Matplotlib  :  This provides various plots and customization options to make any visualizations more meaningful.
1)Line plot : line plot is a data visualization that displays numerical information as a series of data points connected by straight lines.
Example:'''
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[10,20,30,40,50,60]
plt.plot(x,y)
plt.show()
'''
2.Title - (Title)
-->This is used to display data points connected by straight lines.
Example :'''
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[3,19,7,2,15,9]
plt.xlabel('overs')
plt.ylabel('Score')
plt.plot(x,y)
plt.title("Csk Score")
plt.show()
'''
3.Bar Chart :This displays categorical data using rectangular bars.
Example :'''
import matplotlib.pyplot as plt
marks=[15,20,10]
stud_=['Arun,'Lokesh','Teja']
plt.bar(stud_,marks,color='green')
plt.ylabel('Marks')
plt.xlabel('Students')
plt.title('Student Marks')
plt.show()
'''
4.Pie Chart : This is a circular statistical graph divided into slices to illustrate numerical proportions.
Example :'''
import matplotlib.pyplot as plt
sub=['Python','SQL','Flask']
stud_=[20,5,20]
plt.pie(stud_,labels=sub)
plt.title('Courses')
plt.legend(stud_)
'''
5.Histogram : It is a graphical tool used in statistics to show the frequency distribution of continuous numerical data.
Example :'''
import numpy as np
import matplotlib.pyplot as plt
data=np.random.randn(1000)
plt.hist(data,alpha=0.7,edgecolor='black',color='green')
plt.xlabel('Values')
plt.xlabel('Frequency')
plt.title('Histogram Example')
plt.show()
'''
5.Scatter :It is a mathematical diagram that uses Cartesian coordinates to display values for two numerical variables in a dataset.
Example :'''
import matplotlib.pyplot as plt
marks=[2500,1500,2200,3000]
stud_=[2023,2024,2025,2026]
plt.scatter(stud_,marks,color='black')
plt.ylabel('No.of Car Sales')
plt.xlabel('Year')
plt.title('BMW')
plt.show()




















