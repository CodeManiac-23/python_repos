# Arthimetic operator
from typing import List

a = 20
b = 30
print(a + b)

# Comparision operator
x = 4
y = 5
print('x <= y is ' + str(x <= y))

# Assignment operators
num1 = 4
num2 = 5
print("The num1 is " + str(num1))
print("The num2 is " + str(num2))

result = num1 + num2
result += num1
mulresult = num1 * num2
mulresult *= num2
modresult = num1 % num2
modresult %= num2
divresult = num1 / num2
divresult /= num1
fdivresult = num1 // num2
fdivresult //= num2
print("The Result for compound addition  is : " + str(result))
print("The Result for compound multiplication  is : " + str(mulresult))
print("The Result for compound division  is : " + str(divresult))
print("The Result for compound modulus  is : " + str(modresult))
print("The Result for compound floor division  is : " + str(fdivresult))

# Logical Operators
a = True
b = False
print('And operator is : ', a and b)
print('Or operator is : ', a or b)
print('Not Operator for a , b is : ', a is not b)

print("Not Operator for 'a' is : ", not a)
print("Not Operator  for 'b' is : ", not a)

# Membership operators : ( in ) , ( not in )
list = [2, 5, 77, 90]
pkey = 2
nkey = 55
if pkey in list:
    print("The pkey present in list : ", pkey in list)
else:
    print("The pkey not present in list : ", pkey in list)

if nkey not in list:
    print("The nkey  not in list : ", nkey not in list)

else:
    print("The nkey  available  in list : ", nkey not in list)

# Identity operator : is , is not

a = 'hello'
b = 'hello'
print(a + '|' + b)
if a is b:
    print("The a &  b is point to same object")
else:
    print("The a & b is not point to same object")

a = 'hi python'
b = 'hello python'
print(a + '|' + b)
if a is not b:
    print("The a &  b is not point to same object")
else:
    print("The a & b is  point to same object")

# operator precedence : It determines which operators need to evaluate first .

# operator without precedent.

i = 10
j = 45
print(i+j*i)

# operator with precedent '()'.

i = 10
j = 45
print((i+j)*i)
