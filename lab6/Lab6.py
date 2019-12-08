import WintimeClass as WC
import functions as f
options = ["/add", "/edit", "/delete", "/all"]

d = "Dmitriy"
wc = WC.WintimeClass()
print("=="*20)
print("Вас вітає мережа магазинів WINTIME, якщо вы хочете дізнатися інформацію про магазин в вашому місті - введіть назву свого міста")
print("Команди: /all - подивитися доступні міста, /add - додати місто, /edit - редагувати місто, /delete - видалити місто")
print("=="*20)
while True:
    user_input = input("Ввести дані ( для виходу - exit ): ")
    if user_input != "exit" and user_input not in options:
        get = wc.getInfoCities(user_input)

    elif user_input.strip() == "/add":
        next_input = input("Ведіть назву міста, адресу, телефон та години роботи через кому (city,address,phone,time): ")
        new_city = f.split_data(next_input)
        if len(new_city) < 4:
            print("Ви ввели недостатньо даних, спробуйте ще раз:(")
        else:
            add = wc.addCity(new_city)

    elif user_input.strip() == "/edit":
        # print("Введіть назву міста, яке ви хочете редагувати\nДоступні міста")
        # cities = wc.getCities()
        edit_city = input("Введіть назву міста та НОВІ ДАНІ через кому (city, new address, new phone, new time):")
        upd_city = f.split_data(edit_city)
        print(upd_city)
        edit = wc.editCity(upd_city)

    elif user_input.strip() == "/delete":
        print("Доступні міста")
        wc.getCities()
        delete_city = str(input("Введіть назву місту яке ви хочете видалити: "))
        delete = wc.deleteCity(delete_city)
        wc.getCities()
        print("="*20)

    elif user_input.strip() == "/all":
        wc.getCities()
    else:
        print("="*20)
        print("Дякуємо за користування програмою!:)")
        break
