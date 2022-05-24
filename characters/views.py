from django.http.response import HttpResponse
from django.shortcuts import render
from characters.models import Link,Character
import json

# find out, which character has a fewst links and create its instance
# return a link, through which user can speak with her
def createLink(request):
    #get the character with fewest links
    character = list(Character.objects.all().order_by('timesLinked'))[0]    
    #create the link
    link = Link(character = character)
    link.save()
    #return link
    return HttpResponse(link.id)

#get character connected to obtained link,
#return a page with prepared streaming
def loadCharacter(request):
    #get the link
    hash = request.GET["hash"]
    #select the character
    link = Link.objects.all().filter(id = hash)[0]
    character = link.character
    #load its conversations
    renderData = {"name":character.name}
    renderData["conversation"] = json.load(open("static/characters/conversations/json/%s.json"%(character.name)))
    return render(request,"showCharacter.html",renderData)
    #render the page
    #prepare streaming