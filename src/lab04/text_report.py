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