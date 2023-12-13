from django.shortcuts import render, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
# Create your views here.

def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        client_data = Client(email=email, phone=phone, password=password)
        client_data.save()
        return render(request, 'home.html')
    else:
        return render(request, 'signup.html')
    
def loginUser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        client_exists = Client.objects.filter(email=email).exists()
        if client_exists:
            client = get_object_or_404(Client, email=email)
            client_password = client.password
            print(password1, client_password)
            if password1 == client_password:
                return redirect('home')  # Check your URL configuration for 'home'
            else:
                error_message = "Invalid credentials. Please try again."
                return render(request, 'login.html', {'error_message': error_message})
        else:
            error_message = "Invalid credentials. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/")

@csrf_exempt
def home(request):
    return render(request, 'home.html')

    
def automobile(request):
    automobile_data = Automobile.objects.all()
    checkbox_brands = request.GET.get('selected_brands')
    checkbox_states = request.GET.get('selected_states')

    if checkbox_brands is not None and checkbox_states is not None:
        if checkbox_brands and checkbox_states:
            automobile_data = Automobile.objects.filter(brand_name=checkbox_brands, state=checkbox_states)
    
    if checkbox_brands is not None and checkbox_states is None:
        if checkbox_brands:
            automobile_data = Automobile.objects.filter(brand_name=checkbox_brands)

    if checkbox_brands is None and checkbox_states is not None:
        if checkbox_states:
            automobile_data = Automobile.objects.filter(state=checkbox_states)
    
    
    eligable_locations = Automobile.objects.all()
    brands = []
    states = []

    for b in eligable_locations:
        data = {
            'brand': b.brand_name
        }
        if data not in brands:
            brands.append(data)

    for s in eligable_locations:
        data = {
            'state': s.state
        }
        if data not in states:
            states.append(data)

    paginator = Paginator(automobile_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "automobile_data" : automobile_data,
        "brands" : brands,
        "states" : states,
        "page_obj": page_obj,
        "checkbox_brands": checkbox_brands,
        "checkbox_states": checkbox_states
    }
    
    return render(request, 'home.html', context)


def electronic(request):
    electronic_data = Electronic.objects.all()
    checkbox_brands = request.GET.get('selected_brands')
    checkbox_states = request.GET.get('selected_states')

    if checkbox_brands is not None and checkbox_states is not None:
        if checkbox_brands and checkbox_states:
            electronic_data = Electronic.objects.filter(brand=checkbox_brands, state=checkbox_states)
    
    if checkbox_brands is not None and checkbox_states is None:
        if checkbox_brands:
            electronic_data = Electronic.objects.filter(brand=checkbox_brands)

    if checkbox_brands is None and checkbox_states is not None:
        if checkbox_states:
            electronic_data = Electronic.objects.filter(state=checkbox_states)
    
    
    eligable_locations = Electronic.objects.all()
    brands = []
    states = []

    for b in eligable_locations:
        data = {
            'brand': b.brand
        }
        if data not in brands:
            brands.append(data)

    for s in eligable_locations:
        data = {
            'state': s.state
        }
        if data not in states:
            states.append(data)

    paginator = Paginator(electronic_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "electronic_data" : electronic_data,
        "brands" : brands,
        "states" : states,
        "page_obj": page_obj,
        "checkbox_brands": checkbox_brands,
        "checkbox_states": checkbox_states
    }
    
    return render(request, 'home.html', context)

def movietheater(request):
    movietheater_data = Movietheater.objects.all()
    checkbox_brands = request.GET.get('selected_brands')
    checkbox_states = request.GET.get('selected_states')

    if checkbox_brands is not None and checkbox_states is not None:
        if checkbox_brands and checkbox_states:
            movietheater_data = Movietheater.objects.filter(brand_name=checkbox_brands, state=checkbox_states)
    
    if checkbox_brands is not None and checkbox_states is None:
        if checkbox_brands:
            movietheater_data = Movietheater.objects.filter(brand_name=checkbox_brands)

    if checkbox_brands is None and checkbox_states is not None:
        if checkbox_states:
            movietheater_data = Movietheater.objects.filter(state=checkbox_states)
    
    
    eligable_locations = Movietheater.objects.all()
    brands = []
    states = []

    for b in eligable_locations:
        data = {
            'brand': b.brand_name
        }
        if data not in brands:
            brands.append(data)

    for s in eligable_locations:
        data = {
            'state': s.state
        }
        if data not in states:
            states.append(data)

    paginator = Paginator(movietheater_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "movietheater_data" : movietheater_data,
        "brands" : brands,
        "states" : states,
        "page_obj": page_obj,
        "checkbox_brands": checkbox_brands,
        "checkbox_states": checkbox_states
    }
    
    return render(request, 'home.html', context)


def supermarket(request):
    supermarket_data = Supermarket.objects.all()
    checkbox_brands = request.GET.get('selected_brands')
    checkbox_states = request.GET.get('selected_states')

    if checkbox_brands is not None and checkbox_states is not None:
        if checkbox_brands and checkbox_states:
            supermarket_data = Supermarket.objects.filter(store_type=checkbox_brands, state=checkbox_states)
    
    if checkbox_brands is not None and checkbox_states is None:
        if checkbox_brands:
            supermarket_data = Supermarket.objects.filter(store_type=checkbox_brands)

    if checkbox_brands is None and checkbox_states is not None:
        if checkbox_states:
            supermarket_data = Supermarket.objects.filter(state=checkbox_states)
    
    
    eligable_locations = Supermarket.objects.all()
    brands = []
    states = []

    for b in eligable_locations:
        data = {
            'brand': b.store_type
        }
        if data not in brands:
            brands.append(data)

    for s in eligable_locations:
        data = {
            'state': s.state
        }
        if data not in states:
            states.append(data)

    paginator = Paginator(supermarket_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "supermarket_data" : supermarket_data,
        "brands" : brands,
        "states" : states,
        "page_obj": page_obj,
        "checkbox_brands": checkbox_brands,
        "checkbox_states": checkbox_states
    }
    
    return render(request, 'home.html', context)

def telecom(request):
    telecom_data = Telecom.objects.all()
    checkbox_brands = request.GET.get('selected_brands')
    checkbox_states = request.GET.get('selected_states')

    if checkbox_brands is not None and checkbox_states is not None:
        if checkbox_brands and checkbox_states:
            telecom_data = Telecom.objects.filter(brand_name=checkbox_brands, state=checkbox_states)
    
    if checkbox_brands is not None and checkbox_states is None:
        if checkbox_brands:
            telecom_data = Telecom.objects.filter(brand_name=checkbox_brands)

    if checkbox_brands is None and checkbox_states is not None:
        if checkbox_states:
            telecom_data = Telecom.objects.filter(state=checkbox_states)
    
    
    eligable_locations = Telecom.objects.all()
    brands = []
    states = []

    for b in eligable_locations:
        data = {
            'brand': b.brand_name
        }
        if data not in brands:
            brands.append(data)

    for s in eligable_locations:
        data = {
            'state': s.state
        }
        if data not in states:
            states.append(data)

    paginator = Paginator(telecom_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "telecom_data" : telecom_data,
        "brands" : brands,
        "states" : states,
        "page_obj": page_obj,
        "checkbox_brands": checkbox_brands,
        "checkbox_states": checkbox_states
    }
    
    return render(request, 'home.html', context)
        
