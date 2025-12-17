TIL python: create a simple object from SimpleNamespace
---

I have a test which uses monkeypatching to replace an external service with mocked behaviour.  It returns an object, but I want to just drop-in a simple object instead of instantiating the real class.

My TIl is the `SimpleNamespace` object.


Duck typing 
---

...to the rescue. And thus `types.SimpleNamespace`.

```python
from types import SimpleNamespace

# Create a SimpleNamespace object by passing attributes as keyword arguments
user_config = SimpleNamespace(username='Alice', theme='dark', notifications=True)
```

While we're on this topic, lets look at some alternatives:

### Objects

Another way is to use the base `object` class:

```Python
class EmptyObject:
    pass

# Create two instances of the empty class
obj1 = EmptyObject()
obj1.username = 'Bob'
obj1.theme = 'light'
obj1.notifications = False
```
### And then there's the 'namedtuple'

```python
from collections import namedtuple

# Define two different named tuple types with the same fields
User = namedtuple('User', ['username', 'theme', 'notifications'])

p1 = User(username='Carol', theme='default',notifications=False)

```


All of these are similar in terms of accessing properties via dot notation; they each support some 'magic'/ standard methods - eg: `len()`, `str()`, `repr()` etc. But they're not supporting 
any other behaviour: They're just plain data-holding objects, useful in situations such as mocking in testing. 