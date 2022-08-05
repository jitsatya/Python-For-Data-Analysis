
#### Literals in Python
Raw data given to a variable
* Numeric Literal
* String Literal
* Boolean Literal
* Special Literal

##### 1. Numeric Literal


```python
a = 0b1010 # binary literal
b = 100 # Decimal literal
c = 0x12c # Hexadecimal literal
d = 0o310 # Octal literal

#float literal
float_1 = 10.5
float_2 = 1.56e12
float_3 = 1.5e-4

#Complex literal
x =3.14j

print(a,b,c,d)
print(float_1, float_2, float_3)
print(x, x.imag, x.real) # extracting imaginary and real parts
```

    10 100 300 200
    10.5 1560000000000.0 0.00015
    3.14j 3.14 0.0


##### 2.  String Literals


```python
string = 'This is python'
strings = "This is a python string"
char = 'C'
multiline_str = """This is a multiline string and there are a lot of text kjxndkjnkfjndzxfndofnsdonfozdnmfx  sdfvxd"""
unicode = u"\U0001f623" # emojis
raw_str = r"raw \n string" # html etc

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)
```

    This is python
    This is a python string
    C
    This is a multiline string and there are a lot of text kjxndkjnkfjndzxfndofnsdonfozdnmfx  sdfvxd
    😣
    raw \n string


##### 3. Boolean Literal


```python
a = True + 4
b = False + 10 # Implicit type conversion

print("a: ", a)
print("b: ", b)
```

    a:  5
    b:  10


##### 4. Special Literal


```python
a = None #Safest way of variable declaration 
print(a)
```

    None

