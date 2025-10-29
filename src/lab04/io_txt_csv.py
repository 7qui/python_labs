import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encording: str = "utf-8") -> str:
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

