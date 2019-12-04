class DegreesCalculator:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9


print(DegreesCalculator.celsius_to_fahrenheit(15))
print(DegreesCalculator.fahrenheit_to_celsius(59))
