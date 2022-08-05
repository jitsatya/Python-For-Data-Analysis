
### Operators in Python

Operators are used to perform operations on variables and values
* Arithmetic
* Comparison
* Logical
* Bitwise
* Asignment
* Identity
* Membership


```python
# Arithmetic Operators
x = 5
y = 2
print("x+y: ", x+y)
print("x-y: ", x-y)
print("x*y: ", x*y)
print("x/y: ", x/y) # True Division
print("x%y: ", x%y) # Remaider
print("x**y: ", x**y) # Power
print("x//y: ", x//y) # Integer Division
```

    x+y:  7
    x-y:  3
    x*y:  10
    x/y:  2.5
    x%y:  1
    x**y:  25
    x//y:  2



```python
# Comparison Operators
print("x>y: ", x>y)
print("x<y: ", x<y)
print("x>=y: ", x>=y)
print("x<=y: ", x<=y)
print("x==y: ", x==y)
print("x!=y: ", x!=y)
```

    x>y:  True
    x<y:  False
    x>=y:  True
    x<=y:  False
    x==y:  False
    x!=y:  True



```python
# Logical Operators
x= True
y= False

print(x or y)
print(x and y)
print(not x)
```

    True
    False
    False



```python
# Bitwise Operators
x = 3
y = 9

print(x&y) # Binary and opeartion
print(x|y) # Binary or operation
print(x>>1) # Shift right operation
print(y<<12) # Shift Left operation
print(~x) # 1's Complement
```

    1
    11
    1
    36864
    -4



```python
# Assignment Operator
a = 3
print(a)
a+=3 # a = a+3 
print(a)
a-=3
print(a)
a*=3
print(a)
a&=3
print(a)
```

    3
    6
    3
    9
    1



```python
# Identity Operator
a = 3
b = 3

print(a is b) # are both variables in the same memory location

x = [1,2,3]
y = [1,2,3]

print(a is y) # lists stored in differnt locations

```

    True
    False



```python
# Membership Operator
x = "Delhi"
print('D' in x)
print('k' in x)

x = [1,2,3]

print(5 in x)
print(2 in x)
```

    True
    False
    False
    True

