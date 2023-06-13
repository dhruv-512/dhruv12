from django.shortcuts import render,redirect
from .models import*
import random
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
  if 'email' in request.session:
    
    uid = user.objects.get(email = request.session['email'])
    
    contaxt ={
      
      'uid' : uid
    }
    return render(request, "myapp/index.html",contaxt)
  else:
    return render(request, "myapp/login.html")
  

def contact(request):
  if request.POST:
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    message = request.POST['message']
    
    cid = contact_up.objects.create(
                                name = name,
                                phone = phone,
                                email = email,
                                message = message
    )
    
    context ={
       'cid' : cid
    }
    return render(request, "myapp/contact.html",context)
  else:
     return render(request, "myapp/contact.html")

def logout(request):
  if 'email' in request.session:
    
    del request.session['email']
    return render(request, "myapp/login.html")
  else:
    return render(request, "myapp/login.html")


def login(request):
  if 'email' in request.session:
    uid = user.objects.get(email = request.session['email'])
    
    context ={
      'uid' : uid
    }
    return render(request, "myapp/login.html",context)
 
  try:
    
    if request.POST:
      email = request.POST['email']
      password = request.POST['password']
        
      uid = user.objects.get(email = email)
      if uid.password == password:
        
          request.session['email']=uid.email
          context ={
            
            'uid' : uid
          }
          return render(request, "myapp/index.html",context)
      else:
        
        context = {
            'p_msg' : "INVALID PASSWORD"
        }
        return render(request, "myapp/login.html",context)
    else:
      
      return render(request, "myapp/login.html")
  except:
    e_msg = "INVALID EMAIL"
      
    context = {
        'e_msg' : e_msg
    }
    return render(request, "myapp/login.html",context)
    
    
def register(request):
  if request.POST:
    email = request.POST['email']
    password = request.POST['password']
    username = request.POST['username']
    
    uid = user.objects.create(
                            email = email,
                            password = password,
                            username = username
    )
    context = {
      'uid' : uid
    }
    return render(request,"myapp/register.html",context)
  else:
    return render(request,"myapp/register.html")
  
def forget_password(request):
  if request.POST:
    email=request.POST['email']
    otp = random.randint(1111,9999)
    try:
      uid = user.objects.get(email=email)
      uid.otp=otp
      uid.save()
      send_mail ("forgot password","your otp is" +str(otp), "gohiljayb10@gmail.com",[email])
      
      
      context ={
        'email' : email
      }
      return render(request,"myapp/confirm.html",context)
    except:
      e_msg = "INVALID EMAIL"
      
      context = {
        'e_msg' : e_msg
      }
      return render(request,"myapp/forget_password.html",context)
   
  return render(request,"myapp/forget_password.html")
    
 
def confirm(request):
  if request.POST:
    email = request.POST['email']
    otp = request.POST['otp']
    new_password = request.POST['new_password']
    confirm_password = request.POST['confirm_password']
    
    uid = user.objects.get(email=email)
    if str(uid.otp) == otp:
      if new_password == confirm_password:
        uid.password = new_password
        uid.save()
        
        context ={
          'email' : email
         
        }
        return render(request, "myapp/login.html",context) 
      else:
        context ={
          'p_msg' : "INVALID PASSWORD"
          
        }
        return render(request, "myapp/confirm.html",context) 
    else:
      e_msg = "INVALID OTP"
      context = {
        'e_msg' : e_msg
      }
      return render(request, "myapp/confirm.html",context) 
    
  return render(request, "myapp/confirm.html") 
      
           


              
def services(request):
  
  return render(request, "myapp/services.html")       
       

def about(request):
  
  return render(request, "myapp/about.html")

