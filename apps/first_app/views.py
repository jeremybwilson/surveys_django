from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):

    if 'name' not in request.session:
        request.session['name'] = 'No name entered'
    if 'location' not in request.session:
        request.session['location'] = 'No location entered'
    if 'language' not in request.session:
        request.session['language'] = 'No language chosen'
    if 'comments' not in request.session:
        request.session['comments'] = 'No comments entered'
    
    location = ['Seattle', 'Burbank', 'San Jose', 'Chicago', 'Dallas']
    language = ['Python', 'Javascript', 'Angular', 'React']
    context = {
        'locations': location,
        'languages' : language
    }
    print (context)

    return render(request, 'first_app/index.html', context)

def process(request):
    errors = []

    if 'session_count' not in request.session:
        request.session['session_count'] = 0
    else:
        request.session['session_count'] += 1
        print (request.session['session_count'])

    if request.method == 'POST':
        print ('*') * 80
        print ("Here are the form results: ", request.POST)
        name = request.POST['name']
        request.session['name'] = name
        location = request.POST['location']
        request.session['location'] = location
        language = request.POST['language']
        request.session['language'] = language
        comments = request.POST['comments']
        request.session['comments'] = comments
        
        if 'session_attempt' not in request.session:
            request.session['session_attempt'] = 0
        else:
            request.session['session_attempt'] += 1


        if len(name) < 1:
            errors.append('Name cannot be blank.')

        if len(comments) < 1:
            errors.append('Comments field cannot be blank.')

        if len(errors) > 0:
            for error in errors:
                messages.error(request, error)
            return redirect('/')

        return redirect('/results')

    else:
        return redirect('/')

    errors.append('Invalid form entry.')
    return redirect('/')

def results(request):
    context = {
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comments': request.session['comments'],
    }
    return render(request, 'first_app/results.html', context)