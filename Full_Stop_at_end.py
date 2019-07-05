with open('Fani_Informative_Unique.csv', 'r') as istr:
    with open('Fani_Informative_Unique_Full_Stop.csv', 'w') as ostr:
        for i, line in enumerate(istr):
            # Get rid of the trailing newline (if any).
            line = line.rstrip('\n')
            if i % 2 == 0:
                line += '.'
            else:
                line += '.'
            print(line, file=ostr)