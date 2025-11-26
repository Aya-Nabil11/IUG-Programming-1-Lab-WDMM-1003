'''
Type casting : refers to the process of converting the value of one data type into another.
Basic Casting Functions :
int(): Converts compatible values to an integer.
float(): Transforms values into floating-point numbers.
str(): Converts any data type into a string.



'''
# s = "10"
# n = int(s)
# cnt = 5
# f = float(cnt)
# age = 25
# s2 = str(age)
#
# print(n)
# print(f)
# print(s2)




'''
Input: d = 10.23
Output: 10
Explanation: The integer value of 10.23 is 10
'''
# num = float(input("enter a number: "))
# intNum=int(num)
# print("The integer value of "+str(num)+" is "+str(intNum))








# print(type(len("2222")))
# concatenaing int with string can not possible (typeError)
# x=int(6.8)
# print(x)





# take two Numbers from the user and add them
# num1=int(input("enter a first number: "))
# num2=int(input("enter a second number: "))
# print(num1+num2)



'''
Input: num = "5"
Output: 10
Explanation: Typecast "5" to int and then double it 5 * 2 = 10

Input: num = "12"
Output: 24
Explanation: Typecast "12" to int and then double it 12 * 2 = 24
'''





'''
Input: a = 6, b = 4, c = &
Output: 666666&4444
Explanation: 6 printed 6 times and 4 printed 4 times seperated by c = &.
'''
a = int(input("enter a number: "))
b = int(input("enter a number: "))
c=input("enter a sign: ")
print(a*str(a)+c+(b*str(b)))
