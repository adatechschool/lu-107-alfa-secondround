class Pet:
	def __init__(self, name, greeting = "Hello"):
		self.name = name
		self.greeting = greeting

	def say_hi(self):
		print(f"{self.greeting}, I'm {self.name}!")

class Cat(Pet):
	def __init__(self, name):
		super().__init__(name, "Meow")

my_pet = Pet("Gaston")
my_pet.say_hi()


cat = Cat("Félix")
cat.say_hi()

#Hello, I'm Gaston!
#Meow, I'm Félix!
