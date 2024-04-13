def base_converter(in_base, out_base, in_number):
    """Takes the input base, input number, and output base; returns the output number"""

    # Choose which conversion function to use based on in_base vs out_base
    if in_base == 10 and out_base == 2:
        out_number = base_10_to_2(in_number)

    elif in_base == 2 and out_base == 10:
        out_number = base_2_to_10(in_number)

    else:
        raise ValueError

    return out_number


def base_10_to_2(in_number):
    """Takes an input number and converts it from base 10 to base 2"""

    pass


def base_2_to_10(in_number):
    """Takes an input number and converts it from base 2 to base 10"""
    if in_number == 0:
        return "0"
    binary_num = ""
    while in_number > 0:
        binary_num = str(in_number % 2) + binary_num
        in_number //= 2
    return binary_num
