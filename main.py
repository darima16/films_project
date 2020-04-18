def reader():
    d = {}
    with open('films.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            film = line.split(':')[0]
            actors = line.split(':')[1].split(',')
            d[film] = set(actors)
    return d

def create_dict(d):
    new_d = {}
    for film, actors in d.items():
        for actor in actors:
            if actor not in new_d:
                new_d[actor] = set()
                new_d[actor].add(film)
            else:
                new_d[actor].add(film)
    return new_d


def main():
    d = reader()
    while True:
        print('---------------MENU-----------------')
        print('1. Работа с фильмами')
        print('2. Работа с актерами')
        print('3. Выход.')
        print('------------------------------------')
        menu = int(input('Введите инетресуемую опцию(1 или 2, 3): '))
        if menu == 1:
            print('------------------------------------')
            print('В нашей библиотеке имеются следующие фильмы: ')

            for i in d:
                print(i, end='\n')

            film1 = input('Введите название фильма №1: ')
            film2 = input('Введите название фильма №2: ')

            print('------------------------------------')
            print('1. Вывести общий актерский состав')
            print('2. Вывести актеров, снимавшихся и в первом, и во втором фильме.')
            print('3. Вывести актеров, участвующих в '
                  'съемках первого, но не участвующих в съемках второго.')
            option = int(input('Желаемое действие: '))

            if option == 1:
                actors = d[film1] | d[film2]
                for actor in actors:
                    print(actor)
                break
            elif option == 2:
                actors = d[film1] & d[film2]
                if len(actors) == 0:
                    print('Данных актеров нет.')
                    continue
                for actor in actors:
                    print(actor)
                print()
                continue
            elif option == 3:
                actors = d[film1] - d[film2]
                for actor in actors:
                    print(actor)
                continue
            else:
                print('Некорректный ввод!')
                continue
        elif menu == 2:
            print('------------------------------------')
            actor1 = input('Введите имя актера №1: ')
            actor2 = input('Введите имя актера №2: ')
            print('------------------------------------')

            print('1. Вывести названия фильмов, в которых снимался хотя бы один из актеровв')
            print('2. Вывести названия фильмов, в которых снимались оба актера.')
            print('3. Вывести названия фильмов, в которых снимался первый актер, '
                  'но не участвовал в съемках второй.')
            option = int(input('Желаемое действие: '))
            new_d = create_dict(d)

            if option == 1:
                films = new_d[actor1] | new_d[actor2]
                for film in films:
                    print(film)
                print()
                continue

            if option == 2:
                films = new_d[actor1] & new_d[actor2]
                if len(films) == 0:
                    print('Данных фильмов нет.')
                    continue
                for film in films:
                    print(film)
                print()
                continue

            if option == 3:
                films = new_d[actor1] - new_d[actor2]
                for film in films:
                    print(film)
                print()
                continue
            else:
                print('Некорректный ввод!')
                continue
        if menu == 3:
            break

if __name__ == '__main__':
    main()
