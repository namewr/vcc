import calc

para_name = ('target', 'prog')

para = {'target': [],
        'prog' :[]}

def init_Target(file_name = 'vcc_target.vcc'):
    init_file = open(file_name, 'r')
    for line in init_file:
        if line[0] == '#':
            continue
        
        l_list = line.strip('\n').split(' ')
        for each in para_name:
            if l_list[0] == each:
                if len(l_list) < 3:
                    print ("something bad happened")
                    return None
                if len(l_list) < 4:
                    l_list[3] = None
                    
                para[each].append(l_list[1:])

    #replace the prog with absolute path
    '''
    for each in para['prog']:
        each[1] = search(each[1])

    for each in para['target']:
        each[3] = (each[3])
    ''' 
    #deal with prog
    
    return
        
def parse(string):
    # should be large enough
    min_dis = 100000000
    min_lst = None

    for e_list in para:
        for elm in para[e_list]:
             #get the minimal element or a threshold uses to fast the programs
            if elm[2] == None:
                print ("lacking a pinyin")
                return None
            temp = calc.calc(string, elm[2])
            if temp < min_dis:
                min_dis = temp
                min_lst = [e_list ,elm]

    return min_lst
