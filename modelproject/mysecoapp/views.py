from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from mysecoapp.models import Student

# Create your views here.
# Testing case exercise
def raj_view(request):
    #my_dict={"head":"rajaiah"}
    return render(request,"index.html")

def test_view(request):
    my_student=Student.objects.all().values()
    template=loader.get_template("student.html")
    context={"my_student":my_student}
    return HttpResponse(template.render(context,request))


