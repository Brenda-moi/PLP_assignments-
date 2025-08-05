## Satellite classes with encapsulation and inheritance

class Satellite:
    def __init__(self, name, orbit_type, purpose):
        self.name = name                    # Public attribute
        self._orbit_type = orbit_type       # Protected attribute
        self.__purpose = purpose            # Private attribute

    def info(self):
        print("=== Satellite Information ===")
        print(f"Name: {self.name}")
        print(f"Orbit Type: {self._orbit_type}")
        print(f"Purpose: {self.__purpose}")

    # Getter for private attribute
    def get_purpose(self):
        return self.__purpose

    # Setter for private attribute
    def set_purpose(self, new_purpose):
        if isinstance(new_purpose, str) and new_purpose.strip() != "":
            self.__purpose = new_purpose
        else:
            print("❌ Invalid purpose. It must be a non-empty string.")

class CommunicationSatellite(Satellite):
    def __init__(self, name, orbit_type, purpose, frequency_band):
        super().__init__(name, orbit_type, purpose)
        self.frequency_band = frequency_band

    def info(self):
        super().info()
        print(f"Frequency Band: {self.frequency_band}")

class WeatherSatellite(Satellite):
    def __init__(self, name, orbit_type, purpose, sensor_type):
        super().__init__(name, orbit_type, purpose)
        self.sensor_type = sensor_type

    def info(self):
        super().info()
        print(f"Sensor Type: {self.sensor_type}")

#Polymorphism with different satellites transmitting differently

class WeatherSat(Satellite):
    def transmit(self):
        print(f"{self.name}: Transmitting weather data 🌦️")

class SpySat(Satellite):
    def transmit(self):
        print(f"{self.name}: Sending encrypted surveillance footage 🛰️🔒")

class NavigationSat(Satellite):
    def transmit(self):
        print(f"{self.name}: Broadcasting GPS coordinates 📡")

# Polymorphism demonstration function
def send_data(satellite):
    satellite.transmit()

# Example usage
if __name__ == "__main__":
    print("=== Assignment 1: Satellite Info ===")
    sat1 = Satellite("Hubble", "LEO", "Space Observation")
    sat1.info()
    print()

    com_sat = CommunicationSatellite("SES-17", "GEO", "Telecommunications", "Ka-band")
    com_sat.info()
    print()

    weather_sat = WeatherSatellite("NOAA-20", "Polar Orbit", "Weather Monitoring", "Infrared Radiometer")
    weather_sat.info()
    print()

    print("Testing encapsulation:")
    print(f"Original purpose: {weather_sat.get_purpose()}")
    weather_sat.set_purpose("Storm Tracking")
    print(f"Updated purpose: {weather_sat.get_purpose()}")
    print("\n")

    print("=== Polymorphism ===")
    w_sat = WeatherSat("WeatherSat-1", "Polar Orbit", "Weather Data")
    s_sat = SpySat("SpySat-X", "LEO", "Surveillance")
    n_sat = NavigationSat("NavSat-GPS", "MEO", "Navigation")

    send_data(w_sat)  # Weather data transmission
    send_data(s_sat)  # Surveillance transmission
    send_data(n_sat)  # GPS transmission
