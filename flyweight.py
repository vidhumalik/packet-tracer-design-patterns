
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
        
        if extrinsic_state['IP'] == ping['destinationIP']:
            return True
        return False
    def send(self, extrinsic_state, ping):
        forwardToObj = extrinsic_state['adjMat']['byIp'][extrinsic_state['IP']]
        return [forwardToObj]

class HubFlyweight(Flyweight):
    def receive(self, extrinsic_state, ping): #pass, because hub doesnt perform any processing based on the ping, as PC needs to
        pass
    def send(self, extrinsic_state, ping): #Returns list of objects that hub will forward the ping to
        
        forwardToObjList = extrinsic_state['adjMat']['byObj'][extrinsic_state['Hub']]
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
        portOfRouter = -1
        forwardToObj = []
        routingTable = extrinsic_state['routingTable']
        for route in routingTable:
            #if route.network.network.ipaddress[:route.zeroFrom] == ping['destinationIP'][:route.zeroFrom]:
            if route['network'][:route['zeroFrom']] == ping['destinationIP'][:route['zeroFrom']]:
                #to forward on this route
                #routerPortIp = route.nexthop.gateway.ipaddress
                forwardToObj.append(extrinsic_state['adjMat']['byIp'][route['nexthop']])
                if route['nexthop'] in extrinsic_state['IPList']:
                    forwardToObj.append(extrinsic_state['IPList'][route['nexthop']])
                break
        print('f'+str(forwardToObj))
        return forwardToObj