from django.http import HttpResponseRedirect


class RedirectDomainMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.META['HTTP_HOST'].endswith('help.datahub.trade.gov.uk'):
            return HttpResponseRedirect('https://help.datahub.trade.gov.uk' + request.path)

        response = self.get_response(request)

        return response
