import requests
from datetime import datetime
from bs4 import BeautifulSoup
import re
import pandas as pd
from tqdm import tqdm, tqdm_pandas
import time

tqdm.pandas()


def get_wayback_url(url, debug=False):

    time.sleep(10)

    cdx_api = "http://web.archive.org/cdx/search/cdx?url="

    full_url = cdx_api + url + "&fl=timestamp,original"

    if debug:
        print(f"Police Website : httm://www.{url}")
        print(f"cdx api call : {full_url}")

    try:
        response = requests.get(full_url)

        rows = response.text.split("\n")[:-1]

        george_floyd_date = datetime.strptime("20200525", "%Y%m%d")

        index_to_pull = -1

        for i, row in enumerate(rows):
            date_being_tested = datetime.strptime(row.split(" ")[0], "%Y%m%d%H%M%S")

            if date_being_tested > george_floyd_date:
                index_to_pull = i - 1
                break

        if index_to_pull == -1:
            if debug:
                print("No webpages older than May 2020")
            return None

        if debug:
            print("Page older than May 2020 Found!")

        if debug:
            print(f"Number of saved pages : {len(rows)}")
            print(f"Page used : {index_to_pull}")

        original_url = rows[index_to_pull].split(" ")[1]

        date_text = rows[index_to_pull].split(" ")[0]

        date = datetime.strptime(date_text, "%Y%m%d%H%M%S")

        if debug:
            print(f"Date selected : {date.strftime('%m/%d/%Y')}")
            print(f"Original URL: {original_url}")

        wayback_url = "https://web.archive.org/web/" + date_text + "/" + original_url

        if debug:

            print(f"Wayback URL : {wayback_url}")

        return wayback_url

    except Exception as e:
        print(f"Error: {e}")
        print(full_url)
        return None


def get_page_text(url, debug=False):

    wayback_url = get_wayback_url(url, debug)

    try:
        response = requests.get(wayback_url, timeout=60)
    except requests.RequestException as e:
        print(f"Error: {e}")

    soup = BeautifulSoup(response.text, features="html.parser")

    page_text = re.sub(r"\s+", r" ", soup.get_text())

    return page_text


urls = pd.read_csv("Unfinished_URLS.csv").dropna()

stripped_urls = [url.split("www.")[1] for url in urls if "www." in url]

urls["wayback_urls"] = urls["0"].progress_apply(get_wayback_url)

urls.to_csv("wayback_urls.csv")
