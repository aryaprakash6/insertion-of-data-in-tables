from django.shortcuts import render
from app.models import *
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn = request.POST['tn']
        TO = Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        QLTO = Topic.objects.all()
        d = {'topics': QLTO}
        return render(request,'display_topic.html',d )

    return render(request,'insert_topic.html')

def insert_webpages(request):
    QLTO= Topic.objects.all()
    d={'topics': QLTO}
    if request.method =='POST':

        tn = request.POST['tn']
        na = request.POST['na']
        url = request.POST['url']
        TO = Topic.objects.get(topic_name=tn)
        WO = Webpage.objects.get_or_create(topic_name=TO , name=na, url=url)[0]
        WO.save()
        QLWO = Webpage.objects.all()
        d1={'webpages': QLWO}
        return render(request, 'display_webpages.html', d1)
    return render(request, 'insert_webpages.html',d)