from django.conf import settings # import the settings file

def release(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'PHASE': settings.PHASE}