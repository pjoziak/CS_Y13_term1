How to construct decorator?

1. if the decorator is parameterless, it is enough to do 2-level nesting:

```
def decorator(func):
    def inner(*arg, **kwarg):
        # extra logic here
        ret = func(*arg, **kwarg)
        # more extra logic, if needed
        return ret
    return inner
```

2. If the decorator is to be parametrized, you actually construct a function producing decorators:

```
def decorator(decorator_parameters: Any):
    def outer(func_to_be_decorated):
        def inner(func_arguments):
            # do some extra logic here
            return func_to_be_decorated(func_arguments)
        return inner
    return outer
```

in the above example, `outer` is the actual decorator for the given parameters, `decorator` is the production rule for the decorators.
