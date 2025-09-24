time = int(input('Минуты: '))
hour = (time // 60) % 24
minute = time % 60
print(f'{hour}:{minute}')