my_list = [4, 7, 0]

iterator = iter(my_list)

print(next(iterator)) 
print(next(iterator))
print(next(iterator))

# Custom Iterator 

class PowTwo:

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


numbers = PowTwo(3)
i = iter(numbers)

print(next(i))
print(next(i))
print(next(i))
print(next(i)) 
print(next(i)) # Raise an Error