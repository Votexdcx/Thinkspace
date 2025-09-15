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
from .Services.create_message import CreateMessage
from aws_xray_sdk.core import xray_recorder


@api_view(["GET"])
def home_activities(request):
    segment = xray_recorder.begin_segment('test-segment')
    service = HomeActivities()
    result = service.run()
    xray_recorder.end_segment()
    return JsonResponse(result, safe=False)

@api_view(["GET"])
def create_message(request):
    service = CreateMessage()
    result = service.run()
    return JsonResponse(result, safe=False)

@api_view(["GET"])
def create_reply(request):
    service = CreateReply()
    result = service.run()
    return JsonResponse(result, safe=False)

@api_view(["GET"])
def create_activity(request):
    service = CreateActivity()
    result = service.run()
    return JsonResponse(result, safe=False)

@api_view(["GET"])
def message_groups(request):
    service = MessageGroups()
    result = service.run()
    return JsonResponse(result, safe=False)

@api_view(["GET"])
def messages(request):
    service = Messages()
    result = service.run()
    return JsonResponse(result, safe=False)

@api_view(["GET"])
def search_activities(request):
    service = SearchActivities()
    result = service.run()
    return JsonResponse(result, safe=False)

@api_view(["GET"])
def show_activity(request):
    service = ShowActivities()
    result = service.run()
    return JsonResponse(result, safe=False)

@api_view(["GET"])
def user_activities(request):
    service = UserActivities()
    result = service.run()
    return JsonResponse(result, safe=False)

@api_view(["GET"])
def notification_activity(request):
    service = NotificationActivity()
    result = service.run()
    return JsonResponse(result, safe=False)



