def smart_traffic_light(time,traffic):
    hour = int(time[:2])
    rush_hour = ( 7 <= hour < 9 ) or (17 <=hour < 19 )
    if rush_hour :
        if traffic == "heavy":
            print("Green light duration: 2 minutes")
        else:
            print("Green light duration: 1 minute")
    else:
        if traffic == "heavy":
            print("Green light duration: 1.5 minutes")
        else:
            print("Green light duration: 45 seconds")

print("Welcome to Smart Traffic Ligths System.")
time = input("Please enter current Time (in 24-hour format):")
traffic = input("Please enter current Traffic Conditions, type heavy for heavy traffic conditions (any other input will give default outputs): ")
smart_traffic_light(time, traffic)