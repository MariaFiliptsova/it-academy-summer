import collections
import os


'''Given an integer, n, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
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


'''We add a Leap Day on February 29, almost every four years. 
The leap day is an extra, or intercalary day and we add it to 
the shortest month of the year, February. 
In the Gregorian calendar three criteria must be taken into account to identify 
leap years:
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, 
while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
Task 
You are given the year, and you have to write a function to check if the year is leap or not.
Note that you have to complete the function and remaining code is given as template.
'''
def is_leap(year):
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


'''In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs 
in the given string. 
String traversal will take place from left to right, 
not from right to left.
'''
def count_substring(string, sub_string):
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


'''A group of friends want to buy a bouquet of flowers. 
The florist wants to maximize his number of new customers and the money he makes. 
To do this, he decides he'll multiply the price of each flower by the number 
of that customer's previously purchased flowers plus 1. 
The first flower will be original price, (0 + 1) x original price, 
the next will be (1 + 1) x original price and so on.
Given the size of the group of friends, the number of flowers 
they want to purchase and the original prices of the flowers, 
determine the minimum cost to purchase all of the flowers.
For example, if there are k = 3 friends that want to buy n = 4 flowers 
that cost c = [1, 2, 3, 4] each will buy one of the flowers priced [2, 3, 4] 
at the original price. Having each purchased x = 1 flower, the first flower in the list,
c[0], will now cost (current purchase + previous purchases) x c[0] = (1+1)x1=2. 
The total cost will be 2 + 3 + 4 + 2 = 11.
'''
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


"""A newly opened multinational brand has decided to base 
their company logo on the three most common characters 
in the company name. 
They are now trying out various combinations of company names 
and logos based on this condition. 
Given a string , which is the company name in lowercase letters, 
your task is to find the top three most common characters in the string.
Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,
Google would have it's logo with the letters G, O, E.
"""
company_name = 'nazvanie companii'.replace(' ', '')
sorted_symbols = sorted(company_name)
times_seen = dict(collections.Counter(sorted_symbols).most_common(3))
for k, v in times_seen.items():
    print(k, v)
