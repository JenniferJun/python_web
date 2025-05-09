from flask import Flask, render_template, request
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

app = Flask("JobScrapper")

@app.route('/search')
def hello(name=None):
    #print(request.args)
    keyword = request.args.get("keyword")
    indeed = extract_indeed_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobs = indeed + wwr
    return render_template('search.html',keyword=keyword, jobs=jobs)

@app.route("/")
def home(name=None):
    return render_template('home.html', name="Jennifer")

app.run("0.0.0.0")