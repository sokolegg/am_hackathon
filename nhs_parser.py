import os
import requests
import regex as re
import time

from multiprocessing import Pool

html_list = "https://www.mayoclinic.org/diseases-conditions/index?letter="
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dir = "data/mayo/"


def parse_page(page):
    try:
        url = page
        response = requests.get(url, timeout=60)
        with open(f"{dir}{page.split('/')[4]}.html", "w") as f:
            f.write(response.text)
        print(f"Saved {page}.html")
        time.sleep(3)

        if "You don't have permission to access" in response.text:
            print(f"Error: You don't have permission to access {page}")
            raise Exception("You don't have permission to access")

    except Exception as e:
        print(f"Error: {e}")


def check_html_contains(html_path, s: str):
    with open(html_list, "r") as f:
        html = f.read()
        return s in html

def parse_all_pages():
    # open html file and look for every link using pattern href="https://www.mayoclinic.org/diseases-conditions/{page}/symptoms-causes/{code}"
    # page can be with numbers and letters and / !
    # save it as html file to mayo/{page}.html
    # do it in multiple threads and ignore print errors

    # open mayo html age and find all links
    for letter in letters:
        html = f"{html_list}{letter}"
        response = requests.get(html)

        html = response.text
        links = re.findall(r"https://www.mayoclinic.org/diseases-conditions/[\w\d/-]+/symptoms-causes/[\w\d/-]+", html)
        links = list(set(links))
        print(len(links))
        print(links)

        # check html if it ocntains "You don't have permission to access"
        # if yes parse again

        # new_links = []
        # for link in links:
        #     if check_html_contains(f"{dir}{link}.html", "You don't have permission to access"):
        #         new_links.append(link)

        # links = new_links
        # print(new_links)

        with Pool(3) as p:
            p.map(parse_page, links)


if __name__ == "__main__":
    parse_all_pages()
