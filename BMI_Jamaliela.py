######################################################################
# Author: Elaheh Jamali
# Username: Jamalie

# Assignment: A3: All Input is Evil
#
# Purpose: Identify possible points of invalid inputs to code
# Validate user inputs to prevent security and bug flaws
#
######################################################################


import sys


def testit(did_pass):
    """
    Print the result of a unit test.

    This function works correctly--it is verbatim from the textbook, Chapter 6.

    You should reuse this function anytime you are creating a custom test suite

    :param did_pass: Boolean representing if the unit test passed or failed
    :return: None
    """

    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def range_check_testsuite():
    """
    The test suite function utilizes the testit() function,
    and is designed to test the range_check() function (below), returning True
    only when the input is in valid range.

    :return: None
    """
    print("\nRunning range_check_testsuite().")

    # Testing if height is positive
    testit(range_check(-12, 246) == False)
    testit(range_check(60, 125) == True)
    testit(range_check(115, 279) == True)
    testit(range_check(-125, 69) == False)

    # Testing if the weight is positive
    testit(range_check(12, 246) == True)
    testit(range_check(60, -125) == False)
    testit(range_check(115, 245) == True)
    testit(range_check(125, -69) == False)

    print("Run of range_check_testsuite() complete.")


def length_check_testsuite():
    """
    The test suite function utilizes the testit() function,
    and is designed to test the length_check() function (below), returning True
    only when the input is in valid length

    :return: None
    """
    print("\nRunning length_check_testsuite().")

    # Testing if height has more than 1 digit
    testit(length_check(4, 246) == False)
    testit(length_check(60, 125) == True)
    testit(length_check(115, 279) == True)
    testit(length_check(7, 69) == False)

    # Testing if the weight has less than 4 digits
    testit(length_check(12, 246) == True)
    testit(length_check(60, 1245) == False)
    testit(length_check(115, 76) == True)
    testit(length_check(125, 123654) == False)

    print("Run of length_check_testsuite() complete.")


def range_check(h, w):
    """
    Function intended to take two float as input. Returns True if they are positive and false if they are negative

    :param h: the height
    :param w: the weight
    :return: Boolean value representing if the number is positive or negative
    """
    if h > 0 and w > 0:
        return True
    else:
        return False


def length_check(h, w):
    """
    Function intended to take two float as input. Returns True if they are in valid length and false if they are not in valid length

    :param h: the height
    :param w: the weight
    :return: Boolean value representing if the number is positive or negative
    """
    if len(str(round(h))) > 1 and len(str(round(w))) < 4:
        return True
    else:
        return False


def main():
    """
    This main function is intended to test the correctness of the range_check and length_check function
    :return: None
    """
    height = float(input("please input your height in inches: "))
    weight = float(input("Please input your weight in pounds: "))
    if range_check(height, weight) and length_check(height, weight) is True:
        print("Your body mass index is: ", float((weight / (height * height)) * 703))
    else:
        print("your input is not in the valid range or length")
    range_check_testsuite()
    length_check_testsuite()


if __name__ == "__main__":
    main()
