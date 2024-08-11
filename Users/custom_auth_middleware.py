from django.utils.functional import SimpleLazyObject
from django.contrib.auth.models import AnonymousUser
from rest_framework.authentication import TokenAuthentication


def get_user_from_token(request):
    token = request.COOKIES.get('token')

    if token:
        auth = TokenAuthentication()
        try:
            # Создаем объект запроса с токеном в заголовке, чтобы использовать стандартную аутентификацию
            request.META['HTTP_AUTHORIZATION'] = f'Token {token}'
            user_auth_tuple = auth.authenticate(request)
            if user_auth_tuple is not None:
                return user_auth_tuple[0]  # Возвращаем пользователя
        except Exception:
            pass

    return AnonymousUser()  # Если аутентификация не удалась, возвращаем анонимного пользователя


def custom_auth_middleware(get_response):
    def middleware(request):
        request.user = SimpleLazyObject(lambda: get_user_from_token(request))
        response = get_response(request)
        return response

    return middleware
