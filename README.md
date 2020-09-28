# pyfp
A library to implement functional programming structures in Python.

## Features

### Piping

The Pipe object allows you to take a series of nested function calls and convert them into a linear progression of calls that "pipes" the data from one call to the next.

For example, this function call:

```python
result = list(map(lambda x: x.upper(), map(lambda x: chr(x), filter(lambda x: x % 2 == 0, [97, 98, 99, 100]))))
```

Can be expressed with Pipe as this:

```python
result = Pipe([97, 98, 99, 100])
    .to(filter, lambda x: x % 2 == 0) 
    .to(map, lambda x: chr(x)) 
    .to(map, lambda x: x.upper()) 
    .to(list) 
    .get()
```

### Option

The Option object represents two states: Some, the value is there, and empty, the value is not. Using this wrapper in place of None to represent when a value is not present allows you to catch errors more easily.

For example:
```python
def first_occurence(ls, element):

    for i in range(len(ls)):

        if ls[i] == element:
            return i

    return None


ls = [1, 2, 3, 4] index = first_occurence(ls, 5) ls[index] = 6
```

In this example you would have to remember to check to see if index is None before attempting to change its value. Because this code runs fine when the element given is in the list it could be a long time before you catch this issue.

With Option:
```python
    def first_occurence(ls, element):

        for i in range(len(ls)):

            if ls[i] == element:
                return Option.some(i)

        return Option.empty()

    ls = [1, 2, 3, 4] index = first_occurence(ls, 5) ls[index.unwrap()] = 6
```

With Option, forgetting to unwrap a value will result in an error when it is used reminding you to account for the possibility that the value does not exist.
