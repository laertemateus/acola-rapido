from django.shortcuts import render

def home(request):
    '''
    Página incial do site
    '''

    return render(request, 'paginas/home.html',{})