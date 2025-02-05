def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# Test cases
def test_is_leap_year_with_multiple_of_400():
    assert is_leap_year(2400) == True


def test_is_leap_year_with_multiple_of_100_but_not_400():
    assert is_leap_year(1900) == False


def test_is_leap_year_with_multiple_of_4_but_not_100():
    assert is_leap_year(2000) == True


def test_is_leap_year_with_multiple_of_4_but_not_100_non_leap():
    assert is_leap_year(1996) == True


def test_is_leap_year_with_not_multiple_of_4():
    assert is_leap_year(1997) == False


# Run tests
test_is_leap_year_with_multiple_of_400()
test_is_leap_year_with_multiple_of_100_but_not_400()
test_is_leap_year_with_multiple_of_4_but_not_100()
test_is_leap_year_with_multiple_of_4_but_not_100_non_leap()
test_is_leap_year_with_not_multiple_of_4()
