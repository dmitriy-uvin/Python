import stores_data as sd

class WintimeClass:
    stores = sd.stores
    def getInfoCities(self, input):
        cities = list(self.stores.keys())
        if len(str(input)) > 1:
            if input in cities:
                print("="*20)
                print("Філіал компанії WINTIME в м.", input)
                print(" + Адреса : ", self.stores[input][0], "\n",
                      "+ Робочий час : ", self.stores[input][1], "\n",
                      "+ Телефон : ", self.stores[input][2])
                print("=" * 20)
            else:
                print("Такого міста в мережі магазинів WINTIME ще немає, ми працюємо над цим, спробуйте ще раз")
                print("Доступні магазини:")
                for key in cities:
                    print(key, end=", ")
                print("\n")
        elif len(str(input)) == 1:
            letters = []
            for i in cities:
                letters += i[0]
                if input.upper() == i[0]:
                    print("?", i)
            if input.upper() not in letters:
                print("Міст, що починаються з такої букви в компанії ще нема, спробуйте ще раз:)")

    def getCities(self):
        """
        :return: list of available cities
        """
        for city in self.stores:
            print(city, end=", ")
        print("\n")

    def addCity(self, data):
        """
        :param data: data about new city
        :return: new list of stores
        """
        print(self.stores)
        update_dict = {data[0]: ("вул. " + data[1], data[2], data[3])}
        self.stores.update(update_dict)
        print(self.stores)
        print("Місто {0} було успішно додано!".format(data[0]))
        print("="*20)

    def editCity(self, new_data):
        """
        :param new_data: new data about exhists city
        :return: void
        """
        old_info = self.getCity(new_data[0])
        for city in range(len(new_data)):
            if new_data[city] == "":
                new_data[city] = old_info[city-1]
            elif city == 0:
                new_data[0] = new_data[0].replace("вул. ", "")

        info_about_city = {new_data[0]: ("вул. " + new_data[1], new_data[2], new_data[3])}
        self.stores.update(info_about_city)
        print("Місто {0} було відредаговано".format(new_data[0]))

    def deleteCity(self, city):
        """
        deleting city from the dict by his name
        :param city: name of city
        :return: void
        """
        self.stores.pop(city)

    def getCity(self, city):
        """
        gets info of the city by his name and returns arr with information
        :param city: name of city
        :return: arr - info about city
        """
        old_info = self.stores[city]
        return old_info