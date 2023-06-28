from django.utils.translation import activate

class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language = request.POST.get('language')
        if language in ['en', 'es']:
            request.session['language'] = language
        else:
            language = request.session.get('language', 'en')
        activate(language)
        response = self.get_response(request)
        return response