def division():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    # if num2 == 0:
    #     raise ValueError("Cannot divide by zero")
    assert num1 != 100
    result = num1 / num2
    print(result)
    return result


if __name__ == '__main__':
    try:
        f = division()
    except ZeroDivisionError:
        print("Division by zero")
    except ValueError as e:
        print("input error", e)
    except AssertionError as e:
        print("assertion error", e)
    else:
        print("else result: " + str(f))
    finally:
        print("complete calculate")
