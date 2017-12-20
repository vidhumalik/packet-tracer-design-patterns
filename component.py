from flyweightfac import *

flyweightFactory = FlyweightFactory()

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
    def send(self,ping, adjMatrix, IPList):
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

    def send(self,ping, adjMatrix, IPList):
        return self.__flyweight.send({'routingTable':self.getRoutes(),'adjMat':adjMatrix, 'IPList':IPList}, ping)

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

    def send(self,ping, adjMatrix, IPList):
        return self.__flyweight.send({'Hub':self,'adjMat':adjMatrix, 'IPList':IPList}, ping)

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

    def send(self, ping, adjMatrix, IPList):
        return self.__flyweight.send({'IP':self.getIPAddress(),'adjMat':adjMatrix, 'IPList':IPList}, ping)

    def receive(self,ping):
        return self.__flyweight.receive({'IP':self.getIPAddress()}, ping)