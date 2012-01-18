from django.http import HttpResponse
from profiler import profile

#@profile("test")
def index(request):
    filler()
    return HttpResponse("ok")

def filler():
    import time
    time.sleep(1)
