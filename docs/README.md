# Math formulas
Проект содержит файлы, содержащие функции, подсчета площадей и периметра следующих геометрических фигур:

- Круг;
- Прямоугольник;
- Квадрат;
- Треугольник, соответственно.

## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (a $\cdot$ h) / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Функции
## circle.py
  - #### area(r)
    Принимает число r - радиус окружности, возвращает площадь этой окружности по формуле произведения числа Пи на квадрат радиуса. Пример вывода для окружности радиусом 10:

    ```
    input: print(area(10))
    output: 314.1592653589793
    ```
  - #### perimeter(r)
    Так же получает число r - радиус окружности. Результатом фунцкии является периметр окружности, вычисленный по формулуе $P = 2πr$. Пример вызова фунции:

    ```
    input: print(perimeter(10))
    output: 62.83185307179586
    ```

## rectangle.py
  - #### area(a, b)
    Принимает 2 числа: $a$ и $b$ - стороны прямоугольника. Возвращает площадь прямоугольника с данными сторонами по формуле $S = a \cdot b$. Пример при введеных размерах 3 и 5:

    ```
    input: print(area(3, 5))
    output: 15
    ```
  - #### perimeter(a, b)
    Фунция для нахождения периметра прямоугольника по заданным размерам a и b по формуле $P = 2 \cdot a + 2 \cdot b$:
    ```
    input: print(perimeter(3, 5))
    output: 16
    ```
## square.py
  - #### area(a)
    Функция для нахождения площади квадрата со сторонами размера "a" по формуле $S = a^2$. Пример вывода при $a = 4$:
    ```
    input: print(area(4))
    output: print(16)
    ```
  - #### perimeter(a)
    Функция, вычисляющая периметр квадрата размером $a$ по формуле $P = 4 \cdot a$:
    ```
    input: print(perimeter(4))
    output: 16
    ```

## triangle.py
  - #### area(a, h)
    Функция получает два значения: длину основания треугольника и его высоту. Возвращаемое значение: площадь треугольника, вычисляемое по формуле $S = \Large{\frac{a \cdot h}{2}}$. Пример вызова при значениях 5 и 19:
    ```
    input: print(area(5, 19))
    output: 47,5
    ```
  - #### perimeter(a, b, c)
    Функция получает на вход три значения: размеры сторон треугольника. Результат вызова функции: сумма сторон $\Rightarrow$ периметр фигуры. Пример вызова при значениях 8, 13, 21:
    ```
    input: print(8, 13, 21)
    output: 42
    ```

# Автотестирование
Общее количество автотестов $=$ 18.

Из них программа успешно прошла 7.

Autotests success: $\: \Large\frac{7}{18}$ $\:(\sim 38,9\%)$

# История изменений проекта

| Хэш     | Автор     | Дата                     | Комментарий                                    |
| ------- | --------- | ------------------------ | ---------------------------------------------- |
| 51f3f3b | EpicWhal3 | Wed Nov 22 17:07:23 2023 | fix: rectangle and triangle rebuild,           |
|         |           |                          | test_traingle fix                              |
| 7b0f428 | EpicWhal3 | Mon Nov 20 14:16:36 2023 | feat: update circle and triangle tests         |
| ec179bc | EpicWhal3 | Sun Nov 5 15:46:14 2023  | feat: add new tests; fix: modified rectangle   |
|         |           |                          | and triangle tests                             |
| bf2343f | EpicWhal3 | Fri Oct 27 13:31:18 2023 | fix: upd formulas triangle and rectangle;      |
|         |           |                          | test: add rectangle and triangle tests         |
| 726624d | EpicWhal3 | Tue Oct 10 01:14:43 2023 | docs: README update                            |
| 3bd5f51 | EpicWhal3 | Sun Oct 1 15:58:32 2023  | docs: add comment to triangle.py and square.py |
| c12a8fa | EpicWhal3 | Sun Oct 1 15:43:36 2023  | docs: add doc to rectangle.py functions        |
| 21b17dc | EpicWhal3 | Sun Oct 1 15:20:42 2023  | docs: add comment to circle.py                 |
| b792bd2 | EpicWhal3 | Thu Sep 14 15:34:16 2023 | fixed formula                                  |
| 682a830 | EpicWhal3 | Thu Sep 14 15:33:19 2023 | added file triangle.py                         |
| 1055cb6 | EpicWhal3 | Thu Sep 14 15:30:55 2023 | added new file rectangle.py                    |
| d078c8d | smartiqa  | Thu Mar 4 14:55:29 2021  | L-03: Docs added                               |
| 8ba9aeb | smartiqa  | Thu Mar 4 14:54:08 2021  | L-03: Circle and square added                  |
