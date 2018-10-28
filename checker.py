import sys
import argparse
import requests

from bs4 import BeautifulSoup

URL = "https://hacktoberfestchecker.herokuapp.com/?username="


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", required=True, type=str)
    args = parser.parse_args()

    verify_pull_requests(URL + args.username)


def verify_pull_requests(url):
    request = requests.get(url)

    soup = BeautifulSoup(request.text, "lxml")

    span = soup.find(
        "span", attrs={"class": "block rounded text-5xl font-medium white w-64"}
    )
    current, needed = map(int, map(str.strip, span.text.split("/")))
    print("Current Pull Requests submitted: %d" % current)
    print("Minimum Pull Requests needed: %d" % needed)

    if current >= needed:
        print("You have enough Pull Requests!")
    else:
        print("You have %d Pull Requests to go!" % (needed - current))


if __name__ == "__main__":
    main()
