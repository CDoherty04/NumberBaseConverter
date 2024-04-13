def input_handler():
    # Get user input for the input base
    while True:

        # Check for invalid input
        try:
            in_base = int(input("What input base would you like to use: "))
            if 10 >= in_base > 1:
                break
            else:
                raise RuntimeError

        except RuntimeError:
            print("Base system must be between 1 and 10")

        except ValueError:
            print("That isn't a valid input. Try a natural number (Example: 5)")

    # Get user input for the output base
    while True:

        # Check for invalid input
        try:
            out_base = int(input("What output base would you like to use: "))
            if 10 > out_base > 0:
                break
            else:
                raise RuntimeError

        except RuntimeError:
            print("Base system bust be between 1 and 10")

        except ValueError:
            print("That isn't a valid input. Try an integer (2).")

    # Get user input for the input number
    while True:

        # Check for invalid input
        try:
            in_number = input(f"What number would you like to translate from base {in_base} to base {out_base}: ")

            # Check every digit for a number greater than the base system can handle
            for digit in in_number:
                if int(digit) >= in_base:
                    raise RuntimeError

            # If the loop never catches an invalid number then continue
            break

        except ValueError:
            print("\nThat isn't a valid input. Try a natural number (Example: 2)\n")
        except RuntimeError:
            print(f"\nThat is not an acceptable number in base {in_base}\n")

    return in_base, out_base, int(in_number)
