import random,os,sys,re
path=os.getcwd();
record=[{"Account-Holder's Name":None,"Account Number":None,"Amount":None}]
class Account:
    amount=0
    name=""
    account_number=0

    def display(self):
        print("\nAccount Number: ",self.account_number)
        print("Account-Holder's Name: ",self.name)
        print("Current Balance: ", self.amount)
        menu()

    def make_an_account(self):
        print('\n\n---------------------------------------------------------------------------')
        print("Please Fill In The Following Details")
        self.name=input("Enter Your Name: ")
        while not self.name:
            self.name=input("Enter Your Name: ")
        self.amount=1000
        self.account_number=random.randint(10000000,100000000)
        if os.access(str(path)+"/bank_records.txt",os.F_OK):
            with open("bank_records.txt","r") as fs:
                record=fs.readlines()
                for entry in record:
                    s="Account Number: "+ str(self.account_number)
                    while re.search(s,entry):
                        self.account_number=random.randint(10000000,100000000)
            with open("bank_records.txt","a") as fs:
                fs.write("Account Number: {0}, Account-Holder's Name: {1}, Amount: {2}\n".format(self.account_number,self.name,self.amount))
        else:
            with open("bank_records.txt","w") as fs:
                fs.write("Account Number: {0}, Account-Holder's Name: {1}, Amount: {2}\n".format(self.account_number,self.name,self.amount))
        print('\nAccount Created...')
        self.display()

    def deposit_money(self):
        dep_amt=int(input("\nEnter The Amount To Be Deposited: "))
        with open("bank_records.txt","r") as fs:
            fr=fs.read()
        fr=fr.replace("Amount: {0}".format(self.amount), "Amount: {0}".format(self.amount+dep_amt))
        with open("bank_records.txt","w") as fs:
            fs.write(fr)
        self.amount+=dep_amt
        print("Transaction Successful")
        self.display()

    def withdraw_money(self):
        with_amt=int(input("\nEnter The Amount To Be Withdrawn: "))
        if with_amt>self.amount:
            print('\nRequest Could Not Be Processed Due To Insufficient Funds')
            menu()
        else:
            with open("bank_records.txt","r") as fs:
                fr=fs.read()
            fr=fr.replace("Amount: {0}".format(self.amount), "Amount: {0}".format(self.amount-with_amt))
            with open("bank_records.txt","w") as fs:
                fs.write(fr)
            self.amount-=with_amt
            print("Transaction Successful")
            self.display()


def menu():
    def login():
        ac=Account()
        print("\nLogin Required\n")
        acno=int(input("Enter Your Account Number: "))
        if os.access(str(path)+"/bank_records.txt",os.F_OK):
            with open("bank_records.txt","r") as fs:
                record=fs.readlines()
                for entry in record:
                    s='Account Number: {0}'.format(acno)
                    if re.search(s,entry):
                        entry=entry.split(",")
                        ac.account_number=acno
                        ac.name=entry[1][24:]
                        ac.amount=int(entry[2][9:])
                        print('\nLogin Successful')
                        return ac
        print('\nLogin Failed')
        menu()
    user_account=Account()
    print('\n\n--------------------------------------------------------------------------------------------------------')
    print('Make an account (code= "make")')
    print('Deposit Money (code="deposit")')
    print('Withdraw Money (code="withdraw")')
    print('Check Your Balance (code="balance")')
    print('Exit (code="exit")')
    print('\nEnter Any Code Above To Proceed')
    code=input("Your Code: ")
    code=code.strip()
    if code == 'make':
        user_account.make_an_account()
    elif code == 'deposit':
        try:
            user_account=login()
        except:
            menu()
        user_account.deposit_money()
    elif code == 'withdraw':
        user_account=login()
        user_account.withdraw_money()
    elif code == 'balance':
        try:
            user_account=login()
        except:
            menu()
        user_account.display()
    elif code == 'exit':
        return 0
    else:
        print("\nPlease Enter A Valid Code!!!")
        menu()

menu()
    
        
    

    
