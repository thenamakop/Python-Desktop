"""TODO:     
    1 UPI Api 
    2 unique qrcode/sms generation with every iteration
    3 GUI using tkinter.???
    4 Webpapge
    5 Rickroll XD
    6 types of interface: 
                        i) customer : Name , Cash / Card/ Upi , Menu -> Order/Order Selection -> Order Display/
                        graphical quantity selector-> 
                        FIXME: MySql integration(refer to BMS.py)
                        ii) admin
                        iii) tech support
    7 change placeholder menu prices -> Starbucks.?
"""
menu = {
  "Beverages": [
    {"name": "Espresso (single shot)", "price": 35},
    {"name": "Filter Coffee", "price": 30},
    {"name": "Cafe Latte (small)", "price": 55},
    {"name": "Cappuccino (small)", "price": 65},
    {"name": "Iced Coffee", "price": 60},
    {"name": "Cold Brew Coffee", "price": 70, "tip": "Stronger, potentially more economical"},
    {"name": "Tea (hot or iced)", "price": 35}
  ],
  "Food":[ 
    {"name": "Bakery Items (croissants, muffins, cookies)", "price": 35},
    {"name": "Toast with Butter/Jam", "price": 25},
    {"name": "Veg Sandwich", "price": 50},
    {"name": "Egg Sandwich", "price": 60},
    {"name": "Cake Slice", "price": 75},
  ]
}
import tkinter

tkinter._test()
