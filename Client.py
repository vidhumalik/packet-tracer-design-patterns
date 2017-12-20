from director import *
from pathTree import *
from inputProcessing import *

def main():
    director = Director()
    tostop = 0
    isfirst=1
    #adjMat = {}
    adjMat["byName"] = {}
    adjMat["byObj"] = {}
    adjMat['byIp'] = {}
    PCListByIp = {}
    while(not tostop):
        if(isfirst):
            print("Choose to add one of the following components:")
            isfirst = 0
        else:
            print("Make a choice:")
            choice1=int(raw_input("1. Add a new component \n2. Setting Up of network is done \n"))
            if(choice1 == 1):
                print("Which component do you want to add:")
                choice2=int(raw_input("1. PC \n2. Hub \n3. Router\n"))
                if(choice2 == 1):
                    print("Enter the following details:")
                    name = inputName(adjMat) #raw_input("Enter Name: ")
                    ipaddress = inputIp('IP address', adjMat, IPList)
                    #subnetmask = raw_input("Enter Subnet Mask: ") #inputIp('subnet mask')
                    subnetmask = None
                    gateway = inputIpForRoutingTable("Enter Gateway: ", adjMat, IPList) #raw_input("Enter gateway: ")
                  #  dnsserver = raw_input("Enter DNS Server: ") #inputIp('DNS server')
                    dnsserver = None
                    director.setBuilder(PCBuilder())
                    pc = director.createComponent(name = name, ipaddress = ipaddress, subnetmask = subnetmask, gateway = gateway, dnsserver = dnsserver)
                    #adjMat["byName"][name] = pc
                    print("The current list of objects that exists is as follows:")
                    print(list(adjMat["byName"].keys()))
                    PCListByIp[ipaddress] = pc
                    print("Enter the name of object that this given PC connects to. To not enter a link, enter 0")
                    print(pc)
                    linkChoice = checkName('',adjMat) #raw_i()
                    if(linkChoice != '0'):
                        #ensure that linkchoice is valid
                        print('linkChoice: '+str(linkChoice))
                        #director.createLink(linkChoice)
                        tempObj = adjMat["byName"][linkChoice]
                        if pc in adjMat['byObj']:
                            adjMat['byObj'][pc].append(tempObj)
                        else:
                            adjMat['byObj'][pc] = [tempObj]
                        if tempObj in adjMat['byObj']:
                            adjMat['byObj'][tempObj].append(pc)
                        else:
                            adjMat['byObj'][tempObj] = [pc]

                        #Taking care of adjMat['byIp']
                        adjMat['byIp'][pc.getIPAddress()] = tempObj
                        tempObjType = tempObj.getType()
                        if tempObjType == 'PC':
                            adjMat['byIp'][tempObj.getIPAddress()] = pc
                        elif tempObjType == 'Router':
                            portNum = int(raw_input('Enter port number of router to connect to: '))
                            ipOfRouter = tempObj.getFastEthernet()[portNum-1]['ipaddress']
                            adjMat['byIp'][ipOfRouter] = pc

                        #invalid link check
                       # linkChoice = checkName('') #raw_input()
                    pc.specification()

                elif(choice2 == 2):
                    print("Enter the following details:")
                    name = inputName(adjMat) #raw_input("Enter Name: ")
                    director.setBuilder(HubBuilder())
                    hub = director.createComponent(name = name)
                    #adjMat["byName"][name] = hub
                    print("The current list of objects that exists is as follows:")
                    print(list(adjMat["byName"].keys()))
                    print("Enter the names of objects that this given Hub connects to. To stop entering links, enter 0")
                    linkChoice = checkName('', adjMat) #raw_input()
                    while(linkChoice != '0'):
                        #ensure that linkchoice is valid
                        tempObj = adjMat["byName"][linkChoice]
                        if hub in adjMat['byObj']:
                            adjMat['byObj'][hub].append(tempObj)
                        else:
                            adjMat['byObj'][hub] = [tempObj]
                        if tempObj in adjMat['byObj']:
                            adjMat['byObj'][tempObj].append(hub)
                        else:
                            adjMat['byObj'][tempObj] = [hub]

                        #Taking care of adjMat['byIp']
                        tempObjType = tempObj.getType()
                        if tempObjType == 'PC':
                            adjMat['byIp'][tempObj.getIPAddress()] = hub
                        elif tempObjType == 'Router':
                            portNum = int(raw_input('Enter port number of router to connect to: '))
                            ipOfRouter = tempObj.getFastEthernet()[portNum-1]['ipaddress']
                            adjMat['byIp'][ipOfRouter] = hub

                        #invalid link check
                        linkChoice = checkName('', adjMat) #raw_input()
                    hub.specification()
                elif(choice2 == 3):
                    print("Enter the following details:")
                    name = inputName(adjMat) #raw_input("Enter Name: ")
                    print("Enter the details pertaining to the ethernet ports. Maximum number of ports in a router is 4")
                    count= 1
                    tostop2 = 0
                    fastethernet =[]
                    temp = {}
                    '''
                    temp["mac"] = raw_input("Enter mac address: ")
                    temp["ipaddress"] = raw_input("Enter ip address: ")
                    temp["subnetmask"] = raw_input("Enter subnet mask: ")
                    fastethernet.append(temp)
                    '''
                    while(count <= 4 and not tostop2):
                        choice3 = raw_input("Details for port"+str(count)+"\nPress any key to continue, or press 0 to skip setup of this port: ")
                        if(choice3 != '0'):
                            temp = {}
                            temp["mac"] = raw_input("Enter mac address: ")
                            temp["ipaddress"] = inputIp('network address',adjMat, IPList) #raw_input("Enter ip address: ")
                            temp["subnetmask"] = None #inputIp('subnet mask')
                            fastethernet.append(temp)
                            '''
                        else:
                            tostop2 = 1
                            '''
                        count += 1
                    print("Enter the details pertaining to the Routing Table Entries")
                    tostop3 = 0
                    routes =[]
                    while(not tostop3):
                        choice4= raw_input("Press any key to add to routing table. Enter 0 to stop adding routing table entries:")
                        if(choice4 != '0'):
                            temp = {}
                            temp["network"] = inputIpForRoutingTable('network address',adjMat, IPList)
                            temp["mask"] = None # raw_input("Enter subnet mask: ") #inputIp('subnet mask')
                            temp["nexthop"] = inputIpExisting('next hop IP address',adjMat, IPList)
                            zeroFrom = len(temp['network']) #should be 15, for format xxx.xxx.xxx.xxx
                            while zeroFrom > 0:
                                if temp['network'][zeroFrom-1]=='0' or temp['network'][zeroFrom-1]=='.':
                                    zeroFrom -= 1
                                else:
                                    break
                            temp['zeroFrom'] = zeroFrom
                            routes.append(temp)
                        else:
                            tostop3 = 1
                    #print(routes)
                    director.setBuilder(RouterBuilder())
                    router = director.createComponent(name = name, fastethernet = fastethernet, routes = routes)
                    #adjMat["byName"][name] = router
                    print("The current list of objects that exists is as follows:")
                    print(list(adjMat["byName"].keys()))
                    print("Press any key to add a router link. To stop entering links, enter 0")
                    linkChoice = raw_input()
                    while(linkChoice != '0'):
                        #ensure that linkchoice is valid
                        linkChoice = checkName('Enter name of object to connect to: ',adjMat) #raw_input('Enter name of object to connect to: ')
                        portNum1 = int(raw_input('Enter port number of router to connect to: '))
                        tempObj = adjMat["byName"][linkChoice]
                        if router in adjMat['byObj']:
                            adjMat['byObj'][router].append(tempObj)
                        else:
                            adjMat['byObj'][router] = [tempObj]
                        if tempObj in adjMat['byObj']:
                            adjMat['byObj'][tempObj].append(router)
                        else:
                            adjMat['byObj'][tempObj] = [router]

                        #Taking care of adjMat['byIp']
                        #print(router.getFastEthernet())
                        adjMat['byIp'][router.getFastEthernet()[portNum1-1]['ipaddress']] = tempObj
                        tempObjType = tempObj.getType()
                        if tempObjType == 'PC':
                            adjMat['byIp'][tempObj.getIPAddress()] = router
                        elif tempObjType == 'Router':
                            portNum = int(raw_input('Enter port number of router to connect to: '))
                            ipOfRouter = tempObj.getFastEthernet()[portNum-1]['ipaddress']
                            adjMat['byIp'][ipOfRouter] = router

                        #invalid link check
                        linkChoice = raw_input()
                    router.specification()

                else:
                    continue
            elif(choice1 == 2):
                tostop = 1
                print(adjMat)
            else:
                continue

    #print('out of loop')

    print(PCListByIp)
    '''
    while True:
        print('\n\n\n\nPing trial:')
        src = inputIpExisting('source IP address') #raw_input('Enter source IP: ')
        dst = inputIpExisting('destination IP address') #raw_input('Enter destination IP: ')
        ping = {'sourceIP':src,'destinationIP':dst,'visitedObjs':[]}
        if src not in adjMat['byIp'] or dst not in adjMat['byIp']:
            print('Failed ping')
            continue
        #print(ping)
        currentObjs = [adjMat['byIp'][src]]
        #print(currentObjs)
        pingInTransit = True
        while pingInTransit:
            newList = []
            for device in currentObjs:
                if device.receive(ping) == True:
                    print('Successful ping')
                    ping['status'] = True
                    pingInTransit = False
                    break
                else:
                    try:
                        newList += device.send(ping)
                    except KeyError:
                        print('KeyError')
                    #print('nl  '+str(newList))
                    #raw_input('prompt')
            if len(newList) == 0 and pingInTransit:
                print('Failed ping')
                pingInTransit = False
            else:
                currentObjs = newList
    '''

    def printTree(treeRoot):
        children = treeRoot.getChildren()
        print('('+str(treeRoot.getCurrNode().getName())+','+str(treeRoot)+' : '+str(children))
        for i in children:
            printTree(i)


    def pingTraverse(ping, rootTree):
        curr = rootTree.getCurrNode()
        ping['visitedObjs'].append(curr)
        childList = curr.send(ping, adjMat)
        #print(childList)
        for i in childList:
            if i in ping['visitedObjs']:
                continue
            child = pathNode(i, curr)
            rootTree.addChild(child)
            print(str(rootTree.getCurrNode().getName()))
            print(' : ')
            print(str(i.getName()))
            raw_input('')
            if i.receive(ping) == True:
                return True
            currResult = pingTraverse(ping, child)
            if currResult == True:
                return True

    while True:
        print('\n\n\n\nPing trial:')
        src = inputIpExisting('source IP address', adjMat, IPList) #raw_input('Enter source IP: ')
        dst = inputIpExisting('destination IP address', adjMat, IPList) #raw_input('Enter destination IP: ')
        ping = {'sourceIP':src,'destinationIP':dst,'visitedObjs':[]}
        if src not in adjMat['byIp']:# or dst not in adjMat['byIp']:
            print('Failed ping')
            continue
        if src == dst:
            print('Successful ping')
            continue
        currentObjs = [adjMat['byIp'][src]]
        pingTraverseTree = pathNode(PCListByIp[src],None)
        #pingTraverseTree.addChildren(currentObjs)
        resultTree = pingTraverse(ping, pingTraverseTree)
        if resultTree == True:
            print('Successful ping')
        else:
            print('Ping failed')
        #printTree(pingTraverseTree)
        




if __name__ == "__main__":
    main()
