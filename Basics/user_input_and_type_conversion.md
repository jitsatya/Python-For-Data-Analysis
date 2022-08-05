
Taking User Input and type conversion


```python
input(prompt = "Name: ")
```

    Name: Satyajit





    'Satyajit'




```python
first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
result = int(first_number) + int(second_number)
print(result)
```

    Enter the first number: 56
    Enter the second number: 67
    123


User Input comes always in String format as it is universal format


```python
type(first_number)
```




    str



Two types of type conversion
1. Implicit : Python automatically converts
2. Explicit : Should be converted by programmer


```python
#Implicit
4 + 5.5
```




    9.5




```python
5+6j
```




    (5+6j)




```python
#Explicit conversion
int('45')
```




    45




```python
float(4)
```




    4.0




```python
str(5)
```




    '5'




```python
bool(1)
```




    True




```python
complex(4)
```




    (4+0j)




```python
list('hello')
```




    ['h', 'e', 'l', 'l', 'o']



type conversion is not parmanent


```python
a=4.5
```


```python
int(a)
```




    4




```python
a # Original variable stays same
```




    4.5




```python
first_number = int(input("Enter the first number: ")) # converting type when taking input
second_number = int(input("Enter the second number: "))
result = first_number + second_number
print(result)
```

    Enter the first number: 56
    Enter the second number: 87
    143

