#note the single underscore prefix for protected vars. Protected vars can be
#accessed in the same package but not outside
class Protected:
    def _init_(self):
        self._protectedVar = 0

obj = Protected()
obj._protectedVar = 34
print(obj._protectedVar) #output is 34

#note the double underscore prefix for private vars
#private vars can only be accessed wtihin the class itself
class Private:
    def __init__(self):
        self.__privateVar = 12

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Private()
obj.getPrivate() #outputs 12
obj.setPrivate(23) #sets Private to 23
obj.getPrivate() #outputs 23

class ProtectedPrivate:
    def _init_(self):
        self._protectedVar2 = 0

    def __init__(self):
        self.__privateVar2 = 12

    def getPrivate2(self):
        print(self.__privateVar2)

    def setPrivate2(self, private):
        self.__privateVar2 = private

obj = ProtectedPrivate()
obj._protectedVar2 = 42
print(obj._protectedVar2) #outputs 42
obj.getPrivate2() #outputs 12
obj.setPrivate2(50) #sets Private2 to 50
obj.getPrivate2() #outputs 50
