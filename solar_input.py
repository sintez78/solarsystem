# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":  # добавлена обработка планет
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    parts = line.strip().split()
    if len(parts) >= 8:
        star.R = float(parts[1])      # радиус в пикселах
        star.color = parts[2]          # цвет
        star.m = float(parts[3])       # масса
        star.x = float(parts[4])       # координата x
        star.y = float(parts[5])       # координата y
        star.vx = float(parts[6])      # скорость по x
        star.vy = float(parts[7])      # скорость по y


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    parts = line.strip().split()
    if len(parts) >= 8:
        planet.R = float(parts[1])      # радиус в пикселах
        planet.color = parts[2]          # цвет
        planet.m = float(parts[3])       # масса
        planet.x = float(parts[4])       # координата x
        planet.y = float(parts[5])       # координата y
        planet.vx = float(parts[6])      # скорость по x
        planet.vy = float(parts[7])      # скорость по y


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            if isinstance(obj, Star):
                obj_type = "Star"
            elif isinstance(obj, Planet):
                obj_type = "Planet"
            else:
                continue  # пропускаем неизвестные объекты
            out_file.write(f"{obj_type} {obj.R} {obj.color} {obj.m} {obj.x} {obj.y} {obj.vx} {obj.vy}\n")


if __name__ == "__main__":
    print("This module is not for direct call!")
