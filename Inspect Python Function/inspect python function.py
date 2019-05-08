'''
import inspect
inspect.signature(function_name)
'''


# Example
import inspect

# function definition:
def fun(a=0, b=1, c=2):
    print(a,b,c)
    return (a+b+c)

inspect.signature(fun)
