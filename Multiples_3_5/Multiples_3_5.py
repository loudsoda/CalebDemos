'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.

Courtesy of ProjectEuler.net

https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

Solution by Caleb Ellis
Date: 5/27/2020

'''


def solution(number):

    # Create range for loop, mak it so the loop does not exceed x
    # number is simplified to x for the sake of irs
    x = number
    y = range(1, int(x))

    # Create list to find sum
    number_list = []
    # Loop though all iterations of the input number
    for i in y:
        multi_5 = i * 5
        multi_3 = i * 3

        # Check if digits exist in list or if digit is greater than x
        if multi_3 >= x or multi_3 in number_list:
            pass

        else:
            number_list.append(multi_3)

        if multi_5 >= x or multi_5 in number_list:
            pass

        else:
            number_list.append(multi_5)

    # Add contents of list together
    Sum = sum(number_list)
    return (Sum)


print(solution(200))

