# BLUEPRINT | DONT EDIT

from requests import get

movie_ids = [
    238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430
]

# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:
movie_url = "https://nomad-movies.nomadcoders.workers.dev/movies/"
for movie_id in movie_ids:
    response = get( f"{movie_url}{movie_id}")
    if response.status_code == 200:
        data = response.json()
        print("----------------------------")
        print("TITLE : ", data.get("title"))
        print("OverView : ", data.get("overview"))
        print("Vote Average : ", data.get("vote_average")) 

# /YOUR CODE