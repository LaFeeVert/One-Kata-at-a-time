def add(string):
    if string == '':
        return '0'
    
    pos = string.find(',\n')
    if pos != -1:
        raise ValueError(f"Number expected but '\n' found at position {pos+1}.")
    string = string.replace('\n', ',')

    if string.endswith(','):
        raise ValueError("Number expected but EOF found.")

    delim = ','
    if string.startswith('//'):
        delim, string = string.split(delim, 1)
        delim = delim[2:]
        pos = string.find(',')
        if pos != -1:
            raise ValueError(f"'{delim}' expected but ',' found at position {pos}.")

    numbers = string.split(delim)
    numbers = list(map(int, numbers))
    
    negatives = [num for num in numbers if num < 0]
    if negatives:
        nstr = ', '.join(map(str,negatives))
        raise ValueError(f"Negative not allowed : {nstr}")        

    return str(sum(numbers))