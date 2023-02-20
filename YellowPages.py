#Student: Jeffey Aroun bin Omar

#Initialization of DataBase
# A dictionary named Yellow pages where by each key holds a list of dictionary containing values for each contact.
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

# ===================================================================================================================
# Minor Functions START 
# ===================================================================================================================
# Simple functions to print.
def Greeting():
    print("Halo Selamat Datang di program Python Yellow Pages Jeffrey! ")
    print("Bisa saya bantu? ")

# Funtion to print Menu Options
def Menu():
    print('''
    MENU:-
    Silahkan pilih opsi

    1. Tambah Kontak.
    2. Perbaharui Kontak.
    3. Hapus Kontak.
    4. Cari Kontak.
    5. Keluar.
    ''')

# Function to organize the dictionary.
def organize_contact():
    print(' ')
    print("Contact List:- ")
    # organize the alphabets
    # make a new temp dictionary
    organized = dict(sorted(yellow_pages.items()))
# makes a new dictionary that sorts each key.
 
    #Organize each key value list by name.
    for i in organized:
        # sort dictionary indexs list by name
    #use sorted on the nama keys value.
        organized[i]= sorted(yellow_pages[i], key=lambda x: x['nama'])
        if len(organized[i]) > 0:
            print(i)
        else:
            continue
        for j in organized[i]:
            print('  ', j['nama'],'\n','|',"contact: ", j['hp']," "*(15 - len(j['hp'])), "|", "kota: ", j['kota']," "*(15 -len(j['kota'])), "|" ,"zip: ", j['zip']," "*(7 -len(j['zip'])), "|")
            print('--------------------------------------------------------------------------')
        print()
# ===================================================================================================================
# Minor Functions END 
# ===================================================================================================================

# ===================================================================================================================
# Main Functions START 
# ===================================================================================================================

# ===================================================================================================================
# Add contact Start padd
# ===================================================================================================================

# Function to Add Contact
# uses a single while loop to get correct data from user.
def Add_contact():
    state = True
    
    while state:
        # Take contact Details
        # first error check is name
        contactName = input("Nama kontak yang anda ingin tambah: ").title()
        # Get the first character of the name
        # checks if N is an alphabet or something else.
        if len(contactName) == 0 or contactName.isspace():
            print('Kembali ke Menu Utama')
            state = False
            return state
        N = contactName[0] if contactName[0].isalpha() else '#'
        # Need to check if N is in the yellow_pages dict.
        # if it is not it will create a new dict key.
        if N not in yellow_pages:
            yellow_pages[N] = []
            
        # Checks if user already exist
        for i in yellow_pages[N]:
            if (contactName == i['nama']):
                print('\n')
                print("!!!<-- contact dengan nama yang di input sudah wujud. Anda di kembalikan ke menu utama. -->!!!!")
                print('\n')
                state = False
                return state
        # continues if all is in order. 
        contactNum = input("berapa nomor kontaknya: ")
        if len(contactNum) == 0 or contactNum.isspace():
            print('Kembali ke Menu Utama')
            state = False
            return state
        contactKota = input("Kontak Kota: ").title()
        if len(contactKota) == 0 or contactKota.isspace():
            print('Kembali ke Menu Utama')
            state = False
            return state
        contactZip = input("Kontak zip: ")
        if len(contactZip) == 0 or contactZip.isspace():
            print('Kembali ke Menu Utama')
            state = False
            return state
        yellow_pages[N].append({'nama':contactName, 'hp':contactNum, 'kota':contactKota, 'zip':contactZip})
        state = False
# ====================================================================================================================
# Add Contact End 
# ====================================================================================================================

# ====================================================================================================================
# Update Contac Start pup
# ====================================================================================================================

# Update Contact
def Update_contact():
    
    contact = {}

    organize_contact()
    
    contact_found = False
    while not contact_found:
        contactName = input('Kontak mana yang ingin Anda perbarui? ').title()
        if not contactName or contactName.isspace():
            print("Kembali ke Menu Utama")
            return None
        # to handle names starting with non-alphabetic characters
        N = contactName[0] if contactName[0].isalpha() else '#'
        # temp storage for printing later.
        possible_matches = []
        # start false so the program could be sure to move on. 
        found_contact = None
        # finds if user input has any matching results.
        for i in yellow_pages[N]:
            if i['nama'] == contactName:
                found_contact = i
                contact = i
                contact_found = True
            # finds similar matching for double checking
            elif contactName in i['nama']:
                possible_matches.append(i)
                
        if found_contact:
            break
        elif not contactName:
            print("Kembali ke Menu Utama")
            return None
        else:
            print("\nNama tidak cocok dengan salah satu entri di basis data kami. \n\nBisakah maksud Anda salah satu dari kemungkinan nama ini?")
            print('\n'+ N)
            for j in sorted(possible_matches, key=lambda x: x['nama']):
                print('  ', j['nama'],'\n','|',"contact: ", j['hp']," "*(15 -len(j['hp'])), "|", "kota: ", j['kota']," "*(15 -len(j['kota'])), "|" ,"zip: ", j['zip']," "*(7 -len(j['zip'])), "|")
                print('--------------------------------------------------------------------------')
            print('\n')
        if contact:
            print(f"\nKontak yang dipilih: {contact['nama']}, Hp: {contact['hp']}, Kota: {contact['kota']}, Zip: {contact['zip']}\n")
                

    while contact_found:
        print('''
            Kolom kontak mana yang ingin Anda perbarui?:
            1. Nama
            2. Hp
            3. Kota
            4. Zip
            5. Kembali ke menu utama
            ''')
        field_choice = input("Silakan pilih 1 - 5:  ")

        if field_choice == '1':
            new_name = input("Masukkan nama baru: ").title()
            N = new_name[0] if new_name[0].isalpha() else '#'
            contact['nama'] = new_name
            print("Nama berhasil diperbarui.")
        elif field_choice == '2':
            new_hp = input("Masukkan hp baru: ")
            contact['hp'] = new_hp
            print("Hp berhasil diperbarui.")
        elif field_choice == '3':
            new_kota = input("Masukkan kota baru: ").title()
            contact['kota'] = new_kota
            print("Kota berhasil diperbarui.")
        elif field_choice == '4':
            new_zip = input("Masukkan zip baru: ")
            contact['zip'] = new_zip
            print("Zip berhasil diperbarui.")
        elif field_choice == '5':
            print("Kembali ke menu utama.")
            # only way to exit loop
            break
        else:
            print("Pilihan tidak sah. Silakan pilih 1 - 5.\n")
        # update the yellow_pages dictionary with the modified contact
        yellow_pages[N][yellow_pages[N].index(found_contact)] = contact
        
        
        # reset contact
        contact = {}

# ===================================================================================================================
# Update Contact End 
# ===================================================================================================================

# ===================================================================================================================
# Delete Contact Start pdel
# ===================================================================================================================

# Delete contact
def Delete_contact():
    #prints current contact list for better reference
    organize_contact()
    #Starts initial state of first loop.
    contact_found = False

    while not contact_found:
        contactName = input("Silakan tulis nama kontak yang ingin Anda hapus: ").title()
        N = contactName[0] if contactName[0].isalpha() else '#'
        for i in yellow_pages[N]:
            if contactName == i['nama']:
                contact_found = True
                
                print('''
                Sudah Jumpa
                ''')
            if not contact_found:
                print('\n')
                print("!!!<-----Kontak tidak ditemukan----->!!!")
                print('\n')
                suggested_contacts = [j['nama'] for j in yellow_pages[N] if contactName in j['nama']]
                if suggested_contacts:
                    print('Apakah yang Anda maksud adalah salah satu dari kontak berikut?')
                    print(N)
                    for j in yellow_pages[N]:
                        if contactName in j['nama']:
                            print('  ', j['nama'],'\n','|',"contact: ", j['hp']," "*(15 -len(j['hp'])), "|", "kota: ", j['kota']," "*(15 -len(j['kota'])), "|" ,"zip: ", j['zip']," "*(7 -len(j['zip'])), "|")
                            print('--------------------------------------------------------------------------')
                    print('\n')

    while contact_found:    
        assurance = input("Anda yakin ingin menghapus kontak? (Y/N): ").title()
        if assurance == "Y":
            for i in yellow_pages[N]:
                if (contactName == i['nama']):
                    yellow_pages[N].remove(i)
                    print("kontak berhasil dihapus.")
                    contact_found = False
        elif assurance == "N":
            print('\n')
            print("Baik kita akan kembali ke Menu Utama.")
            contact_found = False
        else:
            print('\n')
            print("Input yang salah. Program ini akan kembali ke menu utama.")

# ===================================================================================================================
# Delete Contact End 
# ===================================================================================================================

# ===================================================================================================================
# Search Contact Start pser
# ===================================================================================================================

# Find user by alphabet, name or just list everything at once.
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
            organize_contact()
            print('^^^ Scroll Atas ^^^')
            
        elif userOption == "2":
            contactAlph = input('Huruf apa anda mahu check? ').title()
            N = contactAlph[0] if contactAlph[0].isalpha() else '#'
            count = 0 
            print('\n ')
            print(f"Kontak List dalam huruf {N}:- ")
            if yellow_pages.get(N) is not None:
                print(N)
                sorted_yellowPages = sorted(yellow_pages[N], key=lambda x: x['nama'])
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
            contactName = input('Siapa yang ingin Anda periksa? ').title()
            N = contactName[0] if contactName[0].isalpha() else '#'
            for i in yellow_pages[N]:
                if (contactName == i['nama']):
                    print('  ', i['nama'],'\n','|',"contact: ", i['hp']," "*(15 -len(i['hp'])), "|", "kota: ", i['kota']," "*(15 -len(i['kota'])), "|" ,"zip: ", i['zip']," "*(7 -len(i['zip'])), "|")
                    print('--------------------------------------------------------------------------')
                else:
                    print('\n')
                    print("!!!<-----Kontak tidak ditemukan----->!!!")
            if yellow_pages[N]:
                print('Anda dapat mencoba mencari nama-nama ini sebagai gantinya: - ')
                print('\n')           
                print(f'{N}')
                for i in yellow_pages[N]:
                    if (contactName in i['nama']):
                        print('  ', i['nama'],'\n','|',"contact: ", i['hp']," "*(15 -len(i['hp'])), "|", "kota: ", i['kota']," "*(15 -len(i['kota'])), "|" ,"zip: ", i['zip']," "*(7 -len(i['zip'])), "|")
                        print('--------------------------------------------------------------------------')
            print('\n')           
            
        elif userOption == "4":
            print('Kembali ke menu utama')
            state = False

        else:
            print('\n')
            print("Masukan tidak valid.")
            print('\n')
            print('!!! ERROR !!!')
            print("Silakan Masukkan input yang valid dari 1 - 4")

# ===================================================================================================================
# Search Contact END 
# ====================================================================================================================

# ====================================================================================================================
# Main Functions Start 
# ====================================================================================================================

# ====================================================================================================================
# Program script Start = pstart
# ====================================================================================================================


# Main while loop that executes the menu function then takes a user input 
# organize_contact()
Greeting()
while True:
    Menu()
    userInput = input(" Sila pilih nomor: ")
    varifyInput = int(userInput if userInput.isdigit() else 6)
    if (varifyInput == 1):
        print("Anda pilih: " + str(userInput))
        Add_contact()
    elif (varifyInput == 2):
        print("Anda pilih: " + str(userInput))
        Update_contact()
    elif (varifyInput == 3):
        print("Anda pilih: " + str(userInput))
        Delete_contact()
    elif (varifyInput == 4):
        print("Anda pilih: " + str(userInput))
        organize_options()
    elif (varifyInput == 5):
        print("Anda pilih: " + str(userInput))
        break
    else:
        print('\n')        
        print("!!!<---Pilihan yang anda masukkan salah. Silakan coba lagi.--->!!! ")
        print('\n')        

# ====================================================================================================================
# Program script end
# ====================================================================================================================
