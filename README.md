# Remont-holodilnikov
### Состав команды
- Кутугин Даниил – тимлид, конструктор KSP
- Гуляев Антон - физик, составитель математической модели
- Иванов Александр – продакшн менеджер, заполнял отчёты, делал презентацию
- Аксельрод Анастасия - продакшн менеджер, заполняла отчёты, работала над видео-отчетом

### Модель ракеты создана в конструкторе Kerbal Space Program
![image1](https://github.com/dkutugin3/Remont-holodilnikov/blob/main/Pictures/launch.png)
![image2](https://github.com/dkutugin3/Remont-holodilnikov/blob/main/Pictures/land.png)

Файл с моделью [ракеты](Venus_5.craft)

### Программы 
Программы для сбора данных написаны на языке **Python** с использованием библиотеки **kRPC**
- Программа для [построения графиков](Programming/drawer.py)
- Программа для [сбора данных о скорости и времени из ksp при взлёте с Кербина и выходе на его орбиту](Programming/launch.py)
- Программа для [сбора данных о скорости и времени из ksp при движении по гелиоцентрической орбите](Programming/orbital_transition.py)
- Программа для [сбора данных о скорости и времени из ksp при торможении в сфере действия Евы, переходе на посадочную орбиту и посадке](Programming/eve.py)
- Программа для [рассчёта скорости в каждый момент времени на каждом из трёх участков полёта](Programming/model_graphs.py ) 