from django.shortcuts import render

def support_page(request):
    return render(request, 'support/support.html')
