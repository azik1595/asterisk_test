from cb.forms import CallBackForm
from django.views.generic.edit import FormView
from django.http import HttpResponse
from cb.ami import ConnectToAsterisk
# Create your views here.

class CallBackView(FormView):
    template_name = 'cb.html'
    form_class = CallBackForm
    success_url = '/cb1/'

    def post(self, request):
        ConnectToAsterisk(number=request.POST['phone'])
        return HttpResponse('accept call to %s' % request.POST['phone'])

    def form_valid(self, form):
        return super(CallBackForm, self).form_valid(form)