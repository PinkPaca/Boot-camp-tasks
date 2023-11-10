city_flight=input("Please enter the city you will be flying to.:")
num_nights=int(input("Please enter the number of nights you will be staying at a hotel.:"))
rental_days=int(input("Please enter the number of days that you will be hiring a car for.:"))


def hotel_cost(num_nights):
    print(f"your total cost for hotel stay is 100*{num_nights}=",str(num_nights*100))
    return num_nights*100

def plane_cost(city_flight):
    if city_flight.lower()=="london":
        print(f"your cost for flight to {city_flight} is 50£")
        return 50
    elif city_flight.lower()=="paris":
        print(f"your cost for flight to {city_flight} is 30£")
        return 30
    elif city_flight.lower()=="madrid":
        print(f"your cost for flight to {city_flight} is 70£")
        return 70
    elif city_flight.lower()=="berlin":
        print(f"your cost for flight to {city_flight} is 80£")
        return 80
    elif city_flight.lower()=="dubai":
        print(f"your cost for flight to {city_flight} is 100£")
        return 100
    else:
        print(f"your cost for flight to {city_flight} is 200£")
        return 200
    

def car_rental(rental_days):
    print(f"your total cost for the car rental is 20*{rental_days}=",str(rental_days*20))
    return rental_days*20

def holiday_cost(num_nights,city_flight,rental_days):
    total_cost= hotel_cost(num_nights)+plane_cost(city_flight)+car_rental(rental_days)
    print(f"Your total cost for the holiday is {total_cost}")

holiday_cost(num_nights,city_flight,rental_days)
