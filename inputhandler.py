def input_handler():
    supported_systems = [2, 10]

    # Get user input for the input base
    while True:

        # Check for invalid input
        try:
            in_base = int(input("What input base would you like to use: "))

            # If we support the given base then continue
            if in_base not in supported_systems:
                print(f"We don't support 'base {in_base}' yet")
            else:
                break

        except ValueError:
            print("That isn't a valid input. Try an integer (2).")

    # Get user input for the output base
    while True:

        # Check for invalid input
        try:
            out_base = int(input("What output base would you like to use: "))

            # If we support the given base then continue
            if out_base not in supported_systems:
                print(f"We don't support 'base {out_base}' yet")
            else:
                break

        except ValueError:
            print("That isn't a valid input. Try an integer (2).")

    # Get user input for the input number
    while True:

        # Check for invalid input
        try:
            in_number = int(input("What number would you like to translate: "))
            break

        except ValueError:
            print("That isn't a valid input. Try an integer (2).")

    return in_base, out_base, in_number
