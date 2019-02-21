from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse,HttpResponseRedirect
from .models import User,Stock
import pyrebase
from django.shortcuts import render
from django.contrib import auth
import requests

# Create your views here.

config = {
    "apiKey": "AIzaSyD-hr6ajJUL5b3QPQftNQur0SYaviSIAr8",
    "authDomain": "se-pms.firebaseapp.com",
    "databaseURL": "https://se-pms.firebaseio.com",
    "projectId": "se-pms",
    "storageBucket": "se-pms.appspot.com",
    "messagingSenderId": "318918759627"
  }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database=firebase.database()

def login(request):
    message=""
    return render(request,'login.html',{"messg":message})

def postsignIn(request):

    email=request.POST.get('email')
    passw = request.POST.get("pass")
    message=""
    print(email,passw)
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
        
    except:
        message="Invalid Credentials"
        return render(request,"login.html",{"messg":message})
    
    session_id=user['localId']
    request.session['uid']=str(session_id)
    print(request.session['uid'])
    return render(request, "home.html",{"e":email})

def home(request):
    u = database.child('users').child(request.session['uid']).child('details').get()
    e = u.val()
    ddd = []
    symb={'Microsoft':'MSFT','Google':'GOOG','Barclays':'BCS','JP Morgan Chase':'JPM','Bank of america':'bac'}
    for i in symb.values():
        print('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+i+'&apikey=62Q1OEQMZI876K16')
        response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+i+'&apikey=62Q1OEQMZI876K16')
        stocks = response.json()
        my_dict={}
        #print(stocks.get('Time Series (Daily)').get('2019-02-20').get('1. open'))
        my_dict['company'] = list(symb.keys())[list(symb.values()).index(i)]
        my_dict['low']=stocks.get('Time Series (Daily)').get('2019-02-20').get('3. low')
        my_dict['open']=stocks.get('Time Series (Daily)').get('2019-02-20').get('1. open')
        my_dict['close']=stocks.get('Time Series (Daily)').get('2019-02-20').get('4. close')
        my_dict['high']=stocks.get('Time Series (Daily)').get('2019-02-20').get('2. high')
        #print("item:",item)
        ddd.append(my_dict)
    '''
    symb1={'Infosys':'infy','Tata Motors':'ttm','Berkshire':'berk','toyota':'tm','apple':'aapl'}
    for i in symb1.values():
        print('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+i+'&apikey=4VXBDQUOPRAO55I8')
        response1 = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+i+'&apikey=4VXBDQUOPRAO55I8')
        stocks1 = response1.json()
        my_dict={}
        #print(stocks.get('Time Series (Daily)').get('2019-02-20').get('1. open'))
        my_dict['company'] = list(symb1.keys())[list(symb1.values()).index(i)]
        my_dict['low']=stocks1.get('Time Series (Daily)').get('2019-02-20').get('3. low')
        my_dict['open']=stocks1.get('Time Series (Daily)').get('2019-02-20').get('1. open')
        my_dict['close']=stocks1.get('Time Series (Daily)').get('2019-02-20').get('4. close')
        my_dict['high']=stocks1.get('Time Series (Daily)').get('2019-02-20').get('2. high')
        #print("item:",item)
        ddd.append(my_dict)
    
    symb2={'amazon':'amzn','Tesla':'tsla','Berkshire Hathaway':'brk.a','Facebook':'fb','Twitter':'twtr'}
    for i in symb2.values():
        print('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+i+'&apikey=9I8SAW3QN3113IIJ')
        response2 = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+i+'&apikey=9I8SAW3QN3113IIJ')
        stocks2 = response2.json()
        my_dict={}
        #print(stocks.get('Time Series (Daily)').get('2019-02-20').get('1. open'))
        my_dict['company'] = list(symb2.keys())[list(symb2.values()).index(i)]
        my_dict['low']=stocks2.get('Time Series (Daily)').get('2019-02-20').get('3. low')
        my_dict['open']=stocks2.get('Time Series (Daily)').get('2019-02-20').get('1. open')
        my_dict['close']=stocks2.get('Time Series (Daily)').get('2019-02-20').get('4. close')
        my_dict['high']=stocks2.get('Time Series (Daily)').get('2019-02-20').get('2. high')
        #print("item:",item)
        ddd.append(my_dict)
    #data = { 'low':stocks['low'],'open':stocks['open'],'close':stocks['close'],'high':stocks['high']} 
    '''
    database.child('stocks').set(ddd)
    print(ddd)
    return render(request,'home.html',{"e":e["email"],'data':ddd})

def profile(request):
    u = database.child('users').child(request.session['uid']).child('details').get()
    print(u.val())
    e = u.val()
    return render(request,'profile.html',{"user":u.val(),"e":e["email"]})

def transaction(request):
    u = database.child('users').child(request.session['uid']).child('details').get()
    e = u.val()
    return render(request,'transaction.html',{"e":e["email"]})

def about(request):
    u = database.child('users').child(request.session['uid']).child('details').get()
    e = u.val()
    return render(request,'about.html',{"e":e["email"]})

def graphics(request):
    u = database.child('users').child(request.session['uid']).child('details').get()
    e = u.val()
    return render(request,'graphics.html',{"e":e["email"]})

def logout(request):
    #auth.logout(request)
    return HttpResponseRedirect("/")

def register(request):
    msg = ""
    return render(request,'register.html',{"messg":msg})

def postsignup(request):
    u = User
    name=request.POST['name']
    email=request.POST['email']
    mobile_no = request.POST['mobile']
    password=request.POST['pass']
    portfolio_value=0
    #print("gtit:",email,passw)
    print(u)
    try:
        user=auth.create_user_with_email_and_password(email,password)
        uid = user['localId']
        data={"id":uid,"name":name,"mobile_no":mobile_no,"email":email,"portfolio_value":0,"profession":"none"}
        database.child("users").child(uid).child("details").set(data)
    except:
        message="Unable to create account try again"
        print("broooooooooooooo")
        return HttpResponse(request,"register.html",{"messg":message})
        
    return HttpResponseRedirect("/")

def add(request):
    return render(request,'profile.html')
