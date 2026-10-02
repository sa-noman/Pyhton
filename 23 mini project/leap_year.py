def is_leap_year(year: int) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


if __name__ == "__main__":
    year = int(input("Year: "))
    print("Leap year" if is_leap_year(year) else "Not a leap year")
