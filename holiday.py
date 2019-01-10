def hotel_price(pricePerNight, numOfNights):
    price = 6.5*numOfNights
    return(price)

xNights = int(raw_input("Enter the number of nights you wish stay:"))
hotelCost = hotel_price(6.5, xNights)
  
print("The total price of the hotel will be: £" + str(hotelCost))
  
  
  
  
def plane_price(priceOfFlight):
    if priceOfFlight == 'London':
        price = 120
        return(price)
    elif priceOfFlight == 'Paris':
        price = 150
        return (price)
    elif priceOfFlight == 'Rome':
        price = 200
        return(price)
    elif priceOfFlight == 'New York':
        price = 450
        return (price)

xDestination = raw_input("Enter your choice of destination:") 
planeCost = plane_price(str(xDestination))
  
print("The total price of this flight will be: £" + str(planeCost))
  
  
  
  
def car_rental_price(rentPriceOfCar, numOfDaysCarRent):
    price = 10 * numOfDaysCarRent
    return(price)

xDaysOfRent = int(raw_input("Enter the number of days you wish to rent the car:"))  
carRental = car_rental_price(10, xDaysOfRent)
print("The total price of the car rent will be: £" + str(carRental))
  
  
  
  
def holiday_price(hotelCost, planeCost, carRental):
    price = hotelCost + planeCost + carRental
    return(price)
  
holidayCost = holiday_price(int(hotelCost), int(planeCost), int(carRental))
print("The total price of this holiday will be: £" + str(holidayCost))
