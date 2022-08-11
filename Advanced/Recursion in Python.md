### Recursion in Python


```python
# Example 1:recursion: Multiplication
# First thing is to find base condition
def mul(a,b):
    if b==1:
        return a # Base case
    else:
        return a + mul(a,b-1) # Calling function from inside function
# Return is always passed to the function which called the function
mul(4,6)
# This is very close to Stack, Last in First Out
```




    24




```python
# Example 2: Factorial using recursion
def factorial(a):
    if a == 1:
        return a # Base Case
    else:
        return a * factorial(a-1)
factorial(5)
```




    120




```python
# Example 3: Palindrome using recursion
def palindrome(text):
    if len(text) <= 1: #<= incase the text is palindrome and even
        print("palindrome") # Base Case
    else:
        if text[0] == text[-1]:
            palindrome(text[1:-1])
        else:
            print("Not Palindrome")

palindrome("noon")
        
```

    palindrome



```python
#Example 4: the rabbit problem, fibonacci
def fibonacci(month):
    if month ==0 or month ==1:
        return 1
    else:
        return fibonacci(month -1) + fibonacci(month -2)
    
print("Number of rabbits: ", fibonacci(12)) 
# This code is very inefficient, as the number is increased the time will increase exponentially
# Same logic is solved again and again
# We can solve this problem by using memoization shown below
```

    Number of rabbits:  233



```python
# memoization: Dynamic Programming
# Space time tradeoff
def memo(month, d):
    if month in d:
        return d[month]
    else:
        d[month] = memo(month-1, d) + memo (month-2, d) # storing fibonacci in the dictionary
        return d[month]

d = {0:1, 1:1} # dictionary for storing fibonacii for each value, default base case
memo(50, d)
```




    20365011074




```python
# Example: powerset using recursion
```
