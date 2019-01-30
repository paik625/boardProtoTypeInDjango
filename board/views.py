from django.shortcuts import render
from django.views.generic import DetailView
from .forms import *
from .models import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
class BOARDList(ListView):
    model = BOARD
    paginate_by = 10

class BOARDCreate(CreateView):
    model = BOARD
    fields = ['title', 'author', 'content']
    success_url = reverse_lazy('board:board_list')
    template_name_suffix = '_create'


class BOARDUpdate(UpdateView):
    model = BOARD
    fields = ['title', 'author', 'content']
    template_name_suffix = '_update'
    success_url = reverse_lazy('board:board_list')
    success_url = reverse_lazy('board:board_list')


class BOARDDelete(DeleteView):
    model = BOARD
    template_name_suffix = '_delete'
    success_url = reverse_lazy('board:board_list')


class BOARDDetail(DetailView):
    model = BOARD
#
# def create(request):
#
#     if request.method == 'POST':
#         board_form = createForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(user_form.cleaned_data['password'])
#             new_user.save()
#             return render(request, 'registration/register_done.html', {'new_user':new_user})
#     else:
#         board_form = RegisterForm()
#
#     return render(request, 'registration/r