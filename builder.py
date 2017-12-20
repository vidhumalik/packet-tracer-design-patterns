from component import *
from inputProcessing import *

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
    def createLink(self, linkChoice):
        while(linkChoice != '0'):
            #ensure that linkchoice is valid
            hub = self.myhub
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
    def createLink(self, linkChoice):
        if(linkChoice != '0'):
            #ensure that linkchoice is valid
            print('linkChoice: '+str(linkChoice))
            pc = self.myPC
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
    def createLink(self, linkChoice):
        router = self.myrouter
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