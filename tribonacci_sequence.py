def tribonacci_sequence(start_sequence, length):
    r = []
    match(length):
        case 0:
            return []
        case 1:
            return start_sequence[0:1]
        case 2: 
            return start_sequence[0:2]
        case 3:
            return start_sequence[0:3]

    r = start_sequence + [sum(start_sequence)]
    
    for i in range(4,length):
        r.append(sum(r[i-3:i+1]))
    return r

print(tribonacci_sequence([0, 0, 1], 20))

