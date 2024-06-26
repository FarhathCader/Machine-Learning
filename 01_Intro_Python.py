{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "947024ab-3489-44d2-b7c9-7ead11a5ea13",
   "metadata": {},
   "source": [
    "# Introduction to Python"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "42734792-f632-4f3a-8ea5-a67d6dce9669",
   "metadata": {},
   "source": [
    "To excecute the following Cell, click inside that and pres Ctrl+Enter\n",
    "## Input and Output\n",
    "### Hello World"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "82bb3526-5539-44ce-b251-5112b2447cdf",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello World\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "43e55ac4-560a-4a72-9999-64c7d40ebc48",
   "metadata": {},
   "source": [
    "### Some more Output"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "41ed2e25-bb0c-49b3-9ac0-e642c6b51cae",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "print(5)\n",
    "print(1+1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "62dc9114-8a25-450d-a74a-09ec7f6a192e",
   "metadata": {},
   "source": [
    "### Variables\n",
    "- You will need to store data into variables\n",
    "- You can use those variables later on\n",
    "- You can perform operations with those variables\n",
    "- Variables are declared with a name, followed by ‘=‘ and a value ** An integer, string,… ** When declaring a variable, capitalization is important: *** ‘A’ <> ‘a’"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "714cdbd7-d4b4-4601-8f2b-8ff8857eee19",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "2\n",
      "This is a string\n"
     ]
    }
   ],
   "source": [
    "five = 5\n",
    "one = 1\n",
    "print(five)\n",
    "print(one + one)\n",
    "message = \"This is a string\"\n",
    "print(message)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a877e994-755d-4964-a20e-c6221f79cfb3",
   "metadata": {
    "tags": []
   },
   "source": [
    "#### Input two integers and print the sum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b3cbce81-4e95-434b-b2f9-49fcccb61a10",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number 1: 1\n",
      "Number 2: 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 + 1 = 2\n"
     ]
    }
   ],
   "source": [
    "num1 = int(input(\"Number 1:\"))\n",
    "num2 = int(input(\"Number 2:\"))\n",
    "sum = num1 + num2\n",
    "print(\"%d + %d = %d\"%(num1, num2, sum))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "edb021ea-709f-4088-bc1d-075f6920e04f",
   "metadata": {},
   "source": [
    "### Data Types"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "8aaf9952-2d72-409c-94aa-b0b1d1900b4b",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n",
      "<class 'float'>\n",
      "<class 'str'>\n",
      "-----\n",
      "<class 'int'>\n",
      "<class 'float'>\n",
      "<class 'float'>\n"
     ]
    }
   ],
   "source": [
    "integer_variable = 100\n",
    "floating_point_variable = 100.0\n",
    "string_variable = \"100\"\n",
    "\n",
    "print(type(integer_variable))\n",
    "print(type(floating_point_variable))\n",
    "print(type(string_variable))\n",
    "print(\"-----\")\n",
    "print(type(int(floating_point_variable)))\n",
    "print(type(float(integer_variable)))\n",
    "print(type(float(string_variable)))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3615acb1-3dbf-4125-b8b5-b84f015951d5",
   "metadata": {},
   "source": [
    "## File Input and Output\n",
    "### Writing to a File"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0ce9b692-c79a-445e-8898-da2a46ca4fae",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "my_file = open(\"output_file.txt\",'w')\n",
    "\n",
    "vars = \"This is a string\\n\"\n",
    "my_file.write(vars)\n",
    "\n",
    "var3 = 10\n",
    "my_file.write(str(var3))\n",
    "\n",
    "my_file.write(\"\\n\")\n",
    "\n",
    "var4 = 20.0\n",
    "my_file.write(str(var4))\n",
    "\n",
    "my_file.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f93f98be-3ede-4abb-8b06-cd9ceecce6ef",
   "metadata": {},
   "source": [
    "### Reading from a File"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "750e0d54-a0ae-4cea-b890-cce7cd7d0dae",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n",
      "My Name is Farhath\n",
      "I am 25 Years Old.\n"
     ]
    }
   ],
   "source": [
    "my_file = open(\"output_file.txt\",'r')\n",
    "content = my_file.read()\n",
    "print(content)\n",
    "my_file.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "590ee011-3c7a-4043-9b79-e72960d58f69",
   "metadata": {},
   "source": [
    "### Reading Line by Line"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ebf1ac0b-8dd0-49d3-a9df-5c27109cc459",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Greeting:  Hello\n",
      "\n",
      "Name:  My Name is Farhath\n",
      "\n",
      "Age:  I am 25 Years Old.\n"
     ]
    }
   ],
   "source": [
    "my_file = open(\"output_file.txt\",'r')\n",
    "vars = my_file.readline()\n",
    "var5 = my_file.readline()\n",
    "var6 = my_file.readline()\n",
    "print(\"Greeting: \", vars)\n",
    "print(\"Name: \", var5)\n",
    "print(\"Age: \", var6)\n",
    "my_file.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b63eae5a-3862-4a80-91b3-186d2e34898c",
   "metadata": {},
   "source": [
    "## Arithmetic Operations\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "7e8618e5-a51e-4dd0-9060-540440281884",
   "metadata": {},
   "source": [
    "+    Addition      1 + 1 = 2\n",
    "-    Subtraction   5 – 3 = 2\n",
    "/    Division      4 / 2 = 2\n",
    "%    Modulo      5 % 2 = 1\n",
    "*    Multiplication    5 * 2 = 10\n",
    "//   Floor division    5 // 2 = 2\n",
    "**   To the power of 2 ** 3 = 8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "621eb5ab-d014-4876-851b-e591e11b0534",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.5\n",
      "2\n",
      "2.0\n",
      "helloworld\n",
      "75\n"
     ]
    }
   ],
   "source": [
    "print(5/2)\n",
    "print(5//2)\n",
    "print(5.0//2)\n",
    "print(\"hello\" + \"world\")\n",
    "print(3*5**2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba1e1057-c14b-42f6-971b-89161c26b5c6",
   "metadata": {},
   "source": [
    "## Lists"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "7c405d39-cfef-4f73-bfbf-da50582ce33a",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 3, 4, 6]\n",
      "<class 'list'>\n"
     ]
    }
   ],
   "source": [
    "a = [ 1, 3 ,4, 6]\n",
    "print(a)\n",
    "print(type(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "f88096a7-4bb2-4d40-a0c6-50b279bbfef0",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'banana', 'cherry', 'apple', 'cherry']\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\", \"apple\", \"cherry\"]\n",
    "print(thislist)\n",
    "print(len(thislist))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "1ee9368d-add6-4870-8081-2ef7705c54fc",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "35\n",
      "abcmale\n"
     ]
    }
   ],
   "source": [
    "list1 = [\"abc\", 34, True, 40.5, \"male\"]\n",
    "a = list1[1] + list1[2]\n",
    "print(a)\n",
    "\n",
    "a = list1[0] + list1[4]\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a658a202-cadc-4152-a930-7f64ce0c7dde",
   "metadata": {},
   "source": [
    "## Control Flow\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "96076ba7-348d-4a9b-b8b0-371da79ccbff",
   "metadata": {},
   "source": [
    "### IF condition"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "c88e04ce-4064-4dfc-a372-6bc87f64f533",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "b is greater than a\n"
     ]
    }
   ],
   "source": [
    "a = 33\n",
    "b = 200\n",
    "if b > a:\n",
    "  print(\"b is greater than a\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "03d4b335-3cf7-4187-a2df-0eea0f6fedb0",
   "metadata": {},
   "source": [
    "### Indentation\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "2f30317e-b95d-4713-a0ba-5c14a84cded9",
   "metadata": {},
   "source": [
    "Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "e1c68739-ce3b-4e08-b522-00d1b2325777",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block (1443227691.py, line 4)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[39], line 4\u001b[1;36m\u001b[0m\n\u001b[1;33m    print(\"b is greater than a\") # you will get an error\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m expected an indented block\n"
     ]
    }
   ],
   "source": [
    "a = 33\n",
    "b = 200\n",
    "if b > a:\n",
    "print(\"b is greater than a\") # you will get an error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "5c14c23b-330f-4c19-abef-f5378166e3fd",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Both conditions are True\n"
     ]
    }
   ],
   "source": [
    "a = 200\n",
    "b = 33\n",
    "c = 500\n",
    "#c=50\n",
    "if a > b and c > a:\n",
    "  print(\"Both conditions are True\")\n",
    "else:\n",
    "  print(\"Both conditions are not True\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17e91f59-2053-42bd-bf3f-773fa9717fe8",
   "metadata": {},
   "source": [
    "### for loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "685f4242-6e01-4887-a2e2-7be94be6b450",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apple\n",
      "banana\n",
      "cherry\n"
     ]
    }
   ],
   "source": [
    "fruits = [\"apple\", \"banana\", \"cherry\"]\n",
    "for x in fruits:\n",
    "  print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "b4c89ef9-d09e-45b1-b683-edf51ab198dd",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "b\n",
      "a\n",
      "n\n",
      "a\n",
      "n\n",
      "a\n"
     ]
    }
   ],
   "source": [
    "for x in \"banana\":\n",
    "  print(x)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "b37d53d3-39d5-4feb-b7cd-c4f8d5126d1f",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "for x in range(5):\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "54d0953a-ceac-4b73-87b5-67d2b9eb2490",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "for x in range(5,10):\n",
    "    print(x)"
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
