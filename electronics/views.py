from django.shortcuts import render, redirect
import requests 
from bs4 import BeautifulSoup 
import re
from .models import *
from geopy.geocoders import Nominatim
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
# Create your views here.

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }

geolocator = Nominatim(user_agent="geoapiExercises")
geolocator = Nominatim(user_agent="get_lat_long")

def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        client_data = Client(email=email, phone=phone, password=password)
        client_data.save()
        return render(request, 'login.html')
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
        

def clean_text(text):
    # Remove HTML tags
    clean = re.compile('<.*?>')
    text = re.sub(clean, '', text)
    # Replace '\\n' with actual newlines
    text = text.replace('\\n', '\n')
    text = text.replace('\\t', '\n''\n')
    text = text.replace(',', '\n''\n')
    # Remove extra whitespace, including leading/trailing whitespaces
    return ' '.join(text.split())

def canonfunction(request):

    def loopfunction():

        data = pd.read_csv("C:\FloorWalk\companies\storedata\extra.csv")

        links = data['link'].tolist()

        phonenums = data['page'].tolist()
        
        brands = data['brand'].tolist()

        logos = data['logo'].tolist()

        for link, phonenum, brand, logo in zip(links, phonenums, brands, logos):

            for i in range(1, phonenum):

                brand_name = brand

                b_logo = logo

                data1 = str(link)
                
                url = f"{data1}{i}"

                def data_store(url): 

                    response = requests.get(url, headers=headers)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    data = soup.find_all('h3')[1:]

                    types = []
                    pagenumber = []
                    statuses = []
                    final_brand = []
                    final_name = []
                    final_address = []
                    final_phone = []
                    final_open = []
                    final_lat = []
                    final_lng = []
                    final_pincode = []
                    final_city = []
                    final_state = []
                    brand_logo = []
                    
                    for v in data:

                        if v is not None:
                            
                            pagenumber.append(i)
                            final_brand.append(brand_name)
                            brand_logo.append(b_logo)
                            #print("logo",len((b_logo)))
                            types.append('Service Store')
                            data2 = v.text.split("Address:")
                            name = data2[0].replace('class="_hd">', '').strip()
                            final_name.append(clean_text(name))
                            #print("name",len(name))
                            address_data = data2[1].split("</span>")
                            address_mix_form = address_data[0].strip()
                            address_clean_form = str(clean_text(address_mix_form))
                            
                            if "Phone Number" in address_clean_form:
                                address_replace = address_clean_form.replace("Phone Number:", "^")
                                address_split = address_replace.split('^')
                                if "Directions Opening Hours" in address_split:
                                    phone_replace = address_split[1].replace("Directions Opening Hours", "$")
                                    phone_split = phone_replace.split('$')
                                    address = address_split[0]
                                    final_address.append(address)
                                    phone = phone_split[0]
                                    final_phone.append(phone)
                                    open = phone_split[1]
                                    final_open.append(open)
                                    # print("address", len(address))
                                    # print("phone", len(phone))
                                    # print("open", len(open))
                                    us_zip = r'(\d{5}\-?\d{0,4})'
                                    zip_code = re.search(us_zip, address_split[0])
                                    if zip_code is None:
                                        final_lat.append('')
                                        final_lng.append('')
                                        final_city.append('')
                                        final_state.append('')
                                        final_pincode.append('')
                                        statuses.append('Done')
                                    else:
                                        pincode = zip_code.group(1)
                                        final_pincode.append(pincode)
                                        api_url = f"https://api.postalpincode.in/pincode/{pincode}"
                                        # location = geolocator.geocode(f"{pincode}, India")

                                        # if location:
                                        #     lt = location.latitude
                                        #     lg = location.longitude
                                        final_lat.append('')
                                        final_lng.append('')

                                        response = requests.get(api_url)

                                        if response.status_code == 200:

                                            data = response.json()
                                            if data and data[0]['Status'] == "Success":
                                                location_data = data[0]['PostOffice'][0]
                                                city = location_data.get('District')
                                                state = location_data.get('State')

                                                final_city.append(city)
                                                final_state.append(state)
                                                statuses.append('Done')
                                            else:
                                                final_city.append('')
                                                final_state.append('')
                                                statuses.append('Done')
                                        
                                        else:
                                            print("Failed to retrieve data from the API.")
                                            
                                    
                                elif "Opening Hours" in address_split[1]:
                                    phone_replace = address_split[1].replace("Opening Hours", "$")
                                    phone_split = phone_replace.split('$')
                                    address = address_split[0]
                                    final_address.append(address)
                                    phone = phone_split[0]
                                    final_phone.append(phone)
                                    open = phone_split[1]
                                    final_open.append(open)
                                    # print("address", len(address))
                                    # print("phone", len(phone))
                                    # print("open", len(open))
                                    
                                    us_zip = r'(\d{5}\-?\d{0,4})'
                                    zip_code = re.search(us_zip, address_split[0])
                                    if zip_code is None:
                                        final_lat.append('')
                                        final_lng.append('')
                                        final_city.append('')
                                        final_state.append('')
                                        final_pincode.append('')
                                        statuses.append('Done')
                                    else:
                                        pincode = zip_code.group(1)
                                        final_pincode.append(pincode)
                                        api_url = f"https://api.postalpincode.in/pincode/{pincode}"
                                        # location = geolocator.geocode(f"{pincode}, India")

                                        # if location:
                                        #     lt = location.latitude
                                        #     lg = location.longitude
                                        final_lat.append('')
                                        final_lng.append('')

                                        response = requests.get(api_url)

                                        if response.status_code == 200:

                                            data = response.json()
                                            if data and data[0]['Status'] == "Success":
                                                location_data = data[0]['PostOffice'][0]
                                                city = location_data.get('District')
                                                state = location_data.get('State')

                                                final_city.append(city)
                                                final_state.append(state)
                                                statuses.append('Done')
                                            else:
                                                final_city.append('')
                                                final_state.append('')
                                                statuses.append('Done')
                                        
                                        else:
                                            print("Failed to retrieve data from the API.")
                                
                                else:
                                    address = address_split[0]
                                    final_address.append(address)
                                    
                                    phone = address_split[1].split("D", 1)[0]
                                    match = re.search(r'(\d{10})-(\d+)\s+(.*)$', phone)
                                    if match:
                                        phone_number = match.group(1)
                                    else:
                                        phone_number = ''
                                    # else:
                                    #     match = re.search(r'(\d{6})\s+(\d{4})\s+(.*)$', phone)
                                    #     if match:
                                    #         phone_number = match.group(1) + match.group(2)
                                    final_phone.append(phone_number)
                                    
                                    final_open.append(' ')
                                    # print("address", len(address))
                                    # print("phone", len(phone))
                                    #print("open", len(open))
                                    
                                    us_zip = r'(\d{5}\-?\d{0,4})'
                                    zip_code = re.search(us_zip, address)
                                    if zip_code is None:
                                        final_lat.append('')
                                        final_lng.append('')
                                        final_city.append('')
                                        final_state.append('')
                                        final_pincode.append('')
                                        statuses.append('Done')
                                    else:
                                        pincode = zip_code.group(1)
                                        final_pincode.append(pincode)
                                        api_url = f"https://api.postalpincode.in/pincode/{pincode}"
                                        # location = geolocator.geocode(f"{pincode}, India")

                                        # if location:
                                        #     lt = location.latitude
                                        #     lg = location.longitude
                                        final_lat.append('')
                                        final_lng.append('')

                                        response = requests.get(api_url)

                                        if response.status_code == 200:

                                            data = response.json()
                                            if data and data[0]['Status'] == "Success":
                                                location_data = data[0]['PostOffice'][0]
                                                city = location_data.get('District')
                                                state = location_data.get('State')

                                                final_city.append(city)
                                                final_state.append(state)
                                                statuses.append('Done')
                                            else:
                                                final_city.append('')
                                                final_state.append('')
                                                statuses.append('Done')
                                        
                                        else:
                                            print("Failed to retrieve data from the API.")

                            elif "Directions Opening Hours" in address_clean_form:
                                address_replace = address_clean_form.replace("Directions Opening Hours", "$")
                                address_split = address_replace.split('$')
                                final_phone.append(' ')
                                address = address_split[0]
                                final_address.append(address)
                                open = address_split[1]
                                final_open.append(open)
                                # print("address", len(address))
                                # print("phone", len(phone))
                                # print("open", len(open))
                                #print(time[1])
                                us_zip = r'(\d{5}\-?\d{0,4})'
                                zip_code = re.search(us_zip, address_split[0])
                                if zip_code is None:
                                    final_lat.append('')
                                    final_lng.append('')
                                    final_city.append('')
                                    final_state.append('')
                                    final_pincode.append('')
                                    statuses.append('Done')
                                else:
                                    pincode = zip_code.group(1)
                                    final_pincode.append(pincode)
                                    api_url = f"https://api.postalpincode.in/pincode/{pincode}"
                                    # location = geolocator.geocode(f"{pincode}, India")

                                        # if location:
                                        #     lt = location.latitude
                                        #     lg = location.longitude
                                    final_lat.append('')
                                    final_lng.append('')

                                    response = requests.get(api_url)

                                    if response.status_code == 200:

                                        data = response.json()
                                        if data and data[0]['Status'] == "Success":
                                            location_data = data[0]['PostOffice'][0]
                                            city = location_data.get('District')
                                            state = location_data.get('State')

                                            final_city.append(city)
                                            final_state.append(state)
                                            statuses.append('Done')
                                        else:
                                            final_city.append('')
                                            final_state.append('')
                                            statuses.append('Done')
                                        
                                    else:
                                        print("Failed to retrieve data from the API.")
                            else:
                                address_split = address_clean_form.split("Directions", 1)[0]
                                final_phone.append(' ')
                                final_open.append(' ')
                                address = address_split
                                final_address.append(address)
                                #print("address", len(address))
                                
                                us_zip = r'(\d{5}\-?\d{0,4})'
                                zip_code = re.search(us_zip, address_split)
                                if zip_code is None:
                                    final_lat.append('')
                                    final_lng.append('')
                                    final_city.append('')
                                    final_state.append('')
                                    final_pincode.append('')
                                    statuses.append('Done')
                                else:
                                    pincode = zip_code.group(1)
                                    final_pincode.append(pincode)
                                    api_url = f"https://api.postalpincode.in/pincode/{pincode}"
                                    # location = geolocator.geocode(f"{pincode}, India")

                                        # if location:
                                        #     lt = location.latitude
                                        #     lg = location.longitude
                                    final_lat.append('')
                                    final_lng.append('')

                                    response = requests.get(api_url)

                                    if response.status_code == 200:

                                        data = response.json()
                                        if data and data[0]['Status'] == "Success":
                                            location_data = data[0]['PostOffice'][0]
                                            city = location_data.get('District')
                                            state = location_data.get('State')

                                            final_city.append(city)
                                            final_state.append(state)
                                            statuses.append('Done')
                                        else:
                                            final_city.append('')
                                            final_state.append('')
                                            statuses.append('Done')
                                        
                                    else:
                                        print("Failed to retrieve data from the API.")
                                
                                  
                    for item in zip(final_brand, types, final_name, final_address, final_phone, final_open, final_lat, final_lng, final_pincode, final_city, final_state, statuses, pagenumber, brand_logo):

                        brand = item[0]
                        type = item[1]
                        store_name = item[2]
                        address = item[3]
                        mobile = item[4]
                        operating_time = item[5]
                        lat = item[6]
                        lon = item[7]
                        pin_code = item[8]
                        city = item[9]
                        state = item[10]
                        status = item[11]
                        page_number = item[12]
                        brand_logo = item[13]
                        jiodata = Service(brand=brand, type=type, store_name=store_name, address=address, mobile=mobile, operating_time=operating_time, lat=lat, lon=lon, pin_code=pin_code, city=city, state=state, status=status, page_number=page_number, brand_logo=brand_logo)
                        jiodata.save()

                data_store(url)

    loopfunction()

    return JsonResponse({'message': 'Scraping and saving data is complete.'})

def servicesfunction(request):

    def loopfunction():

        data = pd.read_csv("C:\FloorWalk\companies\storedata\canon.csv")

        links = data['link'].tolist()

        phonenums = data['page'].tolist()
        
        brands = data['brand'].tolist()

        logos = data['logo'].tolist()

        for link, phonenum, brand, logo in zip(links, phonenums, brands, logos):

            for i in range(1, phonenum):

                brand_name = brand

                b_logo = logo

                data1 = str(link)
                
                url = f"{data1}{i}"

                def data_store(url): 

                    response = requests.get(url, headers=headers)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    data = soup.find_all('h3')[1:]

                    types = []
                    pagenumber = []
                    statuses = []
                    final_brand = []
                    final_name = []
                    final_address = []
                    final_phone = []
                    final_open = []
                    final_lat = []
                    final_lng = []
                    final_pincode = []
                    final_city = []
                    final_state = []
                    brand_logo = []
                    
                    for v in data:

                        if v is not None:
                            
                            pagenumber.append(i)
                            final_brand.append(brand_name)
                            brand_logo.append(b_logo)
                            #print(len((b_logo)))
                            types.append('Service Store')
                            data2 = v.text.split("Address:")
                            name = data2[0].replace('class="_hd">', '').strip()
                            final_name.append(clean_text(name))
            
                            address_data = data2[1].split("</span>")
                            address_mix_form = address_data[0].strip()
                            address_clean_form = str(clean_text(address_mix_form))
                            
                            if "Phone Number" in address_clean_form:
                                address_replace = address_clean_form.replace("Phone Number:", "^")
                                address_split = address_replace.split('^')
                                if "Directions Opening Hours" in address_split:
                                    phone_replace = address_split[1].replace("Directions Opening Hours", "$")
                                    phone_split = phone_replace.split('$')
                                    address = address_split[0]
                                    final_address.append(address)
                                    phone = phone_split[0]
                                    final_phone.append(phone)
                                    open = phone_split[1]
                                    final_open.append(open)
                                    
                                    us_zip = r'(\d{5}\-?\d{0,4})'
                                    zip_code = re.search(us_zip, address_split[0])
                                    if zip_code is None:
                                        final_lat.append('')
                                        final_lng.append('')
                                        final_city.append('')
                                        final_state.append('')
                                        final_pincode.append('')
                                        statuses.append('Done')
                                    else:
                                        pincode = zip_code.group(1)
                                        final_pincode.append(pincode)
                                        api_url = f"https://api.postalpincode.in/pincode/{pincode}"
                                        location = geolocator.geocode(f"{pincode}, India")

                                        if location:
                                            lt = location.latitude
                                            lg = location.longitude
                                            final_lat.append(lt)
                                            final_lng.append(lg)

                                        response = requests.get(api_url)

                                        if response.status_code == 200:

                                            data = response.json()
                                            if data and data[0]['Status'] == "Success":
                                                location_data = data[0]['PostOffice'][0]
                                                city = location_data.get('District')
                                                state = location_data.get('State')

                                                final_city.append(city)
                                                final_state.append(state)
                                                statuses.append('Done')
                                            else:
                                                final_city.append('')
                                                final_state.append('')
                                                statuses.append('Done')
                                        
                                        else:
                                            print("Failed to retrieve data from the API.")
                                            
                                    
                                elif "Opening Hours" in address_split[1]:
                                    phone_replace = address_split[1].replace("Opening Hours", "$")
                                    phone_split = phone_replace.split('$')
                                    address = address_split[0]
                                    final_address.append(address)
                                    phone = phone_split[0]
                                    final_phone.append(phone)
                                    open = phone_split[1]
                                    final_open.append(open)
                                    
                                    us_zip = r'(\d{5}\-?\d{0,4})'
                                    zip_code = re.search(us_zip, address_split[0])
                                    if zip_code is None:
                                        final_lat.append('')
                                        final_lng.append('')
                                        final_city.append('')
                                        final_state.append('')
                                        final_pincode.append('')
                                        statuses.append('Done')
                                    else:
                                        pincode = zip_code.group(1)
                                        final_pincode.append(pincode)
                                        api_url = f"https://api.postalpincode.in/pincode/{pincode}"
                                        location = geolocator.geocode(f"{pincode}, India")

                                        if location:
                                            lt = location.latitude
                                            lg = location.longitude
                                            final_lat.append(lt)
                                            final_lng.append(lg)

                                        response = requests.get(api_url)

                                        if response.status_code == 200:

                                            data = response.json()
                                            if data and data[0]['Status'] == "Success":
                                                location_data = data[0]['PostOffice'][0]
                                                city = location_data.get('District')
                                                state = location_data.get('State')

                                                final_city.append(city)
                                                final_state.append(state)
                                                statuses.append('Done')
                                            else:
                                                final_city.append('')
                                                final_state.append('')
                                                statuses.append('Done')
                                        
                                        else:
                                            print("Failed to retrieve data from the API.")
                                
                                else:
                                    address = address_split[0]
                                    final_address.append(address)
                                    
                                    phone = address_split[1].split("D", 1)[0]
                                    match = re.search(r'(\d{10})-(\d+)\s+(.*)$', phone)
                                    if match:
                                        phone_number = match.group(1)
                                    else:
                                        phone_number = ''
                                    # else:
                                    #     match = re.search(r'(\d{6})\s+(\d{4})\s+(.*)$', phone)
                                    #     if match:
                                    #         phone_number = match.group(1) + match.group(2)
                                    final_phone.append(phone_number)
                                    
                                    final_open.append(' ')
                                    
                                    us_zip = r'(\d{5}\-?\d{0,4})'
                                    zip_code = re.search(us_zip, address)
                                    if zip_code is None:
                                        final_lat.append('')
                                        final_lng.append('')
                                        final_city.append('')
                                        final_state.append('')
                                        final_pincode.append('')
                                        statuses.append('Done')
                                    else:
                                        pincode = zip_code.group(1)
                                        final_pincode.append(pincode)
                                        api_url = f"https://api.postalpincode.in/pincode/{pincode}"
                                        location = geolocator.geocode(f"{pincode}, India")

                                        if location:
                                            lt = location.latitude
                                            lg = location.longitude
                                            final_lat.append(lt)
                                            final_lng.append(lg)

                                        response = requests.get(api_url)

                                        if response.status_code == 200:

                                            data = response.json()
                                            if data and data[0]['Status'] == "Success":
                                                location_data = data[0]['PostOffice'][0]
                                                city = location_data.get('District')
                                                state = location_data.get('State')

                                                final_city.append(city)
                                                final_state.append(state)
                                                statuses.append('Done')
                                            else:
                                                final_city.append('')
                                                final_state.append('')
                                                statuses.append('Done')
                                        
                                        else:
                                            print("Failed to retrieve data from the API.")

                            elif "Directions Opening Hours" in address_clean_form:
                                address_replace = address_clean_form.replace("Directions Opening Hours", "$")
                                address_split = address_replace.split('$')
                                final_phone.append(' ')
                                address = address_split[0]
                                final_address.append(address)
                                open = address_split[1]
                                final_open.append(open)
                                #print(time[1])
                                us_zip = r'(\d{5}\-?\d{0,4})'
                                zip_code = re.search(us_zip, address_split[0])
                                if zip_code is None:
                                    final_lat.append('')
                                    final_lng.append('')
                                    final_city.append('')
                                    final_state.append('')
                                    final_pincode.append('')
                                    statuses.append('Done')
                                else:
                                    pincode = zip_code.group(1)
                                    final_pincode.append(pincode)
                                    api_url = f"https://api.postalpincode.in/pincode/{pincode}"
                                    location = geolocator.geocode(f"{pincode}, India")

                                    if location:
                                        lt = location.latitude
                                        lg = location.longitude
                                        final_lat.append(lt)
                                        final_lng.append(lg)

                                    response = requests.get(api_url)

                                    if response.status_code == 200:

                                        data = response.json()
                                        if data and data[0]['Status'] == "Success":
                                            location_data = data[0]['PostOffice'][0]
                                            city = location_data.get('District')
                                            state = location_data.get('State')

                                            final_city.append(city)
                                            final_state.append(state)
                                            statuses.append('Done')
                                        else:
                                            final_city.append('')
                                            final_state.append('')
                                            statuses.append('Done')
                                        
                                    else:
                                        print("Failed to retrieve data from the API.")
                            else:
                                address_split = address_clean_form.split("Directions", 1)[0]
                                final_phone.append(' ')
                                final_open.append(' ')
                                address = address_split
                                final_address.append(address)
                                us_zip = r'(\d{5}\-?\d{0,4})'
                                zip_code = re.search(us_zip, address_split)
                                if zip_code is None:
                                    final_lat.append('')
                                    final_lng.append('')
                                    final_city.append('')
                                    final_state.append('')
                                    final_pincode.append('')
                                    statuses.append('Done')
                                else:
                                    pincode = zip_code.group(1)
                                    final_pincode.append(pincode)
                                    api_url = f"https://api.postalpincode.in/pincode/{pincode}"
                                    location = geolocator.geocode(f"{pincode}, India")

                                    if location:
                                        lt = location.latitude
                                        lg = location.longitude
                                        final_lat.append(lt)
                                        final_lng.append(lg)

                                    response = requests.get(api_url)

                                    if response.status_code == 200:

                                        data = response.json()
                                        if data and data[0]['Status'] == "Success":
                                            location_data = data[0]['PostOffice'][0]
                                            city = location_data.get('District')
                                            state = location_data.get('State')

                                            final_city.append(city)
                                            final_state.append(state)
                                            statuses.append('Done')
                                        else:
                                            final_city.append('')
                                            final_state.append('')
                                            statuses.append('Done')
                                        
                                    else:
                                        print("Failed to retrieve data from the API.")
                                
                                  
                    for item in zip(final_brand, types, final_name, final_address, final_phone, final_open, final_lat, final_lng, final_pincode, final_city, final_state, statuses, pagenumber, brand_logo):

                        brand = item[0]
                        type = item[1]
                        store_name = item[2]
                        address = item[3]
                        mobile = item[4]
                        operating_time = item[5]
                        lat = item[6]
                        lon = item[7]
                        pin_code = item[8]
                        city = item[9]
                        state = item[10]
                        status = item[11]
                        page_number = item[12]
                        brand_logo = item[13]
                        jiodata = Service(brand=brand, type=type, store_name=store_name, address=address, mobile=mobile, operating_time=operating_time, lat=lat, lon=lon, pin_code=pin_code, city=city, state=state, status=status, page_number=page_number, brand_logo=brand_logo)
                        jiodata.save()

                data_store(url)

    loopfunction()

    return JsonResponse({'message': 'Scraping and saving data is complete.'})

def citystatefunction(request):

    data = pd.read_csv("C:\FloorWalk\companies\storedata\stores_electronics.csv")
    addresses = data['address'].tolist()

    zipcodes = []
    cities = []
    states = []
    lats = []
    lngs = []

    for ad in addresses:
        
        us_zip = r'(\d{5}\-?\d{0,4})'
        zip_code = re.search(us_zip, ad)
        pincode = zip_code.group(1)
        if zip_code is None:
            lats.append('')
            lngs.append('')
            cities.append('')
            states.append('')
            zipcodes.append('')
        else:
            zipcodes.append(pincode)
            api_url = f"https://api.postalpincode.in/pincode/{pincode}"
            location = geolocator.geocode(f"{pincode}, India")

            if location:
                latitude = location.latitude
                lats.append(latitude)
                longitude = location.longitude
                lngs.append(longitude)
            
            response = requests.get(api_url)

            if response.status_code == 200:

                data = response.json()
                if data and data[0]['Status'] == "Success":
                    location_data = data[0]['PostOffice'][0]
                    city = location_data.get('District')
                    state = location_data.get('State')
                    
                    cities.append(city)
                    states.append(state)
                else:
                    cities.append('')
                    states.append('')
        
            else:
                print("Failed to retrieve data from the API.")
            

            new_lat = latitude
            new_lon = longitude
            pin_code = pincode
            city = city
            state = state
            jiodata = Service(new_lat=new_lat, new_lon=new_lon, pin_code=pin_code, city=city, state=state)
            jiodata.save()
    
    return JsonResponse({'message': 'saving data is complete.'})

def transferdata(request):

    file_path = r"C:/Users/shrey/Downloads/automobile_dealerships_2wheelers.csv"

    # try:
    #     data = pd.read_csv(file_path, encoding='utf-8')
    #     store_name = data['store_name'].tolist()
    #     address = data['store_address'].tolist()
    #     city = data['City'].tolist()
    #     state = data['State'].tolist()
    #     pincode = data['Pincode'].tolist()
    #     lat = data['lat'].tolist()
    #     lon = data['lon'].tolist()
    #     store_type = data['store_type'].tolist()

    #     for item in zip(store_name, address, city, state, pincode, lat, lon, store_type):
    #         store_name = item[0]
    #         address = item[1]
    #         city = item[2]
    #         state = item[3]
    #         pincode = item[4]
    #         lat = item[5]
    #         lon = item[6]
    #         store_type = item[7]

    #         storedata = Supermarket(store_name=store_name, address=address, city=city, state=state, pincode=pincode, lat=lat, lon=lon, store_type=store_type)
    #         storedata.save()

    # except UnicodeDecodeError:

    #     try:
    #         data = pd.read_csv(file_path, encoding='latin-1')
    #         store_name = data['store_name'].tolist()
    #         address = data['store_address'].tolist()
    #         city = data['City'].tolist()
    #         state = data['State'].tolist()
    #         pincode = data['Pincode'].tolist()
    #         lat = data['lat'].tolist()
    #         lon = data['lon'].tolist()
    #         store_type = data['store_type'].tolist()

    #         for item in zip(store_name, address, city, state, pincode, lat, lon, store_type):
    #             store_name = item[0]
    #             address = item[1]
    #             city = item[2]
    #             state = item[3]
    #             pincode = item[4]
    #             lat = item[5]
    #             lon = item[6]
    #             store_type = item[7]

    #             storedata = Supermarket(store_name=store_name, address=address, city=city, state=state, pincode=pincode, lat=lat, lon=lon, store_type=store_type)
    #             storedata.save()

    #     except UnicodeDecodeError:
    #         data = pd.read_csv(file_path, encoding='ISO-8859-1')
    #         store_name = data['store_name'].tolist()
    #         address = data['store_address'].tolist()
    #         city = data['City'].tolist()
    #         state = data['State'].tolist()
    #         pincode = data['Pincode'].tolist()
    #         lat = data['lat'].tolist()
    #         lon = data['lon'].tolist()
    #         store_type = data['store_type'].tolist()

    #         for item in zip(store_name, address, city, state, pincode, lat, lon, store_type):
    #             store_name = item[0]
    #             address = item[1]
    #             city = item[2]
    #             state = item[3]
    #             pincode = item[4]
    #             lat = item[5]
    #             lon = item[6]
    #             store_type = item[7]

    #             storedata = Supermarket(store_name=store_name, address=address, city=city, state=state, pincode=pincode, lat=lat, lon=lon, store_type=store_type)
    #             storedata.save()

    # try:

    #     data = pd.read_csv(file_path, encoding='utf-8')

    #     brand = data['brand'].tolist()
    #     type = data['type'].tolist()
    #     store_name = data['store_name'].tolist()
    #     address = data['address'].tolist()
    #     mobile = data['mobile'].tolist()
    #     operating_time = data['operating_time'].tolist()
    #     lat = data['lat'].tolist()
    #     lon = data['lon'].tolist()
    #     pin_code = data['pin_code'].tolist()
    #     city = data['city'].tolist()
    #     state = data['state'].tolist()
    #     brand_logo = data['brand_logo'].tolist()
        
    #     for item in zip(brand, type, store_name, address, mobile, operating_time, lat, lon, pin_code, city, state, brand_logo):

    #         brand = item[0]
    #         type = item[1]
    #         store_name = item[2]
    #         address = item[3]
    #         mobile = item[4]
    #         operating_time = item[5]
    #         lat = item[6]
    #         lon = item[7]
    #         pin_code = item[8]
    #         city = item[9]
    #         state = item[10]
    #         brand_logo = item[11]

    #         storedata = Electronic(brand=brand, type=type, store_name=store_name, address=address, mobile=mobile, operating_time=operating_time, lat=lat, lon=lon, pin_code=pin_code, city=city, state=state, brand_logo=brand_logo)
    #         storedata.save()
    
    # except UnicodeDecodeError:

    #     try:
            
    #         data = pd.read_csv(file_path, encoding='latin-1')

    #         brand = data['brand'].tolist()
    #         type = data['type'].tolist()
    #         store_name = data['store_name'].tolist()
    #         address = data['address'].tolist()
    #         mobile = data['mobile'].tolist()
    #         operating_time = data['operating_time'].tolist()
    #         lat = data['lat'].tolist()
    #         lon = data['lon'].tolist()
    #         pin_code = data['pin_code'].tolist()
    #         city = data['city'].tolist()
    #         state = data['state'].tolist()
    #         brand_logo = data['brand_logo'].tolist()
            
    #         for item in zip(brand, type, store_name, address, mobile, operating_time, lat, lon, pin_code, city, state, brand_logo):

    #             brand = item[0]
    #             type = item[1]
    #             store_name = item[2]
    #             address = item[3]
    #             mobile = item[4]
    #             operating_time = item[5]
    #             lat = item[6]
    #             lon = item[7]
    #             pin_code = item[8]
    #             city = item[9]
    #             state = item[10]
    #             brand_logo = item[11]

    #             storedata = Electronic(brand=brand, type=type, store_name=store_name, address=address, mobile=mobile, operating_time=operating_time, lat=lat, lon=lon, pin_code=pin_code, city=city, state=state, brand_logo=brand_logo)
    #             storedata.save()

    #     except UnicodeDecodeError:
            
    #         data = pd.read_csv(file_path, encoding='ISO-8859-1')

    #         brand = data['brand'].tolist()
    #         type = data['type'].tolist()
    #         store_name = data['store_name'].tolist()
    #         address = data['address'].tolist()
    #         mobile = data['mobile'].tolist()
    #         operating_time = data['operating_time'].tolist()
    #         lat = data['lat'].tolist()
    #         lon = data['lon'].tolist()
    #         pin_code = data['pin_code'].tolist()
    #         city = data['city'].tolist()
    #         state = data['state'].tolist()
    #         brand_logo = data['brand_logo'].tolist()
            
    #         for item in zip(brand, type, store_name, address, mobile, operating_time, lat, lon, pin_code, city, state, brand_logo):

    #             brand = item[0]
    #             type = item[1]
    #             store_name = item[2]
    #             address = item[3]
    #             mobile = item[4]
    #             operating_time = item[5]
    #             lat = item[6]
    #             lon = item[7]
    #             pin_code = item[8]
    #             city = item[9]
    #             state = item[10]
    #             brand_logo = item[11]

    #             storedata = Electronic(brand=brand, type=type, store_name=store_name, address=address, mobile=mobile, operating_time=operating_time, lat=lat, lon=lon, pin_code=pin_code, city=city, state=state, brand_logo=brand_logo)
    #             storedata.save()

    # try:
    #     data = pd.read_csv(file_path, encoding='utf-8')
    #     brand_name = data['brand_name'].tolist()
    #     address = data['address'].tolist()
    #     pin_code = data['pin_code'].tolist()
    #     lat = data['lat'].tolist()
    #     lon = data['lon'].tolist()
    #     city = data['city'].tolist()
    #     state = data['state'].tolist()

    #     for item in zip(brand_name, region, address, pin_code, lat, lon, city, state):
    #         brand_name = item[0]
    #         address = item[2]
    #         pin_code = item[3]
    #         lat = item[4]
    #         lon = item[5]
    #         city = item[6]
    #         state = item[7]

    #         storedata = Movietheater(brand_name=brand_name, region=region, address=address, pin_code=pin_code, lat=lat, lon=lon, city=city, state=state)
    #         storedata.save()

    # except UnicodeDecodeError:

    #     try:
    #         data = pd.read_csv(file_path, encoding='latin-1')
    #         brand_name = data['brand_name'].tolist()
  
    #         address = data['address'].tolist()
    #         pin_code = data['pin_code'].tolist()
    #         lat = data['lat'].tolist()
    #         lon = data['lon'].tolist()
    #         city = data['city'].tolist()
    #         state = data['state'].tolist()

    #         for item in zip(brand_name, region, address, pin_code, lat, lon, city, state):
    #             brand_name = item[0]
   
    #             address = item[2]
    #             pin_code = item[3]
    #             lat = item[4]
    #             lon = item[5]
    #             city = item[6]
    #             state = item[7]

    #             storedata = Movietheater(brand_name=brand_name, region=region, address=address, pin_code=pin_code, lat=lat, lon=lon, city=city, state=state)
    #             storedata.save()

    #     except UnicodeDecodeError:
    #         data = pd.read_csv(file_path, encoding='ISO-8859-1')
    #         brand_name = data['brand_name'].tolist()

    #         address = data['address'].tolist()
    #         pin_code = data['pin_code'].tolist()
    #         lat = data['lat'].tolist()
    #         lon = data['lon'].tolist()
    #         city = data['city'].tolist()
    #         state = data['state'].tolist()

    #         for item in zip(brand_name, region, address, pin_code, lat, lon, city, state):
    #             brand_name = item[0]
 
    #             address = item[2]
    #             pin_code = item[3]
    #             lat = item[4]
    #             lon = item[5]
    #             city = item[6]
    #             state = item[7]

    #             storedata = Movietheater(brand_name=brand_name, region=region, address=address, pin_code=pin_code, lat=lat, lon=lon, city=city, state=state)
    #             storedata.save()

    # try:
    #     data = pd.read_csv(file_path, encoding='utf-8')
    #     store_type = data['store_type'].tolist()
    #     store_name = data['store_name'].tolist()
    #     address = data['address'].tolist()
    #     phone = data['phone'].tolist()
    #     operating_time = data['opening_closing'].tolist()
    #     lat = data['lat'].tolist()
    #     lon = data['lon'].tolist()
    #     city = data['city'].tolist()
    #     state = data['state'].tolist()
    #     brand_name = data['brand_name'].tolist()
    #     pincode = data['pincode'].tolist()

    #     for item in zip(store_type, store_name, address, phone, operating_time, lat, lon, city, state, brand_name, pincode):
    #         store_type = item[0]
    #         store_name = item[1]
    #         address = item[2]
    #         phone = item[3]
    #         operating_time = item[4]
    #         lat = item[5]
    #         lon = item[6]
    #         city = item[7]
    #         state = item[8]
    #         brand_name = item[9]
    #         pincode = item[10]

    #         storedata = Telecom(store_type=store_type, store_name=store_name, address=address, phone=phone, operating_time=operating_time, lat=lat, lon=lon, city=city, state=state, brand_name=brand_name, pincode=pincode)
    #         storedata.save()

    # except UnicodeDecodeError:

    #     try:
    #         data = pd.read_csv(file_path, encoding='latin-1')

    #         store_type = data['store_type'].tolist()
    #         store_name = data['store_name'].tolist()
    #         address = data['address'].tolist()
    #         phone = data['phone'].tolist()
    #         operating_time = data['opening_closing'].tolist()
    #         lat = data['lat'].tolist()
    #         lon = data['lon'].tolist()
    #         city = data['city'].tolist()
    #         state = data['state'].tolist()
    #         brand_name = data['brand_name'].tolist()
    #         pincode = data['pincode'].tolist()

    #         for item in zip(store_type, store_name, address, phone, operating_time, lat, lon, city, state, brand_name, pincode):
    #             store_type = item[0]
    #             store_name = item[1]
    #             address = item[2]
    #             phone = item[3]
    #             operating_time = item[4]
    #             lat = item[5]
    #             lon = item[6]
    #             city = item[7]
    #             state = item[8]
    #             brand_name = item[9]
    #             pincode = item[10]

    #             storedata = Telecom(store_type=store_type, store_name=store_name, address=address, phone=phone, operating_time=operating_time, lat=lat, lon=lon, city=city, state=state, brand_name=brand_name, pincode=pincode)
    #             storedata.save()

    #     except UnicodeDecodeError:
    #         data = pd.read_csv(file_path, encoding='ISO-8859-1')

    #         store_type = data['store_type'].tolist()
    #         store_name = data['store_name'].tolist()
    #         address = data['address'].tolist()
    #         phone = data['phone'].tolist()
    #         operating_time = data['opening_closing'].tolist()
    #         lat = data['lat'].tolist()
    #         lon = data['lon'].tolist()
    #         city = data['city'].tolist()
    #         state = data['state'].tolist()
    #         brand_name = data['brand_name'].tolist()
    #         pincode = data['pincode'].tolist()

    #         for item in zip(store_type, store_name, address, phone, operating_time, lat, lon, city, state, brand_name, pincode):
    #             store_type = item[0]
    #             store_name = item[1]
    #             address = item[2]
    #             phone = item[3]
    #             operating_time = item[4]
    #             lat = item[5]
    #             lon = item[6]
    #             city = item[7]
    #             state = item[8]
    #             brand_name = item[9]
    #             pincode = item[10]

    #             storedata = Telecom(store_type=store_type, store_name=store_name, address=address, phone=phone, operating_time=operating_time, lat=lat, lon=lon, city=city, state=state, brand_name=brand_name, pincode=pincode)
    #             storedata.save()


    try:
        data = pd.read_csv(file_path, encoding='utf-8')
        dealership_name = data['dealership_name'].tolist()
        address = data['dealership_address'].tolist()
        phone = data['dealership_phone'].tolist()
        brand_name = data['brand_name'].tolist()
        city = data['city_name'].tolist()
        state = data['state_name'].tolist()
        lat = data['lat'].tolist()
        lon = data['lon'].tolist()
        pincode = data['pincode'].tolist()
        

        for item in zip(dealership_name, address, phone, brand_name, city, state, lat, lon, pincode):
            dealership_name = item[0]
            address = item[1]
            phone = item[2]
            brand_name = item[3]
            city = item[4]
            state = item[5]
            lat = item[6]
            lon = item[7]
            pincode = item[8]

            storedata = Automobile(dealership_name=dealership_name, address=address, phone=phone, brand_name=brand_name, city=city, state=state, lat=lat, lon=lon, pincode=pincode)
            storedata.save()

    except UnicodeDecodeError:

        try:
            data = pd.read_csv(file_path, encoding='latin-1')

            dealership_name = data['dealership_name'].tolist()
            address = data['dealership_address'].tolist()
            phone = data['dealership_phone'].tolist()
            brand_name = data['brand_name'].tolist()
            city = data['city_name'].tolist()
            state = data['state_name'].tolist()
            lat = data['lat'].tolist()
            lon = data['lon'].tolist()
            pincode = data['pincode'].tolist()
            

            for item in zip(dealership_name, address, phone, brand_name, city, state, lat, lon, pincode):
                dealership_name = item[0]
                address = item[1]
                phone = item[2]
                brand_name = item[3]
                city = item[4]
                state = item[5]
                lat = item[6]
                lon = item[7]
                pincode = item[8]

                storedata = Automobile(dealership_name=dealership_name, address=address, phone=phone, brand_name=brand_name, city=city, state=state, lat=lat, lon=lon, pincode=pincode)
                storedata.save()

        except UnicodeDecodeError:
            data = pd.read_csv(file_path, encoding='ISO-8859-1')

            dealership_name = data['dealership_name'].tolist()
            address = data['dealership_address'].tolist()
            phone = data['dealership_phone'].tolist()
            brand_name = data['brand_name'].tolist()
            city = data['city_name'].tolist()
            state = data['state_name'].tolist()
            lat = data['lat'].tolist()
            lon = data['lon'].tolist()
            pincode = data['pincode'].tolist()
            

            for item in zip(dealership_name, address, phone, brand_name, city, state, lat, lon, pincode):
                dealership_name = item[0]
                address = item[1]
                phone = item[2]
                brand_name = item[3]
                city = item[4]
                state = item[5]
                lat = item[6]
                lon = item[7]
                pincode = item[8]

                storedata = Automobile(dealership_name=dealership_name, address=address, phone=phone, brand_name=brand_name, city=city, state=state, lat=lat, lon=lon, pincode=pincode)
                storedata.save()

    return JsonResponse({'message': 'saving data is complete.'})

        