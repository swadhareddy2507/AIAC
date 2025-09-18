# Function to calculate fares for a list of rides
def calculate_fares(rides):
    base_per_km = 22.0
    surgeMultiplier = 2.0
    fares = []
    for ride in rides:
        time_str = ride.get("time", "")
        km = ride.get("km", 0.0)
        try:
            hours, minutes = map(int, time_str.strip().split(":"))
        except Exception:
            fares.append(None)
            continue
        # Surge applies at or after 18:00
        if hours > 18 or (hours == 18 and minutes >= 0):
            fare = km * base_per_km * surgeMultiplier
        else:
            fare = km * base_per_km
        fares.append(round(fare, 2))
    return fares

if __name__ == "__main__":
    time_str = input("Enter time (HH:MM): ")
    try:
        km = float(input("Enter kilometers: "))
    except ValueError:
        print("Invalid kilometers input.")
        exit(1)
    rides = [{"time": time_str, "km": km}]
    fares = calculate_fares(rides)
    if fares[0] is not None:
        print("Fare:", fares[0])
    else:
        print("Invalid time format entered.")
