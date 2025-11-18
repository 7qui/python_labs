import argparse
from src.lib.text import count_freq, tokenize, normalize, top_n
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        """ Реализация команды cat """

        with Path(args.input).open("r", newline='', encoding = 'utf8') as f:
            people = f.read()
            list_p = people.split()

        count = 0

        if args.n:
            for peo in list_p:
                count += 1
                print(f"{count} {peo}")

        else:
            for peo in list_p:
                print(f"{peo}")

    elif args.command == "stats":
        """ Реализация команды stats """

        with Path(args.input).open("r", newline='', encoding = 'utf8') as f:
            people = f.read()

        final = top_n(count_freq(tokenize(normalize(people))), args.top)

        for word, count in final:
            print(f"{word}: {count}")
        
if __name__ == "__main__":
    main()
       