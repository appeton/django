from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import product,slider,order,feedback
from .form import UserRegisterForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    
    context={
        'product':product.objects.all(),
        'slider':slider.objects.all()
    }
    if(request.method=="POST"):
        fname=request.POST['fname']
        lname=request.POST['lname']
        about=request.POST['about']
        form=feedback(firstname=fname,lastname=lname,about=about)
        form.save()
        context={
            'message':'Thank for your feedback :)'
        }
    return render(request,'web/home.html',context)

def Registerform(request):

    form=UserRegisterForm(request.POST)
    if form.is_valid():
        email='mountchitmyrsuu@gmail.com'
        subject='thank you'
        message='dsaf'
        from_email=settings.EMAIL_HOST_USER
        to_list=[settings.EMAIL_HOST_USER]
        # send_mail("this is the subject",
        #  "this is the content", settings.EMAIL_HOST_USER, ["appeton54@gmail.com","appeton54@gmail.com"])
        form.save()
        return redirect('home')
    else:
        form=UserRegisterForm()

    context={
        'form':form,
        'slider':slider.objects.all()
    }
    return render(request,'web/signup.html',context)


def login(request):
    context={   
        'slider':slider.objects.all()
    }
    return render(request,'web/login.html',context)

@login_required
def checkout(request):

  
     
    
    if request.method=='POST':
        data=request.POST['address']
        print(data)
        phone=request.POST['phone']
        print(phone)
        select=request.POST['select']
        print(select)
        city=request.POST['city']
        print(city)
        Zipp=request.POST['zip']
        print(Zipp)
        test=request.POST['test']
        print(test)
        if(test=='true'):
            form=order(address=data,phone=phone,city=city,state=select,Zip=Zipp,userId=request.user.id)
            form.save()
            return redirect('home')
        
        if(test=='false'):
            context={
            'error':"Please Payment first !"
            }
            return render(request,'web/checkout.html',context)

      
        

    return render(request,'web/checkout.html')


