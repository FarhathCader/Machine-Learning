{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f9d6fc80-4486-4590-a059-e1b3963d7a07",
   "metadata": {},
   "source": [
    "# Python Containers"
   ]
  },
  {
   "cell_type": "raw",
   "id": "5d9294ce-8129-4156-89f9-25ea263991a1",
   "metadata": {},
   "source": [
    "Python includes several built-in container types: lists, dictionaries, sets, and tuples."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d49bd994-8c0e-4cd3-9479-c260e7aea62a",
   "metadata": {},
   "source": [
    "## Lists"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b7e939f4-724a-4043-9138-04e7e9db9721",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 1, 2] 2\n",
      "1\n",
      "[3, 1, 'foo']\n",
      "[3, 1, 'foo', 'bar']\n",
      "bar [3, 1, 'foo']\n"
     ]
    }
   ],
   "source": [
    "xs = [3, 1, 2]    # Create a list\n",
    "print(xs, xs[2])  # Prints \"[3, 1, 2] 2\"\n",
    "print(xs[-2])     # Negative indices count from the end of the list; prints \"2\"\n",
    "xs[2] = 'foo'     # Lists can contain elements of different types\n",
    "print(xs)         # Prints \"[3, 1, 'foo']\"\n",
    "xs.append('bar')  # Add a new element to the end of the list\n",
    "print(xs)         # Prints \"[3, 1, 'foo', 'bar']\"\n",
    "x = xs.pop()      # Remove and return the last element of the list\n",
    "print(x, xs)      # Prints \"bar [3, 1, 'foo']\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "14622796-7bfd-42de-a46d-b7e0190eb949",
   "metadata": {},
   "source": [
    "### Slicing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d82a558f-5ebf-47c5-8fef-1d0a3c001d76",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, 3, 4]\n",
      "[2, 3]\n",
      "[2, 3, 4]\n",
      "[0, 1]\n",
      "[0, 1, 2, 3, 4]\n",
      "[0, 1, 2, 3]\n",
      "[0, 1, 8, 9, 4]\n"
     ]
    }
   ],
   "source": [
    "nums = list(range(5))     # range is a built-in function that creates a list of integers\n",
    "print(nums)               # Prints \"[0, 1, 2, 3, 4]\"\n",
    "print(nums[2:4])          # Get a slice from index 2 to 4 (exclusive); prints \"[2, 3]\"\n",
    "print(nums[2:])           # Get a slice from index 2 to the end; prints \"[2, 3, 4]\"\n",
    "print(nums[:2])           # Get a slice from the start to index 2 (exclusive); prints \"[0, 1]\"\n",
    "print(nums[:])            # Get a slice of the whole list; prints \"[0, 1, 2, 3, 4]\"\n",
    "print(nums[:-1])          # Slice indices can be negative; prints \"[0, 1, 2, 3]\"\n",
    "nums[2:4] = [8, 9]        # Assign a new sublist to a slice\n",
    "print(nums)               # Prints \"[0, 1, 8, 9, 4]\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "09ee0c7c-af64-444f-96b8-d3b427ceface",
   "metadata": {},
   "source": [
    "### Access"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "affb5d15-28a0-4bef-8820-1c3aa2c5c5e5",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 4, 9, 16]\n"
     ]
    }
   ],
   "source": [
    "nums = [0, 1, 2, 3, 4]\n",
    "squares = []\n",
    "for x in nums:\n",
    "    squares.append(x ** 2)\n",
    "print(squares)   # Prints [0, 1, 4, 9, 16]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "409f2781-7919-4b23-a9b3-62e316fb8d5d",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 4, 9, 16]\n"
     ]
    }
   ],
   "source": [
    "nums = [0, 1, 2, 3, 4]\n",
    "squares = [x ** 2 for x in nums]\n",
    "print(squares)   # Prints [0, 1, 4, 9, 16]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f86d8ccb-f042-44ac-af0a-54ed4c7164ed",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 4, 16]\n"
     ]
    }
   ],
   "source": [
    "ums = [0, 1, 2, 3, 4]\n",
    "even_squares = [x ** 2 for x in nums if x % 2 == 0]\n",
    "print(even_squares)  # Prints \"[0, 4, 16]\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ff3e3dc6-4982-4fd7-a3ec-ab7253400af8",
   "metadata": {},
   "source": [
    "## Dictionaries\n",
    "A dictionary stores (key, value) pairs, similar to a Map in Java or an object in Javascript. You can use it like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "efb102ac-5b40-427c-a027-9d6062603c75",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cute\n",
      "True\n",
      "wet\n",
      "None\n",
      "wet\n",
      "N/A\n"
     ]
    }
   ],
   "source": [
    "d = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data\n",
    "print(d['cat'])       # Get an entry from a dictionary; prints \"cute\"\n",
    "print('cat' in d)     # Check if a dictionary has a given key; prints \"True\"\n",
    "d['fish'] = 'wet'     # Set an entry in a dictionary\n",
    "print(d['fish'])      # Prints \"wet\"\n",
    "# print(d['monkey'])  # KeyError: 'monkey' not a key of d\n",
    "print(d.get('monkey'))  # Get an element with a default; prints \"N/A\"\n",
    "print(d.get('fish', 'N/A'))    # Get an element with a default; prints \"wet\"\n",
    "del d['fish']         # Remove an element from a dictionary\n",
    "print(d.get('fish', 'N/A')) # \"fish\" is no longer a key; prints \"N/A\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "174c88d0-340f-439d-a2b1-639e994a0e72",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A person has 2 legs\n",
      "A cat has 4 legs\n",
      "A spider has 8 legs\n"
     ]
    }
   ],
   "source": [
    "d = {'person': 2, 'cat': 4, 'spider': 8}\n",
    "for animal in d:\n",
    "    legs = d[animal]\n",
    "    print('A %s has %d legs' % (animal, legs))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9c327064-8e8c-4477-9605-66b8b0b439b7",
   "metadata": {
    "tags": []
   },
   "source": [
    "## Sets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f2a4ab96-61f7-4864-91c0-35311e6e53b8",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "True\n",
      "3\n",
      "3\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "animals = {'cat', 'dog'}\n",
    "print('cat' in animals)   # Check if an element is in a set; prints \"True\"\n",
    "print('fish' in animals)  # prints \"False\"\n",
    "animals.add('fish')       # Add an element to a set\n",
    "print('fish' in animals)  # Prints \"True\"\n",
    "print(len(animals))       # Number of elements in a set; prints \"3\"\n",
    "animals.add('cat')        # Adding an element that is already in the set does nothing\n",
    "print(len(animals))       # Prints \"3\"\n",
    "animals.remove('cat')     # Remove an element from a set\n",
    "print(len(animals))       # Prints \"2\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "910b9479-2f01-4c5d-8d08-0b443846cf10",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "#1: cat\n",
      "#2: fish\n",
      "#3: dog\n"
     ]
    }
   ],
   "source": [
    "animals = {'cat', 'dog', 'fish'}\n",
    "for idx, animal in enumerate(animals):\n",
    "    print('#%d: %s' % (idx + 1, animal))\n",
    "# Prints \"#1: fish\", \"#2: dog\", \"#3: cat\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1d83f089-d658-4965-9e4c-7ac839011c0a",
   "metadata": {},
   "source": [
    "### Tuples\n",
    "A tuple is an (immutable) ordered list of values. A tuple is in many ways similar to a list; one of the most important differences is that tuples can be used as keys in dictionaries and as elements of sets, while lists cannot. Here is a trivial example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3ce862a0-dc04-4acf-8b12-b22177d7e266",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{(0, 1): 0, (1, 2): 1, (2, 3): 2, (3, 4): 3, (4, 5): 4, (5, 6): 5, (6, 7): 6, (7, 8): 7, (8, 9): 8, (9, 10): 9}\n",
      "<class 'tuple'>\n",
      "5\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys\n",
    "print(d)\n",
    "t = (5, 6)        # Create a tuple\n",
    "print(type(t))    # Prints \"<class 'tuple'>\"\n",
    "print(d[t])       # Prints \"5\"\n",
    "print(d[(1, 2)])  # Prints \"1\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7b70f6ae-0bd5-4b7d-bdd7-bdca4bc4ff3f",
   "metadata": {},
   "source": [
    "### Function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3936b05f-66e3-4d51-a968-ac96dfe7781b",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "negative\n",
      "zero\n",
      "positive\n"
     ]
    }
   ],
   "source": [
    "def sign(x):\n",
    "    if x > 0:\n",
    "        return 'positive'\n",
    "    elif x < 0:\n",
    "        return 'negative'\n",
    "    else:\n",
    "        return 'zero'\n",
    "\n",
    "for x in [-1, 0, 1]:\n",
    "    print(sign(x))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e8cbe028-fe47-40d3-8417-e4e9afb196b8",
   "metadata": {},
   "source": [
    "### Classes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "dc94685b-f114-41e4-bd8f-d8c6a701a07b",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, Fred\n",
      "HELLO, FRED!\n"
     ]
    }
   ],
   "source": [
    "class Greeter(object):\n",
    "\n",
    "    # Constructor\n",
    "    def __init__(self, name):\n",
    "        self.name = name  # Create an instance variable\n",
    "\n",
    "    # Instance method\n",
    "    def greet(self, loud = False):\n",
    "        if loud:\n",
    "            print('HELLO, %s!' % self.name.upper())\n",
    "        else:\n",
    "            print('Hello, %s' % self.name)\n",
    "\n",
    "g = Greeter('Fred')  # Construct an instance of the Greeter class\n",
    "g.greet()            # Call an instance method; prints \"Hello, Fred\"\n",
    "g.greet(True)   # Call an instance method; prints \"HELLO, FRED!\""
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
