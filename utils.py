<<<<<<< HEAD
import requests

def get_token(code:str, CLIENT_ID = "", CLIENT_SECRET = ""):
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': "http://127.0.0.1:5000/callback"
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    resp = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
    resp.raise_for_status()
    return resp.json()['access_token']


def get_user_name(token: str):
    resp = requests.get("https://discord.com/api/v10/users/@me", headers={"Authorization": f"Bearer {token}"})
    resp.raise_for_status()
    return resp.json()

def get_user_guilds(token: str):
    resp = requests.get("https://discord.com/api/v10/users/@me/guilds", headers={"Authorization": f"Bearer {token}"})
    resp.raise_for_status()
    return resp.json()

def get_bot_guilds():
    token = ""
    resp = requests.get("https://discord.com/api/v10/users/@me/guilds", headers={"Authorization": f"Bot {token}"})
    resp.raise_for_status()
    return resp.json()

def get_mutual_guilds(user_guilds: list, bot_guilds: list):
   return [guild for guild in user_guilds if guild['id'] in map(lambda i: i['id'], bot_guilds) and (int(guild['permissions']) & 0x20) == 0x20]

def get_guild_data(guild_id: int):
    token = ""
    resp = requests.get(f"https://discord.com/api/v10/guilds/{guild_id}", headers={"Authorization": f"Bot {token}"})  
    try:
        resp.raise_for_status()
        return resp.json()
    
    except requests.exceptions.HTTPError:
        return None

=======
import requests

def get_token(code:str, CLIENT_ID = "", CLIENT_SECRET = ""):
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': "http://127.0.0.1:5000/callback"
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    resp = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
    resp.raise_for_status()
    return resp.json()['access_token']


def get_user_name(token: str):
    resp = requests.get("https://discord.com/api/v10/users/@me", headers={"Authorization": f"Bearer {token}"})
    resp.raise_for_status()
    return resp.json()

def get_user_guilds(token: str):
    resp = requests.get("https://discord.com/api/v10/users/@me/guilds", headers={"Authorization": f"Bearer {token}"})
    resp.raise_for_status()
    return resp.json()

def get_bot_guilds():
    token = ""
    resp = requests.get("https://discord.com/api/v10/users/@me/guilds", headers={"Authorization": f"Bot {token}"})
    resp.raise_for_status()
    return resp.json()

def get_mutual_guilds(user_guilds: list, bot_guilds: list):
   return [guild for guild in user_guilds if guild['id'] in map(lambda i: i['id'], bot_guilds) and (int(guild['permissions']) & 0x20) == 0x20]

def get_guild_data(guild_id: int):
    token = ""
    resp = requests.get(f"https://discord.com/api/v10/guilds/{guild_id}", headers={"Authorization": f"Bot {token}"})  
    try:
        resp.raise_for_status()
        return resp.json()
    
    except requests.exceptions.HTTPError:
        return None

>>>>>>> 63d019208465c0991cd6eac36be5ce37fa99bc92
