import requests
import json
from decouple import config
from asgiref.sync import iscoroutinefunction
from django.utils.decorators import sync_and_async_middleware
from apps.base.models import IpAddress
from apps.users.models import User

LOCALIZATION_API_KEY = config('LOCALIZATION_API_KEY', default='')
LOCALIZATION_API_URL = config('LOCALIZATION_API_URL', default='')

def get_user_ip(request):
    api_url = LOCALIZATION_API_URL + "?apiKey=" + LOCALIZATION_API_KEY
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    if ip:
        user=None
        user_id = request.user.id
        if user_id:
            user = User.objects.filter(id = user_id).first()
        
        try:
            old_ip_address = IpAddress.objects.get(ip=ip)
            if user:
                old_ip_address.user=user
                old_ip_address.save()

        except IpAddress.DoesNotExist:
            ip_info_response = requests.get(api_url + "&ip=" + ip)
            #print(api_url + "&ip=" + ip, ip_info_response.status_code)
            if ip_info_response.status_code == 200:
                ip_info = json.loads(ip_info_response.content)
                #print(ip_info)
                ip_address = IpAddress(ip=ip,
                                       continent_code=ip_info['continent_code'],
                                       continent_name=ip_info['continent_name'],
                                       country_code2=ip_info['country_code2'],
                                       country_code3=ip_info['country_code3'],
                                       country_name=ip_info['country_name'],
                                       state_prov=ip_info['state_prov'],
                                       state_code=ip_info['state_code'],
                                       district=ip_info['district'],
                                       city=ip_info['city'],
                                       zipcode=ip_info['zipcode'],
                                       latitude=ip_info['latitude'],
                                       longitude=ip_info['longitude'],
                                       calling_code=ip_info['calling_code'],
                                       country_flag=ip_info['country_flag'],
                                       organization=ip_info['organization'],
                                       user=user)
                ip_address.save()
    return None

@sync_and_async_middleware
def iplocationuser(get_response):
    # One-time configuration and initialization.

    if iscoroutinefunction(get_response):
        async def middleware(request):
            # Code to be executed for each request before
            # the view (and later middleware) are called.
            get_user_ip(request)
            response = await get_response(request)
            # Code to be executed for each request/response after
            # the view is called.
            return response

    else:

        def middleware(request):
            # Code to be executed for each request before
            # the view (and later middleware) are called.
            get_user_ip(request)
            response = get_response(request)
            # Code to be executed for each request/response after
            # the view is called.
            return response

    return middleware