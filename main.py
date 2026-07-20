from datetime import datetime
from distutils.command.config import config

import requests
import configparser

def call_get_call(url):
    url="https://jsonplaceholder.typicode.com/users"
    print(f"Calling API..\n"
          f"Method:GET\n"
    f"URL:{url}")

    response= requests.get(url)


    assert response.status_code == 200,"API failed"
    print("API Executed successfully and status code is 200")
    tot_time= response.elapsed.total_seconds()
    print(f"Total_response_time= {tot_time:.3f}")
    print("\n" + "* " * 30)
    for key,value in response.headers.items():
        print(f"{key}: {value}")
    print("\n" + "* " * 30)

    for user in response.json():
        print(user)

    print("Application completed")

config= configparser.ConfigParser()
config.read("config.ini")
base_url=config["API"]["base_url"]
users_url=base_url+"/users"
posts_url=base_url+"/posts"
comments_url=base_url+"/comments"
albums_url=base_url+"/albums"

call_get_call(users_url)
call_get_call(posts_url)
call_get_call(comments_url)
call_get_call(albums_url)


