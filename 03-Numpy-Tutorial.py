{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### import numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'numpy.ndarray'>\n",
      "(3,)\n",
      "1 2 3\n",
      "[5 2 3]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "\n",
    "a = np.array([1, 2, 3])   # Create a rank 1 array\n",
    "print(type(a))            # Prints \"<class 'numpy.ndarray'>\"\n",
    "print(a.shape)            # Prints \"(3,)\"\n",
    "print(a[0], a[1], a[2])   # Prints \"1 2 3\"\n",
    "a[0] = 5                  # Change an element of the array\n",
    "print(a)    \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Why we need Numpy?\n",
    "\n",
    "Numpy is faster than the normal list. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.020045042037964 0.064361572265625\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "import numpy as np\n",
    "size_of_vec = 10000000\n",
    "def pure_python_version():\n",
    "    t1 = time.time()\n",
    "    X = range(size_of_vec)\n",
    "    Y = range(size_of_vec)\n",
    "    Z = []\n",
    "    for i in range(len(X)):\n",
    "        Z.append(X[i] + Y[i])\n",
    "    return time.time() - t1\n",
    "\n",
    "def numpy_version():\n",
    "    t1 = time.time()\n",
    "    X = np.arange(size_of_vec)\n",
    "    Y = np.arange(size_of_vec)\n",
    "    Z = X + Y\n",
    "    return time.time() - t1\n",
    "t1 = pure_python_version()\n",
    "t2 = numpy_version()\n",
    "print(t1, t2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 0. Numpy Data Types"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### A list of Numpy Data Types "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Type</th>\n",
       "      <th>Type Code</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>int8</td>\n",
       "      <td>i1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>uint8</td>\n",
       "      <td>u1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>int16</td>\n",
       "      <td>i2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>uint16</td>\n",
       "      <td>u2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>int32</td>\n",
       "      <td>i4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>uint32</td>\n",
       "      <td>u4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>int64</td>\n",
       "      <td>i8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>uint64</td>\n",
       "      <td>u8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>float16</td>\n",
       "      <td>f2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>float32</td>\n",
       "      <td>f4 or f</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>float64</td>\n",
       "      <td>f8 or d</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>float128</td>\n",
       "      <td>f16 or g</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>complex64</td>\n",
       "      <td>c8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>complex128</td>\n",
       "      <td>c16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>bool</td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>object</td>\n",
       "      <td>O</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>string_</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>unicode_</td>\n",
       "      <td>U</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Type Type Code\n",
       "0         int8        i1\n",
       "1        uint8        u1\n",
       "2        int16        i2\n",
       "3       uint16        u2\n",
       "4        int32        i4\n",
       "5       uint32        u4\n",
       "6        int64        i8\n",
       "7       uint64        u8\n",
       "8      float16        f2\n",
       "9      float32   f4 or f\n",
       "10     float64   f8 or d\n",
       "11    float128  f16 or g\n",
       "12   complex64        c8\n",
       "13  complex128       c16\n",
       "14        bool          \n",
       "15      object         O\n",
       "16     string_         S\n",
       "17    unicode_         U"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "dtypes = pd.DataFrame(\n",
    "    {\n",
    "        'Type': ['int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64', 'float16', 'float32', 'float64', 'float128', 'complex64', 'complex128', 'bool', 'object', 'string_', 'unicode_'],\n",
    "        'Type Code': ['i1', 'u1', 'i2', 'u2', 'i4', 'u4', 'i8', 'u8', 'f2', 'f4 or f', 'f8 or d', 'f16 or g', 'c8', 'c16', '', 'O', 'S', 'U']\n",
    "    }\n",
    ")\n",
    "\n",
    "dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[   1    2 1024]\n",
      "int64\n",
      "8\n",
      "3\n",
      "[1.+2.j 3.-4.j]\n",
      "complex64\n"
     ]
    }
   ],
   "source": [
    "# create an array with a specified data type\n",
    "arr = np.array([1,2,1024,], dtype='i8')\n",
    "print(arr)\n",
    "print(arr.dtype)\n",
    "print(arr.itemsize)\n",
    "print(arr.size)\n",
    "\n",
    "arr = np.array([1+2j, 3-4j], dtype=np.complex64)\n",
    "print(arr)\n",
    "print(arr.dtype)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### string data type"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[b'abc' b'def']\n",
      "|S3\n"
     ]
    }
   ],
   "source": [
    "# set the max length of the string using S + some number, such as 'S3'\n",
    "# any string longer than the max length will be truncated\n",
    "s = np.array(['abc', 'defg'], dtype='S3')\n",
    "print(s)\n",
    "print(s.dtype)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1. Create Arrays"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### create an array from a Python array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5]\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([1,2,3,4,5])\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 1 2 3 4 5 6 7 8 9]\n"
     ]
    }
   ],
   "source": [
    "arr = np.array(range(10))\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### create an array in a specified data type"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5 6]\n",
      "<class 'numpy.dtype[int16]'>\n",
      "[1 2 3 4 5 6]\n",
      "<class 'numpy.dtype[int64]'>\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([1,2,3,4,5,6], dtype='i2')\n",
    "print(arr)\n",
    "print(type(arr.dtype))\n",
    "arr = np.array([1,2,3,4,5,6], dtype='i8')\n",
    "print(arr)\n",
    "print(type(arr.dtype))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### create an aray of evenly spaced values within a specified interval"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 0  2  4  6  8 10 12 14 16 18]\n"
     ]
    }
   ],
   "source": [
    "# np.arange(start, stop, step)\n",
    "arr = np.arange(0, 20, 2)  \n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### create an array of evenly spaced numbers in a specified interval"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 0.   0.5  1.   1.5  2.   2.5  3.   3.5  4.   4.5  5.   5.5  6.   6.5\n",
      "  7.   7.5  8.   8.5  9.   9.5 10. ]\n"
     ]
    }
   ],
   "source": [
    "# np.linspace(start, stop, num_of_elements, endpoint=True, retstep=False) \n",
    "arr = np.linspace(0, 10, 21)\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5 5.  5.5 6.  6.5 7.  7.5 8.  8.5\n",
      " 9.  9.5]\n",
      "0.5\n"
     ]
    }
   ],
   "source": [
    "# exclude endpoint and return setp size\n",
    "arr, step = np.linspace(0, 10, 20, endpoint=False, retstep=True)\n",
    "print(arr)\n",
    "print(step)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### create an array of random values in a given shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.6868771  0.34770072 0.8424902 ]\n",
      " [0.66194469 0.02178723 0.09604589]\n",
      " [0.74196836 0.38700025 0.37018871]]\n"
     ]
    }
   ],
   "source": [
    "arr = np.random.rand(3, 3)\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### create an array of zeros in a given shape "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 1 1]\n",
      " [1 1 1]]\n"
     ]
    }
   ],
   "source": [
    "zeros = np.ones((2,3), dtype='i4')\n",
    "print(zeros)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### create an array of integer random values in a given shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[95 70 53 38 27 83]\n",
      " [ 7 72 25 27 17 79]\n",
      " [70 98 13 64 55 16]\n",
      " [54 95 57 40 67 16]\n",
      " [72 28 49 38 19  8]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr = np.random.randint(1,100,size=(5,6))\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### create an array of zeros with the same shape and data type as a given array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0 0 0 0 0 0]\n",
      " [0 0 0 0 0 0]\n",
      " [0 0 0 0 0 0]\n",
      " [0 0 0 0 0 0]\n",
      " [0 0 0 0 0 0]]\n"
     ]
    }
   ],
   "source": [
    "zeros = np.zeros_like(arr)\n",
    "print(zeros)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### create an array of ones in a given shape "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 1. 1.]\n",
      " [1. 1. 1.]]\n"
     ]
    }
   ],
   "source": [
    "ones = np.ones((2,3))\n",
    "print(ones)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### create an array of ones with the same shape and data type as a given array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 1. 1.]\n",
      " [1. 1. 1.]\n",
      " [1. 1. 1.]]\n"
     ]
    }
   ],
   "source": [
    "ones = np.ones_like(arr)\n",
    "print(ones)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### create an array of arbitrary values in a given shape "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 1. 1.]\n",
      " [1. 1. 1.]]\n"
     ]
    }
   ],
   "source": [
    "empty = np.empty((2,3))\n",
    "print(empty)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### create an array of arbitrary values with the same shape and data type as a given array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0 0 0 0 0 0]\n",
      " [0 0 0 0 0 0]\n",
      " [0 0 0 0 0 0]\n",
      " [0 0 0 0 0 0]\n",
      " [0 0 0 0 0 0]]\n"
     ]
    }
   ],
   "source": [
    "empty = np.empty_like(arr)\n",
    "print(empty)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### create an array of constant values in a given shape  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[5 5 5]\n",
      " [5 5 5]]\n"
     ]
    }
   ],
   "source": [
    "p = np.full((2,3), 5)\n",
    "print(p)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### create an array of constant values with the same shape and data type as a given array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[5 5 5 5 5 5]\n",
      " [5 5 5 5 5 5]\n",
      " [5 5 5 5 5 5]\n",
      " [5 5 5 5 5 5]\n",
      " [5 5 5 5 5 5]]\n"
     ]
    }
   ],
   "source": [
    "p = np.full_like(arr, 5)\n",
    "print(p)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### create an array by repetition"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 0 0 1 1 1 2 2 2]\n"
     ]
    }
   ],
   "source": [
    "# repeat each element of an array by a specified number of times\n",
    "# np.repeat(iterable, reps, axis=None)\n",
    "arr = [0, 1, 2]\n",
    "print(np.repeat(arr, 3))    # or np.repeat(range(3), 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2]\n",
      " [3 4]\n",
      " [3 4]]\n"
     ]
    }
   ],
   "source": [
    "# repeat along a specified axis with specified number of repetitions\n",
    "arr = [[1,2], [3,4]]\n",
    "print(np.repeat(arr, [1,2], axis=0))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 1 2 0 1 2 0 1 2]\n"
     ]
    }
   ],
   "source": [
    "# repeat an array by a specified number of times\n",
    "arr = [0, 1, 2]\n",
    "print(np.tile(arr, 3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0 1 2 0 1 2]\n",
      " [0 1 2 0 1 2]]\n"
     ]
    }
   ],
   "source": [
    "# repeat along specified axes\n",
    "print(np.tile(arr, (2,2)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### create an identity matrix with a given diagonal size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 0. 0.]\n",
      " [0. 1. 0.]\n",
      " [0. 0. 1.]]\n"
     ]
    }
   ],
   "source": [
    "identity_matrix = np.eye(3)\n",
    "print(identity_matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 0. 0.]\n",
      " [0. 1. 0.]\n",
      " [0. 0. 1.]]\n"
     ]
    }
   ],
   "source": [
    "identity_matrix = np.identity(3)\n",
    "print(identity_matrix)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### create an identity matrix with a diagonal offset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0. 1. 0. 0. 0.]\n",
      " [0. 0. 1. 0. 0.]\n",
      " [0. 0. 0. 1. 0.]\n",
      " [0. 0. 0. 0. 1.]\n",
      " [0. 0. 0. 0. 0.]]\n"
     ]
    }
   ],
   "source": [
    "identity_matrix = np.eye(5, k=1)    # positive number shifts the diagonal upward\n",
    "print(identity_matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0. 0. 0. 0. 0.]\n",
      " [0. 0. 0. 0. 0.]\n",
      " [1. 0. 0. 0. 0.]\n",
      " [0. 1. 0. 0. 0.]\n",
      " [0. 0. 1. 0. 0.]]\n"
     ]
    }
   ],
   "source": [
    "identity_matrix = np.eye(5, k=-2)   # negative number shifts the diagonal downward\n",
    "print(identity_matrix)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### extract the diagonal array / create a diagonal array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.07710888 0.68905534 0.81142113 0.60805738 0.14322708]\n",
      " [0.70950747 0.11738625 0.5630424  0.27911771 0.91741603]\n",
      " [0.62715481 0.8857803  0.22214541 0.56813747 0.97598708]\n",
      " [0.65309756 0.78466617 0.40848438 0.01693925 0.18625553]\n",
      " [0.97973236 0.15756793 0.28687775 0.1440273  0.08333093]]\n"
     ]
    }
   ],
   "source": [
    "arr = np.random.rand(5,5)\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.07710888 0.11738625 0.22214541 0.01693925 0.08333093]\n"
     ]
    }
   ],
   "source": [
    "# extract the diagonal\n",
    "print(np.diag(arr))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 0 0 0 0]\n",
      " [0 2 0 0 0]\n",
      " [0 0 3 0 0]\n",
      " [0 0 0 4 0]\n",
      " [0 0 0 0 5]]\n"
     ]
    }
   ],
   "source": [
    "# create a matrix with a specified diagonal array\n",
    "arr = np.diag([1,2,3,4,5])\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2. Inspect Arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "arr = np.array([[1,2,3], [4,5,6]], dtype=np.int64)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### inspect general information of an array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "class:  ndarray\n",
      "shape:  (2, 3)\n",
      "strides:  (24, 8)\n",
      "itemsize:  8\n",
      "aligned:  True\n",
      "contiguous:  True\n",
      "fortran:  False\n",
      "data pointer: 0x1c063a4a2b0\n",
      "byteorder:  little\n",
      "byteswap:  False\n",
      "type: int64\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print(np.info(arr))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### inspect the data type of an array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "int64\n"
     ]
    }
   ],
   "source": [
    "print(arr.dtype)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### inspect the dimension of an array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2, 3)\n"
     ]
    }
   ],
   "source": [
    "print(arr.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### inspect length of an array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "print(len(arr))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### inspect the number of dimensions of an array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "print(arr.ndim)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### inspect the number of elements in an array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "print(arr.size)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### inspect the number of bytes of each element in an array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n"
     ]
    }
   ],
   "source": [
    "print(arr.itemsize)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### inspect the memory size of an array (in byte)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "48\n"
     ]
    }
   ],
   "source": [
    "# arr.nbytes = arr.size * arr.itemsize\n",
    "print(arr.nbytes)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 3. Sampling Methods"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### set seed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "np.random.seed(123)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### set random state which is independent from the global seed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.88594794, 0.07791236, 0.97964616, 0.24767146, 0.75288472,\n",
       "       0.52667564, 0.90755375, 0.8840703 , 0.08926896, 0.5173446 ])"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rs = np.random.RandomState(321)\n",
    "rs.rand(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### generate a random sample from interval [0, 1) in a given shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.6964691855978616\n"
     ]
    }
   ],
   "source": [
    "# generate a random scalar\n",
    "print(np.random.rand())      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.28613933 0.22685145 0.55131477]\n"
     ]
    }
   ],
   "source": [
    "# generate a 1-D array\n",
    "print(np.random.rand(3))           "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.71946897 0.42310646 0.9807642 ]\n",
      " [0.68482974 0.4809319  0.39211752]\n",
      " [0.34317802 0.72904971 0.43857224]]\n"
     ]
    }
   ],
   "source": [
    "# generate a 2-D array\n",
    "print(np.random.rand(3,3))          "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### generate a sample from the standard normal distribution (mean = 0, var = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[-0.14337247 -0.6191909  -0.76943347]\n",
      " [ 0.57674602  0.12652592 -1.30148897]\n",
      " [ 2.20742744  0.52274247  0.46564476]]\n"
     ]
    }
   ],
   "source": [
    "print(np.random.randn(3,3))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### generate an array of random integers in a given interval [low, high)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5 7 2]\n"
     ]
    }
   ],
   "source": [
    "# np.ranodm.randint(low, high, size, dtype)\n",
    "print(np.random.randint(1, 10, 3, 'i8'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### generate an array of random floating-point numbers in the interval [0.0, 1.0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.65472131 0.37380143 0.23451288 0.98799529 0.76599595 0.77700444\n",
      " 0.02798196 0.17390652 0.15408224 0.07708648]\n",
      "[0.8898657  0.7503787  0.69340324 0.51176338 0.46426806 0.56843069\n",
      " 0.30254945 0.49730879 0.68326291 0.91669867]\n",
      "[0.10892895 0.49549179 0.23283593 0.43686066 0.75154299 0.48089213\n",
      " 0.79772841 0.28270293 0.43341824 0.00975735]\n",
      "[0.34079598 0.68927201 0.86936929 0.26780382 0.45674792 0.26828131\n",
      " 0.8370528  0.27051466 0.53006201 0.17537266]\n"
     ]
    }
   ],
   "source": [
    "# the following methods are the same as np.random.rand()\n",
    "print(np.random.random_sample(10))\n",
    "print(np.random.random(10))\n",
    "print(np.random.ranf(10))\n",
    "print(np.random.sample(10))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### generate a random sample from a given 1-D array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 1 1 1 1 1 1 2 2 1]\n"
     ]
    }
   ],
   "source": [
    "# np.random.choice(iterable_or_int, size, replace=True, p=weights)\n",
    "print(np.random.choice(range(3), 10, replace=True, p=[0.1, 0.8, 0.1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 0 1 2 2 0 1 1 1 0]\n"
     ]
    }
   ],
   "source": [
    "print(np.random.choice(3, 10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2 2 1 3 2 3 1 2 1 3]\n"
     ]
    }
   ],
   "source": [
    "print(np.random.choice([1,2,3], 10))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### shuffle an array in place"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 1 2 3 4 5 6 7 8 9]\n"
     ]
    }
   ],
   "source": [
    "arr = np.array(range(10))\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 8 5 4 0 6 7 9 3]\n"
     ]
    }
   ],
   "source": [
    "np.random.shuffle(arr)\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### generate a permutation of an array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The initial array:  [0 1 2 3 4 5 6 7 8 9]\n",
      "A permutation of the array:  [7 5 1 0 2 6 9 4 3 8]\n"
     ]
    }
   ],
   "source": [
    "# similar to np.random.shuffle(), but it returns a copy rather than making changes in place\n",
    "arr = np.array(range(10))\n",
    "print('The initial array: ', arr)\n",
    "print('A permutation of the array: ', np.random.permutation(arr))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 4. Math Functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.36178866, 0.22826323, 0.29371405, 0.63097612, 0.09210494],\n",
       "       [0.43370117, 0.43086276, 0.4936851 , 0.42583029, 0.31226122],\n",
       "       [0.42635131, 0.89338916, 0.94416002, 0.50183668, 0.62395295],\n",
       "       [0.1156184 , 0.31728548, 0.41482621, 0.86630916, 0.25045537],\n",
       "       [0.48303426, 0.98555979, 0.51948512, 0.61289453, 0.12062867]])"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr = np.random.rand(5,5)\n",
    "arr"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### element-wise addition, subtraction, multiplication and division"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[10.36178866 10.22826323 10.29371405 10.63097612 10.09210494]\n",
      " [10.43370117 10.43086276 10.4936851  10.42583029 10.31226122]\n",
      " [10.42635131 10.89338916 10.94416002 10.50183668 10.62395295]\n",
      " [10.1156184  10.31728548 10.41482621 10.86630916 10.25045537]\n",
      " [10.48303426 10.98555979 10.51948512 10.61289453 10.12062867]]\n",
      "[[-9.63821134 -9.77173677 -9.70628595 -9.36902388 -9.90789506]\n",
      " [-9.56629883 -9.56913724 -9.5063149  -9.57416971 -9.68773878]\n",
      " [-9.57364869 -9.10661084 -9.05583998 -9.49816332 -9.37604705]\n",
      " [-9.8843816  -9.68271452 -9.58517379 -9.13369084 -9.74954463]\n",
      " [-9.51696574 -9.01444021 -9.48051488 -9.38710547 -9.87937133]]\n",
      "[[3.61788656 2.28263231 2.93714046 6.30976124 0.9210494 ]\n",
      " [4.33701173 4.30862763 4.93685098 4.2583029  3.12261223]\n",
      " [4.26351307 8.93389163 9.44160018 5.01836676 6.23952952]\n",
      " [1.15618395 3.17285482 4.14826212 8.66309158 2.50455365]\n",
      " [4.83034264 9.85559786 5.19485119 6.12894526 1.20628666]]\n",
      "[[0.03617887 0.02282632 0.0293714  0.06309761 0.00921049]\n",
      " [0.04337012 0.04308628 0.04936851 0.04258303 0.03122612]\n",
      " [0.04263513 0.08933892 0.094416   0.05018367 0.0623953 ]\n",
      " [0.01156184 0.03172855 0.04148262 0.08663092 0.02504554]\n",
      " [0.04830343 0.09855598 0.05194851 0.06128945 0.01206287]]\n"
     ]
    }
   ],
   "source": [
    "print(arr + 10)\n",
    "print(arr - 10)\n",
    "print(arr * 10)\n",
    "print(arr / 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 9 11 13]\n",
      "[19 21 23]\n",
      "[11 12 13]\n",
      "[11 24 39]\n"
     ]
    }
   ],
   "source": [
    "arr1 = np.array([1,2,3])\n",
    "# the above operations can be performed using numpy built-in functions\n",
    "# which can save memory as the output can be stored in the original array rather than assigning new memoryarr = np.array([1,2,3])\n",
    "np.add(arr1, [8,9,10], out=arr1)\n",
    "print(arr1)\n",
    "\n",
    "np.add(arr1, 10, out=arr1)\n",
    "print(arr1)\n",
    "\n",
    "np.subtract(arr1, [8,9,10], out=arr1)\n",
    "print(arr1)\n",
    "\n",
    "np.multiply(arr1, [1,2,3], out=arr1)\n",
    "print(arr1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### element-wise exponentiation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5.98741417e+04 2.64891221e+10 8.65934004e+16]\n"
     ]
    }
   ],
   "source": [
    "print(np.exp(arr1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### element-wise logorithm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[-1.01669506 -1.47725579 -1.22514862 -0.46048726 -2.3848267 ]\n",
      " [-0.83539952 -0.84196565 -0.70585742 -0.85371439 -1.16391519]\n",
      " [-0.85249161 -0.112733   -0.05745962 -0.68948056 -0.47168031]\n",
      " [-2.15746021 -1.14795334 -0.87989561 -0.14351344 -1.38447456]\n",
      " [-0.72766769 -0.01454549 -0.65491711 -0.48956242 -2.11503833]]\n"
     ]
    }
   ],
   "source": [
    "# natural log\n",
    "print(np.log(arr))      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[-0.19511665 -5.08687587 -0.85714556 -2.05740665 -0.17656854]\n",
      " [-1.11954666 -2.37205457 -1.76762165 -0.28995511 -0.83782252]\n",
      " [-0.56080147 -0.3055625  -0.20328239 -1.25845119 -4.08465428]\n",
      " [-1.06353278 -0.94020332 -0.78430396 -1.69339245 -0.12047831]\n",
      " [-0.60966799 -1.51770357 -0.88604873 -1.15504109 -1.82459185]]\n"
     ]
    }
   ],
   "source": [
    "# base 2\n",
    "print(np.log2(arr))     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[-0.05873596 -1.53130222 -0.25802652 -0.61934112 -0.05315243]\n",
      " [-0.33701713 -0.71405958 -0.53210714 -0.08728519 -0.25220971]\n",
      " [-0.16881806 -0.09198348 -0.0611941  -0.37883156 -1.22960346]\n",
      " [-0.32015527 -0.2830294  -0.23609902 -0.50976192 -0.03626758]\n",
      " [-0.18352835 -0.4568743  -0.26672725 -0.34770202 -0.54925688]]\n"
     ]
    }
   ],
   "source": [
    "# base 10\n",
    "print(np.log10(arr))    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### element-wise square root"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.93461343 0.17153348 0.74299645 0.49015049 0.94064075]\n",
      " [0.67840874 0.43951147 0.54193404 0.90439345 0.74798889]\n",
      " [0.82336228 0.89951469 0.93197219 0.64652336 0.24277182]\n",
      " [0.69170731 0.72191373 0.76199214 0.55605665 0.95910512]\n",
      " [0.80953536 0.59096648 0.73559095 0.67011446 0.53133884]]\n"
     ]
    }
   ],
   "source": [
    "print(np.sqrt(arr))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### element-wise sine and cosine"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.7665826  0.02941949 0.52442846 0.23794303 0.77379149]\n",
      " [0.44416174 0.19197122 0.28948859 0.72973036 0.5307518 ]\n",
      " [0.62717856 0.72368474 0.76340745 0.40592657 0.05890404]\n",
      " [0.46041177 0.49788598 0.54855249 0.30429572 0.79553051]\n",
      " [0.60943479 0.34218509 0.51507406 0.43411297 0.27858547]]\n"
     ]
    }
   ],
   "source": [
    "print(np.sin(arr))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'arr' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32mc:\\rajitha\\teaching\\ee5253\\ML-Labs-2023\\03-Numpy-Tutorial.ipynb Cell 114\u001b[0m line \u001b[0;36m1\n\u001b[1;32m----> <a href='vscode-notebook-cell:/c%3A/rajitha/teaching/ee5253/ML-Labs-2023/03-Numpy-Tutorial.ipynb#Y221sZmlsZQ%3D%3D?line=0'>1</a>\u001b[0m \u001b[39mprint\u001b[39m(np\u001b[39m.\u001b[39mcos(arr))\n",
      "\u001b[1;31mNameError\u001b[0m: name 'arr' is not defined"
     ]
    }
   ],
   "source": [
    "print(np.cos(arr))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### sum along a specified axis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2.08825411 1.96609652 3.58768227 2.360436   2.60246875]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "# sum along the row\n",
    "print(np.sum(arr, axis=0))  \n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1.9783356  2.51224975 1.82123326 2.86053862 3.43258042]\n"
     ]
    }
   ],
   "source": [
    "# sum along the column\n",
    "print(np.sum(arr, axis=1))    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### compute the min and max along a specified axis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.46023842 0.02942373 0.2936925  0.2402475  0.05893816]\n"
     ]
    }
   ],
   "source": [
    "# calculate min along the row\n",
    "print(np.min(arr, axis=0))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.88480501 0.81792751 0.86857215 0.91988263 0.6553475 ]\n"
     ]
    }
   ],
   "source": [
    "# calculate max along the column\n",
    "print(np.max(arr, axis=1))    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.919882625254582\n",
      "0.029423733551983133\n"
     ]
    }
   ],
   "source": [
    "# if axis not specified, calculate the max/min value of all elements\n",
    "print(np.max(arr))\n",
    "print(np.min(arr))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### compute the indices of the min and max along a specified axis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 0 1 0 2]\n",
      "[0 2 2 1 3]\n"
     ]
    }
   ],
   "source": [
    "# along the row\n",
    "print(np.argmin(arr, axis=0))\n",
    "print(np.argmax(arr, axis=0))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 1 4 3 4]\n",
      "[4 3 2 4 0]\n"
     ]
    }
   ],
   "source": [
    "# along the column\n",
    "print(np.argmin(arr, axis=1))\n",
    "print(np.argmax(arr, axis=1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "19\n"
     ]
    }
   ],
   "source": [
    "# if axis not specified, return the index of the flattened array\n",
    "print(np.argmin(arr))\n",
    "print(np.argmax(arr))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### compute element-wise min and max of two arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 4 5 8 9]\n",
      "[0 3 3 7 7]\n"
     ]
    }
   ],
   "source": [
    "arr1 = np.array([1, 3, 5, 7, 9])\n",
    "arr2 = np.array([0, 4, 3, 8, 7])\n",
    "print(np.maximum(arr1, arr2))\n",
    "print(np.minimum(arr1, arr2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### split fractional and integral parts of a floating-point array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "fractional:  [0.95876525 0.63480983 0.15191279 0.17618677 0.52041829 0.32778859\n",
      " 0.7311902  0.67888445 0.87478322 0.4941493 ]\n",
      "integral:  [2. 5. 7. 5. 3. 6. 8. 1. 9. 3.]\n"
     ]
    }
   ],
   "source": [
    "arr1 = np.random.rand(10) * 10\n",
    "re, intg = np.modf(arr1)\n",
    "print('fractional: ', re)\n",
    "print('integral: ', intg)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### compute the mean"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.5129393054604379\n"
     ]
    }
   ],
   "source": [
    "# compute the overall mean\n",
    "print(np.mean(arr))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.62909453 0.38042431 0.56720689 0.44688397 0.54108683]\n"
     ]
    }
   ],
   "source": [
    "# compute the mean along the row\n",
    "print(np.mean(arr, axis=0))   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.51600445 0.46490323 0.56651098 0.56186642 0.45541146]\n"
     ]
    }
   ],
   "source": [
    "# compute the mean along the column\n",
    "print(np.mean(arr, axis=1)) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### compute the median"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.52115942968839\n"
     ]
    }
   ],
   "source": [
    "# compute the overall median\n",
    "print(np.median(arr))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.6553475  0.34924138 0.55204372 0.41799246 0.55948738]\n"
     ]
    }
   ],
   "source": [
    "# compute the median along the row\n",
    "print(np.median(arr, axis=0)) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.55204372 0.46023842 0.67792545 0.52115943 0.4490534 ]\n"
     ]
    }
   ],
   "source": [
    "# compute the median along the column\n",
    "print(np.median(arr, axis=1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### compute the percentile"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.05596961 0.58954837 0.92058256]\n"
     ]
    }
   ],
   "source": [
    "arr1 = np.random.rand(100)\n",
    "# compute 5, 65, and 95 percentiles of the array\n",
    "print(np.percentile(arr1, [5, 65, 95]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### compute the standard deviation & variance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.25305273176784365\n"
     ]
    }
   ],
   "source": [
    "# compute the overall standard deviation\n",
    "print(np.std(arr))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.15100481 0.26938074 0.18260514 0.20008424 0.33508033]\n"
     ]
    }
   ],
   "source": [
    "# compute the standard deviation along the row\n",
    "print(np.std(arr, axis=0))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.33997649 0.21759869 0.29739013 0.20049061 0.13310804]\n"
     ]
    }
   ],
   "source": [
    "# compute the standard deviation along the column\n",
    "print(np.std(arr, axis=1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.06403568505516823\n"
     ]
    }
   ],
   "source": [
    "# compute the overall variance\n",
    "print(np.var(arr))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.02280245 0.07256599 0.03334464 0.0400337  0.11227883]\n"
     ]
    }
   ],
   "source": [
    "# compute the variance along the row\n",
    "print(np.var(arr, axis=0))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.11558401 0.04734919 0.08844089 0.04019649 0.01771775]\n"
     ]
    }
   ],
   "source": [
    "# compute the variance along the column\n",
    "print(np.var(arr, axis=1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### compute the covariance & correlation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
    "arr = np.random.rand(5,8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 0.05402285  0.03916784  0.03506723  0.0367739  -0.02741259]\n",
      " [ 0.03916784  0.03992086  0.01853696  0.04299328 -0.02678781]\n",
      " [ 0.03506723  0.01853696  0.06217596  0.01094847  0.00254219]\n",
      " [ 0.0367739   0.04299328  0.01094847  0.11372942 -0.02614117]\n",
      " [-0.02741259 -0.02678781  0.00254219 -0.02614117  0.06564368]]\n"
     ]
    }
   ],
   "source": [
    "print(np.cov(arr))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1.         -0.54127501]\n",
      " [-0.54127501  1.        ]]\n"
     ]
    }
   ],
   "source": [
    "print(np.corrcoef(arr[:,0], arr[:,1]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### element-wise comparison"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [],
   "source": [
    "arr1 = np.array([1,2,3,4,5])\n",
    "arr2 = np.array([5,4,3,2,1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[False False  True False False]\n",
      "[ True  True False False False]\n"
     ]
    }
   ],
   "source": [
    "# return an array of bools\n",
    "print(arr1 == arr2)    \n",
    "print(arr1 < 3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 5. Slicing & Indexing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 0  1  2  3  4  5  6  7  8  9]\n",
      " [10 11 12 13 14 15 16 17 18 19]\n",
      " [20 21 22 23 24 25 26 27 28 29]\n",
      " [30 31 32 33 34 35 36 37 38 39]\n",
      " [40 41 42 43 44 45 46 47 48 49]\n",
      " [50 51 52 53 54 55 56 57 58 59]\n",
      " [60 61 62 63 64 65 66 67 68 69]\n",
      " [70 71 72 73 74 75 76 77 78 79]\n",
      " [80 81 82 83 84 85 86 87 88 89]\n",
      " [90 91 92 93 94 95 96 97 98 99]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr = np.array(range(100)).reshape((10,10))\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### select an element by row and column indices"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "55\n",
      "55\n"
     ]
    }
   ],
   "source": [
    "print(arr[5][5])\n",
    "# or more concisely\n",
    "print(arr[5,5])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### indexing with slicing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 0  1  2  3  4  5  6  7  8  9]\n",
      " [10 11 12 13 14 15 16 17 18 19]\n",
      " [20 21 22 23 24 25 26 27 28 29]\n",
      " [30 31 32 33 34 35 36 37 38 39]\n",
      " [40 41 42 43 44 45 46 47 48 49]\n",
      " [50 51 52 53 54 55 56 57 58 59]\n",
      " [60 61 62 63 64 65 66 67 68 69]\n",
      " [70 71 72 73 74 75 76 77 78 79]\n",
      " [80 81 82 83 84 85 86 87 88 89]\n",
      " [90 91 92 93 94 95 96 97 98 99]]\n",
      "[[14 15]\n",
      " [24 25]]\n"
     ]
    }
   ],
   "source": [
    "print(arr)\n",
    "print(arr[1:3, 4:6])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[0 1]\n",
      "  [2 3]]\n",
      "\n",
      " [[4 5]\n",
      "  [6 7]]]\n"
     ]
    }
   ],
   "source": [
    "# ellipsis slicing: auto-complete the dimensions\n",
    "arr = np.array(range(16)).reshape(2,2,2,2)\n",
    "# equivalent to arr[0,:,:,:]\n",
    "print(arr[0, ...])    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### assign a scalar to a slice by broadcasting"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[[  0   1]\n",
      "   [  2   3]]\n",
      "\n",
      "  [[  4   5]\n",
      "   [  6   7]]]\n",
      "\n",
      "\n",
      " [[[100 100]\n",
      "   [100 100]]\n",
      "\n",
      "  [[100 100]\n",
      "   [100 100]]]]\n"
     ]
    }
   ],
   "source": [
    "arr[1:3,:] = 100    # or simply arr[1:3]\n",
    "arr[:,8:] = 100\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### boolean indexing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 0  1  2  3  4]\n",
      " [ 5  6  7  8  9]\n",
      " [10 11 12 13 14]\n",
      " [15 16 17 18 19]\n",
      " [20 21 22 23 24]]\n",
      "[[ 0  1  2  3  4]\n",
      " [ 5  6  7  8  9]\n",
      " [15 16 17 18 19]]\n"
     ]
    }
   ],
   "source": [
    "arr1 = np.arange(25).reshape((5,5))\n",
    "print(arr1)\n",
    "bools = np.array([True, True, False, True, False])\n",
    "print(arr1[bools])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[10 11 12 13 14]\n",
      " [20 21 22 23 24]]\n"
     ]
    }
   ],
   "source": [
    "# negate the condition\n",
    "print(arr1[~bools])    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 0  1  2  3  4]\n",
      " [20 21 22 23 24]]\n"
     ]
    }
   ],
   "source": [
    "arr2 = np.array([1,2,3,4,5])\n",
    "# multiple conditions\n",
    "print(arr1[(arr2<2) | (arr2>4)])    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### fancy indexing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.78099794, 0.28653662, 0.30646975, 0.66526147, 0.11139217,\n",
       "        0.66487245, 0.88785679, 0.69631127, 0.44032788, 0.43821438],\n",
       "       [0.7650961 , 0.565642  , 0.08490416, 0.58267109, 0.8148437 ,\n",
       "        0.33706638, 0.92757658, 0.750717  , 0.57406383, 0.75164399],\n",
       "       [0.07914896, 0.85938908, 0.82150411, 0.90987166, 0.1286312 ,\n",
       "        0.08178009, 0.13841557, 0.39937871, 0.42430686, 0.56221838],\n",
       "       [0.12224355, 0.2013995 , 0.81164435, 0.46798757, 0.80793821,\n",
       "        0.00742638, 0.55159273, 0.93193215, 0.58217546, 0.20609573],\n",
       "       [0.71775756, 0.37898585, 0.66838395, 0.02931972, 0.63590036,\n",
       "        0.03219793, 0.74478066, 0.472913  , 0.12175436, 0.54263593],\n",
       "       [0.06677444, 0.65336487, 0.99608633, 0.76939734, 0.57377411,\n",
       "        0.10263526, 0.69983407, 0.66116787, 0.04909713, 0.7922993 ],\n",
       "       [0.51871659, 0.42586769, 0.78818717, 0.41156922, 0.48102628,\n",
       "        0.18162884, 0.3213189 , 0.845533  , 0.18690375, 0.41729106],\n",
       "       [0.98903451, 0.23659981, 0.91683233, 0.91839747, 0.09129634,\n",
       "        0.46365272, 0.50221634, 0.31366895, 0.04733954, 0.24168564],\n",
       "       [0.09552964, 0.23824991, 0.80779109, 0.89497829, 0.04322289,\n",
       "        0.30194684, 0.9805822 , 0.53950482, 0.62630936, 0.00554541],\n",
       "       [0.48490944, 0.98832853, 0.37518553, 0.09703816, 0.46190876,\n",
       "        0.96300447, 0.34183061, 0.79892273, 0.79884633, 0.2082483 ]])"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr = np.random.rand(10,10)\n",
    "arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.46798757 0.08490416 0.85938908]\n"
     ]
    }
   ],
   "source": [
    "# select arr[3,3], arr[1,2], arr[2,1]\n",
    "print(arr[[3,1,2], [3,2,1]])       "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "index 6 is out of bounds for axis 1 with size 5",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[40], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m# select rows 3,1,2 and columns 6,4,8 \u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[43marr\u001b[49m\u001b[43m[\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;241;43m3\u001b[39;49m\u001b[43m,\u001b[49m\u001b[38;5;241;43m1\u001b[39;49m\u001b[43m,\u001b[49m\u001b[38;5;241;43m2\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m]\u001b[49m\u001b[43m[\u001b[49m\u001b[43m:\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;241;43m6\u001b[39;49m\u001b[43m,\u001b[49m\u001b[38;5;241;43m4\u001b[39;49m\u001b[43m,\u001b[49m\u001b[38;5;241;43m8\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m]\u001b[49m)\n",
      "\u001b[1;31mIndexError\u001b[0m: index 6 is out of bounds for axis 1 with size 5"
     ]
    }
   ],
   "source": [
    "# select rows 3,1,2 and columns 6,4,8 \n",
    "print(arr[[3,1,2]][:, [6,4,8]])    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### dimension inference"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(4, 4)\n"
     ]
    }
   ],
   "source": [
    "# dimension inference using any negative number (usually -1)\n",
    "arr = np.array(range(16)).reshape((4,-1))\n",
    "print(arr.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### find elements/indices by conditions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [],
   "source": [
    "arr = np.arange(16).reshape(4,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 6  7  8  9 10 11 12 13 14 15]\n"
     ]
    }
   ],
   "source": [
    "# find the elements greater than 5 and return a flattened array\n",
    "print(arr[arr>5])    # or arr[np.where(arr>5)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[10 10 10 10]\n",
      " [10 10 -1 -1]\n",
      " [-1 -1 -1 -1]\n",
      " [-1 -1 -1 -1]]\n"
     ]
    }
   ],
   "source": [
    "# return values based on conditions \n",
    "# np.where(condition, true_return, false_return)\n",
    "print(np.where(arr>5, -1, 10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2]\n",
      " [1 3]\n",
      " [2 0]\n",
      " [2 1]\n",
      " [2 2]\n",
      " [2 3]\n",
      " [3 0]\n",
      " [3 1]\n",
      " [3 2]\n",
      " [3 3]]\n"
     ]
    }
   ],
   "source": [
    "# find the indices of the elements on conditions\n",
    "print(np.argwhere(arr>5))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 6. Sort an Array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [],
   "source": [
    "arr = np.random.rand(5,5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### sort an array along a specified axis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.11702945 0.17913374 0.06753657 0.02945699 0.05396756]\n",
      " [0.13630925 0.18249983 0.41165849 0.12910116 0.31981183]\n",
      " [0.36056504 0.51866089 0.42053876 0.56232065 0.37163583]\n",
      " [0.44498496 0.62847058 0.42945962 0.70682921 0.43148605]\n",
      " [0.7740198  0.74238635 0.55147061 0.86890785 0.75572196]]\n"
     ]
    }
   ],
   "source": [
    "# sort along the row and return a copy\n",
    "print(np.sort(arr, axis=0))   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.11702945 0.17913374 0.06753657 0.02945699 0.05396756]\n",
      " [0.13630925 0.18249983 0.41165849 0.12910116 0.31981183]\n",
      " [0.36056504 0.51866089 0.42053876 0.56232065 0.37163583]\n",
      " [0.44498496 0.62847058 0.42945962 0.70682921 0.43148605]\n",
      " [0.7740198  0.74238635 0.55147061 0.86890785 0.75572196]]\n"
     ]
    }
   ],
   "source": [
    "# sort along the row in place\n",
    "arr.sort(axis=0)\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.02945699 0.05396756 0.06753657 0.11702945 0.17913374]\n",
      " [0.12910116 0.13630925 0.18249983 0.31981183 0.41165849]\n",
      " [0.36056504 0.37163583 0.42053876 0.51866089 0.56232065]\n",
      " [0.42945962 0.43148605 0.44498496 0.62847058 0.70682921]\n",
      " [0.55147061 0.74238635 0.75572196 0.7740198  0.86890785]]\n"
     ]
    }
   ],
   "source": [
    "# sort along the column and return a copy\n",
    "print(np.sort(arr, axis=1))    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.02945699 0.05396756 0.06753657 0.11702945 0.17913374]\n",
      " [0.12910116 0.13630925 0.18249983 0.31981183 0.41165849]\n",
      " [0.36056504 0.37163583 0.42053876 0.51866089 0.56232065]\n",
      " [0.42945962 0.43148605 0.44498496 0.62847058 0.70682921]\n",
      " [0.55147061 0.74238635 0.75572196 0.7740198  0.86890785]]\n"
     ]
    }
   ],
   "source": [
    "# sort along the column in place\n",
    "arr.sort(axis=1)    \n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### compute the indices that would sort an array along a specified axis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [],
   "source": [
    "arr = np.random.rand(5,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 0 0 4 3]\n",
      " [3 2 2 1 0]\n",
      " [4 4 3 0 1]\n",
      " [2 1 1 2 4]\n",
      " [0 3 4 3 2]]\n"
     ]
    }
   ],
   "source": [
    "# along the row\n",
    "print(np.argsort(arr, axis=0))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 4 3 0]\n",
      " [0 3 1 4 2]\n",
      " [1 2 0 3 4]\n",
      " [0 4 2 1 3]\n",
      " [3 0 1 4 2]]\n"
     ]
    }
   ],
   "source": [
    "# along the column\n",
    "print(np.argsort(arr, axis=1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 5 23  1 15  2 20 19 11  8 12 17  4  3 21  6  9 24 10 16 13 14  7 22 18\n",
      "  0]\n"
     ]
    }
   ],
   "source": [
    "# if axis=None, return the indices of a flattened array\n",
    "print(np.argsort(arr, axis=None))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [],
   "source": [
    "arr = np.random.rand(3,4)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 7. Manipulate an Array"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### transpose an array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.80614361 0.61240133 0.73322903]\n",
      " [0.86728799 0.65205696 0.13585084]\n",
      " [0.08910079 0.05760322 0.56708195]\n",
      " [0.67553447 0.38582245 0.02315444]]\n",
      "[[0.80614361 0.61240133 0.73322903]\n",
      " [0.86728799 0.65205696 0.13585084]\n",
      " [0.08910079 0.05760322 0.56708195]\n",
      " [0.67553447 0.38582245 0.02315444]]\n",
      "[[0.80614361 0.61240133 0.73322903]\n",
      " [0.86728799 0.65205696 0.13585084]\n",
      " [0.08910079 0.05760322 0.56708195]\n",
      " [0.67553447 0.38582245 0.02315444]]\n"
     ]
    }
   ],
   "source": [
    "# the following methods return a copy\n",
    "print(arr.T)\n",
    "# or \n",
    "print(np.transpose(arr))\n",
    "# or\n",
    "print(arr.transpose())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### transpose of a high dimensional array with specified order of axes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[ 0  1  2  3]\n",
      "  [ 4  5  6  7]]\n",
      "\n",
      " [[ 8  9 10 11]\n",
      "  [12 13 14 15]]]\n",
      "[[[ 0  1  2  3]\n",
      "  [ 4  5  6  7]]\n",
      "\n",
      " [[ 8  9 10 11]\n",
      "  [12 13 14 15]]]\n"
     ]
    }
   ],
   "source": [
    "arr1 = np.arange(16).reshape((2,2,4))\n",
    "print(arr1)\n",
    "\n",
    "arr1.transpose((1,0,2))\n",
    "print(arr1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### swap axes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[ 0  4]\n",
      "  [ 1  5]\n",
      "  [ 2  6]\n",
      "  [ 3  7]]\n",
      "\n",
      " [[ 8 12]\n",
      "  [ 9 13]\n",
      "  [10 14]\n",
      "  [11 15]]]\n"
     ]
    }
   ],
   "source": [
    "arr1 = np.arange(16).reshape((2,2,4))\n",
    "print(arr1.swapaxes(1,2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### change the shape of an array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.80614361, 0.86728799, 0.08910079, 0.67553447, 0.61240133,\n",
       "        0.65205696],\n",
       "       [0.05760322, 0.38582245, 0.73322903, 0.13585084, 0.56708195,\n",
       "        0.02315444]])"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# change the shape of an array and return a copy\n",
    "arr.reshape((2,6))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [],
   "source": [
    "# change the shape of an array in place\n",
    "arr.resize((2,6))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### flatten an array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.80614361, 0.86728799, 0.08910079, 0.67553447, 0.61240133,\n",
       "       0.65205696, 0.05760322, 0.38582245, 0.73322903, 0.13585084,\n",
       "       0.56708195, 0.02315444])"
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# return a copy\n",
    "arr.flatten()    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.80614361, 0.86728799, 0.08910079, 0.67553447, 0.61240133,\n",
       "       0.65205696, 0.05760322, 0.38582245, 0.73322903, 0.13585084,\n",
       "       0.56708195, 0.02315444])"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# return a view\n",
    "# change any element in the view will change the initial array\n",
    "arr.ravel()      "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### append elements to an array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [],
   "source": [
    "arr = np.array([1,2,3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4]\n"
     ]
    }
   ],
   "source": [
    "# append a scalar and return a copy\n",
    "arr1 = np.append(arr, 4)    \n",
    "print(arr1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5 6]\n"
     ]
    }
   ],
   "source": [
    "# append an array and return a copy\n",
    "arr2 = np.append(arr, [4,5,6])    \n",
    "print(arr2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### insert elements into an array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[100   1   2   3]\n"
     ]
    }
   ],
   "source": [
    "# np.insert(array, position, element)\n",
    "\n",
    "# insert a scalar at a certain position\n",
    "arr3 = np.insert(arr, 0, 100)    \n",
    "print(arr3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 1 2 3]\n"
     ]
    }
   ],
   "source": [
    "# insert multiple values at a certain position\n",
    "arr3 = np.insert(arr, 0, [1,2,3])    \n",
    "print(arr3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### delete elements from an array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2 3]\n"
     ]
    }
   ],
   "source": [
    "# remove the element at position 0\n",
    "arr4 = np.delete(arr, 0)    \n",
    "print(arr4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2]\n"
     ]
    }
   ],
   "source": [
    "# remove the element at multiple positions\n",
    "arr4 = np.delete(arr, [0,2])    \n",
    "print(arr4)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### copy an array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [],
   "source": [
    "arr = np.array([1,2,3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [],
   "source": [
    "# the following methods are all deep copy\n",
    "arr1 = np.copy(arr)\n",
    "# or \n",
    "arr1 = arr.copy()\n",
    "# or \n",
    "arr1 = np.array(arr, copy=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 8. Combine & Split an Array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [],
   "source": [
    "arr1 = np.array([[1,2,3,4], [1,2,3,4]])\n",
    "arr2 = np.array([[5,6,7,8], [5,6,7,8]])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### ```np.concatenate((a, b), axis=0)```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3 4]\n",
      " [1 2 3 4]\n",
      " [5 6 7 8]\n",
      " [5 6 7 8]]\n"
     ]
    }
   ],
   "source": [
    "# concat along the row\n",
    "cat = np.concatenate((arr1, arr2), axis=0)        \n",
    "print(cat)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3 4 5 6 7 8]\n",
      " [1 2 3 4 5 6 7 8]]\n"
     ]
    }
   ],
   "source": [
    "# concat along the column\n",
    "cat = np.concatenate((arr1, arr2), axis=1)    \n",
    "print(cat)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### ```np.vstack((a, b))``` \n",
    "### ```np.r_[a, b]```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3 4]\n",
      " [1 2 3 4]\n",
      " [5 6 7 8]\n",
      " [5 6 7 8]]\n"
     ]
    }
   ],
   "source": [
    "# stack arrays vertically\n",
    "cat = np.vstack((arr1, arr2))\n",
    "print(cat)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3 4]\n",
      " [1 2 3 4]\n",
      " [5 6 7 8]\n",
      " [5 6 7 8]]\n"
     ]
    }
   ],
   "source": [
    "# stack arrays vertically\n",
    "cat = np.r_[arr1, arr2]\n",
    "print(cat)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### ```np.hstack((a, b))```\n",
    "### ```np.c_[a, b]```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3 4 5 6 7 8]\n",
      " [1 2 3 4 5 6 7 8]]\n"
     ]
    }
   ],
   "source": [
    "# stack arrays horizontally\n",
    "cat = np.hstack((arr1, arr2))\n",
    "print(cat)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3 4 5 6 7 8]\n",
      " [1 2 3 4 5 6 7 8]]\n"
     ]
    }
   ],
   "source": [
    "# stack arrays horizontally\n",
    "cat = np.c_[arr1, arr2]\n",
    "print(cat)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### split an array "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "metadata": {},
   "outputs": [],
   "source": [
    "arr = np.random.rand(6,6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[array([[0.0174567 , 0.47275939, 0.84410265, 0.88709809, 0.30063103,\n",
      "        0.938766  ],\n",
      "       [0.58832418, 0.09871477, 0.09634253, 0.56561105, 0.75673868,\n",
      "        0.13910753],\n",
      "       [0.37247418, 0.98843246, 0.90281137, 0.35097407, 0.48843214,\n",
      "        0.60597433]]), array([[0.00713459, 0.06267544, 0.65672272, 0.15912001, 0.91006063,\n",
      "        0.3950984 ],\n",
      "       [0.46940726, 0.60966449, 0.82131635, 0.48112601, 0.24688737,\n",
      "        0.40234706],\n",
      "       [0.20452672, 0.77063506, 0.11895435, 0.98447605, 0.25656521,\n",
      "        0.39604327]])]\n"
     ]
    }
   ],
   "source": [
    "# split the array vertically into n evenly spaced chunks\n",
    "arr1 = np.vsplit(arr, 2)\n",
    "print(arr1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[array([[0.0174567 , 0.47275939, 0.84410265],\n",
      "       [0.58832418, 0.09871477, 0.09634253],\n",
      "       [0.37247418, 0.98843246, 0.90281137],\n",
      "       [0.00713459, 0.06267544, 0.65672272],\n",
      "       [0.46940726, 0.60966449, 0.82131635],\n",
      "       [0.20452672, 0.77063506, 0.11895435]]), array([[0.88709809, 0.30063103, 0.938766  ],\n",
      "       [0.56561105, 0.75673868, 0.13910753],\n",
      "       [0.35097407, 0.48843214, 0.60597433],\n",
      "       [0.15912001, 0.91006063, 0.3950984 ],\n",
      "       [0.48112601, 0.24688737, 0.40234706],\n",
      "       [0.98447605, 0.25656521, 0.39604327]])]\n"
     ]
    }
   ],
   "source": [
    "# split the array horizontally into n evenly spaced chunks\n",
    "arr2 = np.hsplit(arr, 2)\n",
    "print(arr2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 9. Set Operations"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### select the unique elements from an array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5 6]\n"
     ]
    }
   ],
   "source": [
    "arr = np.array([1,1,2,2,3,3,4,5,6])\n",
    "print(np.unique(arr))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5 6]\n",
      "[2 2 2 1 1 1]\n"
     ]
    }
   ],
   "source": [
    "# return the number of times each unique item appears\n",
    "arr = np.array([1,1,2,2,3,3,4,5,6])\n",
    "uniques, counts = np.unique(arr, return_counts=True)\n",
    "print(uniques)\n",
    "print(counts)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### compute the intersection & union of two arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "metadata": {},
   "outputs": [],
   "source": [
    "arr1 = np.array([1,2,3,4,5])\n",
    "arr2 = np.array([3,4,5,6,7])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3 4 5]\n"
     ]
    }
   ],
   "source": [
    "# intersection\n",
    "print(np.intersect1d(arr1, arr2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5 6 7]\n"
     ]
    }
   ],
   "source": [
    "# union\n",
    "print(np.union1d(arr1, arr2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### compute whether each element of an array is contained in another"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[False False  True  True  True]\n"
     ]
    }
   ],
   "source": [
    "print(np.in1d(arr1, arr2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[False False  True  True  True]\n"
     ]
    }
   ],
   "source": [
    "# preserve the shape of the array in the output, if the array is of higher dimensions\n",
    "print(np.isin(arr1, arr2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### compute the elements in an array that are not in another"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2]\n"
     ]
    }
   ],
   "source": [
    "print(np.setdiff1d(arr1, arr2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### compute the elements in either of two arrays, but not both"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 6 7]\n"
     ]
    }
   ],
   "source": [
    "print(np.setxor1d(arr1, arr2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 10. Linear Algebra"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "metadata": {},
   "outputs": [],
   "source": [
    "arr1 = np.random.rand(5,5)\n",
    "arr2 = np.random.rand(5,5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### matrix multiplication"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2.51623511 2.86218675 2.46149074 2.04223873 1.68511463]\n",
      " [0.97887139 1.12545821 1.08799709 0.91490076 0.71161775]\n",
      " [1.76553731 2.31931894 1.70683443 1.69936475 1.24178866]\n",
      " [1.16873119 1.51462574 1.20311322 1.18600669 0.82424827]\n",
      " [1.15498347 1.31753805 1.11707168 0.8826558  0.70418125]]\n",
      "[[2.51623511 2.86218675 2.46149074 2.04223873 1.68511463]\n",
      " [0.97887139 1.12545821 1.08799709 0.91490076 0.71161775]\n",
      " [1.76553731 2.31931894 1.70683443 1.69936475 1.24178866]\n",
      " [1.16873119 1.51462574 1.20311322 1.18600669 0.82424827]\n",
      " [1.15498347 1.31753805 1.11707168 0.8826558  0.70418125]]\n",
      "[[2.51623511 2.86218675 2.46149074 2.04223873 1.68511463]\n",
      " [0.97887139 1.12545821 1.08799709 0.91490076 0.71161775]\n",
      " [1.76553731 2.31931894 1.70683443 1.69936475 1.24178866]\n",
      " [1.16873119 1.51462574 1.20311322 1.18600669 0.82424827]\n",
      " [1.15498347 1.31753805 1.11707168 0.8826558  0.70418125]]\n"
     ]
    }
   ],
   "source": [
    "print(arr1.dot(arr2))\n",
    "# or\n",
    "print(np.dot(arr1, arr2))\n",
    "# or\n",
    "print(arr1 @ arr2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### QR factorization "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[-0.4432654   0.32513554  0.61941338 -0.50166373  0.24992646]\n",
      " [-0.53313979 -0.84083639  0.01631061 -0.07809998 -0.04889265]\n",
      " [-0.497832    0.2725315   0.2186724   0.71963447 -0.33496042]\n",
      " [-0.00757871  0.09648464 -0.05319421 -0.440347   -0.89100964]\n",
      " [-0.52094492  0.32202228 -0.75194002 -0.17451256  0.17043949]]\n",
      "[[-1.71197975 -1.721771   -0.91763767 -1.14596917 -1.48828016]\n",
      " [ 0.          0.18511396  0.15670431 -0.3105988  -0.02561779]\n",
      " [ 0.          0.         -0.56886488  0.09863229 -0.28981768]\n",
      " [ 0.          0.          0.         -0.31671114 -0.28469988]\n",
      " [ 0.          0.          0.          0.         -0.67088305]]\n"
     ]
    }
   ],
   "source": [
    "arr = np.random.rand(5,5)\n",
    "\n",
    "q, r = np.linalg.qr(arr)\n",
    "print(q)\n",
    "print(r)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### singular value decomposition (SVD)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[-0.31707494  0.50745837  0.27489595 -0.52708908 -0.53717669]\n",
      " [-0.467027   -0.43107604  0.5391023  -0.31541122  0.4538102 ]\n",
      " [-0.53255432  0.56212351 -0.33998784  0.16799359  0.50654662]\n",
      " [-0.34108705  0.00379167  0.4323183   0.76786776 -0.32729992]\n",
      " [-0.53046657 -0.49057337 -0.57559542 -0.06964278 -0.37654055]]\n",
      "[2.83737775 0.69055824 0.47487856 0.23943839 0.10871122]\n",
      "[[-0.42059018 -0.38307359 -0.21951733 -0.6476369  -0.45687757]\n",
      " [-0.63976954  0.71850762 -0.25227551  0.00271298  0.10388191]\n",
      " [ 0.20378291  0.23608185 -0.1886435   0.38886392 -0.84613023]\n",
      " [-0.40137463 -0.52295215 -0.41054126  0.61598638  0.13204589]\n",
      " [ 0.45953212  0.08824872 -0.82706633 -0.22339365  0.21702294]]\n"
     ]
    }
   ],
   "source": [
    "arr = np.random.rand(5,5)\n",
    "\n",
    "u, s, v = np.linalg.svd(arr)\n",
    "print(u)\n",
    "print(s)\n",
    "print(v)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### compute eigen values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 2.85678022 -0.67311818  0.37430308  0.1524331  -0.07643027]\n"
     ]
    }
   ],
   "source": [
    "arr = np.random.rand(5,5)\n",
    "print(np.linalg.eigvals(arr))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### eigen value decomposition"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 2.76395772+0.j          0.10174612+0.23654886j  0.10174612-0.23654886j\n",
      " -0.52935513+0.05320233j -0.52935513-0.05320233j]\n",
      "[[ 0.27758037+0.j         -0.55997738+0.j         -0.55997738-0.j\n",
      "   0.22379469-0.00692696j  0.22379469+0.00692696j]\n",
      " [ 0.45939229+0.j          0.17076292+0.34885444j  0.17076292-0.34885444j\n",
      "  -0.70496349+0.j         -0.70496349-0.j        ]\n",
      " [ 0.48172485+0.j          0.21554976-0.3991528j   0.21554976+0.3991528j\n",
      "   0.0228234 -0.0005529j   0.0228234 +0.0005529j ]\n",
      " [ 0.48237473+0.j          0.37310246-0.2373618j   0.37310246+0.2373618j\n",
      "   0.12243854-0.18721414j  0.12243854+0.18721414j]\n",
      " [ 0.49715556+0.j         -0.28133211+0.23470715j -0.28133211-0.23470715j\n",
      "   0.60718075+0.18347867j  0.60718075-0.18347867j]]\n"
     ]
    }
   ],
   "source": [
    "arr = np.random.rand(5,5)\n",
    "\n",
    "w, v = np.linalg.eig(arr)\n",
    "print(w)    # eigen values\n",
    "print(v)    # eigen vectors"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### compute the trace & determinant"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.9087397083691204\n"
     ]
    }
   ],
   "source": [
    "# notice this is not a function in linalg!!!\n",
    "print(np.trace(arr))    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.05187451362412388\n"
     ]
    }
   ],
   "source": [
    "print(np.linalg.det(arr))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### calculate the inverse/psedo-inverse of a matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "metadata": {},
   "outputs": [],
   "source": [
    "arr = np.random.rand(5,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[  2.37704915  -2.18278595  14.14976233 -17.3879446   -4.13238747]\n",
      " [ -2.65572368   2.85561316   6.39432678 -11.58940717   1.15627517]\n",
      " [ -0.64187733   2.8106897   11.3550277  -20.17896096  -0.58449384]\n",
      " [  4.52924162  -5.63978854  -0.64934041   4.47682269  -1.75308404]\n",
      " [ -2.16914098   1.49607223 -25.1450202   37.98516176   4.2574866 ]]\n"
     ]
    }
   ],
   "source": [
    "# compute the inverse of a matrix\n",
    "print(np.linalg.inv(arr))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[  2.37704915  -2.18278595  14.14976233 -17.3879446   -4.13238747]\n",
      " [ -2.65572368   2.85561316   6.39432678 -11.58940717   1.15627517]\n",
      " [ -0.64187733   2.8106897   11.3550277  -20.17896096  -0.58449384]\n",
      " [  4.52924162  -5.63978854  -0.64934041   4.47682269  -1.75308404]\n",
      " [ -2.16914098   1.49607223 -25.1450202   37.98516176   4.2574866 ]]\n"
     ]
    }
   ],
   "source": [
    "# compute the psudo-inverse of a matrix\n",
    "print(np.linalg.pinv(arr))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### solve a linear system"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-49.75295153 -18.33776982 -44.59372785   0.44351389  98.61602289]\n"
     ]
    }
   ],
   "source": [
    "# solve a linear system in closed form\n",
    "y = [1,2,3,4,5]\n",
    "print(np.linalg.solve(arr, y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-49.75295153 -18.33776982 -44.59372785   0.44351389  98.61602289]\n",
      "[]\n",
      "5\n",
      "[2.21809418 0.85765544 0.52823685 0.09333081 0.0173482 ]\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\ewang\\AppData\\Local\\Continuum\\miniconda3\\lib\\site-packages\\ipykernel_launcher.py:3: FutureWarning: `rcond` parameter will change to the default of machine precision times ``max(M, N)`` where M and N are the input matrix dimensions.\n",
      "To use the future default and silence this warning we advise to pass `rcond=None`, to keep using the old, explicitly pass `rcond=-1`.\n",
      "  This is separate from the ipykernel package so we can avoid doing imports until\n"
     ]
    }
   ],
   "source": [
    "# calculate the least-squares solution of a linear system\n",
    "y = [1,2,3,4,5]\n",
    "solution, residuals, rank, singular = np.linalg.lstsq(arr, y)\n",
    "print(solution)\n",
    "print(residuals)\n",
    "print(rank)\n",
    "print(singular)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
 "nbformat_minor": 2
}
