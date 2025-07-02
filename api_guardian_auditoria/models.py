from django.db import models
from django.utils.timezone import now

class AuditLog(models.Model):
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    user = models.CharField(max_length=255, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    status_code = models.IntegerField()
    request_body = models.TextField(null=True, blank=True)
    response_body = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(default=now)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"[{self.timestamp}] {self.method} {self.path} ({self.status_code})"
