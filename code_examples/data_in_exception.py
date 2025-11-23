# Source - https://stackoverflow.com/a
# Posted by Ray Salemi
# Retrieved 2025-11-20, License - CC BY-SA 4.0

class MyException(RuntimeError):
    def __init__(self,message,numb):
        super().__init__(message)
        self.numb = numb

try:
    raise MyException("My bad", 3)
except MyException as me:
    print(me)
    print(me.numb)
