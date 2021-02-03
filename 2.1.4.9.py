kilometros = float(input("Escribe los kilómetros a convertir"))
millas = float(input("Escribe las millas a convertir"))

millas_a_kilometros = millas * 0.621371
kilometros_a_millas = kilometros * 1.60934

print(millas, " millas son ", round(millas_a_kilometros, 2), " kilómetros ")
print(kilometros, " kilómetros son ", round(kilometros_a_millas, 2), " millas ")
