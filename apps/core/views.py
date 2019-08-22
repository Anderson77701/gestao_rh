from django.shortcuts import render

def homeCore(request):
    return render(request, 'core/index_core.html')