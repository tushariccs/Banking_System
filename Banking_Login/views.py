from django.shortcuts import redirect, render
from django.http import HttpResponse
from Banking_Login.models import Account_Creation, Transaction
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import random
# from . import models

def members(request):
    if request.method == 'POST':
        username = request.POST.get("Username")
        password = request.POST.get("Password")
        print(username)
        print(password)
        # if User.objects.filter(username=username).exists():
        #     messages.error(request,"Username already exists ,or please register your self")
        #     return redirect('/login')
        user = User.objects.create(
            username = username,
            
        )
        user.set_password(password)
        user.save()
        
    return render(request,'index.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get("Username")
        password = request.POST.get("Password")
        # if not User.objects.filter(username=username).exists():
        #     messages.error(request,"Username already exists ,or please regiter your self")
        #     return redirect('/login')
        # username = User.objects.filter(username=username)[0]
        # password = User.objects.filter(password = password)[1]
        
        user = authenticate(username = username, password = password)
        print(user)
        if user is None:
            messages.error(request,"Invalid Password")
            return redirect('/login')
        else:
            login(request,user)
            return redirect('/Account_Creation')        
    
    return render(request,'login.html') 

def page_404(request):
    return render(request,'404_page.html')
@login_required(login_url="/login")
def account_creation(request):
    if request.method == 'POST':
         First_name = request.POST.get("First_Name")
         Last_Name = request.POST.get("Last_Name")
         Last_Name = request.POST.get("Last_Name")
         Password = request.POST.get("Password")
         Adhaar_Card_Number = request.POST.get("Adhaar_Card_Number")
         Adhaar_Card_Image = request.FILES.get("Adhaar_Card_Image")
         Pan_Card_Number = request.POST.get("Pan_Card_Number")
         Pan_Card_Image = request.FILES.get("Pan_Card_Image")
         Permanant_Address = request.POST.get('Permanant_Address')
         Resdential_Address = request.POST.get('Resdential_Address')
         Personal_Image = request.FILES.get('Personal_Image')
         Basic_Amount = request.POST.get('Basic_Amount')
        #  print(First_name)
        #  print(Last_Name)
        #  print(Adhaar_Card_Number)
        #  print(Adhaar_Card_Image)
        #  print(Pan_Card_Number)
        #  print(Pan_Card_Image)
        #  print(Permanant_Address)
        #  print(Resdential_Address)
        #  print(Personal_Image)
        #  print(Basic_Amount)
         Account_Number = '2024'+str(random.randint(1000,10000000))
         if not Account_Creation.objects.filter(Account_Number = Account_Number).exists():
            messages.info(request,"Account Number exists please try again!! ")
            redirect('/Account_Creation')
         Account_Creation.objects.create(
            First_Name = First_name,
            Pan_Card_Image = Pan_Card_Image,
            Adhaar_Card_Image = Adhaar_Card_Image,
            Last_Name = Last_Name,
            Adhaar_Card_Number = Adhaar_Card_Number,
            Pan_Card_Number = Pan_Card_Number,
            Permanant_Address = Permanant_Address,
            Resdential_Address = Resdential_Address,
            Personal_Image = Personal_Image,
            Account_Number = Account_Number,
            Basic_Amount = Basic_Amount,
            Password = Password,
        )
         Account_Creation.save()
         return redirect('Debit_Auth')
    
    return render(request,'Create_Account.html')

def Debit_amount_auth(request):
    if request.method == 'POST':
        Account_Number = request.POST.get('Account_Number')
        password = request.POST.get('Password')
        
        if (Account_Creation.objects.filter(Account_Number=Account_Number,Password = password).exists()):
            messages.info(request,'Crendentials Verified')
            return redirect('/Debit_Amount')
        else:
            messages.info(request,'Crendentials Not Verified')
            return redirect('/login')
    return render(request, 'Debit.html')


@login_required(login_url="/Debit_Auth")      
def Debit_amount(request):
    if request.method == 'POST':
        Account_Number_Sender = request.POST.get('Account_Number_Sender')
        Account_Number_Receiver = request.POST.get('Account_Number_Receiver')
        Amount_to_Transfer = int(request.POST.get('Amount_to_Transfer'))
        
        if (Account_Creation.objects.filter(Account_Number=Account_Number_Sender).exists()) or (Account_Creation.objects.filter(Account_Number=Account_Number_Receiver).exists()):
            Sender_Amount = Account_Creation.objects.get(Account_Number=Account_Number_Sender)
            Sender_Amount.Basic_Amount = Sender_Amount.Basic_Amount + Amount_to_Transfer
            Receiver_Amount = Account_Creation.objects.get(Account_Number=Account_Number_Receiver)
            Receiver_Amount.Basic_Amount = Receiver_Amount.Basic_Amount - Amount_to_Transfer
            Sender_Amount.save()
            Receiver_Amount.save()   
            Transaction_Id = int(random.randint(1,1000000000))
            Transaction.objects.create(
                Transaction = Transaction_Id,
                Account_Number_Sender = Account_Number_Sender,
                Account_Number_Receiver = Account_Number_Receiver,
            )
            Transaction.save()
        else:
            return render(request,'404_page.html')

    return render(request, 'Debit_Amount.html')  


@login_required(login_url="/Debit_Auth")  
def Credit_Amount(request):
    if request.method == 'POST':
        Account_Number_Sender = request.POST.get('Account_Number_Sender')
        Account_Number_Receiver = request.POST.get('Account_Number_Receiver')
        Amount_to_Transfer = int(request.POST.get('Amount_to_Transfer'))
        Transaction_Id = int(random.randint(1,1000000000))
        if (Account_Creation.objects.filter(Account_Number=Account_Number_Sender).exists()) or (Account_Creation.objects.filter(Account_Number=Account_Number_Receiver).exists()):
            Sender_Amount = Account_Creation.objects.get(Account_Number=Account_Number_Sender)
            Sender_Amount.Basic_Amount = Sender_Amount.Basic_Amount + Amount_to_Transfer
            Receiver_Amount = Account_Creation.objects.get(Account_Number=Account_Number_Receiver)
            Receiver_Amount.Basic_Amount = Receiver_Amount.Basic_Amount - Amount_to_Transfer
            Sender_Amount.save()
            Receiver_Amount.save()   
            Transaction.objects.create(
                Transaction = Transaction_Id,
                Account_Number_Sender = Account_Number_Sender,
                Account_Number_Receiver = Account_Number_Receiver,
            )
            Transaction.save()
        else:
            return render(request,'404_page.html')

    return render(request, 'Credit_Amount.html')

