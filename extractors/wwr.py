from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import csv

def extract_wwr_jobs(query: str, pages: int = 5, headless: bool = False) -> list[dict]:
    """
    Wanted.co.kr 에서 검색어(query)로 잡을 크롤링하여
    jobs 리스트를 반환합니다.
    """
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=headless)
    page = browser.new_page()

    page.goto("https://www.wanted.co.kr/")
    time.sleep(5)

    # 검색창 열고
    page.click("button.Aside_searchButton__rajGo")
    time.sleep(2)
    page.get_by_placeholder("검색어를 입력해 주세요.").fill(query)
    time.sleep(1)
    page.keyboard.press("Enter")
    time.sleep(3)
    page.click("a#search_tab_position")
    time.sleep(2)

    # 스크롤을 pages 번 반복
    for _ in range(pages):
        page.keyboard.press("End")
        time.sleep(2)

    soup = BeautifulSoup(page.content(), "html.parser")
    cards = soup.find_all("div", class_="JobCard_container__REty8")

    jobs = []
    for card in cards:
        href = card.find("a")["href"]
        link = f"https://www.wanted.co.kr/{href}"
        title = card.find("strong", class_="JobCard_title__HBpZf").get_text(strip=True)
        company = card.find("span", class_="JobCard_companyName__N1YrF").get_text(strip=True)
        reward = card.find("span", class_="JobCard_reward__cNlG5").get_text(strip=True)
        jobs.append({
            "title": title,
            "company_name": company,
            "reward": reward,
            "link": link,
        })

    browser.close()
    p.stop()
    return jobs

def save_jobs_to_csv(jobs: list[dict], filename: str = "jobs.csv") -> None:
    """
    jobs 리스트를 받아 CSV로 저장합니다.
    """
    if not jobs:
        print("저장할 데이터가 없습니다.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # 헤더
        header = list(jobs[0].keys())
        writer.writerow([h.replace("_", " ").title() for h in header])
        # 본문
        for job in jobs:
            writer.writerow([job.get(k, "") for k in header])

    print(f"{filename} 파일로 저장 완료")
