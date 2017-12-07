#import flyweight

#flyweightFactory = FlyweightFactory()

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
        print(name,gateway, ipaddress, subnetmask, dnsserver, routes, fastethernet)
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


def main():
    director = Director()
    tostop = 0
    isfirst=1
    adjMat = {}
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
                    name = raw_input("Enter Name: ")
                    ipaddress = raw_input("Enter Ip Address: ")
                    subnetmask = raw_input("Enter Subnet Mask: ")
                    gateway = raw_input("Enter Gateway: ")
                    dnsserver = raw_input("Enter DNS Server: ")
                    director.setBuilder(PCBuilder())
                    pc = director.createComponent(name = name, ipaddress = ipaddress, subnetmask = subnetmask, gateway = gateway, dnsserver = dnsserver)
                    adjMat["byName"][name] = pc
                    print("The current list of objects that exists is as follows:")
                    print(list(adjMat["byName"].keys()))
                    print("Enter the names of objects that this given PC connects to. To stop entering links, enter 0")
                    
                    linkChoice = raw_input()
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
                        linkChoice = raw_input()
                    pc.specification()

                elif(choice2 == 2):
                    print("Enter the following details:")
                    name = raw_input("Enter Name: ")
                    director.setBuilder(HubBuilder())
                    hub = director.createComponent(name = name)
                    adjMat["byName"][name] = hub
                    print("The current list of objects that exists is as follows:")
                    print(list(adjMat["byName"].keys()))
                    print(adjMat['byName'])
                    print("Enter the names of objects that this given Hub connects to. To stop entering links, enter 0")
                    linkChoice = raw_input()
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
                        linkChoice = raw_input()
                    hub.specification()
                elif(choice2 == 3):
                    print("Enter the following details:")
                    name = raw_input("Enter Name: ")
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
                            temp["ipaddress"] = raw_input("Enter ip address: ")
                            temp["subnetmask"] = raw_input("Enter subnet mask: ")
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
                            temp["network"] = raw_input("Enter network address: ")
                            temp["mask"] = raw_input("Enter subnet mask: ")
                            temp["nexthop"] = raw_input("Enter next hop: ")
                            routes.append(temp)
                        else:
                            tostop3 = 1
                    director.setBuilder(RouterBuilder())
                    router = director.createComponent(name = name, fastethernet = fastethernet, routes = routes)
                    adjMat["byName"][name] = router
                    print("The current list of objects that exists is as follows:")
                    print(list(adjMat["byName"].keys()))
                    print("Press any key to add a router link. To stop entering links, enter 0")
                    linkChoice = raw_input()
                    while(linkChoice != '0'):
                        #ensure that linkchoice is valid
                        linkChoice = raw_input('Enter name of object to connect to: ')
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
                        print(router.getFastEthernet())
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



    print "Router"
    director.setBuilder(RouterBuilder())
    router = director.createComponent(gateway='testgateway', name = 'testnamerouter')
    router.specification()

    print ""

    print "PC"
    director.setBuilder(PCBuilder())
    pc = director.createComponent(name = 'testnamepc')
    pc.specification()

    print ""

    print "Hub"
    director.setBuilder(HubBuilder())
    hub = director.createComponent(name = 'testnamehub')
    hub.specification()

if __name__ == "__main__":
    main()