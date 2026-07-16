from datetime import datetime

import requests as rq

print("Application started")

start_time = datetime.now()

response= rq.get("https://jsonplaceholder.typicode.com/users")
end_time = datetime.now()

if response.status_code == 200:
    print("Success")
else::
    raise Exception("API failed")
response_time = (end_time - start_time).total_seconds()
print(f"Time taken: {response_time} seconds")
#print(response.json())
print(response.headers)
print(response.status_code)
print(response.text)

