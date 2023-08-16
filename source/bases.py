"""
part of my module in developement
"""

def __absver(num):
   if num < 0:
       return (abs(num), True)
   else:
       return (num, False)


def to_base(num, startBase, base):
    """
    Converts a number to a different base number.
    :param num: number to be converted
    :type num: int/str
    :param startBase: must be >= 2 and <= 36, can be 0 if starts with '0_'
    :type startBase: int
    :param base: must be >= 2 and <= 36, base to which num will be converted
    :type base: int
    :return: converted number (without the '0_' mark)
    :rtype: str
    :raises ValueError: if unable to convert
    """

    # Make sure that number exists
    num = int(str(num), startBase)

    # Make sure that base is 2-36
    if base < 2 or base > 36:
        raise ValueError("Base must be >= 2 and <= 36")

    # Negative number handling
    num, neg = __absver(num)

    if base != 10:  # Optimize script
        digits = "0123456789abcdefghijklmnopqrstuvwxyz"
        result = ""

        while num > 0:
            remainder = num % base
            result = digits[remainder] + result
            num //= base

    else: result = str(num)
    
    return ('-' if neg else '') + result


b_int = 10
b_dec = 10
b_bin = 2
b_oct = 8
b_hex = 16
b_min = 2
b_max = 36

if __name__ == "__main__":
    print("Please run \"main.py\".")