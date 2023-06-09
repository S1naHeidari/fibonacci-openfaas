def Fibonacci(n):

    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        raise ValueError("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    """handle a request to the function
    Args:
        req (str): request body
    """
    try:
        result = Fibonacci(int(req))
        return str(result)
    except ValueError as e:
        return "Error (value error): " + str(e), 500
    except Exception as e:
        return "Error: " + str(e), 500


