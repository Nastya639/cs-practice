def winner(names, scores):
    TheBest=float('-inf')
    name=''
    for i in range(len(scores)):
        if scores[i]>TheBest:
            TheBest=scores[i]
            name=names[i]
    return name

def average(scores):
    if len(scores)==0:
        return 0.0
    return round(sum(scores)/len(scores),2)

def ranking(names, scores):
    indices=list(range(len(scores)))
    indices.sort(key=lambda x: (-scores[x],x))
    res=[names[i] for i in indices]
    return res

def above_average(names, scores):
    avg=average(scores)
    res=[]
    for i in range(len(scores)):
        if scores[i]>avg:
            res.append(names[i])
    return res

if __name__=="__main__":
    names=['Аня','Вика','Саша']
    scores=[9.0,2.3,5.6]
    print(ranking(names,scores))
