import requests as r
from dotenv import load_dotenv
import os

def get_token(client_id: int, client_secret: str):

    

    headers = {
        "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
    }

    
    body = {
        "client_id" : client_id, 
        "client_secret" : client_secret,
        "grant_type" : "client_credentials",
        "scope" : "public"
    }
    response = r.post("https://osu.ppy.sh/oauth/token", headers=headers, data=body)  

    return response.json()




res = get_token(56915, "NJEJUf9MtJ8AAqLc8KWKOld88bkiyQnQUhPfEz0R")

print(res)