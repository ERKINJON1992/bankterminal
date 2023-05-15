print("Xush kelibsiz Hamkorbamk \n\n kartani kiriting")
password = 1234
choice = 0
balanse = 100000
pin = int(input("Parolni kiriting \n"))
if pin ==password:
    while choice != 4:
        
        print("\n\n**** Menu ****")
        print("1 == Balans")
        print("2 == Naqt")
        print("3 == Dipazit")
        print("4 == chiqish\n")
        
        choice= int(input("\nRaqamni kiriting \n"))
        if choice == 1:
            print(f"balans = {balanse} so'm",)
            
        elif choice == 3:
            dep = int(input("pul qo'shish uchun so'mani kiriting :"))
            balanse += dep
            print(f"\n qo'shilgan {dep}so'm")
            print(f"\nbalansda {balanse} so'm")
            
            
        elif choice == 2:
            naqt = int(input("pul yichish :"))
            balanse -= naqt
            print(f"\n yichilgan {naqt}so'm")
            print(f"\nbalansda {balanse} so'm")
            
        elif choice ==4:
            print("Sizga yordam bergandan Hursanman Hayr")
        else:
            print("***Hayr Salomat biling***")
else:
    print("Parol xato ")