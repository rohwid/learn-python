## Encapsulation

**The encapsulation** is the mechanism of hiding the data implementation were separated in some section such as:
    + Public (example: `data_hiding_public.py`)
    + Protected (example: `data_hiding_protected.py`)
    + Private (example: `data_hiding_private.py`)

The best practice were in `protected.py` and `private.py`.

### Public

Summary:
+ The attribute and function can access from instance.
+ The variable can be inherit or access from child class.

### Protected

Summary:
+ The attribute can be access from instance, the function can't access from instance directly but can be inherit or access from child class.
+ The variable can be inherit or access from child class.

### Private

Summary:
+ The attribute can't be access from instance but must be use special params. The function can't access from instance directly and can't be inherit or access from child class, only can access from the current class.
+ The variable can't be inherit or access from child class, only can access from the current class.
