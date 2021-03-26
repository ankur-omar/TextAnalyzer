
from django.http import HttpResponse
from django.shortcuts import  render



def index(request):

    return render(request,'index.html')

def removepuncuation(request):
    return HttpResponse("removepunc")

def analyzer(request):
    djtext =request.POST.get('text','default')
    removepunc =request.POST.get('removepuncuation','off')
    fullcap =request.POST.get('fullcap','off')
    newlineremover =request.POST.get('newlineremover','off')
    spaceremover =request.POST.get('spaceremover','off')
    charcount =request.POST.get('charcount','off')





    if removepunc =="on":

        puncuation ='''!~@#$%^&())(_-+={}[]\/<>.,?:;'"'''

        analyzed =""
        for char in djtext:
            if char not in puncuation:
                analyzed =analyzed+char

        param ={"purpose":"After Removing the puncuation the Text is : ","analyzed_text":analyzed}
        djtext =analyzed


    if fullcap=='on':
        analyzed =""
        puncuation ='''!~@#$%^&())(_-+={}[]\/<>.,?:;'"'''

        for char in djtext:
            if char not in puncuation:
                analyzed =analyzed+char.upper()
        param ={"purpose":"capital letter Text is : ","analyzed_text":analyzed}
        djtext =analyzed




    if newlineremover=='on':
        analyzed =""

        for index,char in enumerate(djtext):
            if char!="\n" and char!="\r":
                analyzed =analyzed+char
        param ={"purpose":"After Removing the Multiple Line the Text is: ","analyzed_text":analyzed}
        djtext =analyzed






    if spaceremover=='on':
        analyzed =""

        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed =analyzed+char
        param ={"purpose":" After Removing Space The Text is: ","analyzed_text":analyzed}
        djtext =analyzed





    if charcount=='on':
        analyzed =""
        count =0
        for char in djtext:
            count =count+1

        param ={"purpose":"Total Character count is","analyzed_text":count}

    if (removepunc != 'on' and fullcap!='on' and spaceremover!='on' and newlineremover!="on" and charcount!="on"):
        return HttpResponse("Error")

    else:
        return render(request,'analyze.html',param)












