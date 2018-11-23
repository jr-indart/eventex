from django.shortcuts import render


def home(request):
    speakers = [
        {'name': 'Grace Hopper', 'foto': 'http://hbn.link/hopper-pic'},
        {'name': 'Alan Turing', 'foto': 'http://hbn.link/turing-pic'},
    ]
    return render(request, 'index.html', {'speakers': speakers})
