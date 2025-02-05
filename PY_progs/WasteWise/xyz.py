import json

import requests


def get_truck_route(start_lat, start_lng, end_lat, end_lng):
    """
    Calculates a truck route between two points in Delhi using Graphhopper API.

    Args:
      start_lat: Latitude of the starting point.
      start_lng: Longitude of the starting point. m
      end_lat: Latitude of the ending point.
      end_lng: Longitude of the ending point.

    Returns:
      A dictionary containing the route information, including distance and duration.
    """

    base_url = "https://graphhopper.com/api/1/routes"
    params = {
        "point": [f"{start_lat},{start_lng}", f"{end_lat},{end_lng}"],
        "vehicle": "truck",
        "locale": "de",  # For German language (adjust if needed)
        "key": your_api_key,  # Replace with your Graphhopper API key
    }

    response = requests.get(base_url, params=params)
    data = json.loads(response.content)

    # Extract route information
    route_path = data["paths"][0]["points"]
    distance = data["paths"][0]["distance"]
    duration = data["paths"][0]["time"]

    return {"route_path": route_path, "distance": distance, "duration": duration}


# Example usage:
start_lat, start_lng = 28.6139, 77.2090  # Delhi, India
end_lat, end_lng = 28.5401, 77.2880  # Noida, India

route_info = get_truck_route(start_lat, start_lng, end_lat, end_lng)
print(route_info)
