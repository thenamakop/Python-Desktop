import mapbox

mapbox_client = mapbox.Client(
    access_token="sk.eyJ1IjoidGhlbmFtYWsiLCJhIjoiY20wODFuamZlMDVkZDJrc2IweGhsYnVvaCJ9.xX6_eXF9B7z8tisRdG_j_Q"
)

response = mapbox_client.directions(
    [[start_longitude, start_latitude], [end_longitude, end_latitude]],
    profile="driving",
    steps=True,
)
