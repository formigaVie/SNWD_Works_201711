class carinfo(object):
    def __init__(self, brand, model, km, servicedate):
        self.brand = brand
        self.model = model
        self.km = km
        self.servicedate = servicedate

    def get_full_car(self):
        return self.brand + " " + self.model

def list_all_cars(cars):
    for index, car in enumerate(cars):
        print "ID: " + str(index)  # index is an order number of the contact object in the contacts list
        print car.brand
        print car.model
        print car.km
        print car.servicedate
        print ""  # empty line

    if not cars:
        print "You don't have any contacts in your contact list."

def add_new_cars(cars):
    brand = raw_input("Please enter the car brand: ")
    model = raw_input("Please enter the car model: ")
    km = raw_input("Please enter the km: ")
    servicedate = raw_input("Please enter service date: ")

    new = carinfo(brand=brand, model=model, km=km, servicedate=servicedate)
    cars.append(new)

    print ""  # empty line
    print new.get_full_car() + " was successfully added to your car list."


def edit_cars(cars):
    print "Select the number of the car you'd like to edit:"

    for index, car in enumerate(cars):
        print str(index) + ") " + car.get_full_car()

    print ""  # empty line
    selected_id = raw_input("What car would you like to edit? (enter ID number): ")
    selected_cars = cars[int(selected_id)]

    new_km = raw_input("Please enter a new km for {}: " .format(selected_cars.get_full_car()))
    selected_cars.km = new_km
    print ""  # empty line
    print "Km {} updated to {}." .format(selected_cars.km,selected_cars.get_full_car())

    new_sd = raw_input("Please enter a new servicedate for {}: " .format(selected_cars.get_full_car()))
    selected_cars.servicedate = new_sd
    print ""  # empty line
    print "Servicedate {} updated to {}." .format(selected_cars.servicedate,selected_cars.get_full_car())

def main():
    print "Welcome to the carlist"

    # let's add some contacts in our contact list so it's not empty
    vwt4 = carinfo(brand="Volkswagen",model="T4",km="270.000",servicedate="01.04.2017")
    vwt5 = carinfo(brand="Volkswagen",model="T5",km="130.000",servicedate="01.07.2017")
    marcopolo = carinfo(brand="Mercedes",model="Marco Polo",km="75.000",servicedate="01.09.2017")
    cars = [vwt4,vwt5,marcopolo]

    while True:
        print ""  # empty line
        print "Please choose one of these options:"
        print "a) See all your contacts"
        print "b) Add a new contact"
        print "c) Edit a contact"
        print "e) Quit the program."
        print ""  # empty line

        selection = raw_input("Enter your selection (a, b, c or e): ")
        print ""  # empty line

        if selection.lower() == "a":
            list_all_cars(cars)
        elif selection.lower() == "b":
            add_new_cars(cars)
        elif selection.lower() == "c":
            edit_cars(cars)
        elif selection.lower() == "e":
            print "Thank you for using Car List. Goodbye!"
            break
        else:
            print "Sorry, I didn't understand your selection. Please try again."
            continue

if __name__ == "__main__":  # this means that if somebody ran this Python file, execute only the code below
    main()