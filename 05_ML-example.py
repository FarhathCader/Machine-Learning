{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Importing Libraries needed for Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
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
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "2            3         1       3   \n",
       "3            4         1       1   \n",
       "4            5         0       3   \n",
       "\n",
       "                                                Name     Sex   Age  SibSp  \\\n",
       "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
       "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
       "4                           Allen, Mr. William Henry    male  35.0      0   \n",
       "\n",
       "   Parch            Ticket     Fare Cabin Embarked  \n",
       "0      0         A/5 21171   7.2500   NaN        S  \n",
       "1      0          PC 17599  71.2833   C85        C  \n",
       "2      0  STON/O2. 3101282   7.9250   NaN        S  \n",
       "3      0            113803  53.1000  C123        S  \n",
       "4      0            373450   8.0500   NaN        S  "
      ]
     },
     "execution_count": 165,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np \n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "#from sklearn.model_selection import train_test_split\n",
    "%matplotlib inline\n",
    "\n",
    "\n",
    "train=pd.read_csv(r'data/train-titanic.csv')\n",
    "df=train.copy()\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
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
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>887</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>Montvila, Rev. Juozas</td>\n",
       "      <td>male</td>\n",
       "      <td>27.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>211536</td>\n",
       "      <td>13.00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>888</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Graham, Miss. Margaret Edith</td>\n",
       "      <td>female</td>\n",
       "      <td>19.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>112053</td>\n",
       "      <td>30.00</td>\n",
       "      <td>B42</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>889</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Johnston, Miss. Catherine Helen \"Carrie\"</td>\n",
       "      <td>female</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>W./C. 6607</td>\n",
       "      <td>23.45</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>890</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Behr, Mr. Karl Howell</td>\n",
       "      <td>male</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>111369</td>\n",
       "      <td>30.00</td>\n",
       "      <td>C148</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>891</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Dooley, Mr. Patrick</td>\n",
       "      <td>male</td>\n",
       "      <td>32.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>370376</td>\n",
       "      <td>7.75</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Q</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     PassengerId  Survived  Pclass                                      Name  \\\n",
       "886          887         0       2                     Montvila, Rev. Juozas   \n",
       "887          888         1       1              Graham, Miss. Margaret Edith   \n",
       "888          889         0       3  Johnston, Miss. Catherine Helen \"Carrie\"   \n",
       "889          890         1       1                     Behr, Mr. Karl Howell   \n",
       "890          891         0       3                       Dooley, Mr. Patrick   \n",
       "\n",
       "        Sex   Age  SibSp  Parch      Ticket   Fare Cabin Embarked  \n",
       "886    male  27.0      0      0      211536  13.00   NaN        S  \n",
       "887  female  19.0      0      0      112053  30.00   B42        S  \n",
       "888  female   NaN      1      2  W./C. 6607  23.45   NaN        S  \n",
       "889    male  26.0      0      0      111369  30.00  C148        C  \n",
       "890    male  32.0      0      0      370376   7.75   NaN        Q  "
      ]
     },
     "execution_count": 166,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
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
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>714.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>446.000000</td>\n",
       "      <td>0.383838</td>\n",
       "      <td>2.308642</td>\n",
       "      <td>29.699118</td>\n",
       "      <td>0.523008</td>\n",
       "      <td>0.381594</td>\n",
       "      <td>32.204208</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>257.353842</td>\n",
       "      <td>0.486592</td>\n",
       "      <td>0.836071</td>\n",
       "      <td>14.526497</td>\n",
       "      <td>1.102743</td>\n",
       "      <td>0.806057</td>\n",
       "      <td>49.693429</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.420000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>223.500000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>20.125000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>7.910400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>446.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>28.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>14.454200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>668.500000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>38.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>31.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>891.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>512.329200</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       PassengerId    Survived      Pclass         Age       SibSp  \\\n",
       "count   891.000000  891.000000  891.000000  714.000000  891.000000   \n",
       "mean    446.000000    0.383838    2.308642   29.699118    0.523008   \n",
       "std     257.353842    0.486592    0.836071   14.526497    1.102743   \n",
       "min       1.000000    0.000000    1.000000    0.420000    0.000000   \n",
       "25%     223.500000    0.000000    2.000000   20.125000    0.000000   \n",
       "50%     446.000000    0.000000    3.000000   28.000000    0.000000   \n",
       "75%     668.500000    1.000000    3.000000   38.000000    1.000000   \n",
       "max     891.000000    1.000000    3.000000   80.000000    8.000000   \n",
       "\n",
       "            Parch        Fare  \n",
       "count  891.000000  891.000000  \n",
       "mean     0.381594   32.204208  \n",
       "std      0.806057   49.693429  \n",
       "min      0.000000    0.000000  \n",
       "25%      0.000000    7.910400  \n",
       "50%      0.000000   14.454200  \n",
       "75%      0.000000   31.000000  \n",
       "max      6.000000  512.329200  "
      ]
     },
     "execution_count": 167,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(891, 12)"
      ]
     },
     "execution_count": 168,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',\n",
       "       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 169,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3    491\n",
       "1    216\n",
       "2    184\n",
       "Name: Pclass, dtype: int64"
      ]
     },
     "execution_count": 170,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Pclass'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PassengerId      0\n",
       "Survived         0\n",
       "Pclass           0\n",
       "Name             0\n",
       "Sex              0\n",
       "Age            177\n",
       "SibSp            0\n",
       "Parch            0\n",
       "Ticket           0\n",
       "Fare             0\n",
       "Cabin          687\n",
       "Embarked         2\n",
       "dtype: int64"
      ]
     },
     "execution_count": 171,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "177"
      ]
     },
     "execution_count": 172,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Age'].isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Pclass', ylabel='count'>"
      ]
     },
     "execution_count": 173,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x=\"Pclass\",data=df)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Seabon library Reference\n",
    "\n",
    "Please studty different plot types in seabon library"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Pclass', ylabel='count'>"
      ]
     },
     "execution_count": 174,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYcAAAEJCAYAAAB/pOvWAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAbDUlEQVR4nO3dfXRU9b3v8XcgYaAqgqUqilWpzRc0VtooD4UiAse7qIhFRT1YKxzBslpdnOVDT1kHK7Dskw9g9ajcIhErtkqFyCqopwJesSg+RB5Mjd/meoA2ElfFXrUGSUKS+8dMcMIOyQRmz55JPq+1XM785rf3fIeB+cz+/fb+TV5TUxMiIiLJukVdgIiIZB+Fg4iIBCgcREQkQOEgIiIBCgcREQnIj7qAI1VWVhYDzgOqgYaIyxERyRXdgf7A68XFxbUHP5jz4UA8GF6KuggRkRz1LeBPBzd2hnCoBigsLKRHjx5R1yIikhPq6ur4y1/+AonP0IN1hnBoAOjRowexWCzqWkREck2rw/GakBYRkQCFg4iIBIQ6rGRmC4DLgSZgqbsvNLNHgFFATaLbfHcvNbMhwMNAb2AjMMvd9x/J8zc2NlJVVUVNTU37nbuYo446igEDBtCtm74fiEhQaOFgZucDY4GvAQXA22a2FjgXGO3uB0+CLAdmuPtmM1sKzAQeOpIa9uzZQ15eHmamD8EkjY2NvPfee+zZs4fjjz8+6nJEJAuF9onp7i8CFyS+/R9PPIg+A74MlJjZdjObb2bdzOxUoJe7b05svgyYcqQ1fPTRR5xwwgkKhoN069aNE044gY8//jjqUkQkS4U6rOTu9WY2H7gF+D3xI4gNwA+Aj4E1wHVAOS1Pp6oGBnTkucrLywNt3bt3p66ujvr6+sOqvzNramqipqaGsrKyqEsRkSwU+qms7n67mf0S+AMwzt0nNz9mZvcD3wPeJj4v0SwPaOzI8xQVFQVOZa2oqODoo48+3NI7vVgsxuDBg6MuQ0QiUFtb2+qX6mahjbeY2aDEJDPuvhdYBVxpZpcldcsD6oEq4pdxNzsR2B1WbWHYunUr11xzDRdffDETJ05kxowZVFZWRl2WSNZorA+s0JD1crHmdAnzyGEgMN/MRhE/KrgEeBG418w2AJ8C1wOPuvsuM9tnZiPdfRNwDfBsiLWlVV1dHd///vcpKSnhrLPOAmD16tXMnDmT9evX071794grFIlet4IYO6efHnUZHXLaIzuiLiEyYU5IPwOsBbYAZcDL7r4A+DmwifhQ0lZ3/11ik6uBRWb2DnA0cF9YtaXbZ599xj//+U/27t17oG3SpEncdtttNDQ0sGHDBqZMmcJ3vvMdrrrqKrZs2QLAnDlzmD17NgCVlZWMGDGCd999N5LXICKSLOwJ6XnAvIPaHgQebKXvNmBomPWE5dhjj+XWW29lxowZ9OvXj2984xsMGzaMiy66iN27d7No0SJ+85vf0LdvXyorK5k+fTp//OMfue2225g8eTKlpaUsXbqUOXPm8JWvfCXqlyMi0inWVsoK06dPZ8qUKbz++uu8/vrrLFmyhCVLljB16lT+/ve/M23atAN98/Ly+Otf/8qgQYNYtGgRV1xxBZMmTWLSpEnRvQARkSQKhzQoKytjy5YtzJgxgwsuuIALLriAm266iYkTJ/Lpp58yYsQI7r333gP9q6urD1x8tmPHDvr06UNFRQV1dXVaWVZEsoKuDkuD4447joceeog33njjQNsHH3zAp59+yrhx49i0adOBuYQXX3yRSZMmsW/fPqqqqvjpT39KSUkJAwcO5O67747qJYiItKAjhzQ4/fTTeeCBB1i0aBHvv/8+sViMY445hp/97GcMGjSIBQsWcNNNN9HU1ER+fj4PPfQQsViMm2++meuuu47CwkJ+8pOfcPHFF/PNb36TMWPGRP2SRKSLUzikyfDhwxk+fHirj02YMIEJEyYE2p988skDt4899lg2btwYWn0iIh2hYSUREQlQOIiISIDCQUREAhQOIiISoHAQEZEAhYOIiAQoHEREJKBLhUNYa7NnYs33sWPHUlVVFfrziIhAF7sILqz15Lvymu8i0jl1qXCI2quvvsrixYspKCigqqqKsWPH8oUvfIF169YB8Otf/5rnnnuO1atX89lnn1FQUMA999zDwIEDD+yjoaGBO++8k9dee42GhgYuvfTSFiu+ioikQ5caVsoG27ZtY/78+axcuZLHH3+c4447jlWrVmFmrF27lnXr1vHYY4+xZs0axowZw+OPP95i+xUrVgBQWlrKU089xfr161ss+Ccikg46csiwwsJC+veP/1x23759GTFiBAAnnXQSn3zyCffccw9r165l586dvPTSSwwePLjF9q+88goVFRVs3rwZgL179+LunHvuuZl9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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x=\"Pclass\", hue=\"Sex\" ,data=df, palette=\"autumn\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Survived', ylabel='count'>"
      ]
     },
     "execution_count": 175,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYcAAAEJCAYAAAB/pOvWAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAZ70lEQVR4nO3de5RdZZnn8W+lKilCmIR0IyEYARHzAJYSKS5yM3RzUSBrRVYbpwFlUAPDgKDjBdrV6QVIy0XWBAW8TSDQmBalhQgNxMugBhEjbQGBkvCISsBIhhFHYYymcqmaP84prGQnlXNSZ9epCt/PWizPec9+934qnnV+593vPu9u6evrQ5KkgcY0uwBJ0shjOEiSCgwHSVKB4SBJKjAcJEkFbc0uYKi6urragUOB1cDGJpcjSaNFKzAV+I/Ozs6ezV8c9eFAJRh+2OwiJGmUOgZ4cPPGHSEcVgNMnz6dcePGNbsWSRoV1q1bx89//nOofoZubkcIh40A48aNo729vdm1SNJos8XT8U5IS5IKDAdJUsGOcFpJkoZNb28vq1atYs2aNc0upSYTJkxg2rRpjBlT31jAcJCkOrz44ou0tLQQEXV/4A633t5efvOb3/Diiy+y++6719V3ZP9lkjTC/OEPf2DKlCkjPhgAxowZw5QpU3jppZfq71tCPZK0w9q4cSNjx45tdhk1Gzt2LBs2bKi7n+EgSXVqaWlpdgk1295anXPQsOnr3UDLmNH1lhuNNas5Vq1axQknnMD06dNfaevr6+PMM8/k3e9+9xb73HnnnXz729/my1/+8nCVWTPf9Ro2LWPa+P3SLzS7jLpMnnles0vQKLLTTjtx1113vfL8hRdeYNasWXR0dLD//vs3sbL6GQ6SVJIpU6aw9957s3LlSpYuXcrixYtpa2tj77335qqrrtpk28cee4xrrrmGdevW8dvf/pYjjzySK664gg0bNnD55ZfzyCOPMHbsWKZNm8aVV15Je3v7FtsnTJjQkNoNB0kqyaOPPspzzz3Hn//8Z+68805uv/12Jk2axJVXXsmiRYuYMmXKK9veeuutXHjhhRx++OGsWbOG4447ju7ubtauXcvDDz/MfffdR0tLC9dccw2ZSW9v7xbbDz744IbUbjhIUoOsXbuW2bNnA5WrmiZPnsw111zDD3/4Q975zncyadIkAD75yU8ClTmHfldddRUPPPAAX/rSl/jVr35FT08Pf/rTn9h///1pbW1lzpw5HH300bzjHe/gLW95Cy+//PIW2xvFcJCkBtl8zqHfQw89tMlVQy+//DIvv/zyJtu8973vJSI45phjOOmkk1i+fDl9fX1MnDiRu+66i0ceeYRly5bxkY98hA9+8IOcccYZW21vBMNBkkp25JFH8pnPfIa5c+eyyy67cP3119PX18eBBx4IVMLiiSeeYMGCBUyaNImf/OQnPPfcc/T29vL973+fhQsXcvPNN3PooYfS19dHd3f3VtsbxXCQpJLNnDmTX/ziF5x22mkA7Lffflx++eV85zvfAWDixImcc845nHrqqey8885MmTKFgw8+mGeffZY5c+bwwAMPMGvWLHbeeWcmTZrE5ZdfztSpU7fY3igtfX19DdtZM3R1de0DPNPR0eH9HEYBL2XVaLdixQoOOOCAZpdRly3V3NPT0z/SeH1nZ+fKzfuUOnKIiE8B7wb6gJsyc35E3AwcDfQvaXhZZi6OiBnAjcBE4AHg3Mys/zffkqQhKy0cImIm8LfAW4CxwJMRcS9wCPD2zNz81nSLgLmZuSwibgLOBr5YVn2SpK0rbW2lzFwK/E312//uVILoz8BewMKIeDwiLouIMRGxNzA+M5dVu98CzCmrNknS4Eo9rZSZ6yPiMuDjwL9RGUF8DzgPeAm4B/gg0M2mN7leDUyr51iNnKVXOTo7O5tdwnbp6upqdgkaQdra2kbNjX76rVu3ru73celXK2XmJRFxNfDvwHGZeWr/axFxPXAm8CSVeYl+LUBvPcdxQlplGa2hpnKsWLGiYUtUDJdx48Zx0EEHbdI2YEJ6i0o7rRQR+1cnmcnMPwF3Av85Iv5uwGYtwHpgFTB1QPsewPNl1SZJGlyZ93PYF1gQEe0RMQ6YDSwFPhsRkyNiLHAOsDgznwXWRsRR1b7vA5aUWJskaRBlTkjfB9wLPAp0AQ9l5qeAK4EfUTmV9Fhm3lbtcgZwbUQ8BewCXFdWbZLUKBt6y7nivp79/vGPf2TWrFmsWrWqYccve0L6UuDSzdq+ABR+CZWZy4HDyqxHkhqtbUwbVy+9uuH7vXjmxTVtt3z5cubNm8fKlSsbenxvEypJo9jtt9/OJZdcwu67797Q/bq2kiSNYp/+9KdL2a8jB0lSgeEgSSowHCRJBc45SNIQbOjdUPOVRfXut21M8z6iDQdJGoKyPsDr3e/3vve9hh7f00qSpALDQZJUYDhIkgoMB0lSgeEgSSowHCRJBV7KKklDsHFjL62tjf+eXet+b7jhBpYsqdz+ZubMmVx00UUNOb7hIElD0No6hh/c81jD93vsrBnb3Oahhx7iwQcfZPHixbS0tDB37ly++93vcsIJJwz5+IaDJI1Sr3nNa/iHf/gHxo0bB8Ab3vAGnn++MXdYNhwkaZR64xvf+MrjlStXsmTJEm677bZBetTOCWlJGuWefvppPvCBD3DRRRexzz77NGSfhoMkjWJdXV2cddZZfOxjH+PUU09t2H5LPa0UEZ8C3g30ATdl5vyIOB6YD4wHvp6Z86rbzgBuBCYCDwDnZmY5d+6WpB3A6tWrOf/887n22ms54ogjGrrv0kYOETET+FvgLcAhwAURcRCwEJgNHAAcGhEnVbssAj6UmdOBFuDssmqTpB3BTTfdRE9PD1dddRWzZ89m9uzZDZtzKG3kkJlLI+JvMnNDRLy2eqxdgacz8xmAiFgEzImIJ4Hxmbms2v0W4DLgi2XVJ0mNsHFjb02XnW7Pfrf1O4d58+Yxb968hh8bSj6tlJnrI+Iy4OPAvwF7AqsHbLIamDZIe826u7uHVqxK19nZ2ewStktXV1ezS9AI0tbWxpo1a5pdRl3WrVtX9/u49EtZM/OSiLga+HdgOpX5h34tQC+V01tbaq9ZR0cH7e3tQ6xWKhqtoaZyrFixggkTJjS7jLqMGzeOgw46aJO2np6eQb9UlznnsH91kpnM/BNwJ3AsMHXAZnsAzwOrttIuSWqCMi9l3RdYEBHtETGOyiT0l4GIiP0iohU4HViSmc8CayPiqGrf9wFLSqxNkjSI0sIhM+8D7gUeBbqAhzLza8BZwB3Ak8BTwDeqXc4Aro2Ip4BdgOvKqk2SNLiyJ6QvBS7drO1+4KAtbLscOKzMeiRJtfEX0pKkAsNBkoagr7echRxq3e/nPvc5Tj75ZE455RRuvvnmhh3fVVklaQhaxrTx+6VfaPh+J888b5vbPPzwwyxbtoy7776bDRs2cPLJJzNz5kz23XffIR/fkYMkjVKHHXYYt956K21tbfzud79j48aN7Lzzzg3Zt+EgSaPY2LFjue666zjllFM44ogjmDJlSkP2azhI0ih34YUX8uMf/5jVq1dz++23N2SfhoMkjVK//OUvWbFiBQDjx4/nxBNPJDMbsm/DQZJGqVWrVjFv3jzWrVvHunXruP/++xu2FphXK0nSEPT1bqjpyqLt2W/LmME/omfOnMnjjz/Ou971LlpbWznxxBM55ZRTGnJ8w0GShmBbH+Bl7/eCCy7gggsuaPjxPa0kSSowHCRJBYaDJNWpr69v2xuNENtbq+EgSXVobW1l/fr1zS6jZuvXr6etrf55EcNBkuqw66678sILL9DbW9edjJuit7eXF154gUmTJtXd16uVJKkOu+22G6tWrWrYj83KNmHCBHbbbbe6+xkOklSHMWPGsNdeezW7jNJ5WkmSVFDqyCEiLgHeU316b2ZeFBE3A0cDa6rtl2Xm4oiYAdwITAQeAM7NzHLuoiFJGlRp4RARxwMnAm8F+oBvRcSpwCHA2zNz9WZdFgFzM3NZRNwEnA18saz6JElbV+bIYTXwscxcBxARK4C9qv8tjIjXAouBy4DXAeMzc1m17y3VdsNBkpqgtHDIzJ/1P46IN1I5vXQMcCxwHvAScA/wQaCbSpj0Ww1MK6s2SdLgSr9aKSLeBNwLfCIr136dOuC164EzgSepnHrq1wLUdRFxd3f30ItVqRq1lPBw6+rqanYJ0rAre0L6KOAO4COZ+bWIeDMwPTPvqG7SAqwHVgFTB3TdA3i+nmN1dHTQ3t7egKqlTY3WUJMG09PTM+iX6tIuZY2I1wHfBE7PzK9Vm1uAz0bE5IgYC5wDLM7MZ4G11TABeB+wpKzaJEmDK3Pk8HFgJ2B+RPS3fQm4EvgRMBa4IzNvq752BrAgIiYCjwDXlVibJGkQZU5Ifxj48FZe/sIWtl8OHFZWPZKk2vkLaUlSgeEgSSowHCRJBYaDJKnAcJAkFRgOkqQCw0GSVGA4SJIKDAdJUoHhIEkqMBwkSQWGgySpwHCQJBXUFA7V+z1v3nZg48uRJI0Egy7ZHRF/VX14X0QcS+VmPVC5F8OdwP7llSZJapZt3c/hNuCE6uPfDWjfAHyjlIokSU03aDhk5jsAImJhZn5geEqSJDVbTXeCy8wPRMTewF/xl1NLZOYjZRUmSWqemsIhIi4DPgH8H6Cv2twH7FtSXZKkJqr1HtJnAvtl5vP17DwiLgHeU316b2ZeFBHHA/OB8cDXM3NeddsZwI3AROAB4NzM3FDP8SRJjVHr7xx+vR3BcDxwIvBWYAbQGRGnAQuB2cABwKERcVK1yyLgQ5k5ncqpq7PrOZ4kqXFqHTncHxGfAe4C/tzfuI05h9XAxzJzHUBErACmA09n5jPVtkXAnIh4EhifmcuqfW8BLgO+WMffIklqkFrD4azq/84Z0DbonENm/qz/cUS8kcrppeuphEa/1cA0YM+ttEuSmqDWq5Vev70HiIg3AfdSmdDeQGX00K8F6KVyeqtvC+016+7u3t4SNUw6OzubXcJ26erqanYJ0rCr9Wqlj26pPTPnb6PfUcAdwEcy82sRMROYOmCTPYDngVVbaa9ZR0cH7e3t9XSRajJaQ00aTE9Pz6BfqmudkH7zgP86gY8CBw3WISJeB3wTOD0zv1Zt/knlpdgvIlqB04ElmfkssLYaJgDvA5bUWJskqcFqPa30/oHPI2JP4KZtdPs4sBMwPyL6275EZf7ijupr9/GXZTjOABZExETgEeC6WmqTJDVerRPSm8jM5yNin21s82Hgw1t5uTDqyMzlwGHbU48kqbG2Z86hBTiEyq+lJUk7oFpHDm8e8LgPeI7K1UeSpB1QXXMO1cX3xmbmL0qtSpLUVLWeVtqPyq+j9wTGRMSLwKzMXFFmcZKk5qj1UtYbgM9k5uTMnAT8M/D58sqSJDVTreEwJTP/pf9JZt4MvKackiRJzVZrOLQNuJ80EbEbmy53IUnagdR6tdL1wLKI+DqVUPh74NrSqpIkNVWtI4f7qITCOOBA4LXA4rKKkiQ1V63hcAvw+cy8GHgv8I9UbtojSdoB1RoOu2XmdQCZuTYzP8umq6hKknYg9UxI79n/JCKmUFlGQ5K0A6p1Qno+8FhEfIvK3MPxuHyGJO2waho5ZOZCKoHwKPBT4B2Z+dUyC5MkNU/NS3Zn5uPA4yXWIkkaIWqdc5AkvYoYDpKkAsNBklRgOEiSCrbrHtK1ioiJwENU7v2wMiJuBo4G1lQ3uSwzF0fEDOBGYCLwAHBuZm4oszZJ0taVFg4RcTiwAJg+oPkQ4O2ZuXqzzRcBczNzWUTcBJwNfLGs2iRJgytz5HA2cD7wFYCI2BnYC1gYEf0L910GvA4Yn5nLqv1uqbYbDpLUJKWFQ2bOBYiI/qY9gO8B5wEvAfcAHwS6gYEjidXAtLLqkiRtW6lzDgNl5q+AU/ufR8T1wJnAk2x646AWoLfe/Xd3dw+1RJWss7Oz2SVsl66urmaXIA27YQuHiHgzMD0z76g2tQDrgVVsusLrHsDz9e6/o6OD9vb2IdcpbW60hpo0mJ6enkG/VA/npawtwGcjYnJEjAXOARZn5rPA2og4qrrd+4Alw1iXJGkzwxYO1bWZrgR+ROVU0mOZeVv15TOAayPiKWAX4LrhqkuSVFT6aaXM3GfA4y8AX9jCNsuBw8quRZJUG38hLUkqMBwkSQWGgySpwHCQRrgNvaNvmbHRWLM2NWy/c5C0fdrGtHH10qubXUZdLp55cbNL0BA5cpAkFRgOkqQCw0GSVGA4SJIKDAdJUoHhIEkqMBwkSQWGg6RXvb5R+KO9smv2R3CSXvVaxrTx+6WFBaNHtMkzzyt1/44cJEkFhoMkqcBwkCQVGA6SpALDQZJUUOrVShExEXgImJWZKyPieGA+MB74embOq243A7gRmAg8AJybmaPv2jJJ2kGUNnKIiMOBB4Hp1efjgYXAbOAA4NCIOKm6+SLgQ5k5HWgBzi6rLknStpV5Wuls4Hzg+erzw4CnM/OZ6qhgETAnIvYGxmfmsup2twBzSqxLkrQNpZ1Wysy5ABHR37QnsHrAJquBaYO0S5KaZDh/IT0G6BvwvAXoHaS9Lt3d3UMqTuXr7Oxsdgnbpaurq6nH99+tfP4bFw1nOKwCpg54vgeVU05ba69LR0cH7e3tQypwNNm4sZfWVi82Gw6j9YOj2fx3K99Q/o17enoG/VI9nOHwEyAiYj/gGeB0YGFmPhsRayPiqMz8EfA+YMkw1jUqtbaO4Qf3PNbsMupy7KwZzS5BUo2G7atnZq4FzgLuAJ4EngK+UX35DODaiHgK2AW4brjqkiQVlT5yyMx9Bjy+HzhoC9ssp3I1kyRpBPCktSSpwHCQJBUYDpIabuPGuq9G1wjjneAkNdxou5rOK+mKHDlIkgoMB0lSgeFQtaHXFcIlqZ9zDlVtY9q4eunVzS6jZhfPvLjZJUjagTlykCQVGA6SpALDQZJUYDhIkgoMB0lSgeEgSSowHCRJBYaDJKnAcJAkFRgOkqQCw0GSVNCUtZUi4vvA7sD6atN/Bf4TMB8YD3w9M+c1ozZJUhPCISJagOnA3pm5odo2HkhgJvBr4N6IOCkzlwx3fZKk5owcovq/34mIvwYWAE8AT2fmMwARsQiYAxgOktQEzQiHycD9wAXAWOAHwNXA6gHbrAam1bPT7u7uIRXV2dk5pP7acXV1dTX1+L43tTVlvjeHPRwy88fAj/ufR8RNwKeABwds1gLUdYfyjo4O2tvbG1KjNJAfzhqphvLe7OnpGfRL9bBfrRQRR0fEcQOaWoCVwNQBbXsAzw9nXZKkv2jGaaVdgU9FxJFUTiv9F+Bc4PaI2A94BjgdWNiE2iRJNGHkkJn3APcCjwJdwMLqqaazgDuAJ4GngG8Md22SpIqm/M4hM/8J+KfN2u4HDmpGPZKkTfkLaUlSgeEgSSowHCRJBYaDJKnAcJAkFRgOkqQCw0GSVGA4SJIKDAdJUoHhIEkqMBwkSQWGgySpwHCQJBUYDpKkAsNBklRgOEiSCgwHSVKB4SBJKjAcJEkFTbmH9NZExOnAPGAs8NnM/HyTS5KkV6URM3KIiNcCnwaOBmYA50TEgU0tSpJepUbSyOF44HuZ+X8BIuIbwLuBT22jXyvAunXrhlzATi07DXkfw6Wnp4eW1r5ml1GXnp4e1reMa3YZdenp6Wl2CcDoem/C6Ht/vhrfmwM+M1u39HpLX9/I+D8wIj4JTMjMedXnc4HDMvOcwfp1dXUdDfxwGEqUpB3RMZ2dnQ9u3jiSRg5jgIFJ1QL01tDvP4BjgNXAxhLqkqQdUSswlcpnaMFICodVVD7k++0BPL+tTp2dnT1AIfUkSdv0y629MJLC4X8Bl0bEa4A1wN8Bg55SkiSVY8RcrZSZvwH+Efg+8Bjw1cx8uKlFSdKr1IiZkJYkjRwjZuQgSRo5DAdJUoHhIEkqMBwkSQUj6VJWNZkLH2oki4iJwEPArMxc2eRydniOHAS48KFGtog4nMqPXac3u5ZXC8NB/V5Z+DAz1wD9Cx9KI8HZwPnUsGqCGsPTSuq3J5X1qfqtBg5rUi3SJjJzLkBENLuUVw1HDuq3vQsfStoBGQ7qt4rKCo39alr4UNKOydNK6ufCh5Je4chBgAsfStqUC+9JkgocOUiSCgwHSVKB4SBJKjAcJEkFhoMkqcDfOUhVEfE24Ergr6l8cfo18PHM/FkD9n0usGtmXtWAfR0CfCMz9xnqvqStMRwkICLagXuAEzPzkWrbe4ElEfH6zNw4lP1n5pcaUKY0bAwHqWJnYFdglwFt/wq8DBwXEfMzswMgIo4FbsjMjoi4FDiCysKF3VSWPH9XZnZVt/068ANgCrAbcDfwPzLzzdXXdwWeAfat1nADsBeVe2p8LTOvqG7334D/DrwEPFHC3y9twjkHCcjM3wMXAd+KiF9FxFeA91NZVmTdNrrvDbw1M08DFlb7ERGTqSyF/tUB234X2KV6agjgNODe6vG/AizMzE4qK+IeHxHviYgZwKXA2zPz0BrqkYbMcJCqMnM+lW/4F1JZsvxi4FFg0ja6LsvMDdXHC4H3RMQ4Kh/8d2fmSwOO0Vfd5qxq0/uBBRExAZgJXB4RjwHLqIwgZgDHAd/JzP9d7fM/t/+vlGpjOEhARBwVEZ/IzP+Xmfdk5kXAm6gsYz6DyhLm/cZt1v2P/Q8y81ngEWAWlQ/+G7dwuIXAnOqIYNfMXAq0Vo9xZGbOyMwZwNuAK6p9Bh5/A1LJDAep4rfAvIg4ekDbVCqjhm8Ce0XE7hHRAvz9Nva1gMqoY0Jm/mjzF6uLHD4MfJlqeGTmy1RGCx+FV+YifgTMBr4DnBgR06q7OKv+P0+qj+EgAZn5c+BdwBXVOYcngduB92fmciof5D+l8gH+zDZ2dzewD1seNfRbALwV+JcBbacDb4uIJ4CfALdl5r9m5hNU5kPuj4ifAjvV+edJdXNVVklSgSMHSVKB4SBJKjAcJEkFhoMkqcBwkCQVGA6SpALDQZJUYDhIkgr+P/P3YZbbQ7lSAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x=\"Survived\", hue=\"Pclass\" ,data=df, palette=\"Accent\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='Frequency'>"
      ]
     },
     "execution_count": 176,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['Age'].plot.hist()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='Frequency'>"
      ]
     },
     "execution_count": 177,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['Age'].plot.hist(bins=8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='Frequency'>"
      ]
     },
     "execution_count": 178,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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qCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikAAAAAAAAAAAAAAACghmAKAAAAAAAAAAAAAAAAqCGYAgAAAAAAAAAAAAAAAGoIpgAAAAAAAAAAAAAAAIAagikA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MAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAA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QzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAAAAAAAAAAAABQQzAFAAAAAAAAAAAAAAAA1BBMAQAAAAAAAAAAAAAAADUEUwAAAAAAAAAAAAAAAEANwRQAAAAA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AAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAA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AAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANQRTAAAAAAAAAAAAAAAAQA3BFAAAAAAAAAAAAAAAAFBDMAUAAAAAAAAAAAAAAADUEEwBAAAAAAAAAAAAAAAANTbW+ZePMa5N8pkkr5hzfm2McXOSu5Jck+SDc847V487kuQ9Sa5N8skkb5hzfmedswEAAAAAAAAAAAAAAAB91naHqTHGi5N8Osl1q+NrkrwvybEkz0/yojHGy1cPvzvJm+ac1yU5kOT165oLAAAAAAAAAAAAAAAA6LW2YCpb0dMbkzywOr4hyVfmnF9d3T3q7iS3jDGem+SaOefnVo97f5Jb1jgXAAAAAAAAAAAAAAAAUGpjXX/xnPP2JBljPHzqmUkevOghDyZ59mXOPy5f+tKXdjQnbGdzc3PpEQC+L6dPn156BOAK5jkIAGBn7FEAADtjjwIA2Dm7FADAztijYG9aWzD1KK5KcuGi4wNJvnuZ84/L9ddfn6uvvvr7GhAAGgk/gaWcPn3acxAAwA7YowAAdsYeBQCwc3YpAICdsUfBcs6cOXPZmy9dtYuzfCPJMy46fnqSBy5zHgAAAAAAAAAAAAAAAOBx2c1g6vNJxhjjeWOMg0luTXLvnPPrSR4aY7xk9bjXJrl3F+cCAAAAAAAAAAAAAAAASuxaMDXnfCjJbUk+lOTLSe5Pcs/qy69J8vYxxv1JnpTknbs1FwAAAAAAAAAAAAAAANBjY93/gznnj1/0548leeGjPOaLSW5Y9ywAAAAAAAAAAAAAAABAt127wxQAAAAAAAAAAAAAAADAugmmAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAAAAAAgBqCKQAAAAAAAAAAAAAAAKCGYAoAAAAAAAAAAAAAAACoIZgCAAAAAAAAAAAAAAAAagimAAAAAAAAAAAA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AAAAAKghmAIAAAAAAAAAAAAAAABqCKYAAAAAAAAAAAAAAACAGoIpAAAAAAAAAAAAAAAAoIZgCgAAAAAAAAAAAAAAAKghmAIAAAAAAAAAAAAAAABqCKYAAAAAAAAAAAAAAACAGoIpAAAAAAAAAAAAAAAAoIZgCgAAAAAAAAAAAAAAAKghmAIAAAAAAAAAAAAAAABqCKYAAAAAAAAAAAAAAACAGoIpAAAAAAAAAAAAAAAAoIZgCgAAAAAAAAAAAAAAAKghmAIAAAAAAAAAAAAAAABqCKYAAAAAAAAAAAAAAACAGoIpAAAAAAAAAAAAAAAAoIZgCgAAAAAAAAAAAAAAAKghmAIAAAAAAAAAAAAAAABqCKYAAAAAAAAAAAAAAACAGoIpAAAAAAAAAAAAAAAAoIZgCgAAAAAAAAAAAAAAAKghmAIAAAAAAAAAAAAAAABqCKYAAAAAAAAAAAAAAACAGoIpAAAAAAAAAAAAAAAAoIZgCgAAAAAAAAAAAAAAAKghmAIAAAAAAAAAAAAAAABqCKYAAAAAAAAAAAAAAACAGoIpAAAAAAAAAAAAAAAAoIZgCgAAAAAAAAAAAAAAAKghmAIAAAAAAAAAAAAAAABqCKYAAAAAAAAAAAAAAACAGoIpAAAAAAAAAAAAAAAAoIZgCgAAAAAAAAAAAAAAAKghmAIAAAAAAAAAAAAAAABqCKYAAAAAAAAAAAAAAACAGoIpAAAAAAAAAAAAAAAAoIZgCgAAAAAAAAAAAAAAAKghmAIAAAAAAAAAAAAAAABqCKYAAAAAAAAAAAAAAACAGoIpAAAAAAAAAAAAAAAAoIZgCgAAAAAAAAAAAAAAAKghmAIAAAAAAAAAAAAAAABqCKYAAAAAAAAAAAAAAACAGoIpAAAAAAAAAAAAAAAAoIZgCgAAAAAAAAAAAAAAAKghmAIAAAAAAAAAAAAAAABqCKYAAAAAAAAAAAAAAACAGoIpAAAAAAAAAAAAAAAAoIZgCgAAAAAAAAAAAAAAAKghmAIAAAAAAAAAAAAAAABqCKYAAAAAAAAAAAAAAACAGoIpAAAAAAAAAAAAAAAAoIZgCgAAAAAAAAAAAAAAAKghmAIAAAAAAAAAAAAAAABqCKYAAAAAAAAAAAAAAACAGoIpAAAArihnz51fegSKub4AAAAAAAAAAGB5G0sPAAAAALvp8KGDOXr85NJj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",
      "text/plain": [
       "<Figure size 4320x2160 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['Fare'].plot.hist(bins=20,figsize=(60,30))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Age', ylabel='Count'>"
      ]
     },
     "execution_count": 179,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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89hTFQvvAYAGXvDP5/MpMzPzhGNPxwX/mDkAOG2cju/grcLMAcBpg+W+hw4zBwCACeUAADChHAAAJrYqh02bNmnu3LkqLCzUU089ZXUcABi2bHNAurOzU7W1tdq4caNSU1NVVlamSy65RN/97netjgYAAwr0h+R0xPZeO9AflNOREvO+v3f+lJjHDsQ25dDa2qpLL71UZ5xxhiTpqquuUnNzs37+858POM4wDElSX19fTPv1+/0amZoU09jBjj/RWGNE8km3GY/9nowxIpn7K4Fj47nvk91nVv3Og32OWXV/hYIBPfC4J6b93rkgVw88/kZMY4+O9/v9UY87+pp59DX025KME/0kwf70pz+pt7dXFRUVkqT169dr165dWrFixYDjfD6f9uzZk4iIAHDamTRp0nFP8LPNzCEUCikp6X/NbBjGMZdPZNSoUZo0aZKcTmdEtwcAfP0aGwgENGrUqOP+3DblkJ2drR07doQvd3V1yeVynXRccnLygKe1AwCOb8SIESf8mW3+Wumyyy7T9u3b9fnnn+vQoUN64YUXNGvWLKtjAcCwZJuZw9lnn62KigotXLhQgUBApaWluuCCC6yOBQDDkm0OSAMA7MM2HysBAOyDcgAAmFAOAAATygEAYDIsy8FuC/z19PTo6quv1scffyzp66VEiouLVVhYqNraWksyPfLII3K73XK73Vq1apVtcknS73//e82dO1dut1uPPfaYrbJJ0sqVK7V06VLb5FqwYIHcbrfmzZunefPmaefOnbbI1dLSopKSEs2ZM0cPPPCAJHvcX+vXrw/fV/PmzVNubq7uv/9+W2Srr68P/79cuXKlpDjeZ8Yw85///MeYPXu28cUXXxgHDx40iouLjb1791qW55///Kdx9dVXG1OmTDE6OjqMQ4cOGQUFBcZHH31kBAIB4+abbzY2b96c0EyvvfaaccMNNxh+v9/o6+szFi5caGzatMnyXIZhGG+88YZRVlZmBAIB49ChQ8bs2bONd9991xbZDMMwWltbjUsuucS4++67bfFYhkIhY+bMmUYgEAhfZ4dcH330kTFz5kxj//79Rl9fnzF//nxj8+bNluf6tj179hg//OEPjU8//dTybL29vcbFF19sfPbZZ0YgEDBKS0uNl19+OW65ht3M4ZsL/I0cOTK8wJ9V1q1bp+XLl4fPBt+1a5cmTJignJwc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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.set_theme(style=\"whitegrid\")\n",
    "sns.histplot(data=df,x='Age')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Count', ylabel='Age'>"
      ]
     },
     "execution_count": 180,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.histplot(data = df, y = \"Age\", bins=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Count', ylabel='Age'>"
      ]
     },
     "execution_count": 181,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYAAAAEJCAYAAACdePCvAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAjmElEQVR4nO3de1xUdf4/8NfADIh4W1cGUVnKNDNdyUvpmDHZuiMyjnjBgjIr19S+Bkn1M5dl1UpXUr87q9taj90189JjfZiXBB7KozYLc8Fcx5IoM1MgSRanXOUinBlmzu+Pcr4hA8wwc+Z2Xs+/mM+c8/m8P0nnzbm8z0chiqIIIiKSnTB/B0BERP7BBEBEJFNMAEREMsUEQEQkU0wAREQypfR3AK6y2+1obGyESqWCQqHwdzhEREFBFEVYrVZER0cjLKz13/xBkwAaGxvx1Vdf+TsMIqKgdPvtt6Nnz56t2oImAahUKgA/TCIiIsLP0UijvLwcI0eO9HcYkuH8ghvnF5wsFgu++uorxzH0p4ImAdy47BMREYHIyEg/RyOdUJ4bwPkFO84veDm7dM6bwEREMsUEQEQkU0FzCYiIyJfsdjuqq6vR2Njo71BcEh0djUGDBrV50qcjkiaAgwcP4q9//SsAICkpCS+88AJKSkqwbt06CIKAadOmITs7W8oQiIi65LvvvoNCocCwYcPcOqj6g91ux7fffovvvvsOarXa5f0km1VTUxPWrl2LnTt34uDBgzh58iSOHDmCnJwcbNmyBYcOHUJ5eTmKi4ulCoGIqMuuXr2K2NjYgD/4A0BYWBhiY2Nx7do19/aTKB7YbDbY7XY0NTWhpaUFLS0t6NGjBxISEhAfHw+lUgmDwYCioiKpQiAi6jKbzeb00clApVKp0NLS4tY+kl0C6tGjB5555hlMmzYNUVFRuPvuu3H58mXExMQ4tlGr1aitrZUqBCIijwTTWwe6EqtkCeDLL7/Evn378MEHH6Bnz554/vnnUVlZ2SpIURTdDloURdy8ho3FYkF5eblX4vY3k8nk7xAkxfkFNznNT6lUOr0BfOnSJcyYMQNDhgxxtImiiIyMDMycOdNpv/n5+fjnP/+JzZs3ez3mn7JYLG79G0mWAI4dOwaNRoOf//znAIDZs2dj69atCA8Pd2xjNpvdumEBAM3f1cKubB12VOwAjB071vOg/cxkMoXEPNrD+QU3uc3vzJkziI6ObrNdVFQUunXrhoKCAkdbbW0tpk+fjrFjx+KOO+5os09kZCSUSqXT/rwpIiICiYmJrdoEQWj3D2TJEsAdd9yBDRs24Pr164iKisKRI0eQmJiIgoICVFVVYdCgQSgsLMScOXOkCoGIyCdiY2ORkJCAyspKFBcX48CBA1AqlUhISEBeXl6rbT/99FNs2LABFosFZrMZEydOxB/+8Ae0tLTg5ZdfxqlTp6BSqTBo0CCsW7cOkZGRTtu9kUwkSwCTJk3CF198gdmzZ0OlUuGXv/wlMjMzce+99yIzMxOCIECr1SI5OVmqEIiIfOKTTz7BN998g6amJuzfvx979uxB7969sW7dOuzatQuxsbGObXfs2IGsrCyMHz8ejY2N+NWvfoXy8nI0NzfjxIkTOHToEBQKBTZs2ICzZ8/Cbrc7bR8zZozHcUtaB7Bo0SIsWrSoVZtGo0F+fr6UwxIRSaq5uRmpqakAfnha6Gc/+xk2bNiAjz76CMnJyejduzcA4Le//S0AYP/+/Y598/LycPToUbz++uu4cOECBEHA9evXcccddyA8PBxz587FpEmTMHXqVIwaNQp1dXVO272BlcBERG7q1q0bDh482Ka9pKSk1YMtdXV1qKura7XNvHnzMGzYMNx3332YNm0aTp8+DVEU0atXLxw8eBCnTp3C8ePHsWzZMvzmN7/BI4880m67p5gAiIi8ZOLEiVi/fj0WLlyIHj164M9//jNEUcSdd94J4IeE8Nlnn+Fvf/sbevfujY8//hjffPMN7HY7PvjgA7zxxhvYtm0b7r77boiiiPLy8nbbvYEJgIjIS7RaLb7++mtkZGQAAIYMGYKXX34Z7777LgCgV69eWLRoEWbNmoXu3bsjNjYWY8aMQVVVFebOnYujR49i+vTp6N69O3r37o2XX34ZcXFxTtu9QSHe/FB9gLrxKNNtsf0Q4eQx0GAq2GiP3B6zCzWcX3Bz9hjo8OHD/RiR+5zFfOPYOXLkyDbrHQT+Sy6IiEgSQXcJqFu/2Lar9ogiEAJnAEREvhR0CWDXG3thEayt2p5a9rh/giEiCmK8BEREJFNMAEREMsUEQEQkU0wAREQyxQRAROQCqUqm3Om3oaEB06dPR3V1tVfGDrqngIiI/EGhUOD6f771er/d+w90abvTp08jNzcXlZWVXhubZwBEREFgz549WLVqlduLaHWEZwBEREFg7dq1Xu8z6BLAvAVpbSuB4d51tFB4bxARkackSwBvv/02du3a5fhcXV2N1NRUTJkyBevWrYMgCJg2bRqys7Pd6veT/H8CLbZWbYkPjHN5/6jYAW6NR0QUqiRLAHPnzsXcuXMBAOfOncPSpUvx5JNPIiMjAzt37kRcXBwWL16M4uJiaLVaqcIgIqJ2+OQS0OrVq5GdnY2LFy8iISEB8fHxAACDwYCioiImACIKeKIouvzEjrv9+uuytORPAZWUlKC5uRnTpk3D5cuXERMT4/hOrVajtrZW6hCIiDwm1UHa3X6PHDmCQYMGeWVsyc8Adu/ejSeeeAIAYLfbW022K5nPYrVCtLa0aa+pqXFp/8GxA2Aymdwa05cCOTZv4PyCm5zmp1Qq0djY6Mdo3GexWNz6N5I0AVgsFvz73/9GXl4eAKB///4wm82O781ms9vPtEaoVICi7YlLXFycy30E6qpGcltxKdRwfsHN2Ypg0dHRfozIfREREUhMTGzVdmNFMGckvQR09uxZ3HLLLejevTsAIDExERUVFaiqqoLNZkNhYSGSkpKkDIGIiNoh6RnAxYsX0b9/f8fnyMhI5OXlITMzE4IgQKvVIjk5WcoQiIioHZImgJSUFKSkpLRq02g0yM/P73Kfo2dMcVoIRkRE7gm6SmBXC8GiYgew4peIqANBlwCIiPzBbrMjLNz7t01d7ffVV1/F4cOHAQBarRbLly/3eGwmACIiF4SFh6G8oNTr/Y40aDrdpqSkBMeOHcOBAwegUCiwcOFCvPfee/j1r3/t0dhMAEREAS4mJgYrVqxAREQEAOC2227DpUuXPO6XCYCIKMANHTrU8XNlZSUOHz6Mf/zjHx73ywVhiIiCxLlz57BgwQIsX74ct9xyi8f9MQEQEQUBk8mExx9/HM899xxmzZrllT55CYiIKMDV1NRg6dKlMBqN0Gg6v2nsKiYAIqIAt3XrVgiC4HivGgCkp6cjIyPDo36DLgG4Xgkswo1VIiXFgjSi4Ge32V16ZLMr/XZWB5Cbm4vc3Fyvjx10CaC9SuCTxz9t1TZuwl2+C6oDXIKSKDRIUQQmZb8uje23kYmIyK+YAIiIZIoJgIhIppgAiIhkigmAiEimJE0AR44cwezZszFt2jSsWbMGwA9vtTMYDNDpdDAajVIOT0REHZAsAVy8eBGrVq3Cli1bkJ+fjy+++ALFxcXIycnBli1bcOjQIZSXl6O4uFiqEIiIvKalpcWv/W7atAkpKSnQ6/XYtm2bV8aWrA7gvffeQ0pKimNNYKPRiKqqKiQkJCA+Ph4AYDAYUFRUBK1WK1UYREReoVQqscXonQPvT/1P9hOdbnPixAkcP34c+fn5aGlpQUpKCrRaLQYPHuzR2JIlgKqqKqhUKixZsgQ1NTW4//77MXToUMTExDi2UavVqK2tdavf9iqB70sNzIIrURRx6tQpl7c3mUwSRuN/nF9wk9P8lEolGhsbHZ+jo6NhtVgkGfen4zgzYsQIvPbaaxAEAZcuXXKcNdy8n8VicevfSLIEYLPZcPLkSezcuRPdu3fHU089hW7durV6LYIoim6/JsFZJfCAQf09ijXm9kEe7d+RqNgBGDt2rEvbmkwml7cNRpxfcJPb/M6cOYPo6OhW26h+XJDF224epz2bN2/GG2+8geTkZNx6661tjp8RERFITExs1SYIAsrLy532J9k9gH79+kGj0aBv377o1q0bpkyZgpKSEpjNZsc2ZrMZarVaqhCIiEJKVlYWSktLUVNTgz179njcn2QJYPLkyTh27Bjq6upgs9nw0UcfITk5GRUVFaiqqoLNZkNhYSGSkpKkCoGIKCScP38eZ86cAQBERUVBp9Ph7NmzHvcr2SWgxMRELFy4EA8//DCsVivuvfdeZGRkYPDgwcjMzIQgCNBqtUhOTpYqBCKikFBdXY3Nmzc7loF8//33MWfOHI/7lfRtoGlpaUhLS2vVptFokJ+fL+WwRERe19LS4tITO13pV6ns+FCs1WpRVlaGmTNnIjw8HDqdDnq93uOxg+510ERE/tDZQVrqfjMzM5GZmenVsfkqCCIimWICICKSKSYAIqJ2iIGyrqwLuhJr0N0DcH1N4EDh+trEI0eOlDYUInJZeHg4rFYrIiQq/vI2q9Xq9n2KoEsAUlQCt0fKCmFnuH4wUeDo06cPamtrMXDgQISFBfbFErvdjtraWvTu3dut/YIuARAR+UK/fv1QXV3tlYIrX4iOjka/fv3c2ocJgIjIibCwMPziF7/wdxiSCuzzGiIikgwTABGRTDEBEBHJFBMAEZFMMQEQEckUEwARkUwF3WOgwVcJ7A7Xq4b9wd3lO4kosAVdAnBWCSwVdyqMvVE1XFNTg7i4OI/7kQKrlIlCj6QJ4NFHH8WVK1cc76d46aWX0NjYiHXr1kEQBEybNg3Z2dlShkBERO2QLAGIoojKykp88MEHjgTQ3NyM5ORk7Ny5E3FxcVi8eDGKi4uh1WqlCoOIiNohWQK4cOECAGDBggW4evUqHnzwQdx+++1ISEhAfHw8AMBgMKCoqIgJgIjIDyRLAHV1ddBoNPj9738Pq9WK+fPnY+HChYiJiXFso1arUVtb61a/FqsVorXF2+G2q76hwaXtYvDDNXxPeaMPKQyOHQCTyeRxP97oI5BxfsEt1Od3M8kSwOjRozF69GjH57S0NGzevBljx451tImi6PaTJREqFaDw3dOrPXv0cHlbT2/gBvJNYACt/u26wmQyedxHIOP8gluozk8QBJSXlzv9TrIj6cmTJ1FaWur4LIoiBg4cCLPZ7Ggzm81Qq9VShUBERB2QLAHU19dj/fr1EAQBDQ0NOHDgAJ599llUVFSgqqoKNpsNhYWFSEpKkioEIiLqgGSXgCZPnozTp09j5syZsNvtePjhhzF69Gjk5eUhMzMTgiBAq9UiOTlZqhCIiKgDktYBLFu2DMuWLWvVptFokJ+f3+U+Q7kSeHBAF1u1X6XMCmGi4MRK4C5IfGAcTh7/1Ov91tfXo2fPnq3axk24y+vjeBMrhImCF18GR0QkU0wAREQyxQRARCRTTABERDLFBEBEJFNMAEREMsUEQEQkU0wAREQyFXSFYIFSCXxfKgugiCi4dZoAGhsbsXHjRly4cAGbNm3CH//4R7zwwguIjo72RXxtBEIlsKcmZMzAa396s017zaVLiBsQmInlqWWP85UPRCGm00tAa9asQa9evfD9998jMjISDQ0NWLlypS9iIyIiCXWaAM6cOYPs7GwolUpERUVh48aNOHPmjC9iIyIiCXWaAMLCWm9is9natBERUfDp9B7A3XffjQ0bNqC5uRkfffQR3nrrLYwfP94XsRERkYQ6/VP++eefR/fu3dGzZ08YjUYMGzYMy5cvd3mAV155BStWrAAAlJSUwGAwQKfTwWg0dj1qIiLyWKdnACqVCkuXLsXSpUvd7ry0tBQHDhzA/fffj+bmZuTk5GDnzp2Ii4vD4sWLUVxcDK1W26XAiYjIM50mgAceeKDV438KhQJRUVEYOnQoVqxY0e6i7levXoXRaMSSJUvw5ZdfoqysDAkJCYiPjwcAGAwGFBUVMQEQEflJpwlgypQpaGxsxCOPPIKwsDDs3bsXjY2NGDZsGFauXInXX3/d6X4rV65EdnY2ampqAACXL19GTEyM43u1Wo3a2lovTYOIiNzVaQI4efIk9u/f7/icm5uLtLQ0rFu3Dvv27XO6z9tvv424uDhoNBrHvna7vdWZhCiKXSosCpRKYM+IeGrZ4/4Owm1ie4sC38RisaC8vNzpdyaTyZshBRzOL7iF+vxu5lIlcENDA3r06AEAaGhoQFNTU4f7HDp0CGazGampqbh27RquX7+Ob7/9FuHh4Y5tzGZzu5ePOhIKlcDtrSnsbE3gQOHO2sRRsQMwduzYNu0mk8lpe6jg/IJbqM5PEIR2/yDrNAHMmTMHDz74IJKTk2G32/Hee+9h7ty52LlzJwYPHux0n23btjl+3r9/P06cOIEXX3wROp0OVVVVGDRoEAoLCzFnzpwuTomIiDzVaQJYtGgRhg8fjqNHj0KpVOKpp57C9u3bsXr1asyaNcvlgSIjI5GXl4fMzEwIggCtVovk5GSPgicioq5z6W2go0aNwpkzZ7Br1y7s3bsXjz76KEaMGOHSALNnz8bs2bMBABqNBvn5+V2PloiIvKbDBHDhwgVs374d+fn5GDhwIARBwJEjRwL2OjUREbmu3UrgRYsWYd68eVCpVNixYwcKCwsRHR3Ngz8RUYhoNwF88cUXGDFiBIYOHYqEhAQA4PvgiYhCSLsJ4MMPP8SsWbNQWFiISZMmISsrC4Ig+DI2IiKSULv3AJRKJVJSUpCSkoKvv/4au3fvhiAI0Ol0eOKJJ5CRkeHLOB1CoxAs1JeUFOGsZmzMmDEuF5N11Dfg2pmoaLcj7Ce1J0TUmktPAQ0ZMgS5ubl47rnnkJ+fj927d/stAYRCIVh7BIsFkRER/g5DMt6Y34SMGdie6/z1Izd7bM0Sj8YiCnVurewSFRWFhx56CAcOHJAqHiIi8hEu7UVEJFNMAEREMsUEQEQkU0wAREQyxQRARCRTTABERDLFBEBEJFMuFYIFklCpBKauEl0u8BLtdiDMd3/jeKfSOXD5en42mw1KZdAdooJK0P3XZSWwtNyptHWXN5a8fGzNErz2pze9E5CX1Vy6hLgBofuKD1/PLxjXzQ42kv55tGnTJqSkpECv1zuWiSwpKYHBYIBOp4PRaJRyeCIi6oBkZwAnTpzA8ePHkZ+fj5aWFqSkpECj0SAnJwc7d+5EXFwcFi9ejOLiYmi1WqnCICKidkh2BnDPPfdgx44dUCqV+P7772Gz2VBXV4eEhATEx8dDqVTCYDCgqKhIqhCIiKgDkl4CUqlU2Lx5M/R6PTQaDS5fvoyYmBjH92q1GrW1tVKGQERE7ZD8JnBWVhaefPJJLFmyBJWVla1WFRNF0e1VxixWK0Rri7fDDBiCxeLvEFBfXx+4fYs/3IwMVIEcmzf4en4mkymkx/M3yRLA+fPnYbFYMHz4cERFRUGn06GoqAjhP1mgw2w2Q61Wu9VvhEoFKEKzfCEQngICINm6z954CggKBOyTNnwKyPvGjh3rs7FMJpNPx/MVQRBQXl7u9DvJjqTV1dXIzc2FxWKBxWLB+++/j/T0dFRUVKCqqgo2mw2FhYVISkqSKgQiIuqAZGcAWq0WZWVlmDlzJsLDw6HT6aDX69G3b19kZmZCEARotVokJydLFQIREXVAIQZJ6eKN05gRI0awElhSrq+56w+iXYQiTNFpGwU/m83W6pJxV/Z3p5I41C8BjRw5ss2xk5XAAcTXa+b6mlfuATgRKNXBvAcQWFhJ3LnQvJtKRESdYgIgIpIpJgAiIpliAiAikikmACIimWICICKSKSYAIiKZYgIgIpIpVgKHHF9X8vq/cpiVwOSMp5XEgcST9ZFZCRwkAuVtoO5wp/KYawIHN87Pf6SqauYlICIimWICICKSKSYAIiKZYgIgIpIpJgAiIpmSNAG8+uqr0Ov10Ov1WL9+PQCgpKQEBoMBOp0ORqNRyuGJiKgDkiWAkpISHDt2DAcOHMA777yDzz//HIWFhcjJycGWLVtw6NAhlJeXo7i4WKoQiIioA5IlgJiYGKxYsQIRERFQqVS47bbbUFlZiYSEBMTHx0OpVMJgMKCoqEiqEIiIqAOSFYINHTrU8XNlZSUOHz6MefPmISYmxtGuVqtRW1vrVr+jZ0xhJXBAEfHYmiW+G80ucqk/kh1PKoE7Inkl8Llz57B48WIsX74c4eHhqKysdHwniiIUCvdK+D/edxiitcXLUQYf7WNpePWZDS5t+/Sf/h9WvvAHiSMikreX1ufg1KlT/g7DLZImAJPJhKysLOTk5ECv1+PEiRMwm82O781mM9RqtVt9RqhUgCI0H15y91UQLr9WQYGAKHEP5FJ7b+D8gps35jd27FgvReM9N94F5IxkR9KamhosXboUGzduhF6vBwAkJiaioqICVVVVsNlsKCwsRFJSklQhEBFRByQ7A9i6dSsEQUBeXp6jLT09HXl5ecjMzIQgCNBqtUhOTpYqBCIi6oBkCSA3Nxe5ublOv8vPz5dqWCIiclFoXkwnIqJOMQEQEckUEwARkUwxARARyRTXBA5arq/FyzVziaQnVbWup7gmcCcSHxiHk8c/bdN+X2qKT9efZaHN/3lq2eNuV4n7m8lkCshCIG/h/DoWiAf/zvASEBGRTDEBEBHJFBMAEZFMMQEQEckUEwARkUwxARARyRQTABGRTDEBEBHJVNBVLki1JvB9qc4KlLj+rL8EalUlUSgJuv/D/v3ehxBtrSuBfV2xKxWpKoEDparWnUpLHvyJpCfpJaCGhgZMnz4d1dXVAICSkhIYDAbodDoYjUYphyYiok5IlgBOnz6NjIwMVFZWAgCam5uRk5ODLVu24NChQygvL0dxcbFUwxMRUSckSwB79uzBqlWroFarAQBlZWVISEhAfHw8lEolDAYDioqKpBqeiIg6IdmF1rVr17b6fPnyZcTExDg+q9Vq1NbWSjU8ERF1wmd32ux2e6sbkaIodunGZGNjA2zWljbtNZcueRRfoJBqHiaTSZJ+3RUocUiF8wtuoT6/m/ksAfTv3x9ms9nx2Ww2Oy4PuSM6ukebp4AAhMR79KVcDyAQ3uPO98kHN84vON1YEMYZnxWCJSYmoqKiAlVVVbDZbCgsLERSUpKvhiciopv47AwgMjISeXl5yMzMhCAI0Gq1SE5O9tXwRER0E8kTwJEjRxw/azQa5Ofne9Tf3b++30klsDQVu6Gyli6raonImaA7Kuz737dgvW7xyViPrVkiSYVxe5W5Ul2D5MGfiJzhy+CIiGSKCYCISKaYAIiIZIoJgIhIppgAiIhkigmAiEimmACIiGSKCYCISKaCrkJoznOPeLgmsAjAtepe0S7dmsCiKLZpGzNmjNN2p/sHYZWyO/PzBlZAE3Us6P7v+CT/n0BL27eBumpCxgxsz33dixF5T319PXr27OnStlJVKUtJyredOiNV8iYKFbwEREQkU0wAREQyxQRARCRTTABERDLFBEBEJFN+SQAFBQVISUmBTqfDW2+95Y8QiIhkz+ePgdbW1sJoNGL//v2IiIhAeno6xo8fjyFDhvg6FCIiWfN5AigpKcGECRPQp08fAMDUqVNRVFSEp59+2qX9R8+Y4nEh2GNrlniwf2CQskgtVLAQjKhjPv+/4/Lly4iJiXF8VqvVKCsrc3n/zz//XIqwiLzCZDL5OwRJcX6hxecJwG63t1oPVxRFp+vjtmfkyJEengEELqnWBA4UnF9w4/yCkyAIKC8vd/qdz28C9+/fH2az2fHZbDZDrVb7OgwiItnzeQKYOHEiSktLceXKFTQ1NeHdd99FUlKSr8MgIpI9n18Cio2NRXZ2NubPnw+r1Yq0tDSMGjXK12EQEcmeXx6RMBgMMBgM/hiaiIh+xEpgIiKZYgIgIpKpoKmSubGSlMVi8XMk0hIEwd8hSIrzC26cX/C5ccx0thqfQvTlGn0eqK+vx1dffeXvMIiIgtLtt9/eZsXBoEkAdrsdjY2NUKlUbhWOERHJmSiKsFqtiI6ORlhY66v+QZMAiIjIu3gTmIhIppgAiIhkigmAiEimmACIiGSKCYCISKaYAIiIZIoJgIhIpoIiARQUFCAlJQU6nQ5vvfWWv8PxmoaGBkyfPh3V1dUAflgv2WAwQKfTwWg0+jk6z7z66qvQ6/XQ6/VYv349gNCa36ZNm5CSkgK9Xo9t27YBCK353fDKK69gxYoVAEJrfo8++ij0ej1SU1ORmpqK06dPh9T8XCYGuP/85z/i5MmTxf/+979iY2OjaDAYxHPnzvk7LI99+umn4vTp08URI0aIFy9eFJuamkStVit+8803otVqFRcsWCB++OGH/g6zS/71r3+JDz30kCgIgmixWMT58+eLBQUFITO/jz/+WExPTxetVqvY1NQkTp48WTxz5kzIzO+GkpIScfz48eILL7wQUr+fdrtdnDRpkmi1Wh1toTQ/dwT8GUBJSQkmTJiAPn36oHv37pg6dSqKior8HZbH9uzZg1WrVjmWwywrK0NCQgLi4+OhVCphMBiCdp4xMTFYsWIFIiIioFKpcNttt6GysjJk5nfPPfdgx44dUCqV+P7772Gz2VBXVxcy8wOAq1evwmg0YsmSJQBC6/fzwoULAIAFCxZgxowZ2LVrV0jNzx0BnwAuX76MmJgYx2e1Wo3a2lo/RuQda9euxbhx4xyfQ2meQ4cOxV133QUAqKysxOHDh6FQKEJmfgCgUqmwefNm6PV6aDSakPr3A4CVK1ciOzsbvXr1AhBav591dXXQaDT4y1/+gjfffBO7d+/GpUuXQmZ+7gj4BGC321u9/E0UxZB8GVwozvPcuXNYsGABli9fjvj4+JCbX1ZWFkpLS1FTU4PKysqQmd/bb7+NuLg4aDQaR1so/X6OHj0a69evR8+ePdG3b1+kpaVh8+bNITM/dwT8egD9+/fHyZMnHZ/NZrPjskko6d+/P8xms+NzsM/TZDIhKysLOTk50Ov1OHHiRMjM7/z587BYLBg+fDiioqKg0+lQVFSE8PBwxzbBPL9Dhw7BbDYjNTUV165dw/Xr1/Htt9+GzPxOnjwJq9XqSHCiKGLgwIEh8/vpjoA/A5g4cSJKS0tx5coVNDU14d1330VSUpK/w/K6xMREVFRUoKqqCjabDYWFhUE7z5qaGixduhQbN26EXq8HEFrzq66uRm5uLiwWCywWC95//32kp6eHzPy2bduGwsJCHDx4EFlZWXjggQfw97//PWTmV19fj/Xr10MQBDQ0NODAgQN49tlnQ2Z+7gj4M4DY2FhkZ2dj/vz5sFqtSEtLw6hRo/wdltdFRkYiLy8PmZmZEAQBWq0WycnJ/g6rS7Zu3QpBEJCXl+doS09PD5n5abValJWVYebMmQgPD4dOp4Ner0ffvn1DYn7OhNLv5+TJk3H69GnMnDkTdrsdDz/8MEaPHh0y83MH1wMgIpKpgL8ERERE0mACICKSKSYAIiKZYgIgIpIpJgAiIpkK+MdAiXzJZrNhx44dKCgogM1mg9VqxeTJk/HMM88gIiLCq2OVlZVh7969eOmll7zaL5GreAZA9BOrV6/GJ598gu3bt+PgwYPYu3cvKioq8Lvf/c7rY3399deyeN8MBS7WARD9qLq6GtOnT8exY8fQo0cPR7vZbMapU6cwceJEvPjii/jyyy+hUChw33334dlnn4VSqcSwYcNQWlqKvn37AoDj87lz52A0GhEfH49z586hpaUFL774IgYMGICMjAzU19dDp9Nh3bp1/po2yRjPAIh+9Pnnn2PIkCGtDv7AD6+3njp1KtasWYM+ffqgoKAA+/btw9mzZ/HGG2902m9ZWRkWLFiAd955B7Nnz4bRaERcXByysrIwbtw4HvzJb5gAiH4UFhYGu93e7vdHjx7FvHnzoFAoEBERgfT0dBw9erTTfgcMGIDhw4cDAO68805cu3bNazETeYIJgOhHo0aNwoULF9DQ0NCqvba2FosWLWrzSmS73Y6WlpY2/Vgsllafu3Xr5vhZoVCAV10pUDABEP0oNjYWBoMBOTk5jiTQ0NCA1atXo0+fPpg0aRJ27doFURRhsViwZ88eTJw4EQDQt29ffPbZZwCAwsJCl8YLDw93mkCIfIUJgOgnVq1ahSFDhiA9PR2pqamYO3cuhgwZgjVr1iA3NxdXrlyBwWCAwWDArbfe6lgyMTc3Fy+99BJmzZqF8+fPt1pdqj133XUXLl68iKefflrqaRE5xaeAiIhkimcAREQyxQRARCRTTABERDLFBEBEJFNMAEREMsUEQEQkU0wAREQyxQRARCRT/x8QHMKxz78mEwAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.histplot(data = df, y = \"Age\", bins=20,hue=\"Pclass\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='SibSp', ylabel='Count'>"
      ]
     },
     "execution_count": 182,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.histplot(data=df,x='SibSp')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Parch', ylabel='Count'>"
      ]
     },
     "execution_count": 183,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.histplot(data=df,x='Parch')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Data Cleaning (wrangling)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PassengerId      0\n",
       "Survived         0\n",
       "Pclass           0\n",
       "Name             0\n",
       "Sex              0\n",
       "Age            177\n",
       "SibSp            0\n",
       "Parch            0\n",
       "Ticket           0\n",
       "Fare             0\n",
       "Cabin          687\n",
       "Embarked         2\n",
       "dtype: int64"
      ]
     },
     "execution_count": 184,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 185,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(data=df.isnull())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.drop('Cabin', axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_13624/3627053830.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdescribe\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'df' is not defined"
     ]
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 188,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 188,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(data=df.isnull())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_13624/2087891831.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhead\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m100\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'df' is not defined"
     ]
    }
   ],
   "source": [
    "df.head(100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 189,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 189,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['Age'].fillna(df['Age'].mean(),inplace=True)\n",
    "df.head(150)\n",
    "sns.heatmap(data=df.isnull())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df[pd.notnull(df['Embarked'])]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PassengerId    0\n",
       "Survived       0\n",
       "Pclass         0\n",
       "Name           0\n",
       "Sex            0\n",
       "Age            0\n",
       "SibSp          0\n",
       "Parch          0\n",
       "Ticket         0\n",
       "Fare           0\n",
       "Embarked       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 191,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 192,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAX0AAAEzCAYAAADdK9NNAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAABTeUlEQVR4nO3deVhVVfvw8S8yKRGZxmBqaJlaajiQc2g5MSNOKYYUOZYTJYqomKaShlOpPfpkaY44JIihOFukqfhzTLPMTBFlEAVlEDhnv3/weh6PqBxgowz3p2tfl3ufddZex/BmnbXXupeRoigKQgghKoUqT7sBQgghnhwJ+kIIUYlI0BdCiEpEgr4QQlQiEvSFEKISkaAvhBCVSKkE/aioKFxdXenevTtr1qwpjVsIIYQoBtWDfmJiIvPnz2ft2rVEREQQHh7OhQsX1L6NEEKUWYZ2fMePH8+PP/6oO09ISGDgwIE4OzszYsQIMjIyAEhPT2fo0KG4uLgwcOBAkpOTi9021YP+wYMHadu2LdWrV8fCwoIePXqwY8cOtW8jhBBlkiEd38TERIYPH05MTIze9WnTpuHj48OOHTto2rQpS5YsAWDBggU4Ojqyfft2+vbty8yZM4vdPtWDflJSEtbW1rpzGxsbEhMT1b6NEEI8Uenp6cTHxxc40tPT9coZ0vGNioqiS5cuuLi46K7l5uZy9OhRevToAUCvXr1079u/fz8eHh4AuLu78/PPP5Obm1usz2FSrHc9hlarxcjISHeuKIre+ePE1empdnOEEBWUY3xEievITblocNmV635i0aJFBa6PHDmSUaNG6c4f1vE9deqU3nsGDx4MwLFjx3TXbt68iaWlJSYm+WHZ2tpa12G+v04TExMsLS1JTU3F1tbW4Pbfo3rQt7OzIy4uTneenJyMjY2N2rcRQoiS02oMLurn54e3t3eB61ZWVvpVFrPj+7Byj3qfoihUqVK8gRrVh3fat2/PoUOHSE1NJSsri507d+Lk5KT2bYQQouQUrcGHlZUVderUKXA8GPTt7Oz0HrQa2vGtUaMGt2/fRqPRFHifjY0NKSkpAOTl5ZGRkUH16tWL9ZFVD/q2trYEBAQwaNAgevbsibu7O2+88YbatxFCiJLTag0/DFTcjq+pqSmOjo5ER0cDEBERoXtfp06diIiIACA6OhpHR0dMTU2L/nkBo7KUWlnG9IUQhlJjTD8n/rTBZc3qNDO4bFRUFEuXLiU3N5c+ffowZMgQhgwZwujRo2nW7H/1BAUF0bp1a3r16gXA1atXCQoK4saNG9SqVYt58+bx3HPPcevWLYKCgrhy5QrPPvssYWFh1KlTx/APeh8J+kKIckmVoH/lpMFlzeo6lPh+ZYHqD3KFEKLcKMKD3IpCgr4QovJSDB+rryhUCfqzZ8/m5s2buLi4MG/ePN31xMREHBwcWLp0qRq3EUIIdRXhAW1FUeKgf+jQIbZs2ULnzp3p1KkTnTp1AvKnGw0YMICJEyeWuJFCCFEalErY0y/RlM1bt24xf/58hg8fXuC1OXPm0L9/f+rVq1eSWwghROnR5Bl+VBAlCvohISEEBAQUWJxw6dIljhw5wqBBg0rUOCGEKFVajeFHBVHsoL9x40Zq1apFu3btCrwWHh6Oj48PZmZmJWqcEEKUqiKsyK0oij2mHx0dTXJyMl5eXqSlpZGZmcmsWbMIDg5mz549LF++XM12CiGE+uRBruG+//573Z9//PFHjhw5QnBwMKmpqWRnZ1O3bl1VGiiEEKWmAvXgDaX6PP34+Hjs7OzUrlYIIdRXCXv6koZBCFEuqZGGIfvENoPLVm3uXuL7lQWyIlcIUXlVwp6+BH0hROUlY/pFs2zZMjZv3oyZmRmurq6MGDGCiRMncuzYMapVqwbkbyXWrVs3VRorhBCqqkDz7w1V7KB/8OBBoqKi2Lx5M9WqVePjjz9m586dnDlzhtWrV8sWiUKIsk96+oY7e/YsHTt2xNLSEoC33nqLn376iYSEBIKDg0lMTKRbt26MHDmy2Hs5CiFEqapA6RUMVexo3KRJE2JjY7l16xZ3795l79693L59m7Zt2zJr1iw2bNhAXFwcmzZtUrO9QgihnlLYLrGsK3bQb9euHb169cLX15fBgwfTqlUrTE1NWbx4MTY2NlSrVg1fX18OHDigZnuFEEI9lTDoF3t4586dO3Tv3p0PPvgAgG+//Zbs7GxiYmLo0aMHAIqiYGIiE4SEEGWTopTOg9yoqCi++eYb8vLy8PPzY+DAgXqvnzt3jkmTJpGRkYGjoyPTpk0jLS0Nf39/XZnbt29z8+ZNjh8/zpEjRxg1apRu4evrr79OaGhosdpW7J5+fHw8H330EXl5edy+fZtNmzbx8ccfM2vWLNLS0sjNzSU8PFxm7gghyq5S6OknJiYyf/581q5dS0REBOHh4Vy4cEGvTGBgICEhIcTExKAoChs2bKBmzZpERkYSGRnJli1bqF27NtOnTwfgzJkz+Pv7614vbsCHEvT0GzduTPfu3fH09ESj0fD+++/TunVrhg4dyoABA8jLy6N79+64u1eMVWxCiAqoCLN30tPTSU9PL3DdyspKL738wYMHadu2LdWrVwegR48e7Nixg5EjRwJw9epVsrOzad68OQC9evXiq6++wsfHR1fHvVmRHh4eAJw+fZqUlBS2bdtG7dq1mTp1KrVq1SrqpwVKOE//448/5uOPP9a7NnDgwAJfZYQQokwqwuydlStXsmjRogLXR44cyahRo3TnSUlJWFtb685tbGw4derUI1+3trYmMTHxf03SaPjPf/7DkiVLdNeeffZZXFxc6N69O+vWrSMgIID169cb3Pb7yYC7EKLyKsKwjZ+fH97e3gWuP7iJlFarxcjISHeuKIreeWGv//LLL9SrV49GjRrprt0b5gEYMGAAc+fO5fbt2zz77LMGt/8eCfpCiMqrCMM7Dw7jPIqdnR1xcXG68+TkZL3FqnZ2diQnJ+vOU1JS9F7fvXs3rq6uunOtVsvSpUsZOnQoxsbGuuv3/7koZNWUEKLyKoUHue3bt+fQoUOkpqaSlZXFzp07cXJy0r1eu3ZtzM3NOXbsGACRkZF6r584cQJHR0fdeZUqVdi1axcxMTEARERE4ODggIWFRbE+skFB/86dO7i7uxMfH693ffXq1fj6+urOd+/ejZeXF56ennz00UekpaUVq1FCCPFElELQt7W1JSAggEGDBtGzZ0/c3d154403GDJkCKdPnwYgLCyM0NBQnJ2dyczM1NtP/MqVKwX2JJk9ezY//PADbm5ubN68mRkzZhT7IxeaT//kyZNMnjyZf/75hx07dlCnTh0ALly4gL+/P/b29qxatYo7d+7g7OzM5s2bsbW1ZeHChdy+fZvJkycb3BjJpy+EMJQa+fSzts0zuGw1909KfL+yoNCe/oYNG5g6daremFNOTg4hISGMHj1ady03N5epU6dia2sLQKNGjbh27VopNFkIIVSiyTP8qCAKfZA7c+bMAtfmzp1L7969db1+gOeff163ECs7O5tly5bpDf0IIUSZU4HSKxiqyA9yf/31V65du0bv3r0f+vrt27cZOnQojRs3fuj0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",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(data=df.isnull())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
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
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "2            3         1       3   \n",
       "3            4         1       1   \n",
       "4            5         0       3   \n",
       "\n",
       "                                                Name     Sex   Age  SibSp  \\\n",
       "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
       "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
       "4                           Allen, Mr. William Henry    male  35.0      0   \n",
       "\n",
       "   Parch            Ticket     Fare Embarked  \n",
       "0      0         A/5 21171   7.2500        S  \n",
       "1      0          PC 17599  71.2833        C  \n",
       "2      0  STON/O2. 3101282   7.9250        S  \n",
       "3      0            113803  53.1000        S  \n",
       "4      0            373450   8.0500        S  "
      ]
     },
     "execution_count": 202,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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VRMAXV1dAIBvvvlG4UqIiNSnq6sLYWFhXq8pMgroWrhcLrS3t0On03HOdSKiAXK73ejq6sKIESMQFOR91V81AUBERP7Fm8BERIJiABARCYoBQEQkKAYAEZGgGABERIJiABARCYoBQEQkKAbAENHW1obZs2fj7NmzSpdCPnrjjTeQnZ2N7OxsbNiwQelyyAevv/46srKykJ2djW3btildTsAxAIaAo0ePYsGCBaivr1e6FPKRzWbD/v37sWvXLnz88cf46quvvNZ3pqHr0KFDOHjwIEpLS/HRRx+hqKgItbW1SpcVUAyAIWDHjh146aWXuDSmCsXExGDNmjUICQmBTqfDzTffjO+//17psmgApkyZgu3bt0Or1eLChQtwOp2IiIhQuqyAUs1kcMPZa6+9pnQJdI0mTJjg+bq+vh6ffvopPvjgAwUrIl/odDps3rwZ77zzDjIzMzFmzBilSwoo9gCI/ODbb7/F008/jdWrV+Omm25SuhzywfLly3HgwAE0NjZix44dSpcTUAwAokGqqanB7373Ozz//POYO3eu0uXQAH333Xc4ceIEACA8PBxGoxEnT55UuKrAYgAQDUJjYyOWLVuGTZs2ITs7W+lyyAdnz57F2rVr0dnZic7OTlRWViIlJUXpsgKK9wCIBuHtt9+GJEmwWCye18xmMxYsWKBgVTQQBoMBx44dwwMPPIDg4GAYjUbhQpzrARARCYqXgIiIBMUAICISFAOAiEhQDAAiIkExAIiIBMVhoES4MiZ85syZuPXWWz2vud1uPPHEE8jJybnqz+zcuRN///vf8dZbbwWqTCK/YgAQ/SwsLAy7d+/2tJuamjB79mwkJSXh9ttvV7AyInkwAIh6MWbMGMTHx6O+vh7V1dXYtWsXtFot4uPjvR78AoAvv/wSGzduRGdnJxwOB+655x786U9/Qnd3N1555RV88cUX0Ol0uOGGG1BQUIDQ0NCrvj5ixAiFflsSEQOAqBdHjhzB6dOncfnyZezcuRM7duzAqFGjUFBQgPfee89r5sjt27dj+fLluPvuu9He3o7p06fDbrejo6MDhw4dQnl5OTQaDTZu3IiTJ0/C5XJd9fXJkycr+BuTaBgARD/r6OjAnDlzAABOpxNRUVHYuHEjPv/8c2RmZmLUqFEAgBdffBHAlXsAPSwWC/bt24c333wTtbW1kCQJly5dwu23347g4GDMnz8fU6dOxf33348777wTFy9evOrrRIHEACD62S/vAfSw2WzQaDSe9sWLF3Hx4kWv9zz22GO47bbbcN9992HWrFk4evQo3G43rrvuOuzevRtffPEFDh48iBUrVuD3v/89Hn300V5fJwoUBgBRP+655x5s2LABzzzzDEaOHIm//OUvcLvdSExMBHAlEP7zn/9g69atGDVqFP71r3/h9OnTcLlc2LNnD9555x1s27YNd911F9xuN+x2e6+vEwUSA4CoHwaDAadOnfLM8HnLLbfglVdewWeffQYAuO6667Bo0SLMnTsXERERGDNmDCZPnoyGhgbMnz8f+/btw+zZsxEREYFRo0bhlVdewdixY6/6OlEgcTZQIiJB8UlgIiJBMQCIiATFACAiEhQDgIhIUAwAIiJBMQCIiATFACAiEhQDgIhIUP8fRxaWxRTVGSUAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(x='Pclass', y='Age',data=df)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 204,
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
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "2            3         1       3   \n",
       "3            4         1       1   \n",
       "4            5         0       3   \n",
       "\n",
       "                                                Name     Sex   Age  SibSp  \\\n",
       "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
       "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
       "4                           Allen, Mr. William Henry    male  35.0      0   \n",
       "\n",
       "   Parch            Ticket     Fare Embarked  \n",
       "0      0         A/5 21171   7.2500        S  \n",
       "1      0          PC 17599  71.2833        C  \n",
       "2      0  STON/O2. 3101282   7.9250        S  \n",
       "3      0            113803  53.1000        S  \n",
       "4      0            373450   8.0500        S  "
      ]
     },
     "execution_count": 204,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Converting Categorical Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
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
       "      <th>female</th>\n",
       "      <th>male</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   female  male\n",
       "0       0     1\n",
       "1       1     0\n",
       "2       1     0\n",
       "3       1     0\n",
       "4       0     1"
      ]
     },
     "execution_count": 206,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.get_dummies(df['Sex']).head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 207,
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
       "      <th>male</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   male\n",
       "0     1\n",
       "1     0\n",
       "2     0\n",
       "3     0\n",
       "4     1"
      ]
     },
     "execution_count": 207,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.get_dummies(df['Sex'],drop_first=True).head(5)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 209,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     male\n",
      "0       1\n",
      "1       0\n",
      "2       0\n",
      "3       0\n",
      "4       1\n",
      "..    ...\n",
      "886     1\n",
      "887     0\n",
      "888     0\n",
      "889     1\n",
      "890     1\n",
      "\n",
      "[889 rows x 1 columns]\n"
     ]
    }
   ],
   "source": [
    "sex = pd.get_dummies(df['Sex'],drop_first=True)\n",
    "print(sex)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
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
       "      <th>male</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   male\n",
       "0     1\n",
       "1     0\n",
       "2     0\n",
       "3     0\n",
       "4     1"
      ]
     },
     "execution_count": 164,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sex.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
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
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>887</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>Montvila, Rev. Juozas</td>\n",
       "      <td>male</td>\n",
       "      <td>27.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>211536</td>\n",
       "      <td>13.00</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>888</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Graham, Miss. Margaret Edith</td>\n",
       "      <td>female</td>\n",
       "      <td>19.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>112053</td>\n",
       "      <td>30.00</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>889</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Johnston, Miss. Catherine Helen \"Carrie\"</td>\n",
       "      <td>female</td>\n",
       "      <td>29.699118</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>W./C. 6607</td>\n",
       "      <td>23.45</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>890</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Behr, Mr. Karl Howell</td>\n",
       "      <td>male</td>\n",
       "      <td>26.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>111369</td>\n",
       "      <td>30.00</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>891</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Dooley, Mr. Patrick</td>\n",
       "      <td>male</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>370376</td>\n",
       "      <td>7.75</td>\n",
       "      <td>Q</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     PassengerId  Survived  Pclass                                      Name  \\\n",
       "886          887         0       2                     Montvila, Rev. Juozas   \n",
       "887          888         1       1              Graham, Miss. Margaret Edith   \n",
       "888          889         0       3  Johnston, Miss. Catherine Helen \"Carrie\"   \n",
       "889          890         1       1                     Behr, Mr. Karl Howell   \n",
       "890          891         0       3                       Dooley, Mr. Patrick   \n",
       "\n",
       "        Sex        Age  SibSp  Parch      Ticket   Fare Embarked  \n",
       "886    male  27.000000      0      0      211536  13.00        S  \n",
       "887  female  19.000000      0      0      112053  30.00        S  \n",
       "888  female  29.699118      1      2  W./C. 6607  23.45        S  \n",
       "889    male  26.000000      0      0      111369  30.00        C  \n",
       "890    male  32.000000      0      0      370376   7.75        Q  "
      ]
     },
     "execution_count": 214,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
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
       "      <th>Q</th>\n",
       "      <th>S</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Q  S\n",
       "886  0  1\n",
       "887  0  1\n",
       "888  0  1\n",
       "889  0  0\n",
       "890  1  0"
      ]
     },
     "execution_count": 215,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emb = pd.get_dummies(df['Embarked'],drop_first=True)\n",
    "emb.tail(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 216,
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
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   2  3\n",
       "0  0  1\n",
       "1  0  0\n",
       "2  0  1\n",
       "3  0  0\n",
       "4  0  1"
      ]
     },
     "execution_count": 216,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pcl = pd.get_dummies(df['Pclass'],drop_first=True)\n",
    "pcl.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
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
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Embarked</th>\n",
       "      <th>male</th>\n",
       "      <th>Q</th>\n",
       "      <th>S</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>S</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>S</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>S</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>S</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "2            3         1       3   \n",
       "3            4         1       1   \n",
       "4            5         0       3   \n",
       "\n",
       "                                                Name     Sex   Age  SibSp  \\\n",
       "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
       "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
       "4                           Allen, Mr. William Henry    male  35.0      0   \n",
       "\n",
       "   Parch            Ticket     Fare Embarked  male  Q  S  2  3  \n",
       "0      0         A/5 21171   7.2500        S     1  0  1  0  1  \n",
       "1      0          PC 17599  71.2833        C     0  0  0  0  0  \n",
       "2      0  STON/O2. 3101282   7.9250        S     0  0  1  0  1  \n",
       "3      0            113803  53.1000        S     0  0  1  0  0  \n",
       "4      0            373450   8.0500        S     1  0  1  0  1  "
      ]
     },
     "execution_count": 221,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2 = pd.concat([df,sex,emb,pcl],axis=1)\n",
    "df2.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['PassengerId',    'Survived',      'Pclass',        'Name',\n",
       "               'Sex',         'Age',       'SibSp',       'Parch',\n",
       "            'Ticket',        'Fare',    'Embarked',        'male',\n",
       "                 'Q',           'S',             2,             3],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 222,
   "metadata": {},
   "outputs": [],
   "source": [
    "df2.drop(['Name','PassengerId','Pclass', 'Sex', 'Embarked' ],axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 223,
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
       "      <th>Survived</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>male</th>\n",
       "      <th>Q</th>\n",
       "      <th>S</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Survived   Age  SibSp  Parch            Ticket     Fare  male  Q  S  2  3\n",
       "0         0  22.0      1      0         A/5 21171   7.2500     1  0  1  0  1\n",
       "1         1  38.0      1      0          PC 17599  71.2833     0  0  0  0  0\n",
       "2         1  26.0      0      0  STON/O2. 3101282   7.9250     0  0  1  0  1\n",
       "3         1  35.0      1      0            113803  53.1000     0  0  1  0  0\n",
       "4         0  35.0      0      0            373450   8.0500     1  0  1  0  1"
      ]
     },
     "execution_count": 223,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 224,
   "metadata": {},
   "outputs": [],
   "source": [
    "df2.drop('Ticket',axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 225,
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
       "      <th>Survived</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "      <th>male</th>\n",
       "      <th>Q</th>\n",
       "      <th>S</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Survived   Age  SibSp  Parch     Fare  male  Q  S  2  3\n",
       "0         0  22.0      1      0   7.2500     1  0  1  0  1\n",
       "1         1  38.0      1      0  71.2833     0  0  0  0  0"
      ]
     },
     "execution_count": 225,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 231,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = df2.drop('Survived',axis=1)\n",
    "x.columns = x.columns.astype(str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 232,
   "metadata": {},
   "outputs": [],
   "source": [
    "y = df2['Survived']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(889, 10)"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "linReg = LinearRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "linReg.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [],
   "source": [
    "predection = linReg.predict(x_test)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'np' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_13624/3510580515.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mpred\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mround\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpredection\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m0.2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmax\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpredection\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;31m# print(predection)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;31m# print(pred)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'np' is not defined"
     ]
    }
   ],
   "source": [
    "pred = np.round(predection-0.2)\n",
    "print(np.max(predection))\n",
    "# print(predection)\n",
    "# print(pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import classification_report\n",
    "from sklearn.metrics import accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import confusion_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(178,)"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'              precision    recall  f1-score   support\\n\\n           0       0.71      0.98      0.82       105\\n           1       0.94      0.41      0.57        73\\n\\n    accuracy                           0.75       178\\n   macro avg       0.82      0.70      0.70       178\\nweighted avg       0.80      0.75      0.72       178\\n'"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "predection = linReg.predict(x_test)\n",
    "classification_report(y_test,pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7471910112359551"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(y_test,pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[103,   2],\n",
       "       [ 43,  30]], dtype=int64)"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "confusion_matrix(y_test,pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "ML",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
