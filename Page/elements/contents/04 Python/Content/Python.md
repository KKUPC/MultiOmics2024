---
output:
  word_document: default
  html_document: default
---
# **Basics python syntax***

1. **Print Statement:**
   ```python
   print("Hello, World!")
   ```

2. **Variables:**
   ```python
   x = 5
   name = "John"
   ```

3. **Data Types:**
   ```python
   integer_variable = 10
   float_variable = 3.14
   string_variable = "Hello"
   boolean_variable = True
   ```

4. **Lists:**
   ```python
   my_list = [1, 2, 3, 4, 5]
   ```

5. **Tuples:**
   ```python
   my_tuple = (1, 2, 3)
   ```

6. **Dictionaries:**
   ```python
   my_dict = {'key1': 'value1', 'key2': 'value2'}
   ```

7. **Conditional Statements:**
   ```python
   if x > 0:
       print("Positive number")
   elif x == 0:
       print("Zero")
   else:
       print("Negative number")
   ```

8. **Loops:**
   ```python
   for i in range(5):
       print(i)
   
   while x > 0:
       print(x)
       x -= 1
   ```

9. **Functions:**
   ```python
   def greet(name):
       print("Hello, " + name + "!")
   
   greet("Alice")
   ```

10. **Classes:**
    ```python
    class Dog:
        def __init__(self, name):
            self.name = name
    
        def bark(self):
            print("Woof!")
    
    my_dog = Dog("Buddy")
    my_dog.bark()
    ```

11. **Input from User:**
    ```python
    user_input = input("Enter something: ")
    ```

12. **Exception Handling:**
    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    ```
