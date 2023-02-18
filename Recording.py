yellow_pages = { 
    "C":[{"nama":"Chandra", "hp":"6282127289952", "kota":'Jakarta Barat', "zip":'132190'}],
    "D":[{"nama":"Dita Claudia", "hp":"628111366828", "kota":'Jakarta Selatan', "zip":'12190'}],
    "F":[
    {"nama":"Fuad", "hp":"6281482228265", "kota":'Jakarta Selatan', "zip":'668258'},
    {"nama":"Fatima", "hp":"6282242807286", "kota":'Jakarta timur', "zip":'599872'},
    ],
    "J":[{"nama":"Jeffrey Omar", "hp":"085219787939", "kota":'Jakarta Selatan', "zip":'12190'}], 
    "K":[{"nama":"Karina Farida", "hp":"6281515745925", "kota":'Depok', "zip":'294522'}], 
}

def organize_contact():
    print(' ')
    print("Contact List:- ")
    # organize the alphabets
    organized = dict(sorted(yellow_pages.items()))
    #Organize the dictionary of the alphabets
    for i in organized:
    #use sorted based on keys
        organized[i]= sorted(yellow_pages[i], key=lambda d: d['nama'])
        if len(organized[i]) > 0:
            print(i)
        else:
            continue
        for j in organized[i]:
            print('  ', j['nama'],'\n','|',"contact: ", j['hp']," "*(15 -len(j['hp'])), "|", "kota: ", j['kota']," "*(15 -len(j['kota'])), "|" ,"zip: ", j['zip']," "*(7 -len(j['zip'])), "|")
            print('--------------------------------------------------------------------------')
        print()


def organize_options():
    
    state = True
    while state:
        print('''
    Bagaimana Anda lebih suka mengambil kontak yang Anda inginkan.
    1. Semua Kontak yang di hurai.
    2. guna huruf.
    3. guna Nama kontak.
    4. Keluar.
    ''') 
        userOption = input("Input dari 1 - 4: ")
        if userOption == "1":
            print(' ')
            print("Kontak List:- ")
            # organize the alphabets
            organized = dict(sorted(yellow_pages.items()))
            #Organize the dictionary of the alphabets
            for i in organized:
            #use sorted based on keys
                organized[i]= sorted(yellow_pages[i], key=lambda d: d['nama'])
                # If new key is added and empty it skips it.
                if len(organized[i]) > 0:
                    print(i)
                else:
                    continue
                for j in organized[i]:
                    print('  ', j['nama'],'\n','|',"contact: ", j['hp']," "*(15 -len(j['hp'])), "|", "kota: ", j['kota']," "*(15 -len(j['kota'])), "|" ,"zip: ", j['zip']," "*(7 -len(j['zip'])), "|")
                    print('--------------------------------------------------------------------------')
                print()
            print('^^^ Scroll Atas ^^^')
            
        elif userOption == "2":
            contactAlph = input('Huruf apa anda mahu check? ').title()
            N = contactAlph[0] if contactAlph[0].isalpha() else '#'
            count = 0 
            print('\n ')
            print(f"Kontak List dalam huruf {N}:- ")
            if yellow_pages.get(N) is not None:
                print(N)
                sorted_yellowPages = sorted(yellow_pages[N], key=lambda d: d['nama'])
                for i in sorted_yellowPages:
                    print('  ', i['nama'],'\n','|',"contact: ", i['hp']," "*(15 -len(i['hp'])), "|", "kota: ", i['kota']," "*(15 -len(i['kota'])), "|" ,"zip: ", i['zip']," "*(7 -len(i['zip'])), "|")
                    print('--------------------------------------------------------------------------')
                    count += 1
                print('\n')
                print(f"Dalam tab huruf {N} ada {count} orang.")
            else:
                print('\n')
                print(f"Tiada orang dalam tab huruf {N}")
                print('\n')
                print('Balik ke cari Kontak Menu.')
                print('\n')

        elif userOption == '3':
            contactName = input('Who would you like to check? ').title()
            N = contactName[0] if contactName[0].isalpha() else '#'
            for i in yellow_pages[N]:
                if (contactName == i['nama']):
                    print('  ', i['nama'],'\n','|',"contact: ", i['hp']," "*(15 -len(i['hp'])), "|", "kota: ", i['kota']," "*(15 -len(i['kota'])), "|" ,"zip: ", i['zip']," "*(7 -len(i['zip'])), "|")
                    print('--------------------------------------------------------------------------')
                    
            print('\n')
            print("!!!<-----Contact not found----->!!!")
            if yellow_pages[N]:
                print('You could try search for these names instead: - ')
                print('\n')           
                for i in yellow_pages[N]:
                    print(i["nama"])
            print('\n')           
            
        elif userOption == "4":
            print('Returning to main programing')
            state = False

        else:
            print('\n')
            print("Input not valid.")
            print('\n')
            print('!!! ERROR !!!')
            print("Please Input a valid input of 1 - 4")

organize_contact()

organize_options()
