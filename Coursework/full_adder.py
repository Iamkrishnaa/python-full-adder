from Coursework.conversion import binary_conversion, decimal_conversion  # this import specific method from conversion


# this is code for half_adder
def half_adder(first_binary, second_binary):
    sum_ = first_binary ^ second_binary  # logical xor
    carry = first_binary and second_binary  # logical and
    return sum_, carry


# this is code for full_adder
def full_adder(first_binary, second_binary, carry_in):
    first_sum, first_carry = half_adder(first_binary, second_binary)
    second_sum, second_carry = half_adder(first_sum, carry_in)
    carry = first_carry or second_carry  # logical or
    return second_sum, carry


def binary_full_adder():
    first_binary, second_binary = binary_conversion()
    carry_in = 0
    result = []
    for i in range(len(first_binary) - 1, -1, -1):
        sum_, carry_in = full_adder(first_binary[i], second_binary[i], carry_in)
        result.insert(0, sum_)
    result.insert(0, carry_in)

    result = int("".join(str(i) for i in result))

    final_first_binary = ''.join(str(x) for x in first_binary)
    final_second_binary = ''.join(str(x) for x in second_binary)

    if len(str(result)) >= 8:
        print("Output value exceed the bit limit. Try other number")
        binary_full_adder()
    else:
        print("Final answer is: \n")
        print("Binary addition is: \n", final_first_binary, "+", final_second_binary, "=", result)
        print("\nBinary to Decimal is:\n", final_first_binary, "+", final_second_binary, "=", decimal_conversion(result))


while True:
    binary_full_adder()
    query = input("Enter q to quit program, Any other to continue.")
    if query == "q" or query == "Q":
        break
