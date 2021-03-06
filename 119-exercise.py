class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Felix', 2)
cat2 = Cat('Garfield', 6)
cat3 = Cat('Morris', 10)


# Create a function that finds the oldest cat
def findOldestCat(*cats):
    from operator import attrgetter
    return max(cats, key=attrgetter('age'))


# Print our: "The oldest cat is x years old.". x will be the oldest cat's age by using the function in #2.
print(f'The oldest cat is {findOldestCat(cat1, cat2, cat3).age} years old.')