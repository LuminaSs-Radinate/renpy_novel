label escape_project:
    em "Нет, я не собираюсь участвовать в этом безумии. Мне нужно просто выйти отсюда!"

    ba "Эй-эй, ты что делаешь? ."
    sp "Нелогичное решение! Если уйдёшь, проект точно провалится."

    stop music
    scene bg_office with Pixellate(1.2, 9)
    show emrach at center with dissolve
    em "Уф... Кажется, всё обошлось. Но что теперь с проектом?"

    show sergey at left with moveinleft
    sg "Эмрах, я посмотрел твой проект. Что это? Ты вообще ничего не делаешь? Мы теряем клиентов!"

    em "Сергей Геннадьевич, я старался... Всё вышло из-под контроля."

    sg "К сожалению, этого недостаточно. Я вынужден прекратить наше сотрудничество."
    hide sergey at left with moveoutleft

    em "Такого я точно не ожидал. Провал..."

    return