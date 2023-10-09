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
  - ### perimeter(r)
    Так же получает число r - радиус окружности. Результатом фунцкии является периметр окружности, вычисленный по формулуе $P = 2πr$. Пример вызова фунции:

    ```
    input: print(perimeter(10))
    output: 62.83185307179586
    ```

## rectangle.py
  - ### area(a, b)
    Принимает 2 числа: $a$ и $b$ - стороны прямоугольника. Возвращает площадь прямоугольника с данными сторонами по формуле $S = a \cdot b$. Пример при введеных размерах 3 и 5:

    ```
    input: print(area(3, 5))
    output: 15
    ```
  - ### perimeter(a, b)
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
    Функция получает два значения: длину основания треугольника и его высоту. Возвращаемое значение: площадь треугольника, вычисляемое по формуле $S = \frac{a \cdot h}{2}$. Пример вызова при значениях 5 и 19:
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

# История изменений проекта
```
* 3bd5f51 (HEAD -> documentation_408783, origin/documentation_408783) docs: add comment to triangle.py and square.py
* c12a8fa docs: add doc to rectangle.py functions
* 21b17dc docs: add comment to circle.py
* b792bd2 (origin/main, origin/HEAD, new_features_408783, main) fixed formula
* 682a830 added file triangle.py
* 1055cb6 added new file rectangle.py
* d078c8d L-03: Docs added
* 8ba9aeb L-03: Circle and square added
```