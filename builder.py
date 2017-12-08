#import flyweight

currObjs = []
adjMat = {}
IPList = []
'''
Ping working:
Main class keeps a list of objects where ping is at the moment, and runs send function on all of them.
The send function will update the list of current objects.
'''

class FlyweightFactory:
    """
    Create and manage flyweight objects.
    Ensure that flyweights are shared properly. When a client requests a
    flyweight, the FlyweightFactory object supplies an existing instance
    or creates one, if none exists.
    """

    def __init__(self):
        self._flyweights = {'PC':PCFlyweight(),'Hub':HubFlyweight(),'Router':RouterFlyweight()}

    def get_flyweight(self, key):
        try:
            flyweight = self._flyweights[key]
        except KeyError:
            flyweight = ConcreteFlyweight()
            self._flyweights[key] = flyweight
        return flyweight


class Flyweight():
    def __init__(self):
        self.intrinsic_state = None

    def receive(self, extrinsic_state, ping):
        '''
        Ping is a dictionary for ping details, like {destinationIP:__, sourceIP:__, visitedObjs:[]...}
        Similarly, extrinsic_state={IP:__, ...}
        Return value: True for successful ping, False otherwise
        '''
        pass
    
    def send(self, extrinsic_state, ping):
        pass


class ConcreteFlyweight(Flyweight):
    def receive(self, extrinsic_state, ping):
        pass
    def send(self, extrinsic_state, ping):
        pass

class PCFlyweight(Flyweight):
    '''
    Calls actually will be like PC.send(ping) or PC.receive(ping) to PC class.
    PC class will call the flyweight version of the functions, passing the extrinsic_state.
    Same for hub and router classes
    '''
    def receive(self, extrinsic_state, ping):
        '''
        print('In PC')
        print(ping)
        print(extrinsic_state)
        print('-----')
        '''
        if extrinsic_state['IP'] == ping['destinationIP']:
            return True
        return False
    def send(self, extrinsic_state, ping):
        forwardToObj = adjMat['byIp'][extrinsic_state['IP']]
        return [forwardToObj]

class HubFlyweight(Flyweight):
    def receive(self, extrinsic_state, ping): #pass, because hub doesnt perform any processing based on the ping, as PC needs to
        pass
    def send(self, extrinsic_state, ping): #Returns list of objects that hub will forward the ping to
        '''
        print('in Hub')
        print(self)
        print('-----')
        '''
        forwardToObjList = adjMat['byObj'][extrinsic_state['Hub']]
        return forwardToObjList

class RouterFlyweight(Flyweight):
    '''
    Routing table sample (extrinsic_state['routingTable'])
    {destIP:portNumberOfRouter, destIP:portNumberOfRouter, ...}
    
    Sample extrinsic_state['ports'] = {portNumberOfRouter: IPofPort, portNumberOfRouter: IPofPort, ...}
    
    '''
    def receive(self, extrinsic_state, ping): #pass, because router doesnt perform any processing based on the ping, as PC needs to
        pass
    def send(self, extrinsic_state, ping): #Returns object that router will forward the ping to, as a list
        '''
        portOfRouter = extrinsic_state['routingTable'][ping['destinationIP']]
        IPofRouterPort = extrinsic_state['ports'][portOfRouter]
        forwardToObj = adjMat['byIp'][IPofRouterPort]
        '''
        portOfRouter = -1
        forwardToObj = None
        routingTable = extrinsic_state['routingTable']
        for route in routingTable:
            #if route.network.network.ipaddress[:route.zeroFrom] == ping['destinationIP'][:route.zeroFrom]:
            if route['network'][:route['zeroFrom']] == ping['destinationIP'][:route['zeroFrom']]:
                #to forward on this route
                #routerPortIp = route.nexthop.gateway.ipaddress
                forwardToObj = adjMat['byIp'][route['nexthop']]
                break
        return [forwardToObj]










flyweightFactory = FlyweightFactory()

class Director:
    
    """ Controls the construction process.
    Director has a builder associated with him. Director then
    delegates building of the smaller parts to the builder and
    assembles them together.
    """

    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    # The algorithm for assembling a car
    def createComponent(self, name = None, gateway = None,ipaddress = None,subnetmask = None,dnsserver = None, routes = None, fastethernet = None ):
        #print(name,gateway, ipaddress, subnetmask, dnsserver, routes, fastethernet)
        #component = Component()
        #self.__builder.getComponentType()
        self.__builder.addName(name)
        #component.setName(name)

        self.__builder.addGateway(gateway)
        #component.setGateway(gateway)

        self.__builder.addIPAddress(ipaddress)
        #component.setIPAddress(ipaddress)

        self.__builder.addSubnetMask(subnetmask)
        #component.setSubnetMask(subnetmask)

        self.__builder.addDNSServer(dnsserver)
        #component.setDNSServer(dnsserver)

        self.__builder.addRoutes(routes)
        #component.setRoutes(routes)

        self.__builder.addFastEthernet(fastethernet)
        #component.setFastEthernet(fastethernet)

        self.__builder.getFlyweight()
        #component.setFlyweight()

        return self.__builder.getComponent()

# The whole product
class Component:
    
    """ The final product.
    A component is assembled by the `Director' class from
    parts made by `Builder'. Both these classes have
    influence on the resulting object.
    """

    def __init__(self):
        pass
        #self.__name  = None
        #self.__gateway  = None
        #self.__subnetmask  = None
        #self.__dnsserver  = None
        #self.__routes  = None
        #self.__ipaddress  = None
        #self.__fastethernet  = None

    def setName(self, name):
        #self.__name = name
        pass

    def setGateway(self, gateway):
        #self.__gateway = gateway
        pass
    def setSubnetMask(self, subnetmask):
        #self.__subnetmask = subnetmask
        pass
    def setDNSServer(self, dnsserver):
        #self.__dnsserver = dnsserver
        pass
    def setRoutes(self, routes):
        #self.__routes = routes
        pass
    def setIPAddress(self, ipaddress):
        #self.__ipaddress = ipaddress
        pass
    def setFastEthernet(self, fastethernet):
        #self.__fastethernet = fastethernet
        pass
    def specification(self):
        pass
    def setFlyweight(self):
    	pass
        #print "name: %s" % self.__name.displayname
        #print "gateway: %s" % self.__gateway.gateway
        #print "engine horsepower: %d" % self.__engine.horsepower
        #print "tire size: %d\'" % self.__wheels[0].size
    def getType(self):
        pass
    def send(self,ping):
        pass
    def receive(self,ping):
        pass

class Router(Component):

    def __init__(self):
        self.__name  = None
        self.__routes  = None
        self.__fastethernet  = None
        self.__flyweight = None
    def specification(self):
        print "name: %s" % self.__name
        print "routes: %s" % self.__routes
        print "fastethernet: %s" % self.__fastethernet
    def setName(self, name):
        self.__name = name

    def setRoutes(self, routes):
        self.__routes = routes

    def setFastEthernet(self, fastethernet):
        self.__fastethernet = fastethernet

    def setFlyweight(self):
    	self.__flyweight = flyweightFactory.get_flyweight('Router')

    def getName(self):
        return self.__name

    def getRoutes(self):
        return self.__routes

    def getFastEthernet(self):
        return self.__fastethernet

    def getType(self):
        return 'Router'

    def send(self,ping):
        return self.__flyweight.send({'routingTable':self.getRoutes()}, ping)

    def receive(self,ping):
        return self.__flyweight.receive({'routingTable':self.getRoutes()}, ping)

class Hub(Component):

    def __init__(self):
        self.__name  = None
        self.__flyweight = None
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def specification(self):
        print "name: %s" % self.__name

    def setFlyweight(self):
    	self.__flyweight = flyweightFactory.get_flyweight('Hub')

    def getType(self):
        return 'Hub'

    def send(self,ping):
        return self.__flyweight.send({'Hub':self}, ping)

    def receive(self,ping):
        return self.__flyweight.receive({'Hub':self}, ping)
        
class PC(Component):

    def __init__(self):    
        self.__name  = None
        self.__gateway  = None
        self.__subnetmask  = None
        self.__dnsserver  = None
        self.__ipaddress  = None
        self.__flyweight = None
    def setName(self, name):
        self.__name = name

    def setGateway(self, gateway):
        self.__gateway = gateway
        
    def setSubnetMask(self, subnetmask):
        self.__subnetmask = subnetmask
        
    def setDNSServer(self, dnsserver):
        self.__dnsserver = dnsserver
        
    def setIPAddress(self, ipaddress):
        self.__ipaddress = ipaddress

    def getName(self):
        return self.__name

    def getGateway(self):
        return self.__gateway
        
    def getSubnetMask(self):
        return self.__subnetmask
        
    def getDNSServer(self):
        return self.__dnsserver
        
    def getIPAddress(self):
        return self.__ipaddress

    def specification(self):
        print "name: %s" % self.__name
        print "gateway: %s" % self.__gateway
        print "subnetmask: %s" % self.__subnetmask
        print "dnsserver: %s" % self.__dnsserver
        print "ipaddress: %s" % self.__ipaddress

    def setFlyweight(self):
    	self.__flyweight = flyweightFactory.get_flyweight('PC')

    def getType(self):
        return 'PC'

    def send(self,ping):
        return self.__flyweight.send({'IP':self.getIPAddress()}, ping)

    def receive(self,ping):
        return self.__flyweight.receive({'IP':self.getIPAddress()}, ping)


class Builder:

    """ Creates various parts of a vehicle.
    This class is responsible for constructing all
    the parts for a vehicle.
    """

    def addName(self, arg_name): pass
    def getComponentType(self): pass
    def addGateway(self, arg_gateway): pass
    def addIPAddress(self, arg_ipaddress): pass
    def addSubnetMask(self, arg_subnetmask): pass
    def addDNSServer(self, arg_dnsserver): pass
    def addRoutes(self, arg_routes): pass
    def addFastEthernet(self, arg_fastethernet): pass
    def addFlyweight(self): pass
    def getComponent(self): pass
    def getFlyweight(self): pass

class HubBuilder(Builder):

    """ Concrete Builder implementation.
    This class builds parts for Jeep's SUVs.
    """
    myhub = None
    def __init__(self):
        self.myhub = Hub()
    def getComponentType(self):
        return Hub()

    def addName(self, arg_name):
        self.myhub.setName(arg_name)
    def getFlyweight(self):
        self.myhub.setFlyweight()
    def getComponent(self):
        return self.myhub

class PCBuilder(Builder):

    """ Concrete Builder implementation.
    This class builds parts for Jeep's SUVs.
    """
    myPC = None
    def __init__(self):
        self.myPC = PC()
    def getComponentType(self):
        return PC()
    def addGateway(self, arg_gateway):
        self.myPC.setGateway(arg_gateway)

    def addIPAddress(self, arg_ipaddress):
        self.myPC.setIPAddress(arg_ipaddress)

    def addSubnetMask(self, arg_subnetmask):
        self.myPC.setSubnetMask(arg_subnetmask)
    def addDNSServer(self, arg_dnsserver):
        self.myPC.setDNSServer(arg_dnsserver)
       # return dns
    def addName(self,arg_name):
        self.myPC.setName(arg_name)
    def getFlyweight(self):
        self.myPC.setFlyweight()
    def getComponent(self):
        return self.myPC

class RouterBuilder(Builder):

    """ Concrete Builder implementation.
    This class builds parts for Nissan's family cars.
    """
    myrouter = None
    def __init__(self):
        self.myrouter = Router()
    def getComponentType(self):
        return Router()

    def addName(self, arg_name):
        self.myrouter.setName(arg_name)

    def addRoutes(self, arg_routes):
        self.myrouter.setRoutes(arg_routes)
        
    def addFastEthernet(self, arg_fastethernet):
#4 ethernets, each has mac, ip address, subnet mask
        self.myrouter.setFastEthernet(arg_fastethernet)

    def getFlyweight(self):
        self.myrouter.setFlyweight()
    
    def getComponent(self):
        return self.myrouter

# Car parts
#class IPAddress:
 #   ipaddress = None
#class SubnetMask:
 #   subnetmask = IPAddress()

#class Gateway:
 #   gateway = IPAddress()
#class Network:
 #   network = IPAddress()
 

#Fix this soduuuu
class Routes:
    network = None
    mask = None
    nexthop = None
	#zeroFrom = len(network)
	#while zeroFrom > 0:
	#	if network[zeroFrom-1] == 0:
	#		zeroFrom -= 1

class FastEthernet:
    mac = None
    ipaddress = None
    subnetmask = None

class DNSServer:
    dnsserver = None
class fourPartAddress:
    pass

def inputIp(toEnter):
    valid = True
    str1 = 'Please enter '+toEnter+': '
    str2 = 'Invalid entry. Please re-enter '+toEnter+': '
    inp = raw_input(str1)
    ret = ''
    while True:
        checker = inp.split('.')
        valid = True
        if len(checker) != 4 or inp in IPList:
            valid = False
        for i in checker:
            if len(i)==0 or int(i)<0 or int(i)>255:
                valid = False
        if valid == True:
            IPList.append(inp)
            for i in checker:
                str3 = '0'*(3-len(i)) + i
                ret += str3 + '.'
            ret = ret[:-1]
            return ret
        inp = raw_input(str2)

def inputIpForRoutingTable(toEnter):
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

def inputIpExisting(toEnter):
    valid = True
    str1 = 'Please enter '+toEnter+': '
    str2 = 'Invalid entry. Please re-enter '+toEnter+': '
    inp = raw_input(str1)
    ret = ''
    while True:
        checker = inp.split('.')
        valid = True
        if len(checker) != 4 or inp not in IPList:
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

def inputName():
    inp = raw_input('Enter name: ')
    while True:
        if inp not in adjMat['byName']:
            return inp
        inp = raw_input('Name already exists. Please re-enter unique name: ')

def checkName(msg):
    inp = raw_input(msg)
    while True:
        if inp in adjMat['byName'] or inp=='0':
            return inp
        inp = raw_input('Object does not exist. Enter existing object name: ')


def main():
    director = Director()
    tostop = 0
    isfirst=1
    #adjMat = {}
    adjMat["byName"] = {}
    adjMat["byObj"] = {}
    adjMat['byIp'] = {}
    while(not tostop):
        if(isfirst):
            print("Choose to add one of the following components:")
            isfirst = 0
        else:
            print("Make a choice:")
            choice1=int(raw_input("1. Add a new component \n2. Change an existing component \n3. Setting Up of network is done \n"))
            if(choice1 == 1):
                print("Which component do you want to add:")
                choice2=int(raw_input("1. PC \n2. Hub \n3. Router\n"))
                if(choice2 == 1):
                    print("Enter the following details:")
                    name = inputName() #raw_input("Enter Name: ")
                    ipaddress = inputIp('IP address')
                    subnetmask = raw_input("Enter Subnet Mask: ") #inputIp('subnet mask')
                    gateway = raw_input("Enter Gateway: ") #inputIp('gateway')
                    dnsserver = raw_input("Enter DNS Server: ") #inputIp('DNS server')
                    director.setBuilder(PCBuilder())
                    pc = director.createComponent(name = name, ipaddress = ipaddress, subnetmask = subnetmask, gateway = gateway, dnsserver = dnsserver)
                    adjMat["byName"][name] = pc
                    print("The current list of objects that exists is as follows:")
                    print(list(adjMat["byName"].keys()))
                    print("Enter the names of objects that this given PC connects to. To stop entering links, enter 0")
                    
                    linkChoice = checkName('') #raw_input()
                    while(linkChoice != '0'):
                        #ensure that linkchoice is valid
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
                        linkChoice = checkName('') #raw_input()
                    pc.specification()

                elif(choice2 == 2):
                    print("Enter the following details:")
                    name = inputName() #raw_input("Enter Name: ")
                    director.setBuilder(HubBuilder())
                    hub = director.createComponent(name = name)
                    adjMat["byName"][name] = hub
                    print("The current list of objects that exists is as follows:")
                    print(list(adjMat["byName"].keys()))
                    print("Enter the names of objects that this given Hub connects to. To stop entering links, enter 0")
                    linkChoice = checkName('') #raw_input()
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
                        linkChoice = checkName('') #raw_input()
                    hub.specification()
                elif(choice2 == 3):
                    print("Enter the following details:")
                    name = inputName() #raw_input("Enter Name: ")
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
                            temp["ipaddress"] = inputIp('network address') #raw_input("Enter ip address: ")
                            temp["subnetmask"] = raw_input("Enter subnet mask: ") #inputIp('subnet mask')
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
                            temp["network"] = inputIpForRoutingTable('network address')
                            temp["mask"] = raw_input("Enter subnet mask: ") #inputIp('subnet mask')
                            temp["nexthop"] = inputIpExisting('next hop IP address')
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
                    adjMat["byName"][name] = router
                    print("The current list of objects that exists is as follows:")
                    print(list(adjMat["byName"].keys()))
                    print("Press any key to add a router link. To stop entering links, enter 0")
                    linkChoice = raw_input()
                    while(linkChoice != '0'):
                        #ensure that linkchoice is valid
                        linkChoice = checkName('Enter name of object to connect to: ') #raw_input('Enter name of object to connect to: ')
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
                pass

            elif(choice1 == 3):
                tostop = 1
                print(adjMat)
            else:
                continue

    #print('out of loop')
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
            #print(currentObjs)
            for device in currentObjs:
                '''
                if device == None:
                    continue
                '''
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



if __name__ == "__main__":
    main()
