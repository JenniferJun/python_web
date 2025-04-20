from bs4 import BeautifulSoup
import requests

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

jobs = (soup.find("section", class_ = "jobs").find_all("li"))[:-1]

for job in jobs:
    title = job.find("h4", class_="new-listing__header__title").text
    company = job.find("p", class_="new-listing__company-name").text

    # 직접 마지막 카테고리(region) 찾기
    region = job.find_all("p", class_="new-listing__categories__category")[-1].text if job.find_all("p", class_="new-listing__categories__category") else "지역 정보 없음"

    print(f"{title} at {company} in {region}\n")