# I have created this file -Ajaykaran

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):

    # Get the text
    djtext = request.POST.get('text', 'default')
    # Check the checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcap = request.POST.get('fullcap', 'off')
    nlineremover = request.POST.get('nlineremover', 'off')
    exspaceremover = request.POST.get('exspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    analyzed = ""
    params2 = ""
    # Check which text is on
    if removepunc == 'on' and len(djtext) > 0:
        analyzed = ""
        puncs = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in puncs:
                analyzed = analyzed+char
        params = {'purpose': '',
            'analyzed_text': analyzed}
        djtext = analyzed
        params2 = params['purpose'] + "Removed punctuations"
        params['purpose'] = params2
    if fullcap == 'on':
        analyzed = ""
        analyzed = djtext.upper()
        params = {'purpose':'', 'analyzed_text': analyzed}
        djtext = analyzed
        params2 = params2 + " Changed to Uppercase"
        params['purpose'] = params2

    if nlineremover =='on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose':'', 'analyzed_text': analyzed}
        djtext = analyzed
        params2 = params2 + " Removed new lines"
        params['purpose'] = params2

    if exspaceremover =='on':
        analyzed = ""
        for i, char in enumerate(djtext):
            if not (djtext[i] == " " and djtext[i+1] ==" "):
                analyzed = analyzed + char
        params = {'purpose':'', 'analyzed_text': analyzed}
        djtext = analyzed
        params2 = params2 + " Removed Extra spaces"
        params['purpose'] = params2

    if charcount =='on':
        analyzed = djtext
        char = f"The number of characters in your text are {len(djtext)}"
        params = {'purpose':'', 'analyzed_text': analyzed, 'chars':char}
        params2 = params2 + " Counted number of Characters"
        params['purpose'] = params2
        # params["chars"] = char
        

    if removepunc != 'on' and fullcap != 'on' and nlineremover !='on' and exspaceremover !='on' and charcount !='on' or  len(djtext) == 0:
        return HttpResponse("Error !")

    return render(request, 'analyze.html', params)

# -----------------About Us------------------------
def about(request):
    return render(request, 'about.html')
