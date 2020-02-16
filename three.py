def ensure_has_divisible(items,divisor):

    for item in items:
        if item % divisor == 0:
            return item
            
    
    items.append(divisor)
    return divisor
items = [2,3,15,9,36]
divisor = 12
print("{items} contain {found} which is multiple by {divisor}".format(**locals()))