from django.shortcuts import render
from listings.models import Band
from django.http import HttpResponse, Http404
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm, BandForm, ListingForm
from django.core.mail import send_mail
from django.shortcuts import redirect



def bands_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        print(form)
        if form.is_valid():
            band = form.save() 
            return redirect('bands-detail', band.id)
    else:
        form = BandForm()

    return render(request, 'listings/bands_create.html', {'form': form})

def bands_change(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
        return redirect('bands-detail', band.id)        
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/bands_change.html', {'form': form})

def bands_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        band.delete()
        return redirect('bands')        
    return render(request, 'listings/bands_delete.html', {'band': band})

def bands(request):
    bands = Band.objects.all()
    return render(request, 'listings/bands.html', {'bands': bands})

def bands_detail(request, id):
    try:
        band = Band.objects.get(id=id)
    except Band.DoesNotExist:
        raise Http404("Not get")

    return render(request, 'listings/bands_detail.html', {'band': band})

def about(request):
    return render(request, 'listings/about.html')

def email_sent(request):
    return render(request, 'listings/email_sent.html')

def contact(request):
    print('la methode de request est', request.method)
    print('les data de POST est', request.POST)

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['ange@gmail.com']
            ) 
        return redirect('email-sent')       
    else:    
        form = ContactUsForm()

    return render(request, 'listings/contact.html', {'form': form})

def listings_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save() 
            return redirect('listings-detail', listing.id)
    else:
        form = ListingForm()

    return render(request, 'listings/listings_create.html', {'form': form})

def listings_change(request, id):
    listing = Listing.objects.get(id=id)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            listing = form.save() 
            return redirect('listings-detail', listing.id)
    else:
        form = ListingForm(instance=listing)

    return render(request, 'listings/listings_change.html', {'form': form})

def listings(request):
    listings = Listing.objects.all()
    
    return render(request, 'listings/listings.html', {'listings':listings})

def listings_detail(request, id):
    
    try:
       listing = Listing.objects.get(id=id)
       band = Band.objects.get(id=listing.band_id)
    except Band.DoesNotExist:
        raise Http404("Not get")
    return render(request, 'listings/listings_detail.html', {'listing':listing, 'band': band})