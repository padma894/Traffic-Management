import time
import random

class TrafficLight:
    def __init__(self, name):
        self.name = name
        self.state = "RED"
        self.waiting_vehicles = random.randint(5, 20)  # Simulate traffic count

    def change_state(self, new_state):
        self.state = new_state
        print(f"{self.name} light changed to {self.state}")

def control_traffic(lights, cycle_time=10):
    while True:
        max_traffic_light = max(lights, key=lambda light: light.waiting_vehicles)
        for light in lights:
            if light == max_traffic_light:
                light.change_state("GREEN")
                time.sleep(cycle_time)
                light.waiting_vehicles = random.randint(5, 20)  # Update traffic count
                light.change_state("RED")
            else:
                light.change_state("RED")
        print("\nUpdated traffic counts:")
        for light in lights:
            print(f"{light.name}: {light.waiting_vehicles} vehicles waiting")

# Initialize traffic lights
intersection_lights = [
    TrafficLight("North-South"),
    TrafficLight("East-West"),
    TrafficLight("North-East"),
    TrafficLight("South-West"),
]

# Run the system
try:
    control_traffic(intersection_lights)
except KeyboardInterrupt:
    print("Traffic management system stopped.")