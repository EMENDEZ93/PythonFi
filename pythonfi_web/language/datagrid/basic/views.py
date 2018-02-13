from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from pythonfi_web.language.eg.forms import AjaxCrudForm
from pythonfi_web.language.models import Language


def basic(request, templane_name='admin/admin_fi/datagrid/basic/basic.html'):
    data = {}
    data['lenguajes']= Language.objects.all()
    return render(request, templane_name, data)


def basic_update(request):
    data = dict()
    pk = request.POST['id']

    language = get_object_or_404(Language, pk=pk)

    if request.method == 'POST':
        form = AjaxCrudForm(request.POST, instance=language)
    else:
        form = AjaxCrudForm(instance=language)

    data['res'] = pk
    return JsonResponse(data)

