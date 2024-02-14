def menu():
    print("******MENU******")
    print("1-List Books")
    print("2-Add Books")
    print("3-Remove Books")
    print("4- Quit (q)")


class Library():
    def __init__(self,bookname,author,releasedate,numberofpages):
        self.bookname = bookname
        self.author = author
        self.releasedate = releasedate
        self.numberofpages = numberofpages

    def addbooks(self):
        with open("books.txt", "a+") as file:
            eklenecekkitap = f"{book.bookname},{book.author},{book.releasedate},{book.numberofpages}\n"
            file.write(eklenecekkitap)
            print("\nThe book is completely added to the list!")

    def deletebooks(self, booktoremove):
        try:
            with open("books.txt","r") as file:
                lines = file.readlines()
            with open("books.txt","w") as file:
                for line in lines:
                    if not line.startswith(booktoremove):
                        file.write(line)
            print("Book removed successfully.")
        except:
            print("There's an issue happened.")

    def listbooks(self):
        try:
            with open("books.txt", "r") as file:
                print("\n")
                data = file.read()
                newdata = data.splitlines()
                for veri in newdata:
                    veri2 = veri.split(",")
                    print(f"Book Name: {veri2[0]} Author: {veri2[1]}")
        except:
            print("\nThere's an issue happened.")





x=0
while(x!=1):
    print("\n")
    menu()
    cevap = input("Please make a choice: ")

    if(cevap=="q"):
        x=1
        break
    elif(cevap=="1"):
        book = Library("","","","")
        book.listbooks()
    elif (cevap=="2"):
        bookname = input("Enter the book name: ")
        author = input("Enter the name of author: ")
        releasedate = input("Enter the release date: ")
        numberofpages = input("Enter the number of pages: ")
        book = Library(bookname, author, releasedate, numberofpages)
        book.addbooks()
    elif (cevap=="3"):
        booktoremove = input("Enter the book title to remove: ")
        book = Library("","","","")
        book.deletebooks(booktoremove)
    else:
        print("Please enter a valid number!")








