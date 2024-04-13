def base_converter(in_base, out_base, in_number):
    """Takes the input base, input number, and output base; returns the output number"""

    # Choose which conversion function to use based on in_base vs out_base
    if in_base == 10 and out_base == 2:
        out_number = base_10_to_2(in_number)

    elif out_base == 10:
        out_number = base_2_to_10(in_base, in_number)

    else:
        raise ValueError

    return out_number


def base_10_to_2(in_number):
    """Takes an input number and converts it from base 10 to base 2"""

    negative = False
    if in_number < 0:
        negative = True
        in_number = abs(in_number)
    if in_number == 0:
        return "0"
    binary_num = ""
    while in_number > 0:
        binary_num = str(in_number % 2) + binary_num
        in_number //= 2
    if negative is True:
        binary_num = "-" + binary_num
    return binary_num


def base_2_to_10(base,in_number):
    """Takes an input number and converts it from base 2 to base 10"""

    decimal_num = 0
    negative = False
    if in_number < 0:
        negative = True
        in_number = abs(in_number)
    power = len(str(in_number)) - 1
    for num in str(in_number):
        decimal_num += int(num) * (base**power)
        power -= 1
    if negative is True:
        in_number = "-" + str(in_number)
    return decimal_num


def charlie_base_n_to_10(n_base, given_number):
    """Takes an input number and converts it from any base to base 10"""

    out_num = 0

    # Multiply each digit by the base to its digit place
    for digit_index in range(len(str(given_number))):

        digit = int(str(given_number)[::-1][digit_index])
        number_place_multiplier = n_base**digit_index

        # Sum each digit
        out_num += number_place_multiplier*digit

    return out_num


# Test
if __name__ == "__main__":

    print(charlie_base_n_to_10(7, 2166))  # Should be 783
