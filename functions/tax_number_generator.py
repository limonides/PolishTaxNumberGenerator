from random import randint, choice
from offices.list import TaxOffices


class TaxNumberGenerate:
    nip = []
    weight = (6, 5, 7, 2, 3, 4, 5, 6, 7)

    def __init__(self, how_much):
        self.how_much = how_much

    @staticmethod
    def generate_number():

        elem, office = choice(list(TaxOffices.us.items()))
        x = [randint(0, 9) for p in range(0, 6)]
        for i in str(elem)[::-1]:
            x.insert(0, int(i))
        if sum([a * b for a, b in zip(TaxNumberGenerate.weight, x)]) % 11 != 10:
            x.append(sum([a * b for a, b in zip(TaxNumberGenerate.weight, x)]) % 11)
            x = ''.join(map(str, x))
            return x
        else:
            if x[8] in range(0, 8):
                x[8] = x[8]+1
            else:
                x[8] = x[8]-1
            x.append(sum([a * b for a, b in zip(TaxNumberGenerate.weight, x)]) % 11)
            x = ''.join(map(str, x))
            return x

    def print_numbers(self):
        for el in range(self.how_much):
            print(f' {el+1} - {self.generate_number()}')



