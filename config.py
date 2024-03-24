import requests

def get_meme():
    url = f"https://meme-api.com/gimme/"
    response = requests.get(url)
    json_to_dict = response.json()
    
    picture = json_to_dict['preview'][-2]
    title = json_to_dict['title']
    name_sub = json_to_dict['subreddit']

    return picture, title, name_sub