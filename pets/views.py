from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pet, Img
from accounts.models import Cart

def home(request):
    pets = Pet.objects
    if request.user :
        cart = Cart.objects.get(buyer=request.user)
    else:
        cart=NULL
    return render(request,'pets/home.html',{'pets':pets,'cart':cart})

def detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    img = Img.objects.all()
    pics = []
    for i in img :
        if i.info == pet :
            pics.append(i.image)
    return render(request,'pets/detail.html',{'pet':pet,'pics':pics,'f':len(pics)})


@login_required(login_url="/accounts/login")
def cart(request):
    items = Cart.objects.get(buyer=request.user).pet.all()
    return render(request,'pets/cart.html',{'items':items})

@login_required(login_url="/accounts/login")
def sell(request):
    if request.method=='POST':
        if request.POST['name'] and request.POST['breed'] and request.FILES['image1'] :
            pet=Pet()
            pet.name = request.POST['name']
            pet.breed = request.POST['breed']
            pet.seller = request.user
            pet.vaccinated = request.POST['vacc']
            pet.save()
            f='1'
            while f :
                if request.FILES.get('image'+f,False) :
                    img=Img()
                    img.info = pet
                    img.image = request.FILES['image'+f]
                    img.save()
                    p=int(f,10)+1
                    f=str(p)
                else :
                    break
            return redirect ('/pets/' + str(pet.id))
        else:
            range=[1,2,3,4,5]
            return render(request, 'pets/sell.html', {'range':range,'error':'fill all necessary fields.'})
    else:
        range=[1,2,3,4,5]
        return render(request, 'pets/sell.html',{'range':range})

@login_required(login_url="/accounts/login")
def add_to_cart(request, pet_id):
    if request.method=='POST':
        pet = get_object_or_404(Pet, pk=pet_id)
        cart = get_object_or_404(Cart, pk=request.user)
        cart.pet.add(pet)
    return render(request, 'pets/home.html')

@login_required(login_url="/accounts/login")
def remove_from_cart(request, pet_id):
    if request.method=='POST':
        pet = get_object_or_404(Pet, pk=pet_id)
        cart = get_object_or_404(Cart, pk=request.user)
        cart.pet.remove(pet)
        items = Cart.objects.get(buyer=request.user).pet.all()
    return render(request, 'pets/cart.html',{'items':items})
