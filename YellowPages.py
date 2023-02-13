#Student: Jeffey Aroun bin Omar

#Initialization of DataBase
yellow_pages = {
    "J":[{"nama":"Jeffrey Omar", "hp":"085219787939", "kota":'jakarta Selatan', "zip":'12190'}], 
    "D":[{"nama":"Dita Claudia", "hp":"628111366828", "kota":'jakarta Selatan', "zip":'12190'}],
    "C":[{"nama":"Chandra", "hp":"6282127289952", "kota":'jakarta Barat', "zip":'132190'}],
    "K":[{"nama":"Karina Farida", "hp":"6281515745925", "kota":'Depok', "zip":'294522'}],
    "F":[
    {"nama":"Fuad", "hp":"6281482228265", "kota":'jakarta Selatan', "zip":'668258'},
    {"nama":"Fatima", "hp":"6282242807286", "kota":'jakarta timur', "zip":'599872'},
    ]
}



def Greeting():
    print("Halo Selamat Datang ke Jeffrey punya Python Yello Pages Program! ")
    print("Bagai Mana saya bisa Bantu anda? ")


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
        
        print(i)
        print()
        for j in organized[i]:
            print(f'''{j['nama']}\ncontact: {j['hp']}\tkota: {j['kota']}\tzip: {j['zip']}''')
            print()
            
        

organize_contact()

