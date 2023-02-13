#Student: Jeffey Aroun bin Omar

#Initialization of DataBase
yellow_pages = { 
    "C":[{"nama":"Chandra", "hp":"6282127289952", "kota":'jakarta Barat', "zip":'132190'}],
    "D":[{"nama":"Dita Claudia", "hp":"628111366828", "kota":'jakarta Selatan', "zip":'12190'}],
    "E":[],
    "F":[
    {"nama":"Fuad", "hp":"6281482228265", "kota":'jakarta Selatan', "zip":'668258'},
    {"nama":"Fatima", "hp":"6282242807286", "kota":'jakarta timur', "zip":'599872'},
    ],
    "J":[{"nama":"Jeffrey Omar", "hp":"085219787939", "kota":'jakarta Selatan', "zip":'12190'}], 
    "K":[{"nama":"Karina Farida", "hp":"6281515745925", "kota":'Depok', "zip":'294522'}],
   
    
}



def Greeting():
    print("Halo Selamat Datang ke Jeffrey punya Python Yello Pages Program! ")
    print("Bagai Mana saya bisa Bantu anda? ")

# Funtion to print Menu Options
def Menu():
    print('''
    MENU:-
    Sila pulih opsi

    1. add Contact.
    2. Update Contact.
    3. Delete Contact.
    4. Search Contact.
    5. Keluar.
    ''')



# Function to Add Contact

def Add_contact():
    state =True
    while state:
        # Take contact Details
        contactName = input("Name of the person you would like to add: ").title()
        # Get the first character of the name
        N = contactName[0] if contactName[0].isalpha() else '#'
        # If the key doesn't exist in the dictionary, add it
        if N not in yellow_pages:
            yellow_pages[N] = []
        # Checks if user already exist
        for i in yellow_pages[N]:
            if (contactName == i['nama']):
                print('\n')
                print("!!!<---- User already exists ---->!!!!")
                print('\n')
                state = False
                return state
                    
        contactNum = input("what is the contact number: ")
        contactKota = input("contact Kota: ")
        contactZip = input("Contact zip: ")
        yellow_pages[N].append({'nama':contactName, 'hp':contactNum, 'kota':contactKota, 'zip':contactZip})
        state = False
    
    
# How to add an item to a dictionary



# Function to organize the dictionary. 
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
    
            


# organize_contact()
Greeting()
while True:
    Menu()
    userOption = int(input(" Sila pilih nomur: "))
    if (userOption == 1):
        print("user picked: " + str(userOption))
        Add_contact()
    elif (userOption == 2):
        print("user picked: " + str(userOption))
    elif (userOption == 3):
        print("user picked: " + str(userOption))
    elif (userOption == 4):
        print("user picked: " + str(userOption))
        organize_contact()
    elif (userOption == 5):
        print("user picked: " + str(userOption))
        break
    else:
        print("Please input the proper prompt.")
# contactName = input("Name of the person you would like to add: ").title()
# N = contactName[0]
# for i in yellow_pages[N]:
#     print(contactName)
#     if (contactName == i['nama']):
#         print("User name Already exsits")
#     else:
#         print('adding User')