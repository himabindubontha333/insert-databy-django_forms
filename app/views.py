from django.shortcuts import render
from app.models import *
from app.forms import *

# Create your views here.
def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            topic_name=TFD.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()
            TQS=Topic.objects.all()
            d1={'TQS':TQS}
            return render(request,'display_topic.html',d1)
    return render(request,'insert_topic.html',d)

