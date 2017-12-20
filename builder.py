from component import *

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
    def createLink(self): pass

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