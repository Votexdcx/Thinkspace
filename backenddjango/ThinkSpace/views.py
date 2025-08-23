from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def home_activities(request):
    return Response([
        {"id": 1, "title": "Learn Django"},
        {"id": 2, "title": "Connect React frontend"}
    ])
