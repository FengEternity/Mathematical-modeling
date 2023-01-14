with open('销量变化购运方案2.txt', 'r+') as f:
    for line in f.readlines():
        line = line.replace('                               ', '')
        line = line.replace('                              ', '')
        line = line.replace('       ', ',')
        line = line.replace(' ', '')
        line = line.replace('SA(', '')
        line = line.replace(')', '')
        print(line)
