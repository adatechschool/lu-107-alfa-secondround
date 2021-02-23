class Pet:
    legs = 0
    def __init__(self, name ="Boulbi", greeting = "Hello", legs = 4, cri = "ouaf"):
        self.name = name
        self.greeting = greeting
        self.legs = legs
        self.cri = cri

    def say_hi(self):
        print(f"{self.greeting}, I'm {self.name}!")

    @classmethod
    def legs_count(cls):
        return cls.legs




class Cat(Pet):
	def __init__(self, name):
		super().__init__("cat", "Meow", 4, "miaaa")


class Parrot(Pet):
    def __init__(self, name):
        super().__init__("par", "Coucou", 2, "oui")


    def say_hi(self):
        print(f"{self.greeting}, My name is {self.name}!")
        print(self.legs)



jack = Parrot("Jack")

jack.say_hi()
jack.legs_count()
Pet.legs_count()
print(Cat.legs_count())
print(Parrot.legs_count())
