import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()

    if yo2e:
        text = text.replace('ё', 'е').replace("Ё", "Е")

    for ch in ['\n', '\r', '\t']:
        text = text.replace(ch, ' ')

    while '  ' in text:
        text = text.replace('  ', ' ')

    return text.strip()


"""
legal_chars = set()

for i in range(65, 123):
    legal_chars.add(chr(i))


for i in range(1040, 1104):
    legal_chars.add(chr(i))

for i in range(0, 10):
    legal_chars.add(str(i)) 

legal_chars.update(['-', '_'])

def tokenize(text: str) -> list[str]:

    true_text = ''

    for ch in text:

        if ch in legal_chars:
            true_text += ch

        else:
            true_text += ' ' 

    true_text = normalize(true_text)

    return true_text.split()
"""


def tokenize(text: str) -> list[str]:
    text = normalize(text, casefold=True, yo2e=True)
    pattern = r'\w+(?:-\w+)*'

    return re.findall(pattern, text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    sbor = {}

    for i in range(len(tokens)):

        if tokens[i] in sbor:
            continue

        else:
            sbor[tokens[i]] = tokens.count(tokens[i])

    return sbor


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda item: (-item[1], item[0]))

    return sorted_items[:n]
