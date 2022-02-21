from bs4 import BeautifulSoup as BS
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
url1 = 'https://www.google.com/search?q=eur+to+rub&source=hp&ei=Y3kRYuHCA_aTwPAPkMSQ4AQ&iflsig=AHkkrS4AAAAAYhGHc7Ksn3dYdETj2Snv8wwEc1kn93Cy&oq=eur+to&gs_lcp=Cgdnd3Mtd2l6EAEYADIQCAAQgAQQsQMQgwEQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoICAAQgAQQsQM6CwgAEIAEELEDEIMBOhEILhCABBCxAxCDARDHARDRAzoRCC4QgAQQsQMQgwEQxwEQrwE6FAguEIAEELEDEIMBEMcBENEDENQCOgsILhCABBDHARCjAjoLCC4QgAQQxwEQrwE6BwgAEIAEEApQAFi8EmDZJWgAcAB4AIABPYgBlAKSAQE2mAEAoAEB&sclient=gws-wiz'
url2 = 'https://www.google.com/search?q=rub+to+eur&hl=ru&source=hp&ei=yKcRYsrVLvKErwTTxZbICg&iflsig=AHkkrS4AAAAAYhG12H3TcpSNXxe2-wO8Ldgfaof2Dsko&oq=rub&gs_lcp=Cgdnd3Mtd2l6EAEYADILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgsILhCABBDHARCvATIFCAAQgAQ6DgguEIAEELEDEIMBENQCOhEILhCABBCxAxCDARDHARDRAzoICAAQgAQQsQM6DgguEIAEELEDEMcBEKMCOg4ILhCABBDHARCvARDUAjoMCAAQsQMQgwEQChABUABY6gRgkhhoAHAAeACAATiIAaEBkgEBM5gBAKABAQ&sclient=gws-wiz'
url3 = 'https://www.google.com/search?q=eur+to+czk&hl=ru&ei=hJwRYoGUGqOQrgStu59I&oq=eur&gs_lcp=Cgdnd3Mtd2l6EAEYBjIJCAAQQxBGEIICMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDOgcIABBHELADOgcIABCwAxBDOgsIABCABBCxAxCDAToHCAAQsQMQQzoICAAQgAQQsQM6EQguEIAEELEDEIMBEMcBENEDOgUIABCABEoECEEYAEoECEYYAFCRhgFYnI4BYNO_AWgCcAF4AIABQ4gBugGSAQEzmAEAoAEByAEKwAEB&sclient=gws-wiz'
url4 = 'https://www.google.com/search?q=czk+to+eur&hl=ru&ei=f6gRYr2cLoeRrwSq2Zr4CQ&oq=czk&gs_lcp=Cgdnd3Mtd2l6EAEYADIJCAAQQxBGEIICMgUIABCABDIECAAQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBAgAEEMyBQgAEIAEMgUIABCABDoICAAQgAQQsQM6EQguEIAEELEDEIMBEMcBEK8BOg4ILhCABBCxAxDHARDRAzoLCC4QgAQQxwEQ0QM6CwguEIAEEMcBEKMCOg4ILhCxAxCDARDHARCvAToECC4QQzoOCC4QgAQQxwEQ0QMQ1AI6BQguEIAEOggILhCABBDUAkoECEEYAEoECEYYAFAAWLQGYOsVaABwAXgAgAF4iAGrApIBAzIuMZgBAKABAcABAQ&sclient=gws-wiz'
url5 = 'https://www.google.com/search?q=eur+to+aud&ei=cR0SYrWjJezjrgSwkKjYCw&ved=0ahUKEwj1n5vOjo72AhXssYsKHTAICrsQ4dUDCA4&uact=5&oq=eur+to+aud&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEJECMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIABBHELADOgcIABCwAxBDOgoIABCRAhBGEIICOgQIABBDOgcIABCABBAKSgQIQRgASgQIRhgAUIMXWN_UAWC-4AFoBHABeACAAViIAf8DkgEBOZgBAKABAcgBCsABAQ&sclient=gws-wiz'
url6 = 'https://www.google.com/search?q=aud+to+eur&ei=pDoSYubdE-bhrgSH8I_QDQ&oq=aud&gs_lcp=Cgdnd3Mtd2l6EAEYADIJCAAQQxBGEIICMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgUIABCABDIFCAAQgAQyCwguEIAEEMcBEKMCMgUIABCABDoNCC4QxwEQ0QMQ1AIQQzoLCC4QgAQQxwEQ0QM6CwguEIAEEMcBEK8BSgQIQRgASgQIRhgAUABY1wJgwBdoAHABeACAAUuIAdwBkgEBM5gBAKABAcABAQ&sclient=gws-wiz'


def eur_rub(url):
    r = requests.get(url, headers=headers)
    soup = BS(r.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde SwHCTb"})
    return convert[0].text.replace(',', '.')


def main():
    condition = True
    while condition:
        user_choice = input("Choose currency:"
                            "\n1.EUR TO RUB\n2.RUB TO EUR"
                            "\n3.EUR TO CZK\n4.CZK TO EUR\n5.EUR TO AUD\n6.AUD TO EUR"
                            "\n7.Calculate entered amount \n8.Exit\n-->")
        if user_choice == '1':
            print('Now 1 Eur is:', eur_rub(url1), 'Rub')
            continue
        if user_choice == '2':
            print('Now 1 Rub is:', eur_rub(url2), 'Eur')
            continue
        if user_choice == '3':
            print('Now 1 Eur is:', eur_rub(url3), 'Czk')
            continue
        if user_choice == '4':
            print('Now 1 Czk is:', eur_rub(url4), 'Eur')
            continue
        if user_choice == '5':
            print('Now 1 Eur is:', eur_rub(url5), 'Aud')
            continue
        if user_choice == '6':
            print('Now 1 Aud is:', eur_rub(url6), 'Eur')
            continue
        if user_choice == '7':
            while True:
                user_choice2 = input("Choose currency:"
                                     "\n1.EUR TO RUB\n2.RUB TO EUR"
                                     "\n3.EUR TO CZK\n4.CZK TO EUR\n5.EUR TO AUD\n6.AUD TO EUR"
                                     "\n7.Back to the menu \n8.Exit\n-->")
                user_choice3 = input('Enter amount:')
                if user_choice2 == '1':
                    calculate = float((eur_rub(url1)))
                    calculate2 = user_choice3
                    calculate3 = calculate * float(calculate2)
                    print(user_choice3, 'Eur =', calculate3, 'Rub')
                    continue
                if user_choice2 == '2':
                    calculate = float((eur_rub(url2)))
                    calculate2 = user_choice3
                    calculate3 = calculate * float(calculate2)
                    print(user_choice3, 'Rub =', calculate3, 'Eur')
                    continue
                if user_choice2 == '3':
                    calculate = float((eur_rub(url3)))
                    calculate2 = user_choice3
                    calculate3 = calculate * float(calculate2)
                    print(user_choice3, 'Eur =', calculate3, 'Czk')
                    continue
                if user_choice2 == '4':
                    calculate = float((eur_rub(url4)))
                    calculate2 = user_choice3
                    calculate3 = calculate * float(calculate2)
                    print(user_choice3, 'Czk =', calculate3, 'Eur')
                    continue
                if user_choice2 == '5':
                    calculate = float((eur_rub(url5)))
                    calculate2 = user_choice3
                    calculate3 = calculate * float(calculate2)
                    print(user_choice3, 'Eur =', calculate3, 'Aud')
                    continue
                if user_choice2 == '6':
                    calculate = float((eur_rub(url6)))
                    calculate2 = user_choice3
                    calculate3 = calculate * float(calculate2)
                    print(user_choice3, 'Aud =', calculate3, 'Eur')
                    continue
                if user_choice2 == '7':
                    main()
        if user_choice == '8':
            quit(print('Good Bye!'))


main()