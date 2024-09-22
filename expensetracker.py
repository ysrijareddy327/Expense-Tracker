class expense:
    def __init__(self,date,descryption,amount):
        self.date=date
        self.descryption=descryption
        self.amount=amount
class expensetracker:
    def __init__(self):
        self.expenses=[]
    def add_expense(self,g):
        self.expenses.append(g)
    def remove_index(self,index):
        del self.expenses[index]
    def view_expense(self):
        if len(self.expenses)==0:
            print("list is empty")
        else:
            for i,expense in enumerate(self.expenses,start=1):
                print(f"{i}.date:{expense.date},discription:{expense.descryption},expensesamount:{expense.amount}")
    def total_expense(self):
        total=sum(expense.amount for expense in self.expenses)
        print(f"total sum is in ruppees:{total}")


expensetrackerobj=expensetracker()

while True:
    print("the expenses menu is")
    print("1.add expense\n2.delete expense\n3.view the expenses\n4.sum of expenses\n5.exit")
    choice=int(input("enter the choice in (1-5)"))
    if choice<0 and choice>5:
        print(("you choose incorrect option"))
    else:
        if choice==1:
            print("enter the date")
            date=input()
            descryption=input("enter the descryption")
            amount=int(input("enter the amount"))
            g=expense(date,descryption,amount)
            expensetrackerobj.add_expense(g)
        elif choice==2:
            h=int(input())-1
            expensetrackerobj.remove_index(h)
        elif choice==3:
            expensetrackerobj.view_expense()
        elif choice==4:
            expensetrackerobj.total_expense()
        elif choice==5:
            break






