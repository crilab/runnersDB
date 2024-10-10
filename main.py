import random
import json

def get_data(file):
    result = []
    with open(file) as f:
        return [row.split('\t')[1].title() for row in f]

forenames_men = get_data('forenames_men.txt')
forenames_women = get_data('forenames_women.txt')
surenames = get_data('surnames.txt')

with open('cities.json') as f:
    cities = json.load(f)

random.shuffle(forenames_men)
random.shuffle(forenames_women)
random.shuffle(surenames)

names = []

for surename in surenames:
    names.append(f'{forenames_men.pop()} {surename}')
    names.append(f'{forenames_women.pop()} {surename}')

random.shuffle(names)

registrations = []
results = []

for number, name in enumerate(names, start=1):
    registrations.append({
        'number': number,
        'name': name,
        'city': random.choice(cities)
    })
    results.append({
        'number': number,
        'time': random.randint(
            20 * 60,
            50 * 60
        )
    })

fastest_time = min(results, key=lambda r: r['time'])
for registration in registrations:
    if registration['number'] == fastest_time['number']:
        print(fastest_time)
        print(registration)

with open('registrations.json', 'w') as f:
    json.dump(registrations, f, indent=2)

with open('results.json', 'w') as f:
    json.dump(results, f, indent=2)
