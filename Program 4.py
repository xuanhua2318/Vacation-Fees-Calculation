#  ************************************************
#  CS1010  Program 4
#  Name :  Xuan Hua
#  Due: 11/03/2025
#  Purpose: The program will user to input the destination, numbers of days staying hotel, how many weeks until the vacation happening
#           to calculate the fees
#
#  *************************************************


def main():  # Define the main function to contain all program logic
    
    # Dictionary storing hotel prices per night for each destination
    hotel_prices = {
        "Florida": 70.00,
        "Texas": 60.00,
        "Cancun": 100.00,
        "Bahamas": 195.00,
    }

    # Dictionary storing airfare costs for each destination
    air_fares = {
        "Florida": 175.55,
        "Texas": 225.98,
        "Cancun": 474.89,
        "Bahamas": 355.98,
    }

    # Discount rates (as decimals)
    stay_discount_rate = 0.25               # 25% discount for stays of 7 or more days
    early_discount_5_to_6_rate = 0.1        # 10% discount for booking 5-6 weeks early
    early_discount_7_to_9_rate = 0.15       # 15% discount for booking 7-9 weeks early
    early_discount_10_to_more_rate = 0.25   # 25% discount for booking 10+ weeks early

    # Get user input for trip details
    destination = input("Enter Destination: Florida, Texas, Cancun or Bahamas: ")
    stay_days = int(input("Enter the number of days you are staying: "))
    weeks_before = int(input("Enter the number of weeks before your trip: "))

    # Calculate base costs
    hotel_cost = hotel_prices[destination] * stay_days  # Total hotel cost
    air_fares_cost = air_fares[destination]             # Airfare for chosen destination
    
    # Calculate stay discount (25% off if staying 7 or more days)
    stayDiscount = 0.00  # Initialize stay discount to zero
    if (stay_days >= 7):
        stayDiscount = hotel_cost * stay_discount_rate

    # Calculate early booking discount based on weeks before trip
    earlyDiscount = 0.00            # Initialize early discount to zero
    if (5 <= weeks_before <= 6):    # 5-6 weeks early
        earlyDiscount = air_fares_cost * early_discount_5_to_6_rate
    elif (7 <= weeks_before <= 9):  # 7-9 weeks early
        earlyDiscount = air_fares_cost * early_discount_7_to_9_rate
    elif (weeks_before >= 10):      # 10 or more weeks early
        earlyDiscount = air_fares_cost * early_discount_10_to_more_rate

    # Calculate final total cost after applying all discounts
    final_cost = hotel_cost + air_fares_cost - stayDiscount - earlyDiscount

    # Display formatted receipt
    print("\n")             # Blank line for spacing
    print("-" * 40)         # Top border line
    print("BG Vacation:")   # Title
    print("-" * 40)         # Separator line for each section
    
    # Display trip details
    print(f"{'Destination':<15}{':':<10}{destination}")
    print(f"{'Days Stayed':<15}{':':<10}{stay_days}")
    print(f"{'Weeks Before':<15}{':':<10}{weeks_before}")
    print("-" * 40)         # Separator line for each section
    
    # Display cost
    print(f"{'Hotel Cost':<15}:{'$':>9}  {hotel_cost:>6.2f}")
    print(f"{'Air Fare':<15}:{'$':>9}  {air_fares_cost:>6.2f}")
    print(f"{'Stay Discount':<15}:{'$':>9}  {stayDiscount:>6.2f}")
    print(f"{'Early Discount':<15}:{'$':>9}  {earlyDiscount:>6.2f}")
    print("-" * 40)        # Separator line for each section
    
    # Display final total
    print(f"{'Final Cost':<15}:{'$':>9}  {final_cost:>6.2f}")

    
main()  # Call the main function to execute the program