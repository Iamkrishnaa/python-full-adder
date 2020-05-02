def binary_conversion(integer_a, integer_b):
    first_binary_value = []
    second_binary_value = []

    """The below code is used to convert integer_a and integer_b to corresponding binary"""
    while integer_a > 0:
        first_binary_value.append(integer_a % 2)

        integer_a = integer_a // 2

    while integer_b > 0:
        second_binary_value.append(integer_b % 2)

        integer_b = integer_b // 2

    """The below code is used to add extra bits and make whole 8 bit"""
    first_value = []
    second_value = []

    for value in range(8 - len(first_binary_value)):
        first_value.append(0)

    for value in range(8 - len(second_binary_value)):
        second_value.append(0)

    """The below code will make 8 bit digit and arranging the binary values"""
    first_value = first_value + [first_binary_value[i] for i in range(len(first_binary_value) - 1, -1, -1)]
    second_value = second_value + [second_binary_value[i] for i in range(len(second_binary_value) - 1, -1, -1)]

    final_first_value = ''.join(str(x) for x in first_value)
    final_second_value = ''.join(str(x) for x in second_value)

    return final_first_value, final_second_value


def binary_adder(first_number, second_number):
    carry = 0
    sum_value = []
    for i in range(len(first_number)-1, -1, -1):
        if int(first_number[i]) == 1 and int(second_number[i]) == 1 and carry == 0:
            sum_value.append(0)
            carry = 1
        elif int(first_number[i]) == 1 and int(second_number[i]) == 0 and carry == 0:
            sum_value.append(1)
            carry = 0
        elif int(first_number[i]) == 1 and int(second_number[i]) == 0 and carry == 1:
            sum_value.append(0)
            carry = 1
        elif int(first_number[i]) == 1 and int(second_number[i]) == 1 and carry == 1:
            sum_value.append(1)
            carry = 1
        elif int(first_number[i]) == 0 and int(second_number[i]) == 0 and carry == 1:
            sum_value.append(1)
            carry = 0
        elif int(first_number[i]) == 0 and int(second_number[i]) == 1 and carry == 1:
            sum_value.append(0)
            carry = 1
        elif int(first_number[i]) == 0 and int(second_number[i]) == 1 and carry == 0:
            sum_value.append(1)
            carry = 0
        elif int(first_number[i]) == 0 and int(second_number[i]) == 0 and carry == 0:
            sum_value.append(0)
            carry = 0

    result = []
    for i in range(len(sum_value)-1, -1, -1):
        result.append(sum_value[i])

    return ''.join(str(x) for x in result)


if __name__ == '__main__':
    while True:
        """checks if the enter valid is between 0 and 255"""

        integer_first = int(input("Enter first integer\n"))
        integer_second = int(input("Enter second integer\n"))

        if (0 <= integer_first <= 255) and (0 <= integer_second <= 255):
            res = binary_conversion(integer_first, integer_second)
            final_result = binary_adder(res[0], res[1])
            print(res[0], "+", res[1], "=", final_result)
        else:
            print("Please Enter value between 0 and 255")

        condition = input("Press q to quit and any other to continue.\n")
        if condition == "q":
            break
