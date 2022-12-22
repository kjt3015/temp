from django.shortcuts import render

def lending(request):
    return render(
        request,
        'single_pages/login.html'    
    )

def about_me(request):
    return render(
        request,
        'single_pages/signup.html'
    )