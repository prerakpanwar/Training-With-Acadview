#Q1- Create a function to calculate the area of a circle by taking radius from user.


def cal_area(r):
    print(3.14 * r * r)

cal_area(float(input("Enter radius of circle : ")))





#Q2- Write a function “perfect()” that determines perfect numbers between 1 and 1000.


def perfect(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    if sum == n:
        print(str(n) + " is a perfect number.")

for i in range(1,1001):
    perfect(i)




#Q3- Print Multiplication Table of 12 Using Recursion.


def table(n,i):
    print(n*i)
    i=i+1
    if i<=10:
             table(n,i)

table(12,1)




#Q4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.


def power(base,exp):
    if exp == 1:
        return(base)
    if exp != 1:
        return(base*power(base,exp-1))


base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result: " + str(power(base,exp)))





#Q5- Write a function to find factorial of a number but also store the factorials calculated in a dictionary.

dic = []
index = []


def fact(a):
    dic.append(a)
    if a == 1:
        dictionary = dict(zip(index, dic))
        print(dictionary)
        return(a)
    if a != 1:
        return(a*fact(a-1))



x = int(input("Enter a number to get its factorial : "))
d =x

for d in range(0, d):
    index.append("value " + str(d+1))


print("\nFactorial is : " + str(fact(x)))



