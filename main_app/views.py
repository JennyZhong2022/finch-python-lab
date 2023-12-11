from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Finch
from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')    

def finches_index(request):
    finches=Finch.objects.all()
    return render(request,'finches/index.html',{
      'finches':finches
    })    

def finches_detail(request,finch_id):
    finch=Finch.objects.get(id=finch_id)
    feeding_form=FeedingForm()
    return render(request,'finches/detail.html',{
      'finch':finch,
      'feeding_form': feeding_form
    })   

def add_feeding(request,finch_id):
  #   # create a ModelForm instance using the data in request.POST
  form=FeedingForm(request.POST)    

  if form.is_valid():
    # After ensuring that the form contains valid data, we save the form with the commit=False option, which returns an in-memory model object so that we can assign the finch_id before actually saving to the database.
    new_feeding=form.save(commit=False)
    new_feeding.finch_id=finch_id
    new_feeding.save()     
  return redirect('detail',finch_id=finch_id)  

class FinchCreate(CreateView):
  model=Finch
  fields='__all__'

class FinchUpdate(UpdateView):
  model=Finch
  fields=['breed','description','age']


class FinchDelete(DeleteView):
  model=Finch
  success_url='/finches'

