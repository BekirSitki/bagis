from django.shortcuts import redirect, render, HttpResponse


# Create your views here.

def index(request):
    
    if request.method == 'POST':
        bagis_miktari = request.POST['bagis_miktari']
        isim = request.POST['isim']
        mail = request.POST['mail']
        if bagis_miktari:
            return HttpResponse( render( request, 'odeme.html', { 'miktar' : bagis_miktari, 'isim' : isim, 'mail' : mail } ) )

    return HttpResponse( render( request, 'index.html', {} ) )