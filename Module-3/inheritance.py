class animal:
    def sound(self):
        print("Animals make different sounds.  # From Animal class")

class dog(animal):
    def sound(self):
        super().sound()
        print("Dog barks!  # From Dog class")

d = dog()
d.sound() 