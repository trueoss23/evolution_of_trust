
# Evolution of trust
## Данный проект разрабатывался на Windows 10, Python 3.9.13
## Запуск результатов:
запустить с помощью интерпретатора pyhton файл "start_game.py" находясь в папке "src" :
* ``` py start_game.py``` на Windows
* ```python3 start_game.py``` на Mac Os, Linux

Вывод будет содержать первые три места из серии 10 игр. Сначала стандартные 5 классов, а последние 2 вывода тройки победителей с моим классом.
***
## Задание:
* Реализовать простую игру с конфетами, где есть автомат, который управляет подачей конфет для двух групп людей в зависимости от того, положили ли в него один или оба из двух операторов:

|  | Оба сотрудничают | 1 обманывает, 2 сотрудничает | 1 сотрудничает, 2 обманывает | оба обманывают |
|------------|----------|----------|----------|---------|
| Operator 1 | +2 конфеты | +3 конфеты | -1 конфета | 0 конфет |
| Operator 2 | +2 конфеты | -1 конфета | +3 конфеты | 0 конфет |

Итак, если все сотрудничают и кладут конфеты в автомат, как и было согласовано, каждый получает вознаграждение. Но у обоих участников также есть соблазн схитрить и только сделать вид, что они положили конфету в автомат, потому что в этом случае их группа получит обратно 3 конфеты, просто забрав одну конфету у второй группы. Проблема в том, что если оба оператора решат играть грязно, то никто ничего не получит.
Также есть пять моделей поведения, которые нужно использовать для проведения экспериментов:

| Тип поведения | Действия Игрока                                                                                                                                                                                         |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Мошенник       | Всегда обманывает                                                                                                                                                                                          |
| Кооператор    | Всегда сотрудничает                                                                                                                                                                                      |
| Подражатель       | Начинает с сотрудничества, но затем просто повторяет то, что делает другой парень                                                                                                                         |
| Недовольный       | Начинает с того, что всегда сотрудничает, но навсегда переключается на читера, если другой парень изменит хотя бы раз                                                                                                       |
| Детектив     | Первые четыре раза идет с [Сотрудничество, Обман, Сотрудничество, Сотрудничество], и если в течение этих четырех ходов другой парень сжульничает хотя бы один раз - превращается в Подражателя. В противном случае сам переключается на Мошенника |

-----

Чтобы закончить эксперимент, вам нужно смоделировать систему с семью классами - Game и Player пятью типами поведения (подклассы от Player).

Шаблон класса Game выглядит так:

```python
from collections import Counter

class Game(object):

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1, player2):
        # simulate number of matches
        # equal to self.matches

    def top3(self):
        # print top three
```

Здесь regi stryиспользуется для отслеживания текущего количества конфет во время игры, а player1 и player2 являются экземплярами подклассов Player(каждый из которых является одним из 5 типов поведения). Вызов
 play() метода экземпляра Game должен выполнять симуляцию заданного количества матчей между игроками с заданным поведением.
Метод top3() должен печатать текущее поведение трех лучших игроков вместе с их текущим счетом, например:

```
cheater 10
detective 9
grudger 8
```

По умолчанию ваш код при запуске должен имитировать 10 игр (один вызов
 play()) между каждой парой двух игроков с разными типами поведения (всего 10 раундов по 10 игр в каждом, отсутствие совпадений между двумя копиями одного и того же поведения) и вывести трех лучших победителей после всей игры.
Вам настоятельно рекомендуется поэкспериментировать с различным поведением и написать свой собственный класс поведения (это оценивается как бонус). Вы можете получить еще больше бонусных баллов, если экземпляр вашего класса покажет лучшие результаты в том же «состязании между каждой парой игроков», проверьте, что по крайней мере три из пяти предоставленных вариантов поведения.
Не забывайте, что единственное, что игрок может делать на каждом ходу, это либо сотрудничать, либо жульничать, основываясь на истории текущей игры.
