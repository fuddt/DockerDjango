from django.shortcuts import render

# Create your views here.

def before_form(request):
    params = {
        'title': "Let's use Form",
        'msg':'what your name?'
    }
    return render(request, 'form/form.html', params)


def after_form(request):
    get_msg = request.POST['msg']
    params = {
        'title': "Let's use Form",
        'msg':'Hello!' + get_msg + '. Success!'
    }
    return render(request, 'form/form.html', params)
