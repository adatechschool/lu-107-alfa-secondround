class Pet

  def initialize(name, greeting="Hello", legs=4, cri="Ouaf")
    @name = name
    @greeting = greeting
    @legs = legs
    @cri = cri
  end

  def say_hi()
    puts ("#{@greeting}, I'm #{@name}, #{@cri}")
  end

  def count_legs()
    puts(@legs)
  end

end

class Cat < Pet
  def initialize(name)
    super(name, greeting="Hello", legs=4, cri="miaouu")
  end
end

class Parrot < Pet
  def initialize(name)
    super(name, greeting="Coucou", legs=2, cri ="ouii")
  end
end

pitch = Pet.new("Pitch")
felix = Cat.new("Felix")
kevin = Parrot.new("Kevin")
pitch.say_hi
felix.say_hi
pitch.count_legs
kevin.say_hi
kevin.count_legs
