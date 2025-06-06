# Bus class to represent each bus
class Bus:
    def __init__(self, bus_id, bus_type, route):
        self.bus_id = bus_id
        self.bus_type = bus_type  # 'AC' or 'Non-AC'
        self.route = route
        self.seats_available = 40  # Assume each bus has 40 seats

    def book_seat(self):
        if self.seats_available > 0:
            self.seats_available -= 1
            return True
        else:
            return False

class Passenger:
    def __init__(self, name):
        self.name = name


class TravelCompany:
    def __init__(self):
        self.buses = []
        self.routes = ["City A to City B", "City B to City C", "City C to City D"]

    def add_bus(self, bus):
        self.buses.append(bus)

    def show_available_buses(self):
        print("Available Buses:")
        for bus in self.buses:
            print(f"Bus ID: {bus.bus_id}, Type: {bus.bus_type}, Route: {bus.route}, Seats Left: {bus.seats_available}")

    def book_ticket(self, passenger, route, bus_type):
        for bus in self.buses:
            if bus.route == route and bus.bus_type == bus_type and bus.seats_available > 0:
                success = bus.book_seat()
                if success:
                    print(f"Ticket booked successfully for {passenger.name} on Bus {bus.bus_id} ({bus_type}) - {route}")
                    return
        print("Sorry, no available seats for the selected route and bus type.")
