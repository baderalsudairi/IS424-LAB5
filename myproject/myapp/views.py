from django.shortcuts import render, redirect

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

people = []

def add(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        person = Person(username, password)
        people.append(person)
        return redirect('default')

    return render(request, 'myapp/add.html')

def default(request):
    context = {'people': people}
    return render(request, 'myapp/default.html', context)
