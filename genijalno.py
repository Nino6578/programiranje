# Izbornik za kalkulator
print(" Izbornik za kalkulator")
print("--------------------")
print(" Izaberite operaciju:")
print("1. Izračun napona struje")
print("2. Izračun otpora struje")
print("3. Izračun jakosti struje")
print("-----------------")
opcija=int(input(" Izaberite operaciju:"))
#Struktura grananja
if opcija == 1:    # == != < > <> >= <=
# Izračun napona struje
jakost=int(input("Upiši jakost struje:"))
otpor=int(input("Upiši otpor:"))
napon=jakost*otpor
print(f" Napon struje je: {napon} V")
elif opcija==2:
print(" Izračun otpora struje")
napon=int(input("Upiši napon   "))
jakost=int(input("Upiši jakost struje:"))
otpor=napon/jakost
print("Otpor je{otpor}ohm")
elif ==3:
print("Izračunaj jakosti struje")
napon=int(input("Upiši napon":))
otpor=int(input("Upiši napon"))
jakost=napon/otpor
print(f"Jakost struje je:  {jakost}A")

else:
    print("Pogrešan unos")

