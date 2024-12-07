class Bird:
    beak = 1
    eyes = 2
    can_fly = True
    lay_eggs = True

    def fly(self):
        print("The bird is flying")

parrot = Bird()
print(parrot.lay_eggs)
parrot.fly()

