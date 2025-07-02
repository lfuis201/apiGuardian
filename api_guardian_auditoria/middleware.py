import json
from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now
from django.contrib.auth.models import AnonymousUser
from .models import AuditLog

class AuditLogMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.path.startswith('/admin') or request.path.startswith('/static'):
            return response

        try:
            user = getattr(request, 'user', None)
            username = user.username if user and not isinstance(user, AnonymousUser) else None

            AuditLog.objects.create(
                path=request.path,
                method=request.method,
                user=username,
                ip_address=self.get_ip(request),
                status_code=response.status_code,
                request_body=self.get_body(request),
                response_body=self.get_response_body(response),
                timestamp=now()
            )
        except Exception:
            pass  # Nunca debe romper

        return response

    def get_ip(self, request):
        return request.META.get('REMOTE_ADDR', None)

    def get_body(self, request):
        try:
            if request.body:
                return request.body.decode('utf-8')
        except:
            return ''
        return ''

    def get_response_body(self, response):
        try:
            if hasattr(response, 'data'):
                return json.dumps(response.data)
            elif hasattr(response, 'content'):
                return response.content.decode('utf-8')
        except:
            return ''
        return ''
