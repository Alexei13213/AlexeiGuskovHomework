import requests
from bs4 import BeautifulSoup as BS
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
link = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'
r = requests.get(link, headers=headers)
soup = BS(r.content, 'html.parser')
convert = soup.find('tbody').find_all('tr')

data = {}

for dt in convert:
    data[dt.find_all('td')[0].text] = [dt.find_all('td')[1].text, dt.find_all('td')[2].text, dt.find_all('td')[3].text,
                                       dt.find_all('td')[4].text, dt.find_all('td')[5].text, dt.find_all('td')[6].text,
                                       dt.find_all('td')[7].text, dt.find_all('td')[8].text, dt.find_all('td')[9].text,
                                       dt.find_all('td')[10].text]


def main_menu():
    while True:
        user_choice = input("Please choose:"
                            "\n1.Õhutemperatuur (°C)\n2.Maapinna minimaalne temperatuur (°C)"
                            "\n3.Suhteline õhuniiskus (%)\n4.Tuule kiirus (m/s)\n5.Sademed (mm)"
                            "\n6.Päikesepaiste kestus (h)"
                            "\n0.Exit\n-->")
        if user_choice == '1':
            for key in data:
                print()
                print(key)
                if data[key][1] == '':
                    print('No data ATM')
                else:
                    print(f'Max {data[key][1]}')
                if data[key][0] == '':
                    print('No data ATM')
                else:
                    print(f'Mid {data[key][0]}')
                if data[key][2] == '':
                    print('No data ATM')
                else:
                    print(f'Min {data[key][2]}')
            continue
        elif user_choice == '2':
            for key in data:
                print()
                print(key)
                if data[key][3] == '':
                    print('No Data ATM')
                else:
                    print(f'Maapinna minimaalne temperatuur (°C) {data[key][3]}')
                if data[key][4] == '':
                    print('No Data ATM')
                else:
                    print(f'Minimaalne temperatuur 2cm kõrgusel maapinnast (°C) {data[key][4]}')
            continue
        elif user_choice == '3':
            for key in data:
                print()
                print(key)
                if data[key][5] == '':
                    print('No data ATM')
                else:
                    print(f'Mid {data[key][5]}')
                if data[key][6] == '':
                    print('No data atm')
                else:
                    print(f'Min {data[key][6]}')
            continue
        elif user_choice == '4':
            for key in data:
                print()
                print(key)
                if data[key][7] == '':
                    print('No data ATM')
                else:
                    print(f'Mid {data[key][7]}')
                if data[key][8] == '':
                    print('No data ATM')
                else:
                    print(f'Max {data[key][8]}')
            continue
        if user_choice == '5':
            for key in data:
                print()
                print(key)
                if data[key][9] == '':
                    print('No data ATM')
                else:
                    print(data[key][9])
            continue
        if user_choice == '6':
            for key in data:
                print()
                print(key)
                if data[key][10] == '':
                    print('No data ATM')
                else:
                    print(data[key][10])
            continue
        if user_choice == '7':
            quit(print('Good bye.'))


main_menu()