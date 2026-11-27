# Defining Variable for Indian System

train_name = "Rajdhani Expresss"
train_number = 12301
ticket_price = 2450.50
is_ac_available = True
seat_numbers = [1 ,2 ,3 ,4, 5]

# Showing the Details using print Function

# print("Train Name: ",train_name)
# print("Train Number: ",train_number)
# print("Ticket Price: ",ticket_price)
# print("AC Availability: ",is_ac_available)
# print("Seat Numbers: ",seat_numbers)

# Show The data type of the variables using type function

print("The data type of train_name: ",type(train_name))
print("The data type of train_number: ",type(train_number))
print("the data type of ticket price: ",type(ticket_price))
print("the data typr of is_ac_available: ",type(is_ac_available))
print("the data type of seat_numbers: ",type(seat_numbers))

  # Getting passenger information
print("=== Indian railway Booking system ===")
passenger_name = input("Enter passenger name: ")
age = int(input("Enter age: "))
destination = input("Enter destination: ")

# Display booking confirmation
print("/n=== Booking Details === ")
print(f"Passenger: {passenger_name}")
print(f"Age: {age}")
print(f"Destination: {destination}")
print(f"Booking Confirmed!") 

#Arthimetic opratiors

base_price = 1500
service_charge = 100
total_price = base_price + service_charge

print(f"Base Price: ₹{base_price}")
print(f"Service charge: ₹{service_charge}")
print(f"Total price: ₹{total_price}")

#Comparison operators
passenger_age = 25
senior_citizen_age = 60
is_senior = passenger_age >= senior_citizen_age

print(f"/nIs passenger senior citizen? {is_senior}")





