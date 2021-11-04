from django.http import HttpResponse
from django.template import loader
from .forms import PhotoForm
from .models.test import Photo

def index(request):
    template=loader.get_template("deeporeilly/index.html")
    context={"form":PhotoForm()}
    return HttpResponse(template.render(context,request))

def predict(request):
    if not request.method=="POST":
        return redirect("deeporeilly:index")
    form=PhotoForm(request.POST,request.FILES)
    if not form.is_valid():
        raise ValueError("Formが不正です")

    photo=Photo(image=form.cleaned_data["image"])
    template=loader.get_template("deeporeilly/result.html")

    context={
        "photo_data":photo.image_src(),
    }
    return HttpResponse(template.render(context,request))