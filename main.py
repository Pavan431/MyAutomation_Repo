from datetime import datetime

import requests as rq

print("Application started")
response= rq.get("https://jsonplaceholder.typicode.com/users")


assert response.status_code == 200,"API failed"
tot_time= response.elapsed.total_seconds()
print("Total time: ", tot_time)
for key,value in response.headers.items():
    print(f"{key}: {value}")

print(response.status_code)
print(response.json())

print("Application completed")

