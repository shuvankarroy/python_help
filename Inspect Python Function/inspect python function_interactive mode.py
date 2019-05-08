Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import inspect
>>> def fun(a=0, b=1, c=2):
	    print(a,b,c)
	    return (a+b+c)

>>> inspect.signature(fun)
<Signature (a=0, b=1, c=2)>
>>> 
