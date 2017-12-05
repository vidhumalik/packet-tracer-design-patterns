adjMat = {}
'''
Sample:
adjMat=	{'byIp':
			{
			 '1.1.1.1':obj1,
			 '2.2.2.2':obj2
			},
		'byObj':
			{
			 obj1:[obj3,obj4]
			}
		}
'''

currObjs = []
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
        self._flyweights = {}

    def get_flyweight(self, key):
        try:
            flyweight = self._flyweights[key]
        except KeyError:
            flyweight = ConcreteFlyweight()
            self._flyweights[key] = flyweight
        return flyweight


class Flyweight(metaclass=abc.ABCMeta):
    def __init__(self):
        self.intrinsic_state = None

    @abc.abstractmethod
    def receive(self, extrinsic_state, ping):
		'''
		Ping is a dictionary for ping details, like {destinationIP:__, sourceIP:__, ...}
		Similarly, extrinsic_state={IP:__, ...}
		Return value: True for successful ping, False otherwise
		'''
        pass
	
	@abc.abstractmethod
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
		forwardToObj = adjMat['byIp'][extrinsic_state['IP']]
		forwardToObj.receive(ping)

class HubFlyweight(Flyweight):
	def receive(self, extrinsic_state, ping): #pass, because hub doesnt perform any processing based on the ping, as PC needs to
		pass
	def send(self, extrinsic_state, ping): #Returns list of objects that hub will forward the ping to
		forwardToObjList = adjMat['byObj'][self]
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
		portOfRouter = extrinsic_state['routingTable'][ping['destinationIP']]
		IPofRouterPort = extrinsic_state['ports'][portOfRouter]
		forwardToObj = adjMat['byIp'][IPofRouterPort]
		return [forwardToObj]


def main():
    flyweight_factory = FlyweightFactory()
    concrete_flyweight = flyweight_factory.get_flyweight("key")
    concrete_flyweight.operation(None)


if __name__ == "__main__":
    main()