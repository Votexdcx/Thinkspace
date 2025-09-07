from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .Services.create_activity import CreateActivity
from .Services.create_reply import CreateReply
from .Services.show_activity import ShowActivities
from .Services.home_activities import HomeActivities
from .Services.messages import Messages
from .Services.message_groups import MessageGroups
from .Services.notification_activity import NotificationActivity
from .Services.search_activities import SearchActivities
from .Services.user_activities import UserActivities


@api_view(["GET"])
def home_activities(request):
    return Response([
        {"id": 1, "title": "Learn Django"},
        {"id": 2, "title": "Connect React frontend"}
    ])
@api_view(["GET"])
def create_message(request):
    return Response([
        {"id": 1, "title": "Learn Django"},
        {"id": 2, "title": "Connect React frontend"}
    ])
@api_view(["GET"])
def create_reply(request):
    return Response([
        {"id": 1, "title": "Learn Django"},
        {"id": 2, "title": "Connect React frontend"}
    ])
@api_view(["GET"])
def create_activity(request):
    return Response([
        {"id": 1, "title": "Learn Django"},
        {"id": 2, "title": "Connect React frontend"}
    ])
@api_view(["GET"])
def message_groups(request):
    return Response([
        {"id": 1, "title": "Learn Django"},
        {"id": 2, "title": "Connect React frontend"}
    ])
@api_view(["GET"])
def messages(request):
    return Response([
        {"id": 1, "title": "Learn Django"},
        {"id": 2, "title": "Connect React frontend"}
    ])

@api_view(["GET"])
def search_activities(request):
    return Response([
        {"id": 1, "title": "Learn Django"},
        {"id": 2, "title": "Connect React frontend"}
    ])

@api_view(["GET"])
def show_activity(request):
    return Response([
        {"id": 1, "title": "Learn Django"},
        {"id": 2, "title": "Connect React frontend"}
    ])

@api_view(["GET"])
def user_activities(request):
    return Response([
        {"id": 1, "title": "Learn Django"},
        {"id": 2, "title": "Connect React frontend"}
    ])
@api_view(["GET"])
def notification_activity(request):
    service = NotificationActivity()
    result = service.run()
    return JsonResponse(result, safe=False)



