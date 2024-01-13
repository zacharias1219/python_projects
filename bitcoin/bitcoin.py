import requests as r
import sys as s


def main():
    if len(s.argv) == 2:
        try:
            value = float(s.argv[1])
            print(bitcoin_rate(value))
        except:
            print("Command-line argument is not a number")
            s.exit(1)

    else:
        print("Missing command-line argument")
        s.exit(1)


def bitcoin_rate(value):
    try:
        ans = r.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        ans = ans.json()
        bitcoin = ans["bpi"]["USD"]["rate"].replace(",", "")
        total = float(bitcoin) * value
        return f"${total:,.4f}"

    except r.RequestException:
        print("RequestException")
        s.exit(1)


if __name__ == "__main__":
    main()
