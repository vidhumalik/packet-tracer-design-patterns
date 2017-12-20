
adjMat = {}
adjMat["byName"] = {}
adjMat["byObj"] = {}
adjMat['byIp'] = {}
def inputIp(toEnter, adjMat, IPList):
    valid = True
    str1 = 'Please enter '+toEnter+': '
    str2 = 'Invalid entry. Please re-enter '+toEnter+': '
    inp = raw_input(str1)
    while True:
        ret = ''
        checker = inp.split('.')
        valid = True
        for i in checker:
            str3 = '0'*(3-len(i)) + i
            ret += str3 + '.'
        ret = ret[:-1]
        if len(checker) != 4 or ret in IPList:
            valid = False
        for i in checker:
            if len(i)==0 or int(i)<0 or int(i)>255:
                valid = False
        if valid == True:
            IPList.append(ret)
            return ret
        inp = raw_input(str2)

def inputIpForRoutingTable(toEnter, adjMat, IPList):
    valid = True
    str1 = 'Please enter '+toEnter+': '
    str2 = 'Invalid entry. Please re-enter '+toEnter+': '
    inp = raw_input(str1)
    ret = ''
    while True:
        checker = inp.split('.')
        valid = True
        if len(checker) != 4:
            valid = False
        for i in checker:
            if len(i)==0 or int(i)<0 or int(i)>255:
                valid = False
        if valid == True:
            for i in checker:
                str3 = '0'*(3-len(i)) + i
                ret += str3 + '.'
            ret = ret[:-1]
            return ret
        inp = raw_input(str2)

def inputIpExisting(toEnter, adjMat, IPList):
    valid = True
    str1 = 'Please enter '+toEnter+': '
    str2 = 'Invalid entry. Please re-enter '+toEnter+': '
    inp = raw_input(str1)
    while True:
        ret = ''
        checker = inp.split('.')
        valid = True
        for i in checker:
            str3 = '0'*(3-len(i)) + i
            ret += str3 + '.'
        ret = ret[:-1]
        if len(checker) != 4 or ret not in IPList:
            valid = False
        for i in checker:
            if len(i)==0 or int(i)<0 or int(i)>255:
                valid = False
        if valid == True:
            return ret
        inp = raw_input(str2)

def inputName(adjMat):
    inp = raw_input('Enter name: ')
    while True:
        if inp not in adjMat['byName']:
            return inp
        inp = raw_input('Name already exists. Please re-enter unique name: ')

def checkName(msg, adjMat):
    inp = raw_input(msg)
    while True:
        print adjMat['byName']
        if inp in adjMat['byName'] or inp=='0':
            return inp
        inp = raw_input('Object does not exist. Enter existing object name: ')
