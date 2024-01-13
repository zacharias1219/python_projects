def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_without_dollar = d.replace("$","")
    return float(d_without_dollar)



def percent_to_float(p):
    p_without_percentage = p.replace("%","")
    p_without_percentage = float(p_without_percentage)/100
    return p_without_percentage


main()