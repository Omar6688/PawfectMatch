from django.conf import settings
import os
from django.shortcuts import render
from .models import Service

def service_list(request):
    print("DEBUG:", settings.DEBUG)
    print("MEDIA_URL:", settings.MEDIA_URL)
    print("USE_AWS:", os.getenv("USE_AWS"))

    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})
