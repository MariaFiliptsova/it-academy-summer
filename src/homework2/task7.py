'''https://www.hackerrank.com/challenges/py-if-else/problem
'''

n = int(input('Enter your number\n'))
if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
elif n > 20:
    print("Not Weird")

'''https://www.hackerrank.com/challenges/write-a-function/problem
'''


def is_leap(year):
    leap = False
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input())
print(is_leap(year))

'''https://www.hackerrank.com/challenges/find-a-string/problem
'''


def count_substring(string, sub_string):
    length_of_substring = len(sub_string)
    total_ = 0
    for i in range(len(string) - len(sub_string) + 1):
        if (string[i:i + len(sub_string)] == sub_string):
            total_ += 1
    return total_


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

'''https://www.hackerrank.com/challenges/greedy-florist/problem
'''

import math
import os
import random
import re
import sys


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort(reverse=True)
    price = 0
    flowers_bought = 0
    for i in range(n):
        price = price + (flowers_bought + 1) * c[i]
        if (i + 1) % k == 0:
            flowers_bought += 1
    return price


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
