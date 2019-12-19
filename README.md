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

* Numbers in Python are not just arbitrary precision floating point bignums, but complex numbers as well. I like how writing both parts is optional. Makes it easier to define directions in 2D:

    ```python
    ds = [1, 1j, -1, -1j] # for Right, Up, Left, Down.
    ```

## All years AoC solutions

* 2020:
    * [Lang](https://github.com/metalim/metalim.adventofcode.2020.lang), ✌😎
* 2019:
    * [Python in Jupyter Notebook](https://github.com/metalim/metalim.adventofcode.2019.python). Love this one, as it shows pretty results on GitHub.
* 2018
    * [Go](https://github.com/metalim/metalim.adventofcode.2018.go).
* 2017:
    * **[CoffeeScript](https://github.com/metalim/metalim.adventofcode.2017), 👈 first year I was doing AoC.**
    * [Go](https://github.com/metalim/metalim.adventofcode.2017.go), done in December 2018.
* 2016:
    * [CoffeeScript](https://github.com/metalim/metalim.adventofcode.2016), done in December 2017.
    * [Go](https://github.com/metalim/metalim.adventofcode.2016.go), done in January 2019, incomplete.
* 2015:
    * [CoffeeScript](https://github.com/metalim/metalim.adventofcode.2015), done in December 2017.
