from django.shortcuts import render
from .models import Name



def calculate_love_score(first_name, second_name):
    combined_names = (first_name + second_name).lower()  # Concatenate and convert to lowercase
    love_score = 0
    
    for char in combined_names:
        love_score += ord(char) - 96  # Get the ASCII value of the character and subtract 96 to map 'a' to 1, 'b' to 2, etc.
    
    # Normalize the score to a percentage between 0 and 100
    max_possible_score = 26 * len(combined_names)  # Assuming each letter contributes a maximum of 26
    love_percentage = (love_score / max_possible_score) * 100
    
    return love_percentage





# Create your views here.
def home(request):
    return render(request, 'home.html')

def calculate_love(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        # Calculate love percentage (your logic here)
        love_percentage = calculate_love_score(first_name, second_name)
        Name.objects.create(first_name=first_name, second_name=second_name, score=love_percentage)
        return render(request,'result.html',{'first_name': first_name,'second_name': second_name,'love_percentage': love_percentage})
    else:
        return render(request, 'home.html')