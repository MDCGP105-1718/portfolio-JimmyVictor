def hotel_cost(nights):
    night = 70

def plane_ticket_cost (city, seat_class):

#City condition
    if city == "New York":
        ticket_cost = 2000
    elif city == "Auckland":
        ticket_cost = 790
    elif city == "Venice":
        ticket_cost = 154
    elif city == "Glasgow":
        ticket_cost = 65
    else "We do not have this destination."

#Seat condition
    if seat_class = "Economy"
        multiplier = 1.0
    if seat_class = "Premium economy"
        multiplier = 1.3
    if seat_class = "Business"
        multiplier = 1.6
    if seat_class = "First Class"
        multiplier = 1.9

#Rental car cost
def rental_car_cost(days):
    daily_cost = 30
    t_cost = days * daily_cost
    if days >= 7:
        t_cost -= 50
    elif days > 3:
        t_cost -= 30
    return(t_cost)

#Total costs
def total_cost (city,days)
    night = days - 1
    cost_all += hotel_cost(nights)
    city = input("Choose your city: ")
    seat_class = input("Choose your seat class: ")
    cost_all += plane_tichet_cost(city, seat_class)
    cost_all += rental_car_cost(days)
