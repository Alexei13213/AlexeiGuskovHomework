from bs4 import BeautifulSoup as BS
import requests
url = 'https://www.google.com/search?q=eur+to+rub&source=hp&ei=Y3kRYuHCA_aTwPAPkMSQ4AQ&iflsig=AHkkrS4AAAAAYhGHc7Ksn3dYdETj2Snv8wwEc1kn93Cy&oq=eur+to&gs_lcp=Cgdnd3Mtd2l6EAEYADIQCAAQgAQQsQMQgwEQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoICAAQgAQQsQM6CwgAEIAEELEDEIMBOhEILhCABBCxAxCDARDHARDRAzoRCC4QgAQQsQMQgwEQxwEQrwE6FAguEIAEELEDEIMBEMcBENEDENQCOgsILhCABBDHARCjAjoLCC4QgAQQxwEQrwE6BwgAEIAEEApQAFi8EmDZJWgAcAB4AIABPYgBlAKSAQE2mAEAoAEB&sclient=gws-wiz'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
current_conv_price = 0


def eur_rub():
    r = requests.get(url, headers=headers)
    soup = BS(r.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": "2"})
    print("Now 1 Euro is: " + convert[0].text.replace(',', '.') + " Rub")


url2 = 'https://www.google.com/search?q=rub+to+eur&hl=ru&source=hp&ei=yKcRYsrVLvKErwTTxZbICg&iflsig=AHkkrS4AAAAAYhG12H3TcpSNXxe2-wO8Ldgfaof2Dsko&oq=rub&gs_lcp=Cgdnd3Mtd2l6EAEYADILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgsILhCABBDHARCvATIFCAAQgAQ6DgguEIAEELEDEIMBENQCOhEILhCABBCxAxCDARDHARDRAzoICAAQgAQQsQM6DgguEIAEELEDEMcBEKMCOg4ILhCABBDHARCvARDUAjoMCAAQsQMQgwEQChABUABY6gRgkhhoAHAAeACAATiIAaEBkgEBM5gBAKABAQ&sclient=gws-wiz'


def rub_eur():
    r2 = requests.get(url2, headers=headers)
    soup2 = BS(r2.content, 'html.parser')
    convert2 = soup2.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": "3"})
    print("Now 1 Rub is: " + convert2[0].text.replace(',', '.') + " Eur")


url3 = 'https://www.google.com/search?q=eur+to+czk&hl=ru&ei=hJwRYoGUGqOQrgStu59I&oq=eur&gs_lcp=Cgdnd3Mtd2l6EAEYBjIJCAAQQxBGEIICMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDOgcIABBHELADOgcIABCwAxBDOgsIABCABBCxAxCDAToHCAAQsQMQQzoICAAQgAQQsQM6EQguEIAEELEDEIMBEMcBENEDOgUIABCABEoECEEYAEoECEYYAFCRhgFYnI4BYNO_AWgCcAF4AIABQ4gBugGSAQEzmAEAoAEByAEKwAEB&sclient=gws-wiz'


def eur_czk():
    r2 = requests.get(url3, headers=headers)
    soup2 = BS(r2.content, 'html.parser')
    convert2 = soup2.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": "2"})
    print("Now 1 Euro is: " + convert2[0].text.replace(',', '.') + " Czk")


url4 = 'https://www.google.com/search?q=czk+to+eur&hl=ru&ei=f6gRYr2cLoeRrwSq2Zr4CQ&oq=czk&gs_lcp=Cgdnd3Mtd2l6EAEYADIJCAAQQxBGEIICMgUIABCABDIECAAQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBAgAEEMyBQgAEIAEMgUIABCABDoICAAQgAQQsQM6EQguEIAEELEDEIMBEMcBEK8BOg4ILhCABBCxAxDHARDRAzoLCC4QgAQQxwEQ0QM6CwguEIAEEMcBEKMCOg4ILhCxAxCDARDHARCvAToECC4QQzoOCC4QgAQQxwEQ0QMQ1AI6BQguEIAEOggILhCABBDUAkoECEEYAEoECEYYAFAAWLQGYOsVaABwAXgAgAF4iAGrApIBAzIuMZgBAKABAcABAQ&sclient=gws-wiz'


def czk_eur():
    r2 = requests.get(url4, headers=headers)
    soup2 = BS(r2.content, 'html.parser')
    convert2 = soup2.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": "3"})
    print("Now 1 Czk is: " + convert2[0].text.replace(',', '.') + " Eur")


url5 = 'https://www.google.com/search?q=eur+to+aud&ei=cR0SYrWjJezjrgSwkKjYCw&ved=0ahUKEwj1n5vOjo72AhXssYsKHTAICrsQ4dUDCA4&uact=5&oq=eur+to+aud&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEJECMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIABBHELADOgcIABCwAxBDOgoIABCRAhBGEIICOgQIABBDOgcIABCABBAKSgQIQRgASgQIRhgAUIMXWN_UAWC-4AFoBHABeACAAViIAf8DkgEBOZgBAKABAcgBCsABAQ&sclient=gws-wiz'


def eur_aud():
    r2 = requests.get(url5, headers=headers)
    soup2 = BS(r2.content, 'html.parser')
    convert2 = soup2.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": "2"})
    print("Now 1 EUR is: " + convert2[0].text.replace(',', '.') + " AUD")


url6 = 'https://www.google.com/search?q=aud+to+eur&ei=pDoSYubdE-bhrgSH8I_QDQ&oq=aud&gs_lcp=Cgdnd3Mtd2l6EAEYADIJCAAQQxBGEIICMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgUIABCABDIFCAAQgAQyCwguEIAEEMcBEKMCMgUIABCABDoNCC4QxwEQ0QMQ1AIQQzoLCC4QgAQQxwEQ0QM6CwguEIAEEMcBEK8BSgQIQRgASgQIRhgAUABY1wJgwBdoAHABeACAAUuIAdwBkgEBM5gBAKABAcABAQ&sclient=gws-wiz'


def aud_eur():
    r2 = requests.get(url6, headers=headers)
    soup2 = BS(r2.content, 'html.parser')
    convert2 = soup2.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": "2"})
    print("Now 1 AUD is: " + convert2[0].text.replace(',', '.') + " Eur")


def main():
    condition = True
    while condition:
        user_choice = input("Choose currency:"
                            "\n1.EUR TO RUB\n2.RUB TO EUR"
                            "\n3.EUR TO CZK\n4.CZK TO EUR\n5.EUR TO AUD\n6.AUD TO EUR\n7.Exit\n-->")
        if user_choice == '1':
            eur_rub()
            continue
        if user_choice == '2':
            rub_eur()
            continue
        if user_choice == '3':
            eur_czk()
            continue
        if user_choice == '4':
            czk_eur()
            continue
        if user_choice == '5':
            eur_aud()
            continue
        if user_choice == '6':
            aud_eur()
            continue
        if user_choice == '7':
            quit()


main()