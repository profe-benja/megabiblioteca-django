import requests
from django.http import JsonResponse
from django.views import View


class LibrosView(View):
  def get(self, request, *args, **kwargs):
      # URL para obtener el token de autenticación
      auth_url = "http://127.0.0.1:8000/api/v1/auth/"

      # Datos de autenticación (usuario y contraseña)
      auth_data = {
          "username": "benja",
          "password": "123123"
      }

      try:
          # Realizar una solicitud POST para obtener el token de autenticación
          response = requests.post(auth_url, json=auth_data)

          # Verificar si la solicitud fue exitosa
          if response.status_code == 200:
              # Obtener el token de la respuesta
              token_data = response.json()
              auth_token = token_data.get("token")

              # URL de la API principal
              api_url = "http://127.0.0.1:8000/api/v1/libro/?format=json"

              # Realizar una solicitud GET a la API principal con el token de autenticación
            #   headers = {"Authorization": f"Bearer {auth_token}"}
              headers = {"Authorization": f"token {auth_token}"}
              api_response = requests.get(api_url, headers=headers)

              # Verificar si la solicitud a la API principal fue exitosa
              if api_response.status_code == 200:
                  libros_data = api_response.json()
                  return JsonResponse({"libros": libros_data})

              # Si la solicitud a la API principal falló
              else:
                  return JsonResponse({"error": "Error al obtener los datos de la API principal"}, status=api_response.status_code)

          # Si la solicitud para obtener el token de autenticación falló
          else:
              return JsonResponse({"error": "Error al autenticarse"}, status=response.status_code)

      except Exception as e:
          return JsonResponse({"error": str(e)}, status=500)
