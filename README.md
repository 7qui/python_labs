# python_labs
# Лабораторная работа 1

### Задание номер 1
```python
name = input('Имя: ')
age = int(input('Возраст: '))
print(f'Привет, {name}! Через год тебе будет {age + 1}.')
```
![Картинка 1](./image/lab01/01.png)


### Заданиет номер 2
```python
a = float(input('a: ').replace(',', '.'))
b = float(input('b: ').replace(',', '.'))
print(f'{a + b}; avg={round(((a + b)/2),2)}')
```
![Картинка 2](./image/lab01/02.png)

### Задание номер 3
```python
price = 1000
discount = 10
vat = 20
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {format(base,'.2f')}")
print(f'НДС: {format(vat_amount,'.2f')}')
print(f"Итого к оплате: {format(total,".2f")}")
```
![Картинка 3](./image/lab01/03.png)

### Задание номер 4
```python
time = int(input('Минуты: '))
hour = (time // 60) % 24
minute = time % 60
print(f'{hour}:{minute}')
```
![Картинка 4](./image/lab01/04.png)

### Задание номер 5
```python
a = input('ФИО: ').split()
print(f'Инициалы: {a[0][0] + a[1][0] + a[2][0]}.')
print(f'Длина (симоволов): {len(a[0]) + len(a[1]) + len(a[2]) + 2}')
```
![Картинка 5](./image/lab01/05.png)

# Лабораторная работа 2

### Задание номер 1
```python
def min_max(a):
    if not a:
        raise ValueError("Список не может быть пустым")
    return (min(a), max(a))

def unique_sorted(a):
    return sorted(set(a))

def flatten(a):
    result = []
    for item in a:
        if not isinstance(item, (list, tuple)):
            raise TypeError(f"Элемент должен быть списком или кортежем, получен {type(item)}")
        result.extend(item)
    return result

print(min_max([3, 1, 2, 1, 3]))
```
![Картинка 1](./image/lab02/01.02.png)
![Картинка 1](./image/lab02/01.02.02.png)
![Картинка 1](./image/lab02/01.02.03.png)

### Задание номер 2
```python
def transpose(a):
    result = []

    for i in range(len(a) - 1):
        if len(a[i]) < len(a[i + 1]) or (len(a[i]) > len(a[i + 1])):
            print('ValueError')
    
    for i in range(len(a[0])):
        new_list = []
        for k in range(len(a)):
            new_list.append(a[k][i])
        result.append(new_list)

    return result

def row_sums(a):
    sum_list = []

    for i in range(len(a)):
        summ = 0
        for k in (a[i]):
            summ += k
        sum_list.append(summ)
    return sum_list


def col_sums(a):
    sum_list = []

    for i in range(len(a[0])):
        summ = 0
        for k in range(len(a)):
            summ += a[k][i]
        sum_list.append(summ)

    return sum_list


print(row_sums([[1, 2, 3], [4, 5, 6]]))
```
![Картинка 1](./image/lab02/02.02.png)
![Картинка 2](./image/lab02/02.02.02.png)
![Картинка 3](./image/lab02/02.02.03.png)

### Задание номер 3
```python
def format_record(a):
    fio_clean = a[0].strip()
    while "  " in fio_clean:
        fio_clean = fio_clean.replace('  ', ' ')
    FIO = fio_clean.split()

    if len(FIO) == 3:

        return f"{FIO[0]} {FIO[1][0]}.{FIO[2][0]}., гр. {a[1]}, GPA {round(a[2]):.2f} "
    elif len(FIO) == 2:
        return f"{FIO[0]} {FIO[1][0]}., гр. {a[1]}, GPA {round(a[2]):.2f}"
    else:
        return ('ValueError')


print(format_record(('    Громов     Гордей        Александрович    ', 'БИВТ-25', 3.49)))
```
![Картинка 4](./image/lab02/03.02.png)

# Лабораторная работа 3
### Задание A

```python
from src.lib.text import *

print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка", yo2e=True))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))

print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

print(top_n(count_freq(["a", "b", "a", "c", "b", "a"]), n=2))
print(top_n(count_freq(["bb", "aa", "bb", "aa", "cc"]), n=2))
```
```python
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.lib.text import*

text = sys.stdin.read()

textn = text

text = normalize(text)
text = tokenize(text)
textn = text
top = top_n(count_freq(text), n = 5)
text = top_n(count_freq(text))


print(f"Всего слов: {len(textn)}")
print(f"Уникальных слов: {len(text)}")
print("Топ-5:")
for word, count in top:
    print(f"{word}: {count}")
```
![Картинка 1](./image/lab03/a.png)
![Картинка 2](./image/lab03/b.png)

# Лабораторная работа 4
### Задание A

```python
import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encording: str = "cp1251") -> str:
    p = Path(path)

    if p.exists() == False:
        raise FileNotFoundError

    if len(p.read_text(encoding=encording)) <= 0:
        return ''

    return p.read_text(encoding=encording)


def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)

    for i in range(len(rows) - 1):

        if len(rows[i]) != len(rows[i + 1]):
            raise ValueError

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)

        if header is not None:
            w.writerow(header)

        for r in rows:
            w.writerow(r)

```
```python
from src.lab04.io_txt_csv import *
from src.lib.text import *

b = read_text("/Users/grom61/PycharmProjects/python_labs/data/input.txt")
b = normalize(b)
b = tokenize(b)
b_ = b
b = count_freq(b)
top = top_n(b,5)
b = top_n(b)


write_csv(
    rows = b,
    path = "/Users/grom61/PycharmProjects/python_labs/data/report.csv",
    header=["Word","Count"]
)

print(f"Всего слов: {len(b_)}")
print(f"Уникальных слов: {len(b)}")
print("Топ-5:")
for word, count in top:
    print(f"{word}: {count}")
```
![Картинка 1](./image/lab04/11.png)
![Картинка 2](./image/lab04/12.png)
![Картинка 3](./image/lab04/13.png)
![Картинка 4](./image/lab04/21.png)
![Картинка 5](./image/lab04/22.png)
![Картинка 6](./image/lab04/23.png)
![Картинка 7](./image/lab04/31.png)
![Картинка 8](./image/lab04/32.png)
![Картинка 9](./image/lab04/33.png)

