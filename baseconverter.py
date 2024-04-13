def base_converter(in_base, out_base, in_number):
    """Takes the input base, input number, and output base; returns the output number"""

    # Choose which conversion function to use based on in_base vs out_base
    if out_base == 10:
        out_number = base_to_10(in_base, in_number)

    else:
        out_number = base_10_to(in_base, in_number, out_base)

    return out_number


def base_to_10(base, in_number):
    """Takes an input number and a base then turns it into base 10"""
    decimal_num = 0
    negative = False
    if in_number < 0:
        negative = True
        in_number = abs(in_number)
    power = len(str(in_number)) - 1
    for num in str(in_number):
        decimal_num += int(num) * (base ** power)
        power -= 1
    if negative is True:
        in_number = "-" + str(in_number)
    return decimal_num


def base_10_to(base, in_number, in_base):
    """Takes an input number, an original base, and a new base then translates the number to base
       10 then takes that new base 10 number and translates it to the new base"""
    num = base_to_10(base, in_number)
    new_num = ""
    negative = False
    if num < 0:
        negative = True
        num = abs(in_number)
    if num == 0:
        return "0"
    while num > 0:
        new_num = str(num % in_base) + new_num
        num //= in_base
    if negative is True:
        new_num = "-" + new_num
    return new_num
