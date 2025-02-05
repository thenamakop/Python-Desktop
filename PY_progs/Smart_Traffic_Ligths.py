'''Question 2: Smart Traffic Light(5M)
(Scenario: You're programming a smart traffic light that changes its operation based on
the time of day and traffic conditions.
Problem: Write a program that decides the traffic light behavior:
● During rush hour (7-9 AM, 5-7 PM), if the traffic is heavy, the light stays green for
2 minutes; otherwise, 1 minute.
● Outside rush hour, if the traffic is heavy, the light stays green for 1.5 minutes;
otherwise, 45 seconds.
Example Input-Output:
● Input: Time = "18:00", Traffic = "heavy"
● Output: "Green light duration: 2 minutes.'''

import time

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