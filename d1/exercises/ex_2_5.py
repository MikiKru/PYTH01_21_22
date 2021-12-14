height = float(input('podaj wzrost [m]: '))
weight = int(input('podaj wagę [kg]: '))

bmi=weight/pow(height, 2)

if bmi < 16:
    print(f"BMI={bmi:.2f} wygłodzenie")
elif bmi < 16.99:
    print(f"BMI={bmi:.2f} wychudzenie")
elif bmi < 18.49:
    print(f"BMI={bmi:.2f} niedowaga")
elif bmi < 24.99:
    print(f"BMI={bmi:.2f} wartosc prawidłowa")
elif bmi < 29.99:
    print(f"BMI={bmi:.2f} nadwaga")
elif bmi < 34.99:
    print(f"BMI={bmi:.2f} I stopien otyłosci")
elif bmi < 39.99:
    print(f"BMI={bmi:.2f} II stopien otyłosci (otyłosc kliniczna)")
else:
    print(f"BMI='{bmi:.2f} III stopien otyłosci (otyłosc skrajna)")

weight_min = 18.5 * (height ** 2)
weight_max = 24.99 * (height ** 2)
print(f"Prawidłowa waga dla Twojego wzrostu {weight_min:.1f} - {weight_max:.1f}")