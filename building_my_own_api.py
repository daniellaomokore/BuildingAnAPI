from flask import Flask, jsonify, request
from flights_data import flights             # import your data and it's dictionary/s
from utils import search_flight, get_index

app = Flask(__name__)

""" GETTING INFORMATION FROM THE API """
""" This can be done directly from the browser """

# GET request - As an API, info is retrieved from the API URL as requested by client/user.

# @app.route() contains the URL the app exists under and it's HTTP method
@app.route('/', methods=['GET'])
def hello():
    return {'hello': 'Universe'}


@app.route('/flights', methods=['GET'])
def get_flights():
    return jsonify(flights)                       # Returns the 'flights' data in a json format to which was extracted from the 'flights_data.py' file



# on line 26, the <> and it's insides indicate that it's an integer and the variable 'id'
# the id number that's put into the URL path below is then sent to the 'get_flight_by_id' parameter etc
@app.route('/flights/<int:id>', methods=['GET'])   #  this specifies that the input should be an integer and that it's assigned as a variable called id
def get_flight_by_id(id):
    flight = search_flight(id, flights)          # This returns the flights list (from the flight_data.py file) from the dictionary that has the same id number
    return jsonify(flight)



""" ADDING NEW FLIGHTS TO THE API """
""" This can't be done directly from the browser, so we need to use a different program """

# POST request - As an API is when we add info the API URL as requested by client/user

@app.route('/flights', methods=['POST'])
def add_flight():
    flight = request.get_json()                     #  We receive the data from the client via this request
    flights.append(flight)                          #  append the users data input into the 'flights' dictionary
                                                    #  appends the JSON that we receive in the request
    return flight



""" UPDATING A FLIGHT """

# PUT request - As an API we update info in API URL as requested by client/user

@app.route('/flights/<int:id>', methods=['PUT'])
def update_flight(id):
    flight_to_update = request.get_json()            #We receive the data from the client via this request
    index = get_index(id, flights)
    flights[index] = flight_to_update
    return jsonify(flights[index])


""" DELETING A FLIGHT """

# DELETE request - As an API we delete info from API URL as requested by client/user

@app.route('/flights/<int:id>', methods=['DELETE'])
def delete_flight(id):
    index = get_index(id, flights)
    deleted = flights.pop(index)
    return jsonify(deleted), 200


if __name__ == '__main__':                     #if this(current file name) is the program that i'm actually running
    app.run(debug=True)                        #then run this

"""

When you import a library into one program, when you run the program it also goes to that file and runs all the code in that file too,
So when use '__name__ == __main__'  it stops the other program running.
'__Main__' is the name of the current program file that phrase is written on, so the whole phrase means that only if the current file can be run.

"""