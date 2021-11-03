{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOV6S2SgBpC0yV9E5vnSAHZ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/iitdpooja/Deep-Learning-/blob/main/tensor_basics.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5aUk1SilUWEB"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1rOESYr0UXmg",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "4315d528-6828-418a-cca5-db5baadf2225"
      },
      "source": [
        "import numpy as np\n",
        "X = np.arange(24).reshape(2, 3, 4)\n",
        "#print(X)\n",
        "\n",
        "A = np.arange(20).reshape(5, 4)\n",
        "B = A.copy()\n",
        "print(A)\n",
        "print('Addition of Matrix is:', A+B)\n",
        "print('multiplication of Matrix is:',A*B)\n",
        "a=2\n",
        "print('shape:', (a+X).shape)\n",
        "print('sum of matrix elements: ', A.sum())\n",
        "A_sum_axis0 = A.sum(axis=0) # gives sum of columns\n",
        "print('Sum of 0 axis elements: ',A_sum_axis0)\n",
        "print('Dimension of 0 axis: ',A_sum_axis0.shape)\n",
        "\n",
        "A_sum_axis1 = A.sum(axis=1) # gives sum of rows\n",
        "print('Sum of 1 axis elements: ',A_sum_axis1)\n",
        "print('Dimension of 1 axis: ',A_sum_axis1.shape)\n",
        "print(A.mean())\n",
        "print(A.size)\n",
        "print(A.mean(axis=0), A.sum(axis=0) / A.shape[0])\n",
        "sum_A = A.sum(axis=1, keepdims=True) #keepdims to keep number of axis unchanged\n",
        "print(sum_A)\n",
        "print(A / sum_A) #we can divide A by sum_A with broadcasting\n",
        "print(A.cumsum(axis=0))\n",
        "x = np.arange(4)\n",
        "y = np.ones(4)\n",
        "print(np.dot(x,y))\n",
        "print(np.sum(x * y)) # elementwise multiplication plus sum gives dot product\n",
        "print(A.shape, x.shape, np.dot(A, x))\n",
        "B = np.ones(shape=(4, 3))\n",
        "print(np.dot(A, B))\n",
        "u = np.array([3, -4])\n",
        "print(u)\n",
        "print(np.linalg.norm(u)) # gives root mean square value of vector. This is also called as L2 norm\n",
        "print(np.abs(u).sum()) # L1 norms "
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[ 0  1  2  3]\n",
            " [ 4  5  6  7]\n",
            " [ 8  9 10 11]\n",
            " [12 13 14 15]\n",
            " [16 17 18 19]]\n",
            "Addition of Matrix is: [[ 0  2  4  6]\n",
            " [ 8 10 12 14]\n",
            " [16 18 20 22]\n",
            " [24 26 28 30]\n",
            " [32 34 36 38]]\n",
            "multiplication of Matrix is: [[  0   1   4   9]\n",
            " [ 16  25  36  49]\n",
            " [ 64  81 100 121]\n",
            " [144 169 196 225]\n",
            " [256 289 324 361]]\n",
            "shape: (2, 3, 4)\n",
            "sum of matrix elements:  190\n",
            "Sum of 0 axis elements:  [40 45 50 55]\n",
            "Dimension of 0 axis:  (4,)\n",
            "Sum of 1 axis elements:  [ 6 22 38 54 70]\n",
            "Dimension of 1 axis:  (5,)\n",
            "9.5\n",
            "20\n",
            "[ 8.  9. 10. 11.] [ 8.  9. 10. 11.]\n",
            "[[ 6]\n",
            " [22]\n",
            " [38]\n",
            " [54]\n",
            " [70]]\n",
            "[[0.         0.16666667 0.33333333 0.5       ]\n",
            " [0.18181818 0.22727273 0.27272727 0.31818182]\n",
            " [0.21052632 0.23684211 0.26315789 0.28947368]\n",
            " [0.22222222 0.24074074 0.25925926 0.27777778]\n",
            " [0.22857143 0.24285714 0.25714286 0.27142857]]\n",
            "[[ 0  1  2  3]\n",
            " [ 4  6  8 10]\n",
            " [12 15 18 21]\n",
            " [24 28 32 36]\n",
            " [40 45 50 55]]\n",
            "6.0\n",
            "6.0\n",
            "(5, 4) (4,) [ 14  38  62  86 110]\n",
            "[[ 6.  6.  6.]\n",
            " [22. 22. 22.]\n",
            " [38. 38. 38.]\n",
            " [54. 54. 54.]\n",
            " [70. 70. 70.]]\n",
            "[ 3 -4]\n",
            "5.0\n",
            "7\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UFuKsUkUUYUX"
      },
      "source": [
        "\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}