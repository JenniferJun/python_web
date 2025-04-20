from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import csv

p = sync_playwright().start()
q
browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/")

time.sleep(5)

page.click("button.Aside_searchButton__rajGo")

time.sleep(5)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("crm")

time.sleep(5)

page.keyboard.down("Enter")

time.sleep(5)

page.click("a#search_tab_position")

for x in range(5):
    time.sleep(5)
    page.keyboard.down("End")

time.sleep(5)

content = page.content()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__REty8")

jobs_db = []

for job in jobs :
    link = f"https://www.wanted.co.kr/{job.find('a')['href']}"
    title = job.find("strong", class_="JobCard_title__HBpZf").text
    company_name = job.find("span", class_="JobCard_companyName__N1YrF").text
    reward = job.find("span", class_="JobCard_reward__cNlG5").text
    job = {
    "title":title,
    "company_name":company_name,
    "reward":reward,
    "link":link,
    }
    jobs_db.append(job)


print(jobs_db)

file = open("jobs.csv", "w", encoding="utf-8")
print("csv파일 생성")
writer = csv.writer(file)
writer.writerow(["Title","Company", "Reward", "Link"])

for job in jobs_db:
    print(job)
    writer.writerow(job.values())

browser.close()
p.stop()