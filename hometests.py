months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
          "november", "december"]
gender = ["male", "female", "male", "female", "male", "female", "male", "female"]

kuressaare = 0
tartu = 10
idaTallinn = 20
idaViru = 220
maarjaMoisa = 270
narva = 370
parnu = 420
haapsalu = 470
jarvamaa = 490
rakvere = 520
valga = 570
viljandi = 600
lounaEesti = 650



while True:
    try:
        user_input = input('Please enter you ID (type exit to quit): ')
        if user_input.lower() == 'exit':
            break
        int(user_input)
        if len(user_input) != 11:
            if len(user_input) > 11:
                print('ID is too long!')
            else:
                print('ID is too short!')
            raise UserWarning
    except ValueError:
        print('ID you entered is not numeric!')
    except UserWarning:
        print('ID you entered is not 11 digits long')
    else:
        print(user_input)
        break
condition = True
while condition:
    user_choice = input("Check ID. Choose what you want to know:\n1.Print 'Gender'\n2.Print 'Date of birthday'"
                        "\n3.Print 'place of birth'\n5.Exit\n-->")
    for ge in gender:
        ge = int(user_input[0])
        gename = gender[ge - 1]
        if int(user_input[0]) <= 8 and int(user_input[0]) >= 1:
         if int(user_input[0]) == 1 or int(user_input[0]) == 2:
            years = "18" + str(user_input[1] + user_input[2])
        if int(user_input[0]) == 3 or int(user_input[0]) == 4:
            years = "19" + str(user_input[1] + user_input[2])
        if int(user_input[0]) == 5 or int(user_input[0]) == 6:
            years = "20" + str(user_input[1] + user_input[2])
        if int(user_input[0]) == 7 or int(user_input[0]) == 8:
            years = "21" + str(user_input[1] + user_input[2])
        for monthsname in months:
            month = int(user_input[3] + user_input[4])
            monthsname = months[month - 1]
        if month >= 1 and month <= 12:
            day = int(user_input[5] + user_input[6])
            if day >= 1 and day <= 31:
                haigla = int(user_input[7] + user_input[8] + user_input[9])
                if haigla in range(1, 11):
                    haiglaNimi = "Kuressaare Hospital"
                    jarjekorraNr = (int(user_input[7] + user_input[8] + user_input[9]) - kuressaare)
                elif haigla in range(11, 20):
                    haiglaNimi = "University of Tartu Women's Clinic"
                    jarjekorraNr = (int(user_input[7] + user_input[8] + user_input[9]) - tartu)
                elif haigla in range(21, 150):
                    haiglaNimi = "East Tallinn Central Hospital, Pelgulinna Maternity Hospital (Tallinn)"
                    jarjekorraNr = (int(user_input[7] + user_input[8] + user_input[9]) - idaTallinn)
                elif haigla in range(151, 161):
                    haiglaNimi = "Keila Hospital"
                    jarjekorraNr = (int(user_input[7] + user_input[8] + user_input[9]) - idaViru)
                elif haigla in range(161, 221):
                    haiglaNimi = "Rapla Hospital, Loksa Hospital, Hiiumaa Hospital (Kärdla)"
                    jarjekorraNr = (int(user_input[7] + user_input[8] + user_input[9]) - maarjaMoisa)
                elif haigla in range(221, 270):
                    haiglaNimi = "Ida-Viru Central Hospital (Kohtla-Järve, former Jõhvi)"
                    jarjekorraNr = (int(user_input[7] + user_input[8] + user_input[9]) - narva)
                elif haigla in range(271, 371):
                    haiglaNimi = "Maarjamõisa Clinic (Tartu), Jõgeva Hospital"
                    jarjekorraNr = (int(user_input[7] + user_input[8] + user_input[9]) - parnu)
                elif haigla in range(371, 421):
                    haiglaNimi = "Narva Hospital"
                    jarjekorraNr = (int(user_input[7] + user_input[8] + user_input[9]) - haapsalu)
                elif haigla in range(421, 471):
                    haiglaNimi = "Pärnu Hospital"
                    jarjekorraNr = (int(user_input[7] + user_input[8] + user_input[9]) - jarvamaa)
                elif haigla in range(471, 491):
                    haiglaNimi = "Haapsalu Hospital"
                    jarjekorraNr = (int(user_input[7] + user_input[8] + user_input[9]) - rakvere)
                elif haigla in range(491, 521):
                    haiglaNimi = "Järva County Hospital (Paide)"
                    jarjekorraNr = (int(user_input[7] + user_input[8] + user_input[9]) - valga)
                elif haigla in range(521, 571):
                    haiglaNimi = "Rakvere Hospital, Tapa Hospital"
                    jarjekorraNr = (int(user_input[7] + user_input[8] + user_input[9]) - viljandi)
                elif haigla in range(571, 601):
                    haiglaNimi = "Valga Hospital"
                    jarjekorraNr = (int(user_input[7] + user_input[8] + user_input[9]) - lounaEesti)
                elif haigla in range(601, 651):
                    haiglaNimi = "Viljandi Hospital"
                    jarjekorraNr = (int(user_input[7] + user_input[8] + user_input[9]) - lounaEesti)
                elif haigla in range(651, 701):
                    haiglaNimi = "South Estonian Hospital (Võru), Põlva Hospital"
                    jarjekorraNr = (int(user_input[7] + user_input[8] + user_input[9]) - lounaEesti)
                else:
                    haiglaNimi = "teadmata haiglas"
    if user_choice == '1':
        print("you are", gename )
    if user_choice == '2':
        print(". Year of birth " + years + ", your birthday " + str(day) + ". " + monthsname)
    if user_choice == '3':
        print(". You are borned: " + haiglaNimi + ".")