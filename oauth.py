import requests
import os
cs = os.environ.get("cs")
class Oauth:
    client_id = "780835623006240809" # Your Client ID here
    client_secret = f"{cs}" # Your Client Secret here
    redirect_uri = "https://gdm.bothost.repl.co/logged-in"
    scope = "identify%20guilds"
    discord_login_url = "https://discord.com/api/oauth2/authorize?client_id=780835623006240809&permissions=123429059825&redirect_uri=https%3A%2F%2Fgdm.bothost.repl.co%2Flogged-in&response_type=code&scope=identify%20guilds%20bot" # Paste the generated Oauth2 link here
    discord_token_url = "https://discord.com/api/oauth2/token"
    discord_api_url = "https://discord.com/api"
 
    @staticmethod
    def get_access_token(code):
        payload = {
            "client_id": Oauth.client_id,
            "client_secret": Oauth.client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": Oauth.redirect_uri,
            "scope": Oauth.scope
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        access_token = requests.post(url = Oauth.discord_token_url, data = payload, headers=headers).json()
        print(payload)
        return access_token.get("access_token")

    @staticmethod
    def get_user_json(access_token):
        url = f"{Oauth.discord_api_url}/users/@me"
        headers = {"Authorization": f"Bearer {access_token}"}
 
        user_object = requests.get(url = url, headers = headers).json()
        the_thing, the_things_avatar = user_object["id"], user_object["avatar"]
        print(f"https://cdn.discord.com/avatars/{the_thing}/{the_things_avatar}.png?size=256")
        return user_object

