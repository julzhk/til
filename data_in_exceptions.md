TIL a nice way to explicitly pass data into exceptions
-

Exceptions are just classes; so we can extend them and add extra attributes.

Let's pass a `numb` attribute to a custom exception:

```python
# Source - https://stackoverflow.com/a
# Posted by Ray Salemi
# Retrieved 2025-11-20, License - CC BY-SA 4.0

class MyException(RuntimeError):
    def __init__(self,message,numb):
        super().__init__(message)
        self.numb = numb
        
try:
    raise MyException("My bad", 3)
except MyException as err:
    print(err)
    print(err.numb)
```
Previously I'd just added an attribute to the exception dynamically; I wouldn't subclass the Exception definition. This is better.


--- 
### Want to attach some notes to an exception?

Use `add_note`: https://docs.python.org/3/library/exceptions.html#BaseException.add_note

```
my_exception.add_note("Attempted to process invalid data")
```

