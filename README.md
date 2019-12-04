# Advent of Code 2019 in Python / Jupyter
This year I'll be using AoC to learn Python.
As my goal is more Deep Learning, than Python programming itself, I'll be doing AoC in Jupyter Notebook.

## Quirks & tricks
While Python resembles CoffeeScript - my favorite language so far (*well, vice versa in reality: CoffeeScript resembles Python*), Python has many legacy design decisions you have to adapt to. To name a few:

* Order of blocks in short form of `if`:

    ```python
    <code_true> if <condition> else <code_false>

    # it gets weird for nested conditionals
    <true_1> if <cond_1> else <false_1_true_2> if <cond_2> else <false_1_false_2>
    ```

    In CoffeeScript it's:
    ```coffeescript
    <code_true> if <condition>
    # or
    if <condition> then <code_true> else <code_false>
    
    # and for nested
    if <cond_1> then <true_1> else if <cond_2> then <false_1_true_2> else <false_1_false_2>
    ```

    While I clearly see why Python does that, it takes time to adapt to.

* No switch statement. Alternative is wordy:

    ```python
    if x == 0:
        <code_0>
    elif x == 1:
        <code_1>
    elif x == 2:
        <code_2>
    else:
        <code_else>
    ```

* You can write:

    ```python
    <code> for x in <range> if <condition>
    ```

    but you can't write:

    ```python
    for x in <range> if <condition>:
        <code>
    ```

* Breaking outer loop has strange syntax, but I kinda like it:

    ```python
    for <outer_loop>:
        for <inner_loop>:
            if <condition>: break
        else:
            # inner loop completed without breaking
            <code>
    ```
