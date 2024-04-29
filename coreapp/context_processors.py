from .models import Userpermistionupload


def sidebar_data(request):
    userid = request.user.id
    success = Userpermistionupload.objects.filter(user_id=userid)
    # success = "hello"
    
    return {'sidebar_data': success}