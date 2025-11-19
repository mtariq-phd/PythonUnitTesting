def factorial(n):
    """
    Calculate the factorial of a given number.

    :param int n: The factorial to calculate
    :return: The resultant factorial
    """

    # # Limit for this implementation is 999 (due to the recursion depth 
    # - because of how Python manages function calls and its memory stack)
    # if n == 0 or n == 1:
    #     return 1
    # else:
    #     return  n * factorial(n-1)
    
    #  implementation works for larger numbers (due to No Stack Limitation 
    # and Faster and Less Overhead than Recursion)
    #  scope of the function: limit is the afctorial can only have less than 
    # 4300 digits)

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

