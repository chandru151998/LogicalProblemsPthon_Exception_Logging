import logging


def leap_year(year):
    """
    leap_year function checks whether given year is leap year or not
    :param year: contains year value to be checked for leap year
    :return: none
    """
    try:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")

    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    year1 = int(input("Enter a year: "))
    leap_year(year1)
