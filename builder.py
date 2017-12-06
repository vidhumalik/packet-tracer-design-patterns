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
    def createComponent(self, name = None, gateway = None,ipaddress = None,subnetmask = None,dnsserver = None,network = None, nexthop = None, mac = None ):
        print(name,gateway, ipaddress, subnetmask, dnsserver, network, nexthop, mac )
        #component = Component()
        #self.__builder.getComponentType()
        self.__builder.addName(name)
        #component.setName(name)

        self.__builder.addGateway(gateway)
       # component.setGateway(gateway)

        self.__builder.addIPAddress(ipaddress)
       # component.setIPAddress(ipaddress)

        self.__builder.addSubnetMask(subnetmask)
       # component.setSubnetMask(subnetmask)

        self.__builder.addDNSServer(dnsserver)
       # component.setDNSServer(dnsserver)

        self.__builder.addRoutes(network, subnetmask, nexthop)
       # component.setRoutes(routes)

        self.__builder.addFastEthernet(mac, ipaddress, subnetmask)
      #  component.setFastEthernet(fastethernet)

      #  component.setFlyweight()

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
    #    self.__name  = None
     #   self.__gateway  = None
      #  self.__subnetmask  = None
       # self.__dnsserver  = None
    #    self.__routes  = None
     #   self.__ipaddress  = None
      #  self.__fastethernet  = None

    def setName(self, name):
   #     self.__name = name
        pass

    def setGateway(self, gateway):
    #    self.__gateway = gateway
        pass
    def setSubnetMask(self, subnetmask):
     #   self.__subnetmask = subnetmask
        pass
    def setDNSServer(self, dnsserver):
      #  self.__dnsserver = dnsserver
        pass
    def setRoutes(self, routes):
       # self.__routes = routes
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
       # print "name: %s" % self.__name.displayname
        #print "gateway: %s" % self.__gateway.gateway
      #  print "engine horsepower: %d" % self.__engine.horsepower
       # print "tire size: %d\'" % self.__wheels[0].size
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
    def addRoutes(self, arg_network, arg_subnetmask, arg_nexthop): pass
    def addFastEthernet(self, arg_mac, arg_ipaddress, arg_subnetmask): pass
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

    def addRoutes(self, arg_network, arg_subnetmask, arg_nexthop):
        num = 3 #make it user defined
        temproutes = [Routes() for i in range(0,num)]
        temproutes[0].network = arg_network
        temproutes[0].mask = arg_subnetmask
        temproutes[0].nexthop = arg_nexthop
        self.myrouter.setRoutes(temproutes)
        
    def addFastEthernet(self, arg_mac, arg_ipaddress, arg_subnetmask):
#4 ethernets, each has mac, ip address, subnet mask
        tempfastEthernet = [FastEthernet() for i in range(0,4)]
        tempfastEthernet[0].mac = arg_mac
        tempfastEthernet[0].ipaddress = arg_ipaddress
        tempfastEthernet[0].subnetmask = arg_subnetmask
        self.myrouter.setFastEthernet(tempfastEthernet)
    
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
    routerBuilder = RouterBuilder()
    pcBuilder = PCBuilder()
    hubBuilder = HubBuilder()

    director = Director()

    print "Router"
    director.setBuilder(routerBuilder)
    router = director.createComponent(gateway='testgateway', name = 'testnamerouter')
    router.specification()

    print ""

    print "PC"
    director.setBuilder(pcBuilder)
    pc = director.createComponent(name = 'testnamepc')
    pc.specification()

    print ""

    print "Hub"
    director.setBuilder(hubBuilder)
    hub = director.createComponent(name = 'testnamehub')
    hub.specification()

if __name__ == "__main__":
    main()