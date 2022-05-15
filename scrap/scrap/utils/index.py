from urllib.error import HTTPError
import requests

def get_url(url : str, headers : dict):
    try:
        res = requests.get(url,headers = headers)
    except:
        raise HTTPError(url, 404, "Invalid URL", headers)
    
    return res

