def read_rows(lines: list[str]) -> list[dict]:
    if not lines:
        return []
    headers=lines[0].strip().split(',')
    rows=[]
    for line in lines[1:]:
        values=line.strip().split(',')
        if len(values)!=len(headers) or not values[0].strip():
            continue
        row_dict=dict(zip(headers,values))
        rows.append(row_dict)
    return rows
def count_types(rows: list[dict]) -> dict:
    counts={}
    for row in rows:
        type_value=row.get('тип')
        if type_value not in counts:
            counts[type_value]=1
        else:
            counts[type_value]+=1
    return counts





    


