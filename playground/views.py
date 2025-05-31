from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page
import requests
# from .tasks import notify_customers
# from .tasks import fetch_news
# from .tasks import send_email_batch
import logging

logger = logging.getLogger(__name__)


# this is some less code caching method
# @cache_page(5 * 60)
def say_hello(request):
    try:
        logger.info('Calling HttpBin')
        response = requests.get('https://httpbin.org/delay/0.2')
        logger.info('Recieved response')
        data = response.json()
    except requests.ConnectionError:
        logger.critical('Httpbin is not responding')
    return render(request, 'hello.html', {'name': data})   




# THis is manual low level caching method
# def say_hello(request):
#     key = 'http_result'
#     if cache.get(key) is None:
#         response = requests.get('https://httpbin.org/delay/2')
#         data = response.json()
#         cache.set(key, data, timeout=10)

#     return render(request, 'hello.html', {'name': cache.get(key)})    
    
    # Call the Celery task
    # notify_customers.delay("Hello, this is a test message!")
    # delay is used to call the task asynchronously which means it will not block the request/response cycle
    # Render a template
    # You can create a simple HTML file named hello.html in your templates directory


# def say_hello(request):
    # fetch_news.delay()
    # return render(request, 'hello.html')


# from .tasks import send_email_batch

# def say_hello(request):
#     email_list = ['a@test.com', 'b@test.com', 'c@test.com', 'd@test.com']
#     chunks = [email_list[i:i+2] for i in range(0, len(email_list), 2)]
    
#     for chunk in chunks:
#         send_email_batch.delay(chunk)

#     return render(request, 'hello.html')
