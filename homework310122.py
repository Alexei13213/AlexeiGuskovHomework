months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
          "november", "december"]
gender = ["male", "female", "male", "female", "male", "female", "male", "female"]





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
                hospital = int(user_input[7] + user_input[8] + user_input[9])
                if hospital in range(1, 11):
                    hospitalname = "Kuressaare Hospital"
                    hospitalnr = (int(user_input[7] + user_input[8] + user_input[9]))
                elif hospital in range(11, 20):
                    hospitalname = "University of Tartu Women's Clinic"
                    hospitalnr = (int(user_input[7] + user_input[8] + user_input[9]))
                elif hospital in range(21, 150):
                    hospitalname = "East Tallinn Central Hospital, Pelgulinna Maternity Hospital (Tallinn)"
                    hospitalnr = (int(user_input[7] + user_input[8] + user_input[9]))
                elif hospital in range(151, 161):
                    hospitalname = "Keila Hospital"
                    hospitalnr = (int(user_input[7] + user_input[8] + user_input[9]))
                elif hospital in range(161, 221):
                    hospitalname = "Rapla Hospital, Loksa Hospital, Hiiumaa Hospital (Kärdla)"
                    hospitalnr = (int(user_input[7] + user_input[8] + user_input[9]))
                elif hospital in range(221, 270):
                    hospitalname = "Ida-Viru Central Hospital (Kohtla-Järve, former Jõhvi)"
                    hospitalnr = (int(user_input[7] + user_input[8] + user_input[9]))
                elif hospital in range(271, 371):
                    hospitalname = "Maarjamõisa Clinic (Tartu), Jõgeva Hospital"
                    hospitalnr = (int(user_input[7] + user_input[8] + user_input[9]))
                elif hospital in range(371, 421):
                    hospitalname = "Narva Hospital"
                    hospitalnr = (int(user_input[7] + user_input[8] + user_input[9]))
                elif hospital in range(421, 471):
                    hospitalname = "Pärnu Hospital"
                    hospitalnr = (int(user_input[7] + user_input[8] + user_input[9]))
                elif hospital in range(471, 491):
                    hospitalname = "Haapsalu Hospital"
                    hospitalnr = (int(user_input[7] + user_input[8] + user_input[9]))
                elif hospital in range(491, 521):
                    hospitalname = "Järva County Hospital (Paide)"
                    hospitalnr = (int(user_input[7] + user_input[8] + user_input[9]))
                elif hospital in range(521, 571):
                    hospitalname = "Rakvere Hospital, Tapa Hospital"
                    hospitalnr = (int(user_input[7] + user_input[8] + user_input[9]))
                elif hospital in range(571, 601):
                    hospitalname = "Valga Hospital"
                    hospitalnr = (int(user_input[7] + user_input[8] + user_input[9]))
                elif hospital in range(601, 651):
                    hospitalname = "Viljandi Hospital"
                    hospitalnr = (int(user_input[7] + user_input[8] + user_input[9]))
                elif hospital in range(651, 701):
                    hospitalname = "South Estonian Hospital (Võru), Põlva Hospital"
                    hospitalnr = (int(user_input[7] + user_input[8] + user_input[9]))
                else:
                    hospitalname = "Unknown hospital"
    if user_choice == '1':
        print("you are", gename )
    if user_choice == '2':
        print(". Year of birth " + years + ", your birthday " + str(day) + ". " + monthsname)
    if user_choice == '3':
        print(". You are borned: " + hospitalname + ".")