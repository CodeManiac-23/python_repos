print("hello world!")
res = "im global res variable"
x = 10
y = 100
print(x != y)

x +=12
print(x)


def printnumbers(a, b):
    global res
    print(res)
    res = a + b
    # del res
    print("Sum of two numbers : " + str(res))


printnumbers(2, 5)

print("guru88")
