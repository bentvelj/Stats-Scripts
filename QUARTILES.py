from math import floor, ceil
data=[int(x) for x in input("Enter data, comma separated:").split(',')]
data.sort()
N=len(data)
print("Mean = ", sum(data)/N)
q1i=(N+1)/4-1
q1=data[floor(q1i)]+q1i%1*(data[ceil(q1i)]-data[floor(q1i)])
print("Q1 = ",q1)
q2i=(N+1)/2-1
q2=data[floor(q2i)]+q2i%1*(data[ceil(q2i)]-data[floor(q2i)])
print("Median = ",q2)
q3i=3*(N+1)/4-1
q3=data[floor(q3i)]+q3i%1*(data[ceil(q3i)]-data[floor(q3i)])
print("Q3 = ",q3)
print("IQR = ", q3 - q1)
print("Outliers: ", [x for x in data if x > q3 + 1.5*(q3 - q1) or x < q1 - 1.5*(q3 - q1)])