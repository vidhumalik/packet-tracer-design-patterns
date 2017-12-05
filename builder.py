
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
    def getComponent(self):

        #component = Component()
        component = self.__builder.getComponentType()
        name = self.__builder.getName()
        component.setName(name)

        gateway = self.__builder.getGateway()
        component.setGateway(gateway)

        ipaddress = self.__builder.getIPAddress()
        component.setIPAddress(ipaddress)

        subnetmask = self.__builder.getSubnetMask()
        component.setSubnetMask(subnetmask)

        dnsserver = self.__builder.getDNSServer()
        component.setDNSServer(dnsserver)

        routes = self.__builder.getRoutes()
        component.setRoutes(routes)

        fastethernet = self.__builder.getFastEthernet()
        component.setFastEthernet(fastethernet)

        return component

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
       # print "name: %s" % self.__name.displayname
        #print "gateway: %s" % self.__gateway.gateway
      #  print "engine horsepower: %d" % self.__engine.horsepower
       # print "tire size: %d\'" % self.__wheels[0].size
class Router(Component):

    def __init__(self):
        self.__name  = None
        self.__routes  = None
        self.__fastethernet  = None
    def specification(self):
        print "name: %s" % self.__name.displayname
        print "routes: %s" % self.__routes
        print "fastethernet: %s" % self.__fastethernet
    def setName(self, name):
        self.__name = name

    def setRoutes(self, routes):
        self.__routes = routes

    def setFastEthernet(self, fastethernet):
        self.__fastethernet = fastethernet
class Hub(Component):

    def __init__(self):
        self.__name  = None
    def setName(self, name):
        self.__name = name

    def specification(self):
        print "name: %s" % self.__name.displayname
        
class PC(Component):

    def __init__(self):    
        self.__name  = None
        self.__gateway  = None
        self.__subnetmask  = None
        self.__dnsserver  = None
        self.__ipaddress  = None
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

    def specification(self):
        print "name: %s" % self.__name.displayname
        print "gateway: %s" % self.__gateway
        print "subnetmask: %s" % self.__subnetmask
        print "dnsserver: %s" % self.__dnsserver
        print "ipaddress: %s" % self.__ipaddress


class Builder:

    """ Creates various parts of a vehicle.
    This class is responsible for constructing all
    the parts for a vehicle.
    """

    def getName(self): pass
    def getComponentType(self): pass
    def getGateway(self): pass
    def getIPAddress(self): pass
    def getSubnetMask(self): pass
    def getDNSServer(self): pass
    def getRoutes(self): pass
    def getFastEthernet(self): pass

class HubBuilder(Builder):

    """ Concrete Builder implementation.
    This class builds parts for Jeep's SUVs.
    """
    def getComponentType(self):
        return Hub()

    def getName(self):
        name = Name()
        name.displayname = 'Hub A'
        return name

class PCBuilder(Builder):

    """ Concrete Builder implementation.
    This class builds parts for Jeep's SUVs.
    """
    def getComponentType(self):
        return PC()
    def getGateway(self):
        gw = Gateway()
        gw.gateway = 'gwaddr'
        return gw

    def getIPAddress(self):
        ip = IPAddress()
        ip.ipaddress = 'ipaddr'
        return ip

    def getSubnetMask(self):
        subnet = SubnetMask()
        subnet.subnetmask = 'smaddr'
        return subnet
    def getDNSServer(self):
        dns = DNSServer()
        dns.dnsserver = 'dnsaddr'
        return dns
    def getName(self):
        name = Name()
        name.displayname = 'PC A'
        return name

class RouterBuilder(Builder):

    """ Concrete Builder implementation.
    This class builds parts for Nissan's family cars.
    """
    def getComponentType(self):
        return Router()

    def getName(self):
        name = Name()
        name.displayname = 'Router A'
        return name

    def getRoutes(self):
        num = 3 #make it user defined
        routes = [Routes() for i in range(0,num)]
        routes.network = 'nwaddr'
        routes.maskk = 'maskaddr'
        routes.nexthop = 'nxthopaddr'
        return routes #put network mask nexthop within it

    def getFastEthernet(self):
#4 ethernets, each has mac, ip address, subnet mask
        fastEthernet = [FastEthernet() for i in range(0,4)]
        fastEthernet[0].mac = "macaddr"
        fastEthernet[0].iPaddress.ipaddress = "ipaddr"
        fastEthernet[0].subneTmask.subnetmask = "smaddr"
        return fastEthernet

# Car parts
class IPAddress:
    ipaddress = None
class SubnetMask:
    subnetmask = IPAddress()
class Name:
    displayname = None

class Routes:
    network = Network()
    mask = SubnetMask()
    nexthop = Gateway()

class FastEthernet:
    mac = None
    iPaddress = IPAddress()
    subneTmask = SubnetMask()
class Network()
    network = IPAddress()
class DNSServer:
    dnsserver = None
class Gateway:
    gateway = IPAddress()
class fourPartAddress:
    pass


def main():
    routerBuilder = RouterBuilder()
    pcBuilder = PCBuilder()
    hubBuilder = HubBuilder()

    director = Director()

    print "Router"
    director.setBuilder(routerBuilder)
    router = director.getComponent()
    router.specification()

    print ""

    print "PC"
    director.setBuilder(pcBuilder)
    pc = director.getComponent()
    pc.specification()

    print ""

    print "Hub"
    director.setBuilder(hubBuilder)
    hub = director.getComponent()
    hub.specification()

if __name__ == "__main__":
    main()