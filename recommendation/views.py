from django.shortcuts import render, redirect 
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForm
from .models import *


# from .filters import OrderFilter



def index(request):
	movies = Movie.objects.all()
	context = {
		'movies' : movies
	}
	return render(request, 'recommendation/index.html', context)


def signup(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = CreateUserForm()
		title = 'signup'
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account created sucessfully ' + user)
				return redirect('signin')
			
		context = {
			'form':form,
			'title': title	
		}
		return render(request, 'recommendation/signup.html', context)

def signin(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'invalid credentials')

		context = {}
		return render(request, 'recommendation/signin.html', context)

def signout(request):
	logout(request)
	return redirect('signin')


# @login_required(login_url='login')
# def home(request):
# 	orders = Order.objects.all()
# 	customers = Customer.objects.all()

# 	total_customers = customers.count()

# 	total_orders = orders.count()
# 	delivered = orders.filter(status='Delivered').count()
# 	pending = orders.filter(status='Pending').count()

# 	context = {'orders':orders, 'customers':customers,
# 	'total_orders':total_orders,'delivered':delivered,
# 	'pending':pending }

# 	return render(request, 'accounts/dashboard.html', context)

# @login_required(login_url='login')
# def products(request):
# 	products = Product.objects.all()

# 	return render(request, 'accounts/products.html', {'products':products})

# @login_required(login_url='login')
# def customer(request, pk_test):
# 	customer = Customer.objects.get(id=pk_test)

# 	orders = customer.order_set.all()
# 	order_count = orders.count()

# 	myFilter = OrderFilter(request.GET, queryset=orders)
# 	orders = myFilter.qs 

# 	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
# 	'myFilter':myFilter}
# 	return render(request, 'accounts/customer.html',context)

# @login_required(login_url='login')
# def createOrder(request, pk):
# 	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
# 	customer = Customer.objects.get(id=pk)
# 	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
# 	#form = OrderForm(initial={'customer':customer})
# 	if request.method == 'POST':
# 		#print('Printing POST:', request.POST)
# 		form = OrderForm(request.POST)
# 		formset = OrderFormSet(request.POST, instance=customer)
# 		if formset.is_valid():
# 			formset.save()
# 			return redirect('/')

# 	context = {'form':formset}
# 	return render(request, 'accounts/order_form.html', context)

# @login_required(login_url='login')
# def updateOrder(request, pk):

# 	order = Order.objects.get(id=pk)
# 	form = OrderForm(instance=order)

# 	if request.method == 'POST':
# 		form = OrderForm(request.POST, instance=order)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/')

# 	context = {'form':form}
# 	return render(request, 'accounts/order_form.html', context)

# @login_required(login_url='login')
# def deleteOrder(request, pk):
# 	order = Order.objects.get(id=pk)
# 	if request.method == "POST":
# 		order.delete()
# 		return redirect('/')

# 	context = {'item':order}
# 	return render(request, 'accounts/delete.html', context)