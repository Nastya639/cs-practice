names=input('Введите имена через пробел: ').split()
scores=[float(x) for x in input('Введите баллы через пробел: ').split()]

def winner(names: list[str], scores: list[float]) -> str:
    TheBest=float('-inf')
    name=''
    for i in range(len(scores)):
        if scores[i]>TheBest:
            TheBest=scores[i]
            name=names[i]
    return name




    