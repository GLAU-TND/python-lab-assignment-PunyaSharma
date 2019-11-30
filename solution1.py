class MyException(Exception):
    def _init_(self,v=''):
        self.v = v
    def _str_(self):
        return str(self.v)
def xyz(a,b):
    c=a+b
    if c<=150:
        raise MyException("custom Exception occured")
    else:
        return c
print(xyz(30,40))
