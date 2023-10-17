class fishcakemaker:
    def __init__(self, **kwargs):
        self.size=10
        self.flavor="슈크림"
        self.price=10000000000

        if "size" in kwargs:
            self.size=kwargs.get("size")
        if "flavor" in kwargs:
            self.flavor=kwargs.get("flavor")
        if "price" in kwargs:
            self.price=kwargs.get("price")
    def show(self):
        print("붕어빵 크기{}".format(self.size))
        print("붕어빵 종류{}".format(self.flavor))
        print("붕어빵 가격{}".format(self.price))
        print("*"*30)
fish1=fishcakemaker()
fish2=fishcakemaker(size=200000,price=300000000000000000000000000000000000000000000000000000)
fish3=fishcakemaker(flavor="피자",size=10000000)

fish1.show()
fish2.show()
fish3.show()

class markegoods(fishcakemaker):
    def __init__(self,margin=100,**kwargs):
        super().__init__(**kwargs)
        self.market_price=self.price+margin
    def show(self):
        print(self.flavor,self.market_price)
fish1=markegoods(size=20,price=500)
fish1.show()
