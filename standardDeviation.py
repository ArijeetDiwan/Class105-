import math
import csv 
with open('./data.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)

    mean=total/n
    return mean 

#squaring and getting the value 
squared_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squared_list.append(a)

#getting the sum of the square list
sum=0
for i in squared_list:
    sum=sum+i

#print(len(data))
#dividing the sum of the total value N
#result=sum/(len(data)-1)
result=sum/(len(data))


#getting the standard deviation by taking the square root of the root result 
std_devition=math.sqrt(result)
print(std_devition)








     