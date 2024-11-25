from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Contacto

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        # Guardar el mensaje en la base de datos
        Contacto.objects.create(nombre=nombre, email=email, mensaje=mensaje)

        # Enviar el correo
        asunto = f"Nuevo mensaje de {nombre} - Contacto desde el Portafolio"
        mensaje_completo = f"Nombre: {nombre}\nCorreo: {email}\n\nMensaje:\n{mensaje}"
        destinatario = 'alesandro3644@gmail.com'  # Tu correo personal

        try:
            send_mail(asunto, mensaje_completo, email, [destinatario], fail_silently=False)
        except Exception as e:
            print(f"Error al enviar el correo: {e}")

        # Redirigir a la misma página después de enviar el mensaje
        return redirect('contacto')

    # Renderizar el template de contacto
    return render(request, 'contacto/contacto.html')
