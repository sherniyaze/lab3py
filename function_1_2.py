def FahrtoCentigr(fahr):
    return(5/9)*(fahr-32)
fahr = float(input())
x = FahrtoCentigr(fahr)
print(f"{x:.2f}°C")

