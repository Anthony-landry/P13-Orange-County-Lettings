from django.shortcuts import render


def index(request):
    r"""Fonction qui permet de rendre le template oc_lettings_site/index.hmtl,
    page d'accueile oc_letting.

    :param request: la rêquete HTTP.
    :type request: HttpRequest
    :return: La réponse HTTP qui contient le template oc_lettings_site/index.html
    :rtype: HttpResponse.
    """
    return render(request, 'oc_lettings_site/index.html')


def error404(request, exception):
    r"""Fonction qui permet de rendre le template index.hmtl,
    page d'accueile oc_lettings_site/error404.html.

    :param request: la rêquete HTTP.
    :param exception: parametre requis par handler404.
    :type request: HttpRequest
    :type exception: Exception
    :return: La réponse HTTP qui contient le template index.html
    :rtype: HttpResponse
    """
    response = render(request, 'oc_lettings_site/error404.html')

    response.status_code = 404

    return response


def error500(request):
    r"""Fonction qui permet de rendre le template index.hmtl,
    page d'accueile oc_lettings_site/error500.html.

    :param request: la rêquete HTTP.
    :type request: HttpRequest
    :return: La réponse HTTP qui contient le template index.html
    :rtype: HttpResponse
    """
    response = render(request, 'oc_lettings_site/error500.html')

    response.status_code = 500

    return response
