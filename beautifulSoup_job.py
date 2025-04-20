import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_one_page(url):
  print(f"scraping {url}......")
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  jobs_list = soup.find("div", class_="jobs-container").find_all(
      "li", class_="new-listing-container")
  jobs_list_wo_ad = [
      job for job in jobs_list if 'feature--ad' not in job['class']
  ]  #without ad
  jobs = []
  for job in jobs_list_wo_ad:
    title = job.find("h4", class_="new-listing__header__title").text.strip()
    company = job.find("p", class_="new-listing__company-name").text.strip()
    categories = job.find_all("p", class_="new-listing__categories__category")
    # remove 'Featured', 'Top 100', and 'Pro' categories
    categories = [
        cat.text.strip() for cat in categories
        if cat.text.strip() not in ['Featured', 'Top 100', 'Pro']
    ]
    contract_type = categories[0]
    if '$' in categories[1]:
      salary = categories[1]
      region = categories[2:]
    else:
      salary = ''
      region = categories[1:]

    anchors = job.find_all("a")
    url = f"https://weworkremotely.com{anchors[1]['href']}"
    job_dict = {
        'title': title,
        'company': company,
        'contract_type': contract_type,
        'salary': salary,
        'region': region,
        'url': url
    }
    jobs.append(job_dict)
  return pd.DataFrame(jobs)


def scrape_jobs(url):
  #urls like "https://weworkremotely.com/categories/remote-full-time-jobs#job-listings?page=2" doesn't work
  url = url.replace("#job-listings", "")

  # get pagination (if non-existent, return None)
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  pagination = soup.find("div", class_="pagination")

  #if pagination div exists, scrape all the pages and concatenate them
  if pagination:
    result = pd.DataFrame()
    for i in range(len(pagination.find_all("span", class_="page"))):
      res_current_page = scrape_one_page(
          f"{url}?page={i+1}")  #cf. page: query argument
      result = pd.concat([result, res_current_page], ignore_index=True)
    return result

  #if pagination div doesn't exist, scrape only one page
  else:
    return scrape_one_page(url)


fulltime_url = "https://weworkremotely.com/remote-full-time-jobs#job-listings"
design_url = "https://weworkremotely.com/categories/remote-design-jobs#job-listings"

fulltime_jobs = scrape_jobs(fulltime_url)
design_jobs = scrape_jobs(design_url)

print(fulltime_jobs.head(), fulltime_jobs.shape)
print(design_jobs.head(), design_jobs.shape)
