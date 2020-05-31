# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре

#image day_menu = Movie(play="gui/Menu/day_sky_background.mpg",size=(config.screen_width, config.screen_height))
#импортировали модуль datetime
init python:
    import datetime

init -2:
    image day_menu = Movie(play="gui/Menu_video/day_sky_background.mpg", size=(720,1280))
    image night_menu = Movie(play="gui/Menu_video/night_sky_background.mpg", size=(720,1280))

label main_menu:
    #получаем нынешнее время в числовом виде и берем только часы
    #Происходит сравнение нынешним временем и с числовым ограничителем. От времени ставится определенное видео
    if int(datetime.datetime.now().hour) >= 6 and int(datetime.datetime.now().hour) < 20:
        scene day_menu
    else:
        scene night_menu

    jump main_menu_screen
label start:

    "Перед началом игры введите свое имя:"

    # Фраза в скобках послужит игроку подсказкой о том, что нужно ввести выбранное им имя.

    $ player_name = renpy.input("Как тебя зовут?")

    $ player_name = player_name.strip()

    # .strip() - данный параметр удалит лишние или случайно набранные игроком пробелы.
    # Если игрок не хочет придумывать себе имя, то будет использовано имя по умолчанию:

    if player_name == "":
        $ player_name = "Ханна"

    # Теперь другие персонажи могут звать игрока выбранным именем.

    "Приятной игры, [player_name]!"
    ##pov "Меня зовут [player_name]!"
    jump glava1
    return

label glava1:

    scene black with dissolve
    pause 1
    scene imag
    "В таверне было немноголюдно, так как шла усиленная подготовка к сбору урожая.\nТолько хозяин заведения устало бродил между столами, собирая мусор, \nкоторый остался после бурной ночи. \nНебольшая компания чужаков ютилась в тёмном углу, пересказывая друг другу последние слухи. Почти никто не заметил тени, скользнувшей к выходу. \nПочти."
    show traktorchik with dissolve
    t "Эй, [player_name] , ты уже уходишь?"
    "Тень застыла и обернулась."
    pov "Да, Фридрих, мне уже пора."
    return
