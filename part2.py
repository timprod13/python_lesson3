def my_info(name, surname, date, city, email, tel_num):
    print("Привет,", name, "с фамилией", surname, "рождённый", date, "из города", city, "с e-mail", email,
          "и номером телефона", tel_num)


my_info(name=input("Введите имя "), surname=input("Введите фамилию "), date=input("Введите дату рождения "),
        city=input("Введите город "), email=input("Введите e-mail адрес "), tel_num=input("Введите номер телефона "))
