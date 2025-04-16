import requests

websites = (
	"google.com", "airbnb.com","twitter.com","facebook.com","tiktok.com"
)
results = {
}

for website in websites: 
	if not website.startswith("https://"):
		website=f"https://{website}"
	response = requests.get(website) 
	if response.status_code == 200:
		results[website] = "OK"
	else:
		results[website] = "FAILED"

print(results) 