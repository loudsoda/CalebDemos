'''
Title: Create a function that formats a Phone Number, a test from codewars.com. Test created by xDranik
Solution by: Caleb Ellis
Date: 5/19/2020


Info:
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the
form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
'''


def create_phone_number(n):

    # Create an empty list to dump strings converted from int
    list_of_numbers = []

    # Convert
    for i in n:
        x = str(i)

        list_of_numbers.append(x)

    # Change list_of_number to 'n' for easier indexing when organizing numbers.
    n = list_of_numbers

    # Organize the sections of the phone number.
    area = n[0] + n[1] + n[2]
    prefix = n[3] + n[4] + n[5]
    subscriber = n[6] + n[7] + n[8] + n[9]

    # Format the number.
    number = ("(" + area + ") " + prefix + "-" + subscriber)

    # Output formatted number.
    print(number)

    return number


create_phone_number([0, 5, 7, 4, 5, 3, 2, 1, 3, 4])
