from datetime import datetime

import requests
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

