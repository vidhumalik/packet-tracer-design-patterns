#import flyweight
from builder import *
currObjs = []
adjMat = {}
IPList = []

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
    def createLink(self, linkChoice):
        self.__builder.createLink(linkChoice)

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
        comp = self.__builder.getComponent()
        adjMat["byName"][name] = comp
        return comp