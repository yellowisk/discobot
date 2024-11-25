import requests

def authenticate(client_id, client_secret):
    url = "https://id.twitch.tv/oauth2/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        return None


def get_genre_names(client_id, access_token, genre_ids):
    url = "https://api.igdb.com/v4/genres"
    headers = {
        "Client-ID": client_id,
        "Authorization": f"Bearer {access_token}"
    }
    data = f"fields name; where id = ({', '.join(map(str, genre_ids))});"

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        genres = response.json()
        # Map genre IDs to names
        return {genre["id"]: genre["name"] for genre in genres}
    else:
        print("Request failed:", response.status_code, response.text)
        return {}


def get_all_games(client_id, access_token, batch_size=500):
    url = "https://api.igdb.com/v4/games"
    headers = {
        "Client-ID": client_id,
        "Authorization": f"Bearer {access_token}"
    }
    offset = 0
    all_games = []

    while True:
        data = f"fields name, summary, storyline, rating, genres; limit {batch_size}; offset {offset};"
        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            games = response.json()
            genres = get_genre_names(client_id, access_token, {genre_id for game in games for genre_id in game.get("genres", [])})
            for game in games:
                game["genres"] = [genres.get(genre_id, "Unknown") for genre_id in game.get("genres", [])]
            if not games:
                break
            all_games.extend(games)
            offset += batch_size
        else:
            print("Request failed:", response.status_code, response.text)
            break

    return all_games

def get_games_by_name(client_id, access_token, game_name: str):
    url = "https://api.igdb.com/v4/games"
    headers = {
        "Client-ID": client_id,
        "Authorization": f"Bearer {access_token}"
    }
    data = f'search "{game_name}"; fields name, summary, storyline, rating, genres;'
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        games = response.json()
        genres = get_genre_names(client_id, access_token, {genre_id for game in games for genre_id in game.get("genres", [])})
        for game in games:
            game["genres"] = [genres.get(genre_id, "Unknown") for genre_id in game.get("genres", [])]
        return games
    else:
        print("Request failed:", response.status_code, response.text)
        return []

def get_games_by_genre(client_id, access_token, genre: str):
    url = "https://api.igdb.com/v4/games"
    headers = {
        "Client-ID": client_id,
        "Authorization": f"Bearer {access_token}"
    }
    data = f"fields name, summary, storyline, rating, genres; where genres.name = \"{genre}\";"
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        games = response.json()
        genres = get_genre_names(client_id, access_token, {genre_id for game in games for genre_id in game.get("genres", [])})
        for game in games:
            game["genres"] = [genres.get(genre_id, "Unknown") for genre_id in game.get("genres", [])]
        return games
    else:
        print("Request failed:", response.status_code, response.text)
        return []
    
def get_games_by_rating(client_id, access_token, min_rating: float, max_rating: float, batch_size=500):
    url = "https://api.igdb.com/v4/games"
    headers = {
        "Client-ID": client_id,
        "Authorization": f"Bearer {access_token}"
    }
    offset = 0
    
    data = f"fields name, summary, storyline, rating, genres; where rating >= {min_rating} & rating <= {max_rating}; limit {batch_size}; offset {offset};"
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        games = response.json()
        genres = get_genre_names(client_id, access_token, {genre_id for game in games for genre_id in game.get("genres", [])})
        for game in games:
            game["genres"] = [genres.get(genre_id, "Unknown") for genre_id in game.get("genres", [])]
        return games
    else:
        print("Request failed:", response.status_code, response.text)
        return []