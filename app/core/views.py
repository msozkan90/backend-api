from django.http import JsonResponse


def hello_page(request):
    """
    View function to return a JSON response with a welcome message.

    Args:
        request: HTTP request object.

    Returns:
        JsonResponse: JSON response with a welcome message.
    """
    response_data = {'message': 'Hello, welcome to my API.'}
    return JsonResponse(response_data)


def not_found_json_response(request, unrecognized_path):
    """
    View function to return a JSON response for a 404 Not Found error.

    Args:
        request: HTTP request object.
        unrecognized_path (str): The unrecognized path that triggered the 404 error.

    Returns:
        JsonResponse: JSON response indicating a 404 Not Found error.
    """
    response_data = {'detail': '404 Not found.'}
    return JsonResponse(response_data, status=404)
