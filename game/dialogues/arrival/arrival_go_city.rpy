label arrival_go_city:
    em "Город кажется логичным направлением. Надеюсь, мы найдём что-то полезное."
    ba "Логика, говоришь? В городе столько всего, что найти что-то конкретное — задача не из лёгких."
    sp "А я поддерживаю. Город — это центр активности. Там точно будет подсказка, и скорее всего, мы найдём ошибку именно там."
    em "Ладно, пойдёмте уже."

    scene city
    show bagio at bagio_dynamic
    show spaghettinio at spagetinio_dynamic
    with Fade(0.5, 1, 0.75)
    
    sp "Вот он, город! Но где нам искать?"
    em "Да, пришли... а дальше я даже не знаю, с чего начать."
    show bagio happy with dissolve
    ba "У меня есть идея. Давайте я взлечу и осмотрюсь сверху. Может, увижу что-нибудь странное."
    show bagio with dissolve
    em "Хорошая идея! Давай попробуй."
    play sound "audio/baggio_flying.mp3" volume 0.1
    hide bagio with moveouttop 
    pause 2.5
    play sound "audio/baggio_back.mp3" volume 0.1
    show bagio at bagio_dynamic with moveintop
    pause 0.5
    em "Ну что, удалось что-то заметить?"
    ba "Осмотрелся. Ничего особо интересного. Спереди длинная дорога, справа дома, слева тоже дома, но..."
    show bagio happy with dissolve
    ba "Ха, вот прикол! Там здание стоит, а двери нет. Это же надо было такое придумать."
    show bagio with dissolve
    show spaghettinio offended with dissolve
    sp "Ба, ты серьёзно? Здание без двери? Это, скорее всего и есть наша ошибка! Хотя неудивительно, что ты не заметил её важности."
    em "Это может быть той самой проблемой, которую мы ищем. Покажи, где это здание."
    show bagio offended with dissolve
    ba "Ладно-ладно, идём. Покажу."

    scene radik
    play sound "audio/radik_sounds.mp3" loop volume 0.1
    show bagio at bagio_dynamic
    show spaghettinio at spagetinio_dynamic
    with Fade(0.5, 1, 0.75)

    ba "Вот оно. У здания нет двери."
    em "Ну и ну... Теперь я вспомнил. Этот участок проекта делал я. Видимо, я полностью забыл добавить дверь."
    sp "Да, очевидно, это проблема. Давай исправим её."
    
    hide bagio
    hide spaghettinio
    with Fade(0.4, 0.3, 0.4)
    return
