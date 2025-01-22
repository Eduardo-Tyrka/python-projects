# convert measurement units

# value
print("select the value")
unityValue = float(input())

# conversion type
print("select the conversion")
print("1. Meters ---> Feet")
print("2. Feet ---> Meters")
print("3. Kilometers ---> Miles")
print("4. Miles ---> Kilometers")
convertUnity = int(input())

# conversion
if convertUnity == 1:
    result = unityValue * 3.28
elif convertUnity == 2:
    result = unityValue / 3.28
elif convertUnity == 3:
    result = unityValue / 1.6
elif convertUnity == 4:
    result = unityValue * 1.6
else:
    print("select a valid conversion")

print("the result is:")
print(result)
