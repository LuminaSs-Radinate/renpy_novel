label arrival_go_escape:
    em "Нет, я не собираюсь участвовать в этом безумии. Мне нужно просто выйти отсюда!"
    ba "Эй-эй, стой. Ты что делаешь?!"
    sp "Нелогичное решение! Если уйдёшь, проект точно провалится."
    stop music fadeout 0.75

    scene office
    show emrach scared at center 
    with Pixellate(2, 10)
    em "Уф... Кажется, всё обошлось."
    show sergey angry at left with moveinleft
    sg "Эмрах, я посмотрел твой проект, там ошибка. Ты вообще ничего не делаешь?! Мы потеряем клиентов из-за тебя!"
    show emrach sad
    em "Сергей Геннадьевич, я стараюсь... всё вышло из-под контро..."
    sg "Этого недостаточно! Я вынужден прекратить наше сотрудничество. Ты уволен!"
    hide sergey angry at left with moveoutleft

    em "Такого я точно не ожидал. Это провал..."

    return
