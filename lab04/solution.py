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

def average(scores: list[float]) -> float:
    if len(scores)==0:
        return 0.0
    return round(sum(scores)/len(scores),2)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    indices=list(range(len(scores)))
    indices.sort(key=lambda x: (-scores[x],x))
    res=[names[i] for i in indices]
    return res



    