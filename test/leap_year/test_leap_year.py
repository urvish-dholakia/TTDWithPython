from src.leap_year.leap_year import leap_year


def test_leap_year():
    assert leap_year("1997") == "N"
    assert leap_year("1996") == "Y"
    assert leap_year("1600") == "Y"
    assert leap_year("1800") == "N"
