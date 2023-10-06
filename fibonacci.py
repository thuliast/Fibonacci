def fibonacci(n):
    """
    Calculates the Fibonacci sequence of an integer positive number
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    number = int(input("Enter the number to calculate Fibonacci:\n"))
    result = fibonacci(number)
    print("The Fibonacci sequence of {0} is {1}\n".format(number,str(result)))

if __name__ == "__main__":
    main()
    
