How to construct decorator?
```
def decorator(decorator_parameters: Any):
    def outer(func_to_be_decorated):
        def inner(func_arguments):
            # do some extra logic here
            return func_to_be_decorated(func_arguments)
        return inner
    return outer
```

if the decorator is parameterless, it is enough to do 2-level nesting:

```
def decorator(func):
    def inner(*arg, **kwarg):
        # extra logic here
        ret = func(*arg, **kwarg)
        # more extra logic, if needed
        return ret
    return inner
```