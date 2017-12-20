from flyweight import *

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
        self._flyweights = {'PC':PCFlyweight(),'Hub':HubFlyweight(),'Router':RouterFlyweight()}

    def get_flyweight(self, key):
        try:
            flyweight = self._flyweights[key]
        except KeyError:
            flyweight = ConcreteFlyweight()
            self._flyweights[key] = flyweight
        return flyweight

