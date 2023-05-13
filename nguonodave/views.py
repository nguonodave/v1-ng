from django.shortcuts import render
from placesOfWork.models import PlacesOfWork
from workExperience.models import WorkExperience
from about.models import About
from projects.models import Projects

def everthing(request):
    me = About.objects.get()

    projects = Projects.objects.all()

    firstPlaceOfWork = PlacesOfWork.objects.filter().first()
    otherPlacesOfWork = PlacesOfWork.objects.filter().order_by("created_date")[1:]

    firstExperience = WorkExperience.objects.filter().first()
    otherExperiences = WorkExperience.objects.filter().order_by("created_date")[1:]

    context = {
        "me": me,

        "projects" :projects,

        "firstPlaceOfWork": firstPlaceOfWork,
        "otherPlacesOfWork": otherPlacesOfWork,

        "firstExperience": firstExperience,
        "otherExperiences": otherExperiences,
    }
    return render(request, "portfolio/portfolio.html", context)




