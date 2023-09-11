from django.shortcuts import render

# Create your views here.
finches = [
    {'name': 'Tweety', 'breed': 'finch',
        'description': 'the bird is the word', 'age': 7},
    {'name': 'Love', 'breed': 'florida finch',
        'description': 'The bird was good', 'age': 5},
]


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finch_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })
