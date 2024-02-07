# import data                                      # 1-й вариант
# from data import documents, directories          # 2-й вариант
from data_package.data import documents as docs, directories as dirs  # 3-й вариант
from data_package.data import a

# print(a)


class Secretary:

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def peoples_info(self):
        number = input("Введите номер документа")
        # for people in data.documents:       # 1-й если используем import data, то добавляем data через точку перед documents
        # for people in documents:            # 2-й вариант без всякой даты
        for people in docs:  # 3-й вариант docs вместо documents
            if people["number"] == number:
                # return print(f'{people["name"]}')
                return print(f'{people["name"].split()[0]} \n')
        print("Не верный номер")
        return


def main():
    secretary = Secretary("Petya", "12345")
    print("Доброе утро", secretary.name)
    while True:
        comand = input("Введите команду")
        if comand == "p":
            secretary.peoples_info()
        elif comand == "q":
            print("До свидания")
            break
        else:
            int("Введите корректную команду")


if __name__ == "__main__":
    main()
