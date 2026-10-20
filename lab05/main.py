from tablestats import *
def main():
    path=input().strip()
    with open(path,encoding='utf-8') as table:
        lines=table.readlines()
        rows=read_rows(lines)
    counts=count_types(rows)
    sum_min=total_minutes(rows,'ошибка')
    print(len(rows))
    print(len(counts))
    print(sum_min)
    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(to_csv(counts))
if __name__ == "__main__":
    main()
