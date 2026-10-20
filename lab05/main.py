from tablestats import *
def main():
    path=input().strip()
    with open(path,encoding='utf-8') as table:
        lines=table.readlines()
        rows=read_rows(lines)
    counts=count_types(rows)
    sum_min=total_minutes(rows,'ошибка')
    print(f'Записей прочитано: {len(rows)}')
    print(f'Количеcтво различных типов: {counts}')
    print(f'Суммарное количество минут для типа "Ошибка": {sum_min}')
    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(to_csv(counts))
if __name__ == "__main__":
    main()
