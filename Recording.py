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



def Delete_contact():
    #prints current contact list for better reference
    
    #Starts initial state of first loop.
    contact_found = False
    
    contact = []
    while not contact_found:
        contactName = input("Silakan tulis nama kontak yang ingin Anda hapus: ").title()
        N = contactName[0] if contactName[0].isalpha() else '#'
        for i in yellow_pages[N]:
            if contactName == i['nama']:
                contact_found = True
                contact = i
                print('''
                Sudah Jumpa
                ''')
            else:
                print('\n')
                print("!!!<-----Kontak tidak ditemukan----->!!!")
                print('\n')
                print('Apakah yang Anda maksud adalah salah satu dari kontak berikut?')
                print(N)
                for j in contact:
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

Delete_contact()
