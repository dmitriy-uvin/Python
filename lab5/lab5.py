names = ["Млечный Путь", "Большое Магелланово Облако", "Малое Магелланово Облако",
         "Галактика Андромеды", "Галактика Треугольника", "Галактика Боде"]
coord = ["0", "160 тыс. св. лет (50 кпк)", "200 тыс. св. лет (60 кпк)", "2,5 млн св. лет (780 кпк)", "2,9 млн св. лет (900 кпк)", "12 млн св. лет (3,6 Мпк)"]
about = [
    "Наша галактика. Большинство объектов, видимых невооружённым глазом на небе.",
    "Видна только в южном полушарии. Самая яркая туманность на небе",
    "Видна только в южном полушарии",
    "Также называется Туманностью Андромеды. Находится в созвездии Андромеды.",
    "Наблюдение невооружённым глазом очень затруднено",
    "Это наиболее удалённый объект, видимый невооружённым глазом."
]
galactic = {value: key for key, value in enumerate(names)}
keys = list(galactic.keys())

synonyms = " ".join(names)
synonyms = synonyms.lower()
synonyms = list(synonyms.split(" "))


while True:
    choice = input("Enter the name of galactic ( enter 'exit' to exit ): ")

    if choice != "exit":
        if (choice.lower() not in synonyms) and (choice not in names):
            print("Not synonym!")

        for gal in names:
            if choice.lower() == gal.lower():
                index = galactic[choice]
                print(choice, end=" - ")
                print(about[index])
                print(coord[index])
                break
            elif choice.lower() != gal.lower() and choice.lower() not in keys and choice.lower() in synonyms:
                print(gal)
    else:
        break
