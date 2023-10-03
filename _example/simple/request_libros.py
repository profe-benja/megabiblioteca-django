import requests
from django.http import JsonResponse
from django.views import View

class LibrosView(View):
    def get(self, request, *args, **kwargs):
        # URL de la API principal
        api_url = "http://127.0.0.1:8000/api/v1/libro/?format=json"

        try:
            # Realizar una solicitud GET a la API principal
            response = requests.get(api_url)

            # Verificar si la solicitud fue exitosa
            if response.status_code == 200:
                libros_data = response.json()
                return JsonResponse({"libros": libros_data})

            # Si la solicitud a la API principal falló
            else:
                return JsonResponse({"error": "Error al obtener los datos de la API principal"}, status=response.status_code)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
