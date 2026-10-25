def read_rows(lines):
    headers=None
    rows=[]
    for line in lines:
        line_str=line.strip()
        if not line_str:
            continue
        values=[f.strip() for f in line_str.split(',')]
        if headers is None:
            headers=values
            continue
        if len(values)!=len(headers):
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
        row_kind = str(row.get('тип')).strip().lower()
        if row_kind.get('тип')==kind:
            minutes=row.get('минуты')
            try:
                minutes_clean = str(minutes).replace(',', '.').strip()
                total+=float(minutes_clean)
            except (ValueError,TypeError):
                continue
    return round(total,1)
def to_csv(counts):
    result='тип,количество\n'
    sorted_counts=sorted(counts.keys())
    for type_value in sorted_counts:
        value=counts[type_value]
        result+=f'{type_value},{value}\n'
    return result



    


