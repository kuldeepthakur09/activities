frequency = float(input("Enter frequency in Hertz (Hz): "))

if frequency < 3e9:
    category = "Radio Waves"
elif 3e9 <= frequency < 3e12:
    category = "Microwaves"
elif 3e12 <= frequency < 4.3e14:
    category = "Infrared Light"
elif 4.3e14 <= frequency < 7.5e14:
    category = "Visible Light"
elif 7.5e14 <= frequency < 3e17:
    category = "Ultraviolet Light"
elif 3e17 <= frequency < 3e19:
    category = "X-Rays"
else: # frequency is 3e19 or greater
    category = "Gamma Rays"
print(f"A frequency of {frequency} Hz corresponds to {category}.")