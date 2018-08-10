# 1
# In interactive mode, the last printed expression is assigned to the
# variable ‘_’.  This means that when you are using Python as a desk
# calculator, it is somewhat easier to continue calculations, for example:

tax = 12.5 / 100
price = 100.50
price * tax

price + _

round(_, 2)

# 2
# One way to remember how slices work is to think of the indices as
# pointing `between' characters, with the left edge of the first character
# numbered 0.  Then the right edge of the last character of a string of
# `n' characters has index `n', for example:

#       +---+---+---+---+---+---+
#       | P | y | t | h | o | n |
#       +---+---+---+---+---+---+
#       0   1   2   3   4   5   6
#      -6  -5  -4  -3  -2  -1

# 3
# In Python, like in C, any non-zero integer value is true; zero is false.
# The condition may also be a string or list value, in fact any sequence;
# anything with a non-zero length is true, empty sequences are false.

# 4
# If you need to modify the sequence you are iterating over while inside
# the loop (for example to duplicate selected items), it is recommended
# that you first make a copy.  Iterating over a sequence does not
# implicitly make a copy.  The slice notation makes this especially
# convenient:

words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)

words

# 5
# When a final formal parameter of the form ‘**name’ is present, it
# receives a dictionary containing all keyword arguments except for those
# corresponding to a formal parameter.  This may be combined with a formal
# parameter of the form ‘*name’ which receives a tuple
# containing the positional arguments beyond the formal parameter list.
# (‘*name’ must occur before ‘**name’.)


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
        print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# 6
# the built-in *note range(): function expects separate `start' and `stop' arguments.
# If they are not available separately, write the function call with the
# ‘*’-operator to unpack the arguments out of a list or tuple:

args = [3, 6]
list(range(*args))    # call with arguments unpacked from a list

# In the same fashion, dictionaries can deliver keyword arguments with the
# ‘**’-operator:


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
