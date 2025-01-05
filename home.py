from django.shortcuts import render 
def view(request):
    return render(request,'home.html')

def reverse(request):
    return render(request,'reverse.html')