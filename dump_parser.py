
import fileinput

def get_breakpoints(dumpfile):
    '''Returns a list of line numbers that represent line number
    in the dumpfile for each unique encapsulated table
    '''
    
    breakpoints = [] # list of line numbers starting new subtable
    cur_line = 0
    
    with open(dumpfile) as f:
        for line in f:
            if line != ' \n' and line[0] == ' ':
                breakpoints.append(cur_line)
            cur_line += 1
    
    #print(breakpoints)
    return(breakpoints)
        
def print_table(table):
    '''Prints the table out to console'''
    
    print('>> Sub-Table Records:', len(table) - 1,'<<')
    row = 0
    while row < len(table):
        print(table[row], end='')
        row += 1
    print('\n-----------------\n')


def main():
    
    breakpoints = get_breakpoints('dump.txt')
    #print(breakpoints)
    
    in_subtable_flag = False
    
    with fileinput.input('dump.txt') as f:
        for line in f:
            line_num = fileinput.filelineno()
            if line_num in breakpoints:    # line begins subtable
                print('>> Subtable #', breakpoints.index(line_num), ' @ line '+
                 '{}'.format(line_num))
                in_subtable_flag = True  
                subtable = []
            elif (line_num not in breakpoints) and in_subtable_flag:
                subtable.append(line)
            
            # At end of subtable section, print out the subtable
            if (line_num +1 in breakpoints) and in_subtable_flag:
                print_table(subtable)
                              
    
if __name__ == "__main__": main()