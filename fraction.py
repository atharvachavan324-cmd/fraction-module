{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "03738c83-336f-49ae-a853-82998296b0ee",
   "metadata": {},
   "source": [
    "**Fraction function***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "101ebbb2-194e-4165-a084-49fc66ef2978",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10/8\n"
     ]
    }
   ],
   "source": [
    "class fraction :\n",
    "    def __init__(self, n , d):\n",
    "        self.num=n\n",
    "        self.den=d\n",
    "        \n",
    "    def __str__(self):\n",
    "        return\"{}/{}\".format(self.num , self.den)\n",
    "        \n",
    "    def __add__(self,other):\n",
    "        temp_num = self.num * other.den + other.num * self.den\n",
    "        temp_den = self.den * other.den\n",
    "        return\"{}/{}\".format(temp_num , temp_den)\n",
    "\n",
    "    def __sub__(self,other):\n",
    "        temp_num = self.num * other.den - other.num * self.den\n",
    "        temp_den = self.den * other.den\n",
    "        return\"{}/{}\".format(temp_num , temp_den)\n",
    "\n",
    "    def __mul__(self,other):\n",
    "        temp_num = self.num * other.den * other.num * self.den\n",
    "        temp_den = self.den * other.den\n",
    "        return\"{}/{}\".format(temp_num , temp_den)\n",
    "\n",
    "    def __truediv__(self,other):\n",
    "        temp_num = self.num * other.den \n",
    "        temp_den = self.den * other.num\n",
    "        return\"{}/{}\".format(temp_num , temp_den)\n",
    "        \n",
    "\n",
    "        \n",
    "x= fraction(1,2)\n",
    "y=fraction(3,4)\n",
    "print(x+y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "0c7559e3-9885-4003-9f14-0c39d197b31a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-2/8\n"
     ]
    }
   ],
   "source": [
    "print(x-y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "11b2af90-ad32-46f7-b56e-6221029de63f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "24/8\n"
     ]
    }
   ],
   "source": [
    "print(x*y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "a29c1a4f-3a49-4e4d-a8c7-4bc24abc32b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4/6\n"
     ]
    }
   ],
   "source": [
    "print(x/y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "7b84c530-9fb1-4063-8f49-907cf5932ba3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "__main__.fraction"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "ec12f8af-8875-4627-b5de-8b281f646152",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "13306e22-3ce8-4722-813d-1192b90f461e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f5a3696-cf8e-4bb0-8a0d-f2f18943dfd8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "55ebe30a-bcef-4e2f-a727-d52d67a4a183",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
