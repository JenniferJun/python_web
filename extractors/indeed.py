from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

def extract_indeed_jobs(query: str, pages: int = 5, headless: bool = True) -> list[dict]:
    """
    Indeed.com 에서 검색어(query)로 잡을 크롤링하여
    jobs 리스트를 반환합니다.
    """
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=headless)
    page = browser.new_page()
    page.goto(f"https://www.indeed.com/jobs?q={query}")
    time.sleep(5)

    # End 키로 페이지 스크롤 (무한 스크롤 형태 처리)
    for _ in range(pages):
        page.keyboard.press("End")
        time.sleep(3)

    soup = BeautifulSoup(page.content(), "html.parser")
    cards = soup.find_all("div", class_="job_seen_beacon")

    jobs = []
    for card in cards:
        link_tag = card.find("a", href=True)
        if not link_tag:
            continue
        link = "https://www.indeed.com" + link_tag["href"]
        title = card.find("h2", class_="jobTitle").get_text(strip=True)
        company = card.find("span", class_="companyName").get_text(strip=True)
        location = card.find("div", class_="companyLocation").get_text(strip=True)
        jobs.append({
            "title": title,
            "company_name": company,
            "location": location,
            "link": link,
        })

    browser.close()
    p.stop()
    return jobs
