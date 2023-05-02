# Creating a Class Utility_Banking:

class Utility_Banking:
     Rent = 0
     Electric_bill = 0
     Sanitary_bill = 0
     Bank_bal = 0
     withdrawal = 0

#Instance Methods of the Class, Utility_Banking:

     def House_expense(self):
        Total_expense = self.Rent + self.Electric_bill + self.Sanitary_bill
        return Total_expense
    

     def Debit_func(self):
         Final_bal = self.Bank_bal - self.withdrawal
         return Final_bal
         
     
     def deleet(self):
         del Utility_Banking.House_expense
         print("House Expense Method is deleted")
         print("")


#Creating my expense Object:
My_expense = Utility_Banking()


#The Object Properties and their values:
My_expense.Rent = 200000
My_expense.Electric_bill= 10000
My_expense.Sanitary_bill = 5000
My_expense.Bank_bal = 500000
My_expense.withdrawal = 70000

#Calling the Functions
print(My_expense.House_expense())
print(My_expense.Debit_func())
My_expense.deleet()
