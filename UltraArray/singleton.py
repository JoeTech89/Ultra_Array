bug=0
class MetaSingleton(type):
    def __init__(self,*args,**kwargs):
        if bug:print('Meta Singleton init')
        self.__instance=None
        super().__init__(*args,**kwargs)

    def __call__(self,*args,**kwargs):
        if bug:print('Meta Singleton call')
        if self.__instance==None:
            self.__instance=super().__call__(*args,**kwargs)
        return self.__instance


class Singleton(metaclass=MetaSingleton):
    print(f"{'Rukus Singleton':_^100}")


if __name__=='__main__':
    print('Testing Singleton CLass')
    
    class TestClass:
        def __init__(self):
            pass

    s0=Singleton()
    s1=Singleton()
    tc0=TestClass()
    tc1=TestClass()
    
    print(f"{'Name':^30}"+f"{'Object':^30}")
    print(f"{'Singleton 0':<30}"+f"{str(s0):<30}")
    print(f"{'Singleton 1':<30}"+f"{str(s1):<30}")
    print(f"{'Test Class0':<30}"+f"{str(tc0):<30}")
    print(f"{'Test CLass1':<30}"+f"{str(tc1):<30}")