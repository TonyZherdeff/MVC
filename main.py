import sys


class Article:
    def __init__(self, name, author,
                 cnt_symb, pub_name='', descrip=''):
        self.name = name
        self.author = author
        self.cnt_symb = cnt_symb
        self.pub_name = pub_name
        self.descrip = descrip

    def __str__(self):
        str_data = ''
        rus_captions = ["Название:", "Автор:", "Количество символов:", "Издательство:", "Описание:"]
        dict_data = self.__dict__
        list_data = []
        for i in dict_data.values():
            list_data.append(i)
        j = 0
        while j < len(list_data):
            str_data = str_data + f'{rus_captions[j]} {list_data[j]}\n'
            j += 1
        return f'{str_data}'


class Model:
    @staticmethod
    def _read_txt(path):
        data = []
        with open(path) as f:
            for line in f:
                data.append(line.replace('\n', ''))
        return data

    @staticmethod
    def view_author(path):
        data = Model._read_txt(path)
        author_data = []
        for article in data:
            author_data.append(article.split(';')[1])
        return set(author_data)

    @staticmethod
    def count_article(path, author):
        data = Model._read_txt(path)
        count = 0
        for article in data:
            if article.split(';')[1] == author:
                count += 1
        return count

    @staticmethod
    def _str_to_Article(list_txt):
        data = []
        for line in list_txt:
            buf = Article(*line.split(';'))
            data.append(buf)
        return data

    @staticmethod
    def new_article(path):
        data = Model._read_txt(path)
        return Model._str_to_Article(data)

    @staticmethod
    def add_new_article(path, args: str):
        with open(path, 'a') as f:
            f.seek(0, 2)
            f.writelines(args)


class View:
    @staticmethod
    def print_list(plist):
        for i in plist:
            print(i)

    @staticmethod
    def ready_info():
        print("Готово!")

    @staticmethod
    def count_article_info(author, count):
        print(f'У автора {author} имеется {count} статей.')

    @staticmethod
    def print_select_menu():
        print("Выбор действия:")
        print("4 - Для подсчета количества статей у выбранного автора")
        print("3 - Для вывода всех имеющихся авторов")
        print("2 - Добавить новую статью")
        print("1 - Вывести все статьи")
        print("0 - Выйти из программы")


class Control:
    @staticmethod
    def menu():
        View.print_select_menu()
        buf = input()
        if buf == "0":
            sys.exit()
        elif buf == "1":
            res = Model.new_article('./log.txt')
            View.print_list(res)
        elif buf == "2":
            art_info = str(input("Введите через точку с запятой данные в следующем порядке:\n 'Название статьи:Автор;"
                                 "Количество символов;Название издательства;Описание'\n"))
            Model.add_new_article('./log.txt', art_info)
            View.ready_info()
        elif buf == "3":
            author = Model.view_author('./log.txt')
            View.print_list(author)
        elif buf == "4":
            author = input("Введите имя автора:\n")
            searching = Model.count_article('./log.txt', author)
            View.count_article_info(author, searching)


while True:
    Control.menu()

