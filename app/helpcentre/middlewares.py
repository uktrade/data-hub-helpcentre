from django.http import HttpResponseRedirect


class RedirectDomainMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.META['HTTP_HOST'].endswith('datahub-helpcentre.london.cloudapps.digital'):
            return HttpResponseRedirect('https://help.datahub.trade.gov.uk' + request.path)

        response = self.get_response(request)

        return response
