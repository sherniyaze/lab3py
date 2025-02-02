from functions_1_12 import histogram
from function_1_2 import FahrtoCentigr

how_much_FAHR = float(input("temperature: "))
centigrade = FahrtoCentigr(how_much_FAHR)
print(f"{centigrade:.2f}°C")


histolist = []
size_of_list = int(input("Height of our histiogram: "))
for _ in range(size_of_list):
    stars = int(input())
    histolist.append(stars)

histogram(histolist)

