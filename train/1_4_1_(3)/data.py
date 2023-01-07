with open('临时','r+') as f:
    for line in f:
        line = line.replace('\'','')
        line = line.replace('dtype=object','')
        line = line.replace('),','')
        line = line.replace('array(','')
        line = line.replace(', =,', '=[')

        # line = line.replace('array(', '')
        print(line)

