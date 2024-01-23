import json
from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def pagar(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        cursos = request.POST['cursos']
        nombre = request.POST['nombre']
        numero = request.POST['numero']
        fecha = request.POST['fecha']
        cvv = request.POST['cvv']

        cursosUrl = 'http://127.0.0.1:8080/api/cursos/'
        response = requests.get(cursosUrl)
        data = response.json()

        if not email or not password or not cursos or not nombre or not numero or not fecha or not cvv:
            return render(request, 'pagar.html', {
                'error': 'Todos los campos son obligatorios',
                'cursos': data
            })

        url = 'http://127.0.0.1:8080/api/users/login/'
        data = {'email': email, 'password': password}

        response = requests.post(url, data=data)

        if response.status_code == 200:
            data = response.json()
            idUser = data['id']
            urlDataUser = f'http://127.0.0.1:8080/api/users/{idUser}/'
            
            # Obtener cursos actuales del usuario
            cursos_actuales = data.get('cursos', [])
            
            # Agregar el nuevo curso
            cursos_actuales.append(cursos)

            # Preparar datos para la solicitud PATCH
            datos = {
                'cursos': cursos_actuales
            }

            # Convertir los datos a formato JSON
            datos_json = json.dumps(datos)

            # Realizar la solicitud PATCH
            response = requests.patch(
                urlDataUser,
                data=datos_json,
                headers={'Content-Type': 'application/json'}
            )

            # Obtener la respuesta
            data = response.json()
            return render(request, 'index.html', {'success': 'Compra realizada con éxito'})
        else:
            return render(request, 'index.html', {'error': 'Credenciales incorrectas'})
    else:
        cursosUrl = 'http://127.0.0.1:8080/api/cursos/'
        response = requests.get(cursosUrl)
        data = response.json()
        return render(request, 'pagar.html', {
            'cursos': data
        })