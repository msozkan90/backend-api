from django.http import JsonResponse


def not_found_json_response(request, unrecognized_path):
    response_data = {'detail': '404 Not found.'}
    return JsonResponse(response_data, status=404)
