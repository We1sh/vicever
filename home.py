from django.shortcuts import render 
def view(request):
    return render(request,'home.html')

def reverse(request):
    user_text=request.GET['usertext']
    words=len(user_text.split())
    reversed_text=user_text[::-1]
    return render(request,'reverse.html',{'usertext':user_text,'reversedtext':reversed_text,
    'words':words})
