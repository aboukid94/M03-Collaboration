
def get_odds():
    for number in range(10):
        if number % 2 != 0:
            yield number
            
counter = 0
for odd in get_odds():
    if counter == 2:
        print()
        print(odd)
        print()
        break
    counter += 1