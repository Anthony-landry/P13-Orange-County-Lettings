from django.shortcuts import render
from lettings.models import Letting


def index(request):
    r"""Fonction qui permet de rendre le template lettings/index.hmtl, page d'accueile oc_letting.

    :param request: la rêquete HTTP.
    :type request: HttpRequest
    :return: La réponse HTTP qui contient le template lettings/index.html
    :rtype: HttpResponse
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    r"""Fonction qui permet de rendre le template.

    :param request: la rêquete HTTP.
    :param letting_id: id de l'objet letting concerné.
    :type request: HttpRequest
    :type letting_id: int
    :return: La réponse HTTP qui contient le template letting.html
    :rtype: HttpResponse
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
