from django.contrib import admin
from .models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user', 'ip_address', 'method', 'path', 'status_code')
    search_fields = ('user', 'path', 'ip_address', 'method')
    list_filter = ('method', 'status_code', 'timestamp')
    readonly_fields = [f.name for f in AuditLog._meta.fields]  # evita edición
    ordering = ('-timestamp',)

    def has_add_permission(self, request):
        return False  # opcional: evita añadir manualmente

    def has_delete_permission(self, request, obj=None):
        return False  # opcional: evita borrar logs desde el admin
