class Family():
    def __init__(self, name, age, relation, qualification):
        self.name = name
        self.age = age
        self.relation = relation
        self.qualification = qualification

    def eating(self):
        print("Let's have lunch together")

myself = Family("Sarang Menon", 14, "Son", "Student")
mother = Family("Renu Sadanandan", 43, "Mother", "Tourism")
father = Family("Abcy Menon", 45, "Father", "Finance")

print(myself.relation)
print(mother.name, mother.age, mother.relation, mother.qualification)

