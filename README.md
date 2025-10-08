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
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список не может быть пустым")
    return (min(nums), max(nums))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    result = []
    for item in mat:
        if not isinstance(item, (list, tuple)):
            raise TypeError(f"Элемент должен быть списком или кортежем, получен {type(item)}")
        result.extend(item)
    return result

print(flatten([[1, 2, 3], [], [4, 5]]))
```
![Картинка 1](./image/lab02/01.02.png)
![Картинка 1](./image/lab02/01.02.02.png)
![Картинка 1](./image/lab02/01.02.03.png)

### Задание номер 2
```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    result = []
    
    for i in range(len(mat) - 1):
        if len(mat[i]) < len(mat[i+1]) or (len(mat[i]) > len(mat[i+1])):
            print('ValueError')
            return
    
    for i in range(len(mat[0])):
        new_list = []
        for k in range(len(mat)):
            new_list.append(mat[k][i])
        result.append(new_list)
    
    return result

def row_sums(mat: list[list[float | int]]) -> list[float]:
    
    sum_list = []
    
    for i in range(len(mat)):
        summ = 0
        for k in (mat[i]):
            summ += k
        sum_list.append(summ)
    return sum_list

def col_sums(mat: list[list[float | int]]) -> list[float]:

    sum_list = []

    for i in range(len(mat[0])):
        summ = 0
        for k in range(len(mat)):
            summ += mat[k][i]
        sum_list.append(summ)
    
    return sum_list

print(col_sums([
    [1,2,3],
    [4,5,6]
]))
```
![Картинка 5](./image/lab02/02.02.png)
![Картинка 5](./image/lab02/02.02.02png)
![Картинка 5](./image/lab02/02.02.03png)

### Задание номер 3
```python
def format_record(rec: tuple[str, str, float]) -> str:
    fio_clean = rec[0].strip()
    while "  " in fio_clean:
        fio_clean = fio_clean.replace('  ', ' ')
    FIO = fio_clean.split()

    if len(FIO) == 3:

        return f"{FIO[0]} {FIO[1][0]}.{FIO[2][0]}., гр. {rec[1]}, GPA {round(rec[2]):.2f} "
    elif len(FIO) == 2:
        return f"{FIO[0]} {FIO[1][0]}., гр. {rec[1]}, GPA {round(rec[2]):.2f}"
    else:
        return ('ValueError')


print(format_record(('    Громов     Гордей        Александрович    ', 'БИВТ-25', 3.49)))
```
![Картинка 4](./image/lab02/03.02.png)
