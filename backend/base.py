from rest_framework.response import Response


def send_response(data, status):
    return Response(data=data, content_type='application/json', status=status)
