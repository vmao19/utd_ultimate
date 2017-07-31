from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

#def woofabout(request):
#	return render(request, 'woof/about.html')
def woofroster(request):
	return render(request, 'woof/roster.html')
#def woofgallery(request):
#	return render(request, 'woof/gallery.html')
#def woofcontactus(request):
#	return render(request, 'woof/contactus.html')

#def barkabout(request):
#	return render(request, 'bark/about.html')
#def barkroster(request):
#	return render(request, 'bark/roster.html')
#def barkgallery(request):
#	return render(request, 'bark/gallery.html')
#def barkcontactus(request):
#	return render(request, 'bark/contactus.html')

#def monstarsabout(request):
#	return render(request, 'monstars/about.html')
#def monstarsroster(request):
#	return render(request, 'monstars/roster.html')
#def monstarsgallery(request):
#	return render(request, 'monstars/gallery.html')
#def monstarscontactus(request):
#	return render(request, 'monstars/contactus.html')