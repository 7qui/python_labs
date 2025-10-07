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