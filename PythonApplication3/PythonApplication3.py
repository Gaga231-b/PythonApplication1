import random

def igra_kamen_papir_mazaze():
    opcije = ["камен", "маказе", "папир"]
    print("🎮 Добродошао у игру 'Камен – Маказе – Папир'!")
    
    while True:
        racunar_izbor = random.choice(opcije)
        igrac_izbor = input("Унеси свој избор (камен, маказе, папир) или 'излаз' за крај: ").lower()

        if igrac_izbor == "излаз":
            print("👋 Хвала што си играо!")
            break

        if igrac_izbor not in opcije:
            print("❌ Неважећи избор. Покушај поново.")
            continue

        print(f"🧑 Ти: {igrac_izbor}  |  💻 Рачунар: {racunar_izbor}")

        if igrac_izbor == racunar_izbor:
            print("🤝 Нерешено!")
        elif (igrac_izbor == "камен" and racunar_izbor == "маказе") or \
             (igrac_izbor == "маказе" and racunar_izbor == "папир") or \
             (igrac_izbor == "папир" and racunar_izbor == "камен"):
            print("✅ Победио си!")
        else:
            print("❌ Изгубио си!")

        print("-" * 30)

# Покретање игре
igra_kamen_papir_mazaze()