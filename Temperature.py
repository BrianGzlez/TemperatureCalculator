class TemperatureScale:
    Celsius = "Celsius"
    Fahrenheit = "Fahrenheit"
    Kelvin = "Kelvin"

class Temperature:
    def __init__(self, value, scale):
        self.value = value
        self.scale = scale

    def add(self, other):
        if self.scale != other.scale:
            raise ValueError("Both temperatures must be in the same scale")
        return Temperature(self.value + other.value, self.scale)

    def subtract(self, other):
        if self.scale != other.scale:
            raise ValueError("Both temperatures must be in the same scale")
        return Temperature(self.value - other.value, self.scale)

    def multiply_by(self, other):
        if self.scale != other.scale:
            raise ValueError("Both temperatures must be in the same scale")
        return Temperature(self.value * other.value, self.scale)

    def divide_by(self, other):
        if self.scale != other.scale:
            raise ValueError("Both temperatures must be in the same scale")
        if other.value == 0:
            raise ValueError("Cannot divide by zero")
        return Temperature(self.value / other.value, self.scale)

    def to_fahrenheit(self):
        if self.scale == TemperatureScale.Celsius:
            return Temperature((self.value * 9/5) + 32, TemperatureScale.Fahrenheit)
        elif self.scale == TemperatureScale.Kelvin:
            return Temperature((self.value - 273.15) * 9/5 + 32, TemperatureScale.Fahrenheit)
        else:
            return self  # Already in Fahrenheit

    def to_celsius(self):
        if self.scale == TemperatureScale.Fahrenheit:
            return Temperature((self.value - 32) * 5/9, TemperatureScale.Celsius)
        elif self.scale == TemperatureScale.Kelvin:
            return Temperature(self.value - 273.15, TemperatureScale.Celsius)
        else:
            return self  # Already in Celsius

    def to_kelvin(self):
        if self.scale == TemperatureScale.Celsius:
            return Temperature(self.value + 273.15, TemperatureScale.Kelvin)
        elif self.scale == TemperatureScale.Fahrenheit:
            return Temperature((self.value - 32) * 5/9 + 273.15, TemperatureScale.Kelvin)
        else:
            return self  # Already in Kelvin

    def __str__(self):
        return f"{self.value:.4f}{self.scale[0]}"


if __name__ == "__main__":
    a = Temperature(2, TemperatureScale.Kelvin)
    b = Temperature(-2, TemperatureScale.Celsius)
    
    diff = a.subtract(b)
    print(f"Resultado de la resta: {diff}")

    # Ejemplo de conversión
    temp_celsius = Temperature(25, TemperatureScale.Celsius)
    temp_fahrenheit = temp_celsius.to_fahrenheit()
    print(f"Temperatura en Fahrenheit: {temp_fahrenheit}")

    temp_kelvin = temp_celsius.to_kelvin()
    print(f"Temperatura en Kelvin: {temp_kelvin}")
