from django.shortcuts import render

from profiles.models import Profile


def index(request):
    r"""Liste tous les profils.

    :param request: la rêquete HTTP.
    :type request: HttpRequest
    :return: La réponse HTTP qui contient le template profiles/index.html
    :rtype: HttpResponse
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    r"""Liste un seul profil.

    :param request: la rêquete HTTP.
    :param username: le username
    :type request: HttpRequest
    :type username: str
    :return: La réponse HTTP qui contient le template profiles/profile.html
    :rtype: HttpResponse
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
