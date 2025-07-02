from django.dispatch import receiver
from axes.signals import user_locked_out
from django.core.mail import send_mail
from django.utils.timezone import now

@receiver(user_locked_out)
def report_user_locked(sender, request, username, ip_address, **kwargs):
    print("🚨 Señal 'user_locked_out' capturada. Enviando correo de alerta...")

    try:
        send_mail(
            subject='🚨 Usuario o IP bloqueado por múltiples intentos fallidos',
            message=(
                f'🔒 Se ha bloqueado la cuenta o IP debido a múltiples intentos fallidos.\n\n'
                f'👤 Usuario: {username}\n'
                f'🌐 IP: {ip_address}\n'
                f'🔗 Ruta: {request.path if request else "N/A"}\n'
                f'🕒 Hora: {now().strftime("%Y-%m-%d %H:%M:%S")}'
            ),
            from_email='Guardian API <no-reply@tudominio.com>',
            recipient_list=['luisfeliperodrigo30@gmail.com'],
            fail_silently=False
        )
    except Exception as e:
        print(f"❌ Error al enviar el correo de alerta: {e}")
