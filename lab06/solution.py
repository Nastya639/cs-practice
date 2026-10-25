def count_items(values):
    counts={}
    for value in values:
        counts[value]=counts.get(value,0)+1
    return counts

