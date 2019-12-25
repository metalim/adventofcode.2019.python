# Advent of Code 2019 in Python / Jupyter Notebook

This year I'll be using [Advent of Code](https://adventofcode.com/2019/) to learn [Python](https://www.python.org/).
As my goal is more Deep Learning, than Python programming itself, I'll be doing AoC in [Jupyter Notebook](https://jupyter.org/).

Goals:

* Learn Python tricks.
* Learn Jupyter Notebook tricks.
* Make it look pretty on GitHub.

## Quirks & tricks

While Python resembles [CoffeeScript](https://coffeescript.org/) - my favorite language so far (*well, vice versa in reality: CoffeeScript resembles Python*), Python has many legacy design decisions you have to adapt to. To name a few:

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

* Sets in Python are powerful.

  ```python
  A = {1,2,3,4}
  B = {3,4,5}
  C = A - B # == {1,2}
  D = B - A # == {5}
  D = B | {1} # == {1,3,4,5}
  ```

* Python doesn't allow inline assignment operations. Following is not possible:

  ```python
  for s in input.split('\n'):
      if (match = re.match(r'some number: (-?\d+)', s)) != None:
          # do something with match.group(1)
      elif (match = re.match(r'something else: (.+)', s)) != None:
          # do something with match.group(1)
  ```

  Instead you have to write something like:

  ```python
  for s in input.split('\n'):
      match = re.match(r'some number: (-?\d+)', s)
      if match != None:
          # do something with match.group(1)
          continue
      match = re.match(r'something else: (.+)', s)
      if match != None:
          # do something with match.group(1)
          continue
  ```

  That's no longer true in Python 3.8, where you can use special "walrus operator" `:=`, introduced especially for inline assignments:

  ```python
  for s in input.split('\n'):
      if (match := re.match(r'some number: (-?\d+)', s)) != None:
          # do something with match.group(1)
      elif (match := re.match(r'something else: (.+)', s)) != None:
          # do something with match.group(1)
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

## Useful links

* [Advent of Code](https://adventofcode.com/) - obviously.
  * [Scatterplot](http://www.maurits.vdschee.nl/scatterplot/) - timings of first 100 solvers for all AoC tasks.
  * [Medals](http://www.maurits.vdschee.nl/scatterplot/medals.html) - top 3 positions for each task.
  * [r/adventofcode](https://www.reddit.com/r/adventofcode/) - subreddit with solutions and discussions. [Visualizations](https://www.reddit.com/r/adventofcode/search?q=flair_name%3A%22Visualization%22&restrict_sr=1&sort=new) are nice.

* Other challenges/exercises:
  * [Exercism](https://exercism.io/) - exercises in many language tracks. Submit code. Can see other solutions. Tasks are mostly trivial. Can request mentor to improve you coding style. I was very satisfied with Go mentor *bitfield*.
  * [Codewars](https://www.codewars.com/) - programming tasks in many languages. Submit code. Can see other solutions. 1 kyu (hardest level) katas often question your understanding of language internals.
  * [Project Euler](https://projecteuler.net/) - probably the oldest programming challenge resource. Heavily math-based. Submit answers.
  * [CodinGame](https://www.codingame.com/) - programming tasks in many languages. Submit code and see resulting animation. Can see ofther solutions. Has bot battles, if you want competition.
  * [CodeForces](https://codeforces.com/) - coding contests several times a month. Similar to IT Olympics/Olympiads, but online. Can solve tasks in archive, if you don't want competition. Can participate in Virtual contests, if you want competition, but contest is over.
  * Will not include link to Topcoder, as their website now looks like marketing sh↓t. Never used, probably never will.
