def search_flight(fid, flights):
    # flights is a list of dictionaries in the flight_data file
    # within each dictionary, there is a key flights_id
    for entry in flights:
        # each entry will be a dictionary
        if entry['flight_id'] == fid:
            return entry
    return None

def get_index(fid, flights):
    for i, flight in enumerate(flights):
        if flight['flight_id'] == fid:
            return i
    return -1

    