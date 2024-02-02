from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from .forms import SignupForm, AddRec
from .models import CRM

def home(request):

    rec = CRM.objects.all()
    # Check to see if logging 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "You Have Been Loged In!")
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in, Please try again...')
            return redirect('home')

    else:
        return render(request, 'testapp/home.html', {'rec':rec})
    


def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged Out...')
    return redirect('home')


### passwd ==== Chetan@1133


def register_user(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignupForm()
		return render(request, 'testapp/register.html', {'form':form})

	return render(request, 'testapp/register.html', {'form':form})


def cust_rec(request,id):
     if request.user.is_authenticated:
          rec = CRM.objects.get(id=id)
          return render(request, 'testapp/record.html', {'rec':rec})
     else:
          messages.success(request, 'You have to login first...')
          return redirect('home')
     

def delete_rec(request,id):
     if request.user.is_authenticated:
        cut = CRM.objects.get(id=id)
        cut.delete()
        messages.success(request,'Record deleted Successfully...')
        return redirect('/')
     else:
          messages.success(request, 'You have to login first...')
          return redirect('/')
          

def add_rec(request):
     form = AddRec(request.POST or None)
     if request.user.is_authenticated:
        if request.method == 'POST':
             if form.is_valid():
                  add_record = form.save()
                  messages.success(request,'Record Inserted Successfully...')
                  return redirect('home')
        return render(request, 'testapp/add.html', {'form':form})
     else:
          messages.success(request,'You have to loged In...')
          return redirect('home')
     

def update_rec(request, pk):
     if request.user.is_authenticated:
        up = CRM.objects.get(id=pk)
        form = AddRec(request.POST or None, instance=up)
        if form.is_valid():
             form.save()
             messages.success(request,'Record has been updated successfully...')
             return redirect('home')
        else:
             return render(request,'testapp/update_record.html',{'form':form})


     