temperature=24

def weather(temperature):
    if temperature > 30:
        print("It's hot outside! Stay hydrated and avoid direct sunlight.")
    elif 20 <= temperature <= 30:
        print("Enjoy the pleasant weather!")
    else:
        print("It's a bit chilly. Bring a light jacket.")