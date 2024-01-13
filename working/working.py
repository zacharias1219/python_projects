import re as r


def main():
    hours = input("Hours:")
    converted_hours = convert(hours)
    print(converted_hours)


def convert(hours):
    check_time = r.search(
        r"^(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM) to (0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)$",
        hours,
    )
    if check_time:
        if int(check_time.group(1)) > 12 or int(check_time.group(4)) > 12:
            raise ValueError
        initial_time = standard_time(
            check_time.group(1), check_time.group(2), check_time.group(3)
        )
        final_time = standard_time(
            check_time.group(4), check_time.group(5), check_time.group(6)
        )
        return f"{initial_time} to {final_time}"
    else:
        raise ValueError


def standard_time(h, m, ampm):
    if ampm == "AM":
        if h == "12":
            hour = "00"
        else:
            hour = f"{int(h):02}"
    else:
        if h == "12":
            hour = "12"
        else:
            hour = f"{int(h)+12}"
    if m == None:
        minute = "00"
    else:
        minute = f"{int(m):02}"
    return f"{hour}:{minute}"


if __name__ == "__main__":
    main()
