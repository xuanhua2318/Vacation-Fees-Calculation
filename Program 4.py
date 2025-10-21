

hotel_prices = {
    "Florida": 70.00,
    "Texas": 60.00,
    "Cancun": 100.00,
    "Bahamas": 195.00,
}

air_fares = {
    "Florida": 175.55,
    "Texas": 225.98,
    "Cancun": 474.89,
    "Bahamas": 355.98,
}

stay_discount_rate = 0.25
early_discount_5_to_6_rate = 0.1
early_discount_7_to_9_rate = 0.15
early_discount_10_to_more_rate = 0.25

destination = input("Enter Destination: Florida, Texas, Cancun or Bahamas: ")
stay_days = int(input("Enter the number of days you are staying: "))
weeks_before = int(input("Enter the number of weeks before your trip: "))

hotel_cost = hotel_prices[destination] * stay_days
air_fares_cost = air_fares[destination]
stayDiscount = 0.00
if (stay_days >= 7):
    stayDiscount = hotel_cost * stay_discount_rate

earlyDiscount = 0.00
if (5 <= weeks_before <= 6):
    earlyDiscount = air_fares_cost * early_discount_5_to_6_rate
elif (7 <= weeks_before <= 9):
    earlyDiscount = air_fares_cost * early_discount_7_to_9_rate
elif (weeks_before >= 10):
    earlyDiscount = air_fares_cost * early_discount_10_to_more_rate

final_cost = hotel_cost + air_fares_cost - stayDiscount - earlyDiscount

print ("\n")
print ("-"*40)
print ("BG Vacation:")
print ("-"*40)
print (f"{'Destination':<15}:{destination:>10}")
print (f"{'Days Stayed':<15}:{stay_days:>10}")
print (f"{'Weeks Before':<15}:{weeks_before:>10}")
print ("-"*40)
print (f"{'Hotel Cost':<15}:{'$':>9}  {hotel_cost:>6.2f}")
print (f"{'Air Fare':<15}:{'$':>9}  {air_fares_cost:>6.2f}")
print (f"{'Stay Discount':<15}:{'$':>9}  {stayDiscount:>6.2f}")
print (f"{'Early Discount':<15}:{'$':>9}  {earlyDiscount:>6.2f}")
print ("-"*40)
print (f"{'Final Cost':<15}:{'$':>9}  {final_cost:>6.2f}")