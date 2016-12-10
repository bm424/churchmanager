from django.views.generic import DetailView, ListView

from .models import Church


def grouped(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]


class ChurchDetail(DetailView):

    model = Church


class ChurchList(ListView):

    model = Church

    def get_context_data(self, *args, **kwargs):
        context = super(ListView, self).get_context_data(*args, **kwargs)
        context['church_groups'] = grouped(context['church_list'], 3)
        return context
