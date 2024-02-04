from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    
def analyze(request):
     #Get the text
     djtext = request.POST.get('text', 'default')
     
     #Check checkbox values
     removepunc = request.POST.get('removepunc', 'off')
     fullcpas = request.POST.get('fullcaps', 'off')
     newlineremover = request.POST.get('newlineremover', 'off')
     extraspaceremover = request.POST.get('extra_spaceremover', 'off')
     charcount = request.POST.get('charcounter', 'off')

     params = {'purpose': '', 'analyzed_text': ''}
     analyzed = djtext
     purpose = ""
    
     #Check which checkbox is on
     if(removepunc == "on"):
        punctuations = '''!()-[]{};:'"\',<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        purpose = "Removed Punctuation"
        djtext = analyzed
        
     if(fullcpas == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        purpose = purpose + " and " + "Converted To Upper Case"
        djtext = analyzed
        
     if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                analyzed = analyzed + " "
        purpose = purpose + " and " + "Removed New Lines"
        djtext = analyzed
    
     if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
                
        purpose = purpose + " and " + "Removed Extra Spaces"
        djtext = analyzed
    
     if(charcount == "on"):
         analyzed2=('\nNo. of characters given in the text are : '+str(len(djtext)))
         analyzed = djtext + " " + analyzed2
         purpose = purpose + " and " + "Characters Counted"
         djtext = analyzed
         
        
     elif(removepunc != "on" and fullcpas != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
         return HttpResponse("Error")
     
     params = {'purpose': purpose, 'analyzed_text': analyzed}
     return render(request, 'analyze.html', params)
    
