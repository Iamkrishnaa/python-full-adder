from Coursework.full_adder import binary_full_adder


def run():
    """
    This code is responsible to run binary adder until the user intentionally
    stop it.
    This uses a loop that will run until user press 'q' otherwise it will run infinitely.
    """
    while True:
        binary_full_adder()  # this calls binary_full_adder function from full_adder module
        query = input("Enter q to quit program, Any other to continue.")
        if query == "q" or query == "Q":  # we can convert it to lowercase and apply too.
            break


if __name__ == '__main__':
    run()
