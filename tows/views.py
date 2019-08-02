from django.shortcuts import render
from tows.models import Crane, Pilot, Assignment
from django.views import generic
from django.shortcuts import HttpResponseRedirect, reverse, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def show(request):
    num_cranes = Crane.objects.all().count()
    num_pilots = Pilot.objects.count()
    num_assignments = Assignment.objects.all().count()
    num_assignments_available = Assignment.objects.filter(status__exact='A').count()

    context = {
        'num_cranes': num_cranes,
        'num_pilots': num_pilots,
        'num_assignments': num_assignments,
        'num_assignments_available': num_assignments_available,
    }
    return render(request, 'tows/page.html', context=context)


def show_available(request):
    template = 'tows/show-available.html'
    available_list = Assignment.objects.filter(status__exact='A')
    page = request.GET.get('page', 1)

    paginator = Paginator(available_list, 10)
    try:
        available = paginator.page(page)
    except PageNotAnInteger:
        available = paginator.page(1)
    except EmptyPage:
        available = paginator.page(paginator.num_pages)

    return render(request, template, {'available': available})

    """
    context = {
        'assignment_available': Assignment.objects.filter(status__exact='A')
    }"""


class AssignmentListView(generic.ListView):
    model = Assignment
    paginate_by = 10


def create_crane_form(request):
    template = 'tows/create_crane_form.html'
    return render(request, template)


def confirm_create_crane(request):
    if request.method == 'POST':
        new_crane = Crane(
            license_plate=request.POST['license_plate'],
            trademark=request.POST['trademark'],
            year=request.POST['year'],
            characteristic=request.POST['characteristic'],
        )
        new_crane.save()

        return HttpResponseRedirect(reverse('tows:page'))
    return HttpResponse('No se puede guardar')


def create_pilot_form(request):
    template = 'tows/create_pilot_form.html'
    return render(request, template)


def confirm_create_pilot(request):
    if request.method == 'POST':
        new_pilot = Pilot(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            DPI=request.POST['DPI'],
        )
        new_pilot.save()

        return HttpResponseRedirect(reverse('tows:page'))
    return HttpResponse('No se puede guardar')


def create_assignment_form(request):
    template = 'tows/assignment_form.html'
    context = {
        'pilots': Pilot.objects.all(),
        'cranes': Crane.objects.all(),
    }
    return render(request, template, context)

    
def confirm_create_assignment(request):
    if request.method == 'POST':
        post_pilot = Pilot.objects.get(pk=request.POST['pilot'])
        post_crane = Crane.objects.get(pk=request.POST['crane'])
        new_assignment = Assignment(
            status=request.POST['status'],
            start_time=request.POST['start_time'],
            pilot_assigned=post_pilot,
            crane_assigned=post_crane,
        )
        new_assignment.save()

        return HttpResponseRedirect(reverse('tows:page'))
    return HttpResponse('No se puede guardar')


def delete_assignment(request, assignment_id):
    deleted_assignment = Assignment.objects.get(id=assignment_id)
    deleted_assignment.delete()

    return HttpResponseRedirect(reverse('tows:show-assignments'))


def delete_available_assignment(request, available_id):
    deleted_available_assignment = Assignment.objects.get(id=available_id)
    deleted_available_assignment.delete()

    return HttpResponseRedirect(reverse('tows:show-available'))
