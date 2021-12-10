from django.shortcuts import render
from django.http import HttpResponse
from .models import Customers,History
def index(request):
    #customer=History.objects.all()
    #customers=History(sender_name ='Naresh',sender_no = '1001',receiver_name = 'Prasath',receiver_no = '1002',date ='2021-10-25',amount ='5000.0')
    #customers.save()
    #print('success')
    return render(request,'Index.html')
def customer(request):
    ##
    c=0
    try:
        name1=str(request.POST['name'])
        gender1=str(request.POST['gender'])
        age1=int(request.POST['age'])
        phone_no1=str(request.POST['phone_no'])
        email1=str(request.POST['email'])
        depositamount1=float(request.POST['depositamount'])
        c=1
        customerdb=Customers(name=name1,gender=gender1,age=age1,phone_no=phone_no1,email=email1,balance=depositamount1)
        customerdb.save()

    except:
        pass
    ##
    customer1=Customers.objects.all()
    n=[i+1 for i in range(len(customer1))]
    customer2=zip(n,customer1)
    return render(request,'customer.html',{'customer':customer2,'c':c})
def create_user(request):
    account=0
    customer=None
    try:
        account=int(request.POST['account_no'])
        customer=Customers.objects.filter(account_no=account)
    except:
        pass
    return render(request,'create_user.html',{'customer':customer,'account_no':account})
def transfer(request):
    customer1=Customers.objects.all()
    n=[i+1 for i in range(len(customer1))]
    customer2=zip(n,customer1)
    return render(request,'transfer.html',{'customer':customer2})
def transaction(request):
    a_no=int(request.POST['account_no'])
    customer1=Customers.objects.exclude(account_no =a_no)
    customer2=Customers.objects.filter(account_no=a_no)
    return render(request,'transaction.html',{'customer1':customer1,'customer2':customer2})
def transaction_history(request):
    f=0
    try:
        sender_no1=int(request.POST['sender_no'])
        sender_name1=str(request.POST['sender_name'])
        receiver_no1=int(request.POST['receiver_no'])
        amount1=float(request.POST['amount'])
        customer=Customers.objects.filter(account_no=receiver_no1)
        for i in customer:
            receiver_name1=i.name
        historydb=History(sender_name=sender_name1,sender_no=sender_no1,receiver_name=receiver_name1,receiver_no=receiver_no1,amount=amount1)
        s=Customers.objects.get(account_no=sender_no1)
        s.balance-=amount1
        s.save()
        r=Customers.objects.get(account_no=receiver_no1)
        r.balance+=amount1
        r.save()
        historydb.save()
        f=1
    except:
        pass
    history=History.objects.all()
    history=reversed(history)
    return render(request,'transaction_history.html',{'history':history,'f':f})
# Create your views here.
