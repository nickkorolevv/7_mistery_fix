


# Решатель квадратных уравнений

 - Данный скрипт находит корни квадратного уравнения
 - Если дискриминант больше нуля, то скрипт выдает 2 вещественных корня
 - Если дискриминант равен нулю, то скрипт выдает один вещественный
   корень
 - Если дискриминант меньше нуля, то вещественных корней нет.

# Как использовать
Переменная a - старший коэффициент
b - средний коэффициент
с - свободный член 
D - дискриминант 
 - Используется модуль `math`.
 - Был добавлен исход, когда дискриминант меньше нуля и корни получались
   комплексные.
 - Пример импорта функции `get_roots()`

    

```python
        from quadratic_equation import get_roots
```
Для нахождения корней квадратного уравнения с произвольными коэффициентами нужно вызвать 

   ```python 
    get_roots(a,b,c)
```

    root1, root2 = get_roots(a, b, c)
Эта функция возвращает корни квадратного уравнения, когда мы задаем коэффициенты. root1- первый корень. root2 - второй корень
# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)


