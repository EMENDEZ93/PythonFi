from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from pythonfi_web.language.eg.forms import AjaxCrudForm
from pythonfi_web.language.models import Language



def ajax_crud(request):
    language = Language.objects.all()
    return render(request,'admin/admin_fi/eg/ajax_crud/ajax_crud.html', {'language':language})


def ajax_crud_save_lenguage_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            language = Language.objects.all()
            data['html_book_list'] = render_to_string('admin/admin_fi/eg/ajax_crud/ajax_crud_list.html', {'language':language})
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name,context,request,)
    return JsonResponse(data)


def ajax_crud_create(request):
    if request.method == 'POST':
        form = AjaxCrudForm(request.POST)
    else:
        form = AjaxCrudForm()

    return ajax_crud_save_lenguage_form(request, form, 'admin/admin_fi/eg/ajax_crud/ajax_crud_create.html')


def ajax_crud_update(request, pk):
    language = get_object_or_404(Language, pk=pk)
    if request.method == 'POST':
        form = AjaxCrudForm(request.POST, instance=language)
    else:
        form = AjaxCrudForm(instance=language)

    return ajax_crud_save_lenguage_form(request, form, 'admin/admin_fi/eg/ajax_crud/ajax_crud_update.html')


def ajax_crud_delete(request, pk):
    lan = get_object_or_404(Language, pk=pk)
    data = dict()
    if request.method == 'POST':
        lan.delete()
        data['form_is_valid'] = True
        language = Language.objects.all()
        data['html_book_list'] = render_to_string('admin/admin_fi/eg/ajax_crud/ajax_crud_list.html', {'language': language})
    else:
        context = {'book':lan}
        data['html_form'] = render_to_string('admin/admin_fi/eg/ajax_crud/ajax_crud_delete.html', context, request=request)

    return JsonResponse(data)
