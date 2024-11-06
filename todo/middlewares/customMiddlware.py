import time
from django.utils.deprecation import MiddlewareMixin


class MyMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()
        
    def process_response(self, request, response):
        duration = time.time() - getattr(request,'start_time',time.time())
        
        print(f"Path: {request.path}, Method: {request.method}, Duration: {duration:.3f}s")

        return response