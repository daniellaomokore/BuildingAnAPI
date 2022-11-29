import requests
import json

""" These all show the functions that carry out the HTTP request methods (POST,PUT,DELETE) to the API """
""" We don't need GET here as GET is automatically run by default whenever we just load the URL endpoints """

# NOTE run each request type separately by commenting out the other to show how the all work on the endpoint correctly
# NOTE POST & PUT requests use request body as they are sending info. GET and DELETE do not use request body
# NOTE you only need the authorisation header if the api is private/secret

# POST REQUEST
new_flight = {
      "from_city": "Stockholm",
      "to_city": "Oslo",
      "days": [1, 7],
      "captain": {'name': 'Ole',
                  'surname': 'Johansson'},
      "duration_min": 30,
      "capacity": 50,
      "booked": 20,
      "available":  30,
      "flight_id": 777
}

# lines 26-30 below shows us creating a HTTP POST request with headers and body
headers = {'content-type': 'application/json',
           'Authorization': '[your API key]'}
result = requests.post(
    'http://127.0.0.1:5000/flights', headers=headers, data=json.dumps(new_flight),
)
print(result)




# PUT REQUEST
updated_flight = {
     "new content": "test",
     "flight_id": 555
}

fid = 555

# lines 45-49 below shows us creating a HTTP PUT request with headers and body
headers = {'content-type': 'application/json',
           'Authorization': '[your API key]'}
result = requests.put(
    'http://127.0.0.1:5000/flights/{}'.format(fid), headers=headers, data=json.dumps(updated_flight)
)
print(result)





# DELETE REQUEST

fid = 555

# lines 61-65 below shows us creating a HTTP DELETE request with headers and body
headers = {'content-type': 'application/json',
           'Authorization': '[your API key]'}
result = requests.delete(
    'http://127.0.0.1:5000/flights/{}'.format(fid), headers=headers
)

print(result)