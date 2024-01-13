import re as r


def main():
    URL = input("HTML: ")
    searched_url = parse(URL)
    print(searched_url)


def parse(searching):
    if r.search(r"<iframe(.)*><\/iframe>", searching):
        searched_url = r.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", searching)

        if searched_url:
            grouped_url = searched_url.groups()
            return "https://youtu.be/" + grouped_url[3]


if __name__ == "__main__":
    main()
