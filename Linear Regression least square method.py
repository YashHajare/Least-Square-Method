import matplotlib.pyplot as plt

##################################
##X_pseudo = [2005,2006,2007,2008,2009,2010,2011] #YEARS
##
##Y = [80,90,92,83,94,99,92] #PRODUCTION
##
##A = 2008 #ASSUMED MEAN
#######################################

#################################
##X_pseudo = [2002,2004,2005,2006,2007,2008,2011] #YEARS
##
##Y = [80,95,104,93,100,110,108] #PRODUCTION
##
##A = 2006 #ASSUMED MEAN
##################################

X_pseudo = [2013,2014,2015,2016,2017,2018,2019,2020,2021] #YEARS

Y = [0.08,1.43,4.45,8.80,10.66,12.52,14.38,16.24,18.10] #CAGR

A = 2017 #ASSUMED MEAN

print("Given Years:",X_pseudo)
print("Production:",Y,"TOTAL:",sum(Y))
Y_total = sum(Y)
print("Assumed Mean:",A)

X = [num - A for num in X_pseudo]
print("X:",X,"TOTAL:",sum(X))
##X = sum(X)

XY = [X[i] * Y[i] for i in range(len(X))]
print("XY:",XY,"TOTAL:",sum(XY))
XY = sum(XY)

X2 = [X[i] * X[i] for i in range(len(X))]
print("X2:",X2,"TOTAL:",sum(X2))
X2 = sum(X2)

#CALCULATE A AND B
print("--------------------")
print("FORMULA: a = <Y/N and b = <XY/<X2")

a = Y_total//len(X)
print("a:",a)

b = XY//X2
print("b:",b)

print("Calculating Yc = a + b(x)")

Yc = [a + b * x for x in X]
print(Yc)

plt.xlabel("Year")
plt.ylabel("CAGR")
plt.plot(X_pseudo,Y)
plt.plot(X_pseudo,Yc)
plt.show()

future = int(input("Enter the Year:"))
x_pred = future - A
print("In ",future,", the production will be", a + b * x_pred)














