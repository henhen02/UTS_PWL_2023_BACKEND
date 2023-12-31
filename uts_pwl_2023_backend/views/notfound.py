from pyramid.view import notfound_view_config


@notfound_view_config(renderer='uts_pwl_2023_backend:templates/404.pt')
def notfound_view(request):
    request.response.status = 404
    return {}
