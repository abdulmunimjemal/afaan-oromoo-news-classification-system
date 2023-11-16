"""
FBC Scraper Class

This module contains the FBCScraper class, which is degined to scrape news data
from Fana Broadcasting Corporation's website for a specific category.

Usage:
    1. Instantiate the FBCScraper with the base URL and category, max_pages(optional)
    2. Run the scraper using the run_scrapper() method
    
Dependencies:
    1. BeautifulSoup
    2. requests
    3. concurrent.futures # built in
    4. csv

Note:
    Mkae sure to customize the cleaner string in the run_scrapper() for each category.
    
Author:
    Abdulmunim Jundurahman Jemal
    abdulmunimjemal@gmail.com
    github.com/abdulmunimjemal

Date:
    16 Nov 2023
"""


import requests
from bs4 import BeautifulSoup
import re
import concurrent.futures
import csv
import os
import logging

# Logging
if not os.path.exists('logs'):
    os.makedirs('logs')
log_file_path = os.path.join('logs', 'fbc_scrapper.log')
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt='%Y-%m-%d %H:%M:%D',
    handlers=[
        logging.FileHandler(log_file_path, mode='a')
    ]
)


class FBCScraper:
    def __init__(self, base_url, category, max_pages=None):
        self.base_url = base_url
        self.category = category
        self.pages = self.get_pages(max_pages)

    def get_pages(self, max_pages):
        pages = [self.base_url]

        page = requests.get(self.base_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        if max_pages is None:
            page_numbers = soup.find_all("a", class_="page-numbers")
            max_pages = page_numbers[-2].text if page_numbers and len(
                page_numbers) > 1 else "226"
        max_pages = str(max_pages) if str(max_pages).isdigit() else "226"

        for i in range(2, int(max_pages)+1):
            pages.append(f"{self.base_url}page/{i}/")

        return pages

    def get_all_links(self, page):
        soup = BeautifulSoup(requests.get(page).content, 'html.parser')
        links = [t.get('href') for t in soup.find_all('a', class_='post-url')]
        return links

    def clean(self, content: BeautifulSoup):
        patterns = [
            r"Finfinnee.*\(FBC\)",
            r"–"
        ]
        cleaned_content = content.text.strip().replace("’", "h").replace("\n", " ")
        for pattern in patterns:
            cleaned_content = re.sub(pattern, "", cleaned_content)
        return cleaned_content

    def process_page(self, page_link):
        result = [""] * 5
        try:
            page = requests.get(page_link)

            if page.status_code != 200:
                print(f"Error {page.status_code} accessing: {page_link}")
                return result

            soup = BeautifulSoup(page.content, "html.parser")
            content = soup.find(
                "div", class_="entry-content clearfix single-post-content")

            title = soup.find("h1", class_="single-post-title")
            date = soup.find("time", class_="post-published updated")
            date = date.get("datetime") if date else ""

            if not content or not title or not date:
                print(f"Error processing: {page_link}")
                return result

            result[0] = self.clean(title)
            result[1] = self.clean(content)
            result[2] = self.category
            result[3] = date.split("T")[0]
            result[4] = page_link
            logging.info(f"Processed page: {page_link}")
            return result
        except Exception as e:
            logging.exception(f"Error processing page: {page_link}")
            if isinstance(e, KeyboardInterrupt):  # Print critical errors on the screen
                print(f"Critical Error: {str(e)}")
            return result

    def run_scraper(self):
        headers = ["headline", "content", "category", "date", "link"]
        links = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.get_all_links, page)
                       for page in self.pages]
            for future in concurrent.futures.as_completed(futures):
                links += future.result()
            print("Done: Get all Links for: ", self.category)

        links = list(set(links))
        results = []

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.process_page, link)
                       for link in links]
            for future in concurrent.futures.as_completed(futures):
                results.append(future.result())
            print("Done: Scrapping contents for: ", self.category)

        # Export results to tsv file
        file_path = os.path.join("data", f"{self.category}.tsv")

        if os.path.exists(file_path):
            existing_headers = []
            with open(file_path, "r", encoding="UTF-8") as existing_file:
                existing_headers = existing_file.readline().strip().split("\t")

            if existing_headers == headers:
                # Append to the existing file
                with open(file_path, "a", encoding="UTF-8", newline="") as f:
                    writer = csv.writer(f, delimiter="\t")
                    writer.writerows(results)
                print(f"Results appended to {file_path}")
            else:
                # Headers don't match, prompt for action
                action = input(
                    "File with different headers exists. Enter 'r' to rewrite, 'n' for a new name, or 'c' to cancel: ")

                if action.lower() == 'r':
                    with open(file_path, "w", encoding="UTF-8", newline="") as f:
                        writer = csv.writer(f, delimiter="\t")
                        writer.writerow(headers)
                        writer.writerows(results)
                    print(f"Results rewritten to {file_path}")
                elif action.lower() == 'n':
                    new_file_name = input(
                        "Enter a new file name (without extension): ")
                    new_file_path = os.path.join(
                        "data", f"{new_file_name}.tsv")
                    with open(new_file_path, "w", encoding="UTF-8", newline="") as f:
                        writer = csv.writer(f, delimiter="\t")
                        writer.writerow(headers)
                        writer.writerows(results)
                    print(f"Results saved to {new_file_path}")
                else:
                    print("Operation canceled.")
        else:
            # File doesn't exist, create a new one
            with open(file_path, "w", encoding="UTF-8", newline="") as f:
                writer = csv.writer(f, delimiter="\t")
                writer.writerow(headers)
                writer.writerows(results)
            print(f"Results saved to {file_path}")


# Running The Scrapper
sources = {
    'teeknooloojii': ['https://www.fanabc.com/afaanoromoo/category/technology/', 38],
    'fayyaa': ['https://www.fanabc.com/afaanoromoo/category/health/', 81],
    'biiznasii': ['https://www.fanabc.com/afaanoromoo/category/business/', 113],
    'idil_addunyaa': ['https://www.fanabc.com/afaanoromoo/category/worldnews/', 169],
    'ispoortii': ['https://www.fanabc.com/afaanoromoo/category/sport/', None],
    'oduu_biyya_keessaa': ['https://www.fanabc.com/afaanoromoo/category/localnews/', 2158],
}

for category, (base_link, max_pages) in sources.items():
    scraper = FBCScraper(base_link, category, max_pages)
    scraper.run_scraper()
    print("Done Scrapping: ", category)
