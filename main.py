def celsius_to_fahrenheit(temperature):
    return temperature * 1.8 + 32


def celsius_to_kelvin(temperature):
    return temperature + 273.15


if __name__ == '__main__':
    with open("input.txt", "r") as file, open("result.txt", "w") as result:
        content = file.readlines()
        temperatures = []
        for line in content:
            temperatures.append(float(line.strip()))
        result.write("Celsius; Kelvin; Fahrenheit\n")
        for temperature in temperatures:
            result.write(f"{temperature}; {round(celsius_to_kelvin(temperature), 2)}; {round(celsius_to_fahrenheit(temperature), 2)}\n")