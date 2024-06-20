def add_waste(waste, category):
    with open('waste.txt', 'a') as f:
        f.write(f'{waste} - {category}\n')


def view_waste():
    with open('waste.txt', 'r') as f:
        waste = f.readlines()
        for item in waste:
            print(item)


def by_category(category):
    total_waste = 0
    with open('waste.txt', 'r') as f:
        waste = f.readlines()
        for item in waste:
            waste_item, waste_category = item.strip().split(' - ')
            if waste_category == category:
                total_waste += int(waste_item)
    print(f'Total waste in {category}: {total_waste}')


request = input('Enter an action (Add a waste, View wastes, By category) A/V/B: ')
if request == 'A':
    waste = input('Enter the waste: ')
    category = input('Enter the category: ')
    add_waste(waste, category)
elif request == 'V':
    view_waste()
elif request == 'B':
    category = input('Enter the category: ')
    by_category(category)