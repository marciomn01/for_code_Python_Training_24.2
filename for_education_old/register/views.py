from django.views.generic import *
from .models import RegisterClient
from django.urls import reverse_lazy


# Create your views here.


class Login(TemplateView):
    template_name = "register/login_templateview.html"


class RegisterCreate(CreateView):
    model = RegisterClient
    fields = ['name', 'email', 'phone', 'password']
    template_name = "register/register_form.html"
    success_url = reverse_lazy("login")




# def register(request):
#     return render(request, "pdi/register.html")

# def login(request):
#     return render(request, "pdi/login.html")

# def passwordchange(request):
#     return render(request, "pdi/passwordchange.html")

# def home(request):
#     todos = Todo.objects.all()
#     return render(request, "pdi/home.html", {"todos": todos})