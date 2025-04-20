from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import csv


class SiteScriper():
    def __init__(self, keyword):
        print("01. 생성자 호출.")
        self.keyword = keyword

    def __enter__(self):
        print("02. 컨텍스트 진입.")
        self.p = sync_playwright().start()
        self.browser = self.p.chromium.launch(headless=False)
        self.page = self.browser.new_page()

        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("04. 컨텍스트 이탈.")
        self.browser.close()
        self.p.stop()

        if exc_type is not None:
            print(f"예외 발생: {exc_type}, {exc_value}")


    def scraping(self):
        url = f"https://www.wanted.co.kr/search?query={self.keyword}&tab=position"
        self.page.goto(url)
        time.sleep(10)

        for i in range(6):
            time.sleep(3)
            self.page.keyboard.down("End")

        content = self.page.content()
        soup = BeautifulSoup(content, "html.parser")
        jobs = soup.find_all("div", class_="JobCard_container__FqChn")
        jobs_db = []

        for job in jobs:
            title = job.find("strong", class_="JobCard_title__ddkwM").text
            link = f"https://www.wanted.co.kr{job.find('a')['href']}"
            company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
            location = job.find("span", class_="JobCard_location__2EOr5").text
            reword = job.find("span", class_="JobCard_reward__sdyHn").text

            job = {
                "title": title,
                "link": link,
                "company_name": company_name,
                "location": location,
                "reword": reword
            }
            jobs_db.append(job) 

        file = open(f"{self.keyword}.csv", mode="w", newline="", encoding="utf-8")
        writer = csv.writer(file)
        writer.writerow(["title", "link", "company_name", "location", "reword"])
        for job in jobs_db:
            writer.writerow(list(job.values()))

        file.close()

with SiteScriper("python") as s:
    s.scraping()
    print("03. 컨텍스트 수행.")