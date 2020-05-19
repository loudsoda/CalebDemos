'''
Title: Fibonacci Functions
Created by: Caleb Ellis
Date: 5/18/2020

Required:
matplotlib

Info:
I have heard of the Fibonacci Sequence before and somewhat understood how it works, but I never looked at the
formula behind it, nor have I taken the time to understand the logic until now. These functions seem to follow the
sequence accurately. My goal was to create a function that can generate the sequence on from the factorial.

I have made two functions, fibonacci() and fibonacci_graph(). Both run off the same logic, fibonacci_graph() with
graph the outputs of the sequence.

This was the first time I applied an unfamiliar mathematical concept and I found it quite fun.
'''


# A function printing the Fibonacci sequence
def fibonacci(n):
    # Print out the value of factorials is being iterated through
    print("The factorial is : n =", n)

    # make a list of with
    seq = list(range(n))

    for y in seq:
        print("n =", (y + 1))

        # Begin the sequence, f0 = 0, f1 = 1
        if y == 0:
            n1 = y
            n2 = 1

            fn = n1 + n2

            print(n1, "+", n2, "=", fn)

        # After the first sequence, begin iterating based off the previous sequence
        if y > 0:
            fn = n1 + n2

            print(n1, "+", n2, "=", fn)

            # Shift the numbers for the next iteration of the loop
            n1 = n2
            n2 = fn


def fibonacci_graph(n):
    import matplotlib.pyplot as plt
    seq = list(range(n))

    # Create a list to add Fibonacci numbers to for the graph
    list_graph = []

    for y in seq:

        print("n = ", (y + 1))

        # Begin the sequence, f0 = 0, f1 = 1
        if y == 0:
            n1 = y
            n2 = 1

            fn = n1 + n2
            print(n1, "+", n2, "=", fn)

        # After the first sequence, begin iterating based off the previous sequence
        if y > 0:
            fn = n1 + n2

            print(n1, "+", n2, "=", fn)

            # Shift the numbers for the next iteration of the loop
            n1 = n2
            n2 = fn

        list_graph.append(fn)

    plt.plot(list_graph, 'ro')
    plt.xlabel("Factorials of the Fibonacci Sequence (n)")
    plt.ylabel("Fibonacci number")
    plt.show()


# Change the variable 'n' to illustrate different factorials of the Fibonacci Sequence
n = 21

# Run functions
fibonacci(n)
fibonacci_graph(n)
