# convert_miles
miles_value = float(input("Mile: "))


def convert_miles():
    km = 1.6 * miles_value
    return km


conversion = convert_miles()
print("Kilometer: " + str(conversion) + " KM")
