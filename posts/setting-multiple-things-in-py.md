TIL: In python you can set multiple variables simultaneously:

eg: This works: 

```python
a = b = c = d = 123
print(a, b, c, d)
# >> 123 123 123 123
```

And similarly, with unpacking:
```python
a, b, *c = 1,2,3,4,5
print(a, b, c)
# >> 1 2 [3, 4, 5]
a, *b, c = 1,2,3,4,5
print(a, b, c)
# >> 1 [2, 3, 4] 5
```
I'm not surprised it works tbh, but I don't think I'd ever seen it in the wild before; so hence TIL!

---
There's a similar multiple attribute trick for assigning multiple returns from a function:
```python
a, b = fn(1,2)
```
This is (of course) just doing a swift tuple unpacking from the implicit tuple the function is returning.

It gives a nice answer to the (silly) coding interview question about swapping two variables without using an intermediate variable.

It's a silly question as it's unrealistic and the only way you'd know the answer (imho) is to have seen it previously. I guess the expected answer requires clever maths or something, allowing the 
interviewer a chance to flex. 

I was actually asked it in an interview once. And immediately gave the following:

```python
a, b = b, a
```

Did they think that was neat? Clever? Simple? Elegant? 

No! They appeared to be annoyed they couldn't show-off! 