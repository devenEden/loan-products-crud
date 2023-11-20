from django.shortcuts import render, redirect
from loan_products.forms import LoanProductForm
from loan_products.models import LoanProduct
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required(login_url='/login/')
def new_loan_product(request):
    if request.method == "POST":
        form = LoanProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/loan-products/')
            except:
                pass
    else:
        form = LoanProductForm()
    return render(request,'new_loan_product.html', {'form':form})

def show(request):
    loan_products = LoanProduct.objects.all()
    return render(request,"show.html",{'loan_products':loan_products})

@login_required(login_url='/login/')
def edit(request, id):
    loan_product = LoanProduct.objects.get(id=id)
    form = LoanProductForm(request.POST, instance = loan_product)
    if form.is_valid():
        form.save()
        return redirect("/loan-products/")
    return render(request, 'edit.html', {'loan_product': loan_product})

@login_required(login_url='/login/')
def destroy(request, id):
    loan_product = LoanProduct.objects.get(id=id)
    loan_product.delete()
    return redirect("/loan-products/")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('loan_products')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('loan_products')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')