def read_rows(lines):
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
def count_types(rows):
    counts={}
    for row in rows:
        type_value=row.get('тип')
        if type_value not in counts:
            counts[type_value]=1
        else:
            counts[type_value]+=1
    return counts
def total_minutes(rows, kind):
    total=0.0
    for row in rows:
        minutes=row.get('минуты')
        if row.get('тип')==kind:
            try:
                total+=float(minutes)
            except:
                continue
    return round(total,1)
def to_csv(counts):
    result='тип,количество\n'
    sorted_counts=sorted(counts.keys())
    for type_value in sorted_counts:
        value=counts[type_value]
        result+=f'{type_value},{value}\n'
    return result



    


