from django.http import HttpResponseRedirect


# redirect requests from datahub-helpcentre.london.cloudapps.digital to help.datahub.trade.gov.uk, except API calls
class RedirectDomainMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.META['HTTP_HOST'].endswith('datahub-helpcentre.london.cloudapps.digital') \
                and not request.path.startswith('/api/'):
            return HttpResponseRedirect('https://help.datahub.trade.gov.uk' + request.path)

        if request.META['HTTP_HOST'].endswith('data-services-helpcentre.london.cloudapps.digital') \
                and not request.path.startswith('/api/'):
            return HttpResponseRedirect('https://data-services-help.trade.gov.uk' + request.path)

        response = self.get_response(request)

        return response
