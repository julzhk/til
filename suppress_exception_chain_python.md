Exception Chains in Python
---

TIL, that you can hide the exception context in Python.

---

Saw somthing like this in some code today. 

```raise RuntimeError("Cannot divide by zero") from None```

Had to do a bit of a search to understand it. Turns out it hides the exception context. 

What does this mean?

Example 1/3: Simple Exception
-
```python
try:
    1/0
except ZeroDivisionError as e:
    raise RuntimeError("Cannot divide by zero")
```
**This gives us:**

```Console
Traceback (most recent call last):
  File "divzero.py", line 2, in <module>
    1/0
    ~^~
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "divzero.py", line 4, in <module>
    raise RuntimeError("Cannot divide by zero")
RuntimeError: Cannot divide by zero
```
We get the raised exception and then the exception that caused the raised exception.

Example 2/3: Exception with Chain
-

```python
try:
    1/0
except ZeroDivisionError as e:
    raise RuntimeError("Cannot divide by zero") from e
```
which gives:

```Console
Traceback (most recent call last):
  File "divzero.py", line 2, in <module>
    1/0
    ~^~
ZeroDivisionError: division by zero

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "divzero.py", line 4, in <module>
    raise RuntimeError("Cannot divide by zero") from e
RuntimeError: Cannot divide by zero
```

We get the raised exception that caused the re-raised exception.

Finally...

Example 3/3: Exception without a Chain 
-
```python
try:
    1/0
except ZeroDivisionError as e:
    raise RuntimeError("Cannot divide by zero") from None
```
Gives a much simpler traceback:
```Console
  File "divzero.py", line 4, in <module>
    raise RuntimeError("Cannot divide by zero") from None
RuntimeError: Cannot divide by zero
```

It's just the raised exception - now we just see a 'Runtime Error', not a 'ZeroDivisionError'.

This'll be useful for raising exceptions that might be user-facing or in a library: nobody needs to know the details - just the resultant exception.


Is there a PEP for this?
-

Of course there's a PEP for this! 

[PEP 0409](https://peps.python.org/pep-0409/) - It's been available since 2012!
