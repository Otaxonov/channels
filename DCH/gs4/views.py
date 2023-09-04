from django.shortcuts import render
from gs2.models import Group, Chat

# Create your views here.

def index_view(request, group_name):

    try:
        group = Group.objects.get(name=group_name)
    except Group.DoesNotExist:
        group = False

    if group:
        chats = Chat.objects.filter(group=group).order_by('time_stamp')
    else:
        chats = False

    context = {
        "group_name": group_name,
        "group": group,
        "chats": chats
    }
    return render(request, 'gs4/index.html', context)
