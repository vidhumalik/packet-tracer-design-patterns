from director import *
from pathTree import *

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
                    name = inputName(adjMat)
                    ipaddress = inputIp('IP address', adjMat, IPList)
                    subnetmask = None
                    gateway = inputIpForRoutingTable("Enter Gateway: ", adjMat, IPList)
                    dnsserver = None
                    director.setBuilder(PCBuilder())
                    pc = director.createComponent(name = name, ipaddress = ipaddress, subnetmask = subnetmask, gateway = gateway, dnsserver = dnsserver)
                    print("The current list of objects that exists is as follows:")
                    print(list(adjMat["byName"].keys()))
                    PCListByIp[ipaddress] = pc
                    print("Enter the name of object that this given PC connects to. To not enter a link, enter 0")
                    print(pc)
                    linkChoice = checkName('',adjMat)
                    director.createLink(linkChoice)
                 
                    pc.specification()

                elif(choice2 == 2):
                    print("Enter the following details:")
                    name = inputName(adjMat) 
                    director.setBuilder(HubBuilder())
                    hub = director.createComponent(name = name)
                    print("The current list of objects that exists is as follows:")
                    print(list(adjMat["byName"].keys()))
                    print("Enter the names of objects that this given Hub connects to. To stop entering links, enter 0")
                    linkChoice = checkName('', adjMat) #raw_input()
                    director.createLink(linkChoice)
                    
                    hub.specification()
                elif(choice2 == 3):
                    print("Enter the following details:")
                    name = inputName(adjMat) #raw_input("Enter Name: ")
                    mac =  raw_input("Enter mac address: ")
                    print("Enter the details pertaining to the ethernet ports. Maximum number of ports in a router is 4")
                    count= 1
                    tostop2 = 0
                    fastethernet =[]
                    temp = {}
                    while(count <= 4 and not tostop2):
                        choice3 = raw_input("Details for port"+str(count)+"\nPress any key to continue, or press 0 to skip setup of this port: ")
                        if(choice3 != '0'):
                            temp = {}
                            temp["mac"] = mac
                            temp["ipaddress"] = inputIp('ip address for this port',adjMat, IPList) #raw_input("Enter ip address: ")
                            temp["subnetmask"] = None #inputIp('subnet mask')
                            fastethernet.append(temp)
                        count += 1
                    print("Enter the details pertaining to the Routing Table Entries")
                    tostop3 = 0
                    routes =[]
                    while(not tostop3):
                        choice4= raw_input("Press any key to add to routing table. Enter 0 to stop adding routing table entries:")
                        if(choice4 != '0'):
                            temp = {}
                            temp["network"] = inputIpForRoutingTable('network address',adjMat, IPList)
                            temp["mask"] = None 
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
                    director.setBuilder(RouterBuilder())
                    router = director.createComponent(name = name, fastethernet = fastethernet, routes = routes)
                    print("The current list of objects that exists is as follows:")
                    print(list(adjMat["byName"].keys()))
                    print("Press any key to add a router link. To stop entering links, enter 0")
                    linkChoice = raw_input()
                    director.createLink(linkChoice)
                    router.specification()

                else:
                    continue
            elif(choice1 == 2):
                tostop = 1
                print(adjMat)
            else:
                continue

    print(PCListByIp)


    def printTree(treeRoot):
        children = treeRoot.getChildren()
        print('('+str(treeRoot.getCurrNode().getName())+','+str(treeRoot)+' : '+str(children))
        for i in children:
            printTree(i)


    def pingTraverse(ping, rootTree):
        curr = rootTree.getCurrNode()
        ping['visitedObjs'].append(curr)
        childList = curr.send(ping, adjMat)
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
        src = inputIpExisting('source IP address', adjMat, IPList) 
        dst = inputIpExisting('destination IP address', adjMat, IPList) 
        ping = {'sourceIP':src,'destinationIP':dst,'visitedObjs':[]}
        if src not in adjMat['byIp']:
            print('Failed ping')
            continue
        if src == dst:
            print('Successful ping')
            continue
        currentObjs = [adjMat['byIp'][src]]
        pingTraverseTree = pathNode(PCListByIp[src],None)
        resultTree = pingTraverse(ping, pingTraverseTree)
        if resultTree == True:
            print('Successful ping')
        else:
            print('Ping failed')
        #printTree(pingTraverseTree)
        




if __name__ == "__main__":
    main()
