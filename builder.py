
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
        component = Component()

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
        self.__name  = None
        self.__gateway  = None
        self.__subnetmask  = None
        self.__dnsserver  = None
        self.__routes  = None
        self.__ipaddress  = None
        self.__fastethernet  = None

    def setName(self, name):
        self.__name = name

    def setGateway(self, gateway):
        self.__gateway = gateway
        
    def setSubnetMask(self, subnetmask):
        self.__subnetmask = subnetmask
        
    def setDNSServer(self, dnsserver):
        self.__dnsserver = dnsserver
        
    def setRoutes(self, routes):
        self.__routes = routes
        
    def setIPAddress(self, ipaddress):
        self.__ipaddress = ipaddress
        
    def setFastEthernet(self, fastethernet):
        self.__fastethernet = fastethernet
        
    def specification(self):
        print "name: %s" % self.__name.displayname
        print "gateway: %s" % self.__gateway.gateway
      #  print "engine horsepower: %d" % self.__engine.horsepower
       # print "tire size: %d\'" % self.__wheels[0].size


class Builder:

    """ Creates various parts of a vehicle.
    This class is responsible for constructing all
    the parts for a vehicle.
    """

    def getName(self): pass
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

    def getName(self):
        name = Name()
        name.displayname = 'Hub A'
        return name

class PCBuilder(Builder):

    """ Concrete Builder implementation.
    This class builds parts for Jeep's SUVs.
    """

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

    def getName(self):
        name = Name()
        name.displayname = 'Router A'
        return name

    def getRoutes(self):
        routes = Routes()
        routes.network = 'nwaddr'
        routes.maskk = 'maskaddr'
        routes.nexthop = 'nxthopaddr'
        return routes #put network mask nexthop within it

    def getFastEthernet(self):
#4 ethernets, each has mac, ip address, subnet mask
        fastEthernet = FastEthernet()
        fastEthernet.mac = "macaddr"
        fastEthernet.iPaddress.ipaddress = "ipaddr"
        fastEthernet.subneTmask.subnetmask = "smaddr"
        return fastEthernet

# Car parts
class IPAddress:
    ipaddress = None
class SubnetMask:
    subnetmask = None
class Name:
    displayname = None

class Routes:
    network = None
    mask = None
    nexthop = None

class FastEthernet:
    mac = None
    iPaddress = IPAddress()
    subneTmask = SubnetMask()

class DNSServer:
    dnsserver = None
class Gateway:
    gateway = None



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