class BookStore:
    def __init__(self, list_of_book, name):
        self.books = list_of_book
        self.name=name
        self.lenddickt={}

    def displaybooks(self):
        print(f"Books present in our Store are ")

        for books in self.books:
            print("\t" + books)

    def lendbook(self, user, book):
        if book not in self.lenddickt.keys():
            self.books.remove(book)
            self.lenddickt.update({book:user})
            print("Lender-Book Database has been updated.You can take the book now")

        else:
            print(f"Book has been taken by{self.lenddickt}")

    def addbook(self,book, name):
        self.books.append(book)
        print(f"The book {book} has been added soled by {name}")
        print("book has been updated")





if __name__ == '__main__':
    ProgramingBookStore = BookStore(["Python", "C++", "Java", "C", "CLRS", "R.D.Sharma", "OOPS IN PYTHON", "OOPS IN C++", "OOPS IN JAVA"], "SuperBookStore")
    while True:
        print(f'Welcome to {ProgramingBookStore.name} store. Enter your choice to continue')
        print(f'1 to Display book')
        print(f'2 to Lend a book')
        print(f'3 to Return or Add book')
        print("------------------YOUR CHOICE------------")
        choice=int(input())

        if choice==1:
            ProgramingBookStore.displaybooks()

        elif choice==2:
            book=input("Enter the name of the book: ")
            name=input("Enter your name: ")
            ProgramingBookStore.lendbook(name, book)

        elif choice==3:
            book=input("Enter the name of the book: ")
            name =input("Enter your name: ")
            ProgramingBookStore.addbook(book, name)

        else:
            print("Wrong input")

        print("press q to quit c to continue")
        choice2=""
        while(choice2 !="c" and choice2 !="q"):
            choice2=input()
            choice2.lower()
            if choice2=="q":
                print("Tanks for visiting our book store")
                exit()

            elif choice2=='c':
                continue
