def add_contact(contact):
   name = input("Enter name:").lower()
   phoneno = input("Enter Phoneno:") #store phonenum as string
   email = input("Enter email :").lower()
   address = input("enter address:").lower()
  # contact.update({name:{phoneno,email,address}}) it is storing as set data structure
   contact[name]={
      "phoneno.":phoneno,
       "email" :email,
       "address":address
  }
   print("Contact saved Successfully")


def view(contact):
    for item ,val in contact.items():
        print(f"{item.title()}")
        for key,val in val.items():
            print(f"{key.title()}:{val}")
        print("-----------------------------")









def search(contact):
    find =input("Enter name:").lower()
    if find not in contact:
        print("Not found")
    else:
        for key,val in contact.items():
            if key == find:
                print(f"{key}")
                for item ,value in val.items():
                    print(f'{item}:{value}')



        print("-----------------------------")






def delete(contact):
      name_todelte = input("enter name want to delete:").lower()
      if name_todelte in contact:
          contact.pop(name_todelte)
          print("Contact Deleted")
      else :print("not found")




def main():
    contact ={
        "arpit": {
            "phoneno.": 566789568,
            "email":"arpit3332@gmail.com",
            "address" : "Rudrapur,SLN"
        },
        "aditya":{
            "phoneno.": 7068992372,
            "email": "aditya342@gmail.com",
            "address": "Gomtinagar,LKO"
        },
        "ayush": {
            "phoneno.": 7068944372,
            "email": "ayush342@gmail.com",
            "address": "sector-52,noida"
        }
    }
    is_running = True
    while is_running:
        print("1.Adding a new contact")
        print("2.Viewing all saved contacts")
        print("3.Searching for a contact by name")
        print("4.Deleting a contact")
        print("5.Exit")

        choice = input("Enter choice from above menu(1,2,3,4,5):")
        if choice=="1":
            add_contact(contact)
        elif choice =="2":
            view(contact)
        elif choice =="3":
            search(contact)
        elif choice=="4":
            delete(contact)
        elif choice =="5":
            print("Thanks For Visiting!")
            break    
        else : is_running = False


main()