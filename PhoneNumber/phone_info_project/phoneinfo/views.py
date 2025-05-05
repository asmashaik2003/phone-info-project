from django.shortcuts import render

# Create your views here.

import phonenumbers
from phonenumbers import timezone, geocoder, carrier

def phone_info(request):
    if request.method == "POST":
        number = request.POST.get('number')
        try:
            phone = phonenumbers.parse(number)
            time = timezone.time_zones_for_number(phone)
            car = carrier.name_for_number(phone, "en")
            reg = geocoder.description_for_number(phone, "en")
            context = {
                'number': number,
                'time': time,
                'car': car,
                'reg': reg,
            }
            return render(request, 'phoneinfo/phone_info.html', context)
        except phonenumbers.phonenumberutil.NumberParseException:
            return render(request, 'phoneinfo/phone_info.html', {'error': 'Invalid number. Please enter a valid phone number.'})
    return render(request, 'phoneinfo/phone_info.html')
