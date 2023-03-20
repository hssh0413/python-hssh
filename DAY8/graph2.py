import matplotlib.pyplot as plt
# plt.figure()
# x1=[]
# y1=[]
# x2=[]
# y2=[]
# x3=[]
# y3=[]
# x4=[]
# y4=[]
# for i in range(-10,11):
#     x1.append(i)
#     y1.append(i)
#     x2.append(i)
#     y2.append(i**i)
#     x3.append(i)
#     y3.append(i*i**2)
#     x4.append(i)
#     y4.append(i*-i**2)
# plt.plot(x1,y1,x2,y2,x3,y3,x4,y4)
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.show()
figure,axes=plt.subplots(2,2)
fruits=["apple","banana","chery","orange"]
counts=[4,6,5,10]
bar_color=["red","yellow","black","orange"]
x=[]
y1=[]
y2=[]
for i in range(-10,11):
    x.append(i)
    y1.append(i)
    y2.append(i**2)
plt.xlabel("x axis")
plt.ylabel("y axis")
axes[0,0].barh(fruits,counts,color=bar_color)
axes[0,1].plot(x,y1)
axes[1,0].bar(fruits,counts,color=bar_color)
axes[1,1].plot(x,y2)
plt.show()