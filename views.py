
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import chat
from .forms import NameForm
import requests

#def home(request):
  
  # rendering the template in templates folder
  #return render(request, "home.html", {'response': r.json()['result']['fulfillment']['speech']})



def inp_msg(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            S = form.cleaned_data['You']
            #print(S)
            url=f"https://api.dialogflow.com/v1/query?v=20150910&contexts=smalltalk&lang=en&query={S}&sessionId=12345&timezone=America/New_York"
            Headers = {
                    'Authorization': 'Bearer e12769e5afd94ad49a7016f4b8d40ece',
                    } 
            r = requests.get(url, headers=Headers)
            myresponse = r.json()['result']['fulfillment']['speech']
            print(S,myresponse)
            chat.objects.create(request=S,response=myresponse)
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        data = {
            'form' : form,
            'res': chat.objects.all()
            }


    return render(request, 'home.html', {'data': data})









