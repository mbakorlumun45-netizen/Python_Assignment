velocity = int(input("Enter velocty in m/s: "))

acceleration = int(input("Enter acceleration: "))

runway_length = velocity * 2

velocity = runway_length

runway_length = acceleration * 2

minimum_runway_time_needed = velocity / runway_length

print("The minimum runway length for this airplane is", minimum_runway_time_needed)
