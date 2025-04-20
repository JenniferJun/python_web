from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs, save_jobs_to_csv
from file import save_to_file

keyword = input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr 

save_to_file(keyword, jobs)
 
 