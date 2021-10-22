from functions.tax_number_generator import TaxNumberGenerate as tng

how = None
while not isinstance(how, int):
    try:
        how = int(input('Podaj liczbę Nip-ów do wygenerowania: '))
    except ValueError as error:
        print('Podana wartość nie jest liczbą. Spróbuj ponownie.')
        continue

numbers = tng(how)
numbers.print_numbers()