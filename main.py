from datetime import datetime
from distutils.command.config import config

import requests
import configparser

def send_get_request(url):
    print(f"Calling API..\n"
          f"Method:GET\n"
    f"URL:{url}")
    response= requests.get(url)
    assert response.status_code == 200,"API failed"
    print(f"status code : f{response.status_code}")
    print("API Executed successfully")
    response_time= response.elapsed.total_seconds()
    print(f"Total_response_time= {response_time:.3f}")
    print("\n" + "* " * 30)
    for key,value in response.headers.items():
        print(f"{key}: {value}")
    print("\n" + "* " * 30)

    for user in response.json():
        print(user)

    print("Application completed")
    return response.json()

config= configparser.ConfigParser()
config.read("config.ini")
base_url=config["API"]["base_url"]
users_url=base_url+"/users"
posts_url=base_url+"/posts"
comments_url=base_url+"/comments"
albums_url=base_url+"/albums"

send_get_request(users_url)
send_get_request(posts_url)
send_get_request(comments_url)
send_get_request(albums_url)


