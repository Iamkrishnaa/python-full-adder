# The below method will accept two inputs from user
def accept_input():
    # until and unless satisfying numbers are inserted, the loop will continue
    while True:
        first_value = int  # this will declare first_value as integer
        second_value = int  # this will declare second_value as integer

        # try-except will handle any exception occurred during accepting inputs
        try:
            first_value = int(input("Enter first integer:\n"))
            second_value = int(input("Enter second integer:\n"))

        except:
            print("Non integer value detected.")
            continue
        else:
            if (first_value < 0 or first_value > 255) or (second_value < 0 or second_value > 255):
                print("Please, enter value between 0 and 255")
                continue
            break

    # returns value of first and second integer from user
    return first_value, second_value


# the below method will convert the respected integers to binary format and store in list
def binary_conversion():
    # declaring value of two variables with return value from accept_input function
    first_integer, second_integer = accept_input()
    first_binary = []
    second_binary = []

    # the below code will add remainder to new list and again divide initial value by 2
    while first_integer > 0:
        first_binary.append(first_integer % 2)
        first_integer = first_integer // 2

    while second_integer > 0:
        second_binary.append(second_integer % 2)
        second_integer = second_integer // 2

    # This will arrange the binary digits from right to left
    final_binary_first = first_binary[::-1]
    final_binary_second = second_binary[::-1]

    # The below code is responsible to add extra bit to make exact 8 bit value
    while len(final_binary_first) != 8:
        final_binary_first.insert(0, 0)

    while len(final_binary_second) != 8:
        final_binary_second.insert(0, 0)

    # this will return converted binary values
    return final_binary_first, final_binary_second


def decimal_conversion(binary_value):
    """The below code is used to again convert result binary value to final decimal/integer value"""
    num = binary_value
    integer_value = 0
    base = 1
    temp = num
    while temp:
        last_digit = temp % 10
        temp = int(temp / 10)

        integer_value += last_digit * base
        base = base * 2
    return integer_value
