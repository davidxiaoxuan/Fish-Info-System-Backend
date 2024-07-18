from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from core.settings import EMAIL_CONFIRM_REDIRECT_BASE_URL, PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL


def email_confirm_redirect(request, key):
    return HttpResponseRedirect(f"{EMAIL_CONFIRM_REDIRECT_BASE_URL}{key}/")


def password_reset_confirm_redirect(request, uidb64, token):
    return HttpResponseRedirect(
        f"{PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL}{uidb64}/{token}/"
    )


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:3000/api/auth/callback/google"
    client_class = OAuth2Client

def search_fish(request):
    query = request.GET.get('query', '')
    # 这里应该包含搜索逻辑，根据 query 检索数据库
    results = []
    # 示例：假设你已经有鱼的信息在数据库中
    if query.lower() == 'shiner perch':
        results.append({'id': 1, 'name': 'Shiner Perch'})
    return JsonResponse(results, safe=False)
