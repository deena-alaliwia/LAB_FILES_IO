try:
    while True:
        answer=input("do you wants to add a new TO-DO item ? enter 'y' for yes or 'n' for no :")
        if answer=='y' or answer=='Y':
            file =open ("to-do.txt","a+",encoding="UTF-8")
            to_do =input ("enter the item you want to do :"+"\n")
            file.write(to_do+"\n")
            file.close()
        elif  answer=="n"or answer=="N" :  
            answer2=input("do you want to list your TO-DO items y/n:")
            if answer2=='y':
              file =open ("to-do.txt","r",encoding="UTF-8") 
              file.seek(0)
              print(file.read ())
              file.close()
            elif answer2=='n' :
                answer3=input("do you wants to repeat question or eixt {y or exit}:")
                if answer3=="exit":
                    break
                elif answer3=="y":
                    continue

except Exception:
    print("somethong is worng")

print("thank you for using the to do program , come back again sonn ")
                
             
        



