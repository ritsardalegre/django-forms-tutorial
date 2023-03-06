from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .forms import ReviewForm
from .models import Review
# Create your views here.





# #Accessing forms using "View"
# # CLASS-BASED views https://docs.djangoproject.com/en/4.1/topics/class-based-views/intro/
# class ReviewView(View):
#     def get(self, request):

#         form = ReviewForm()

#         return render(request, "reviews_app/review.html", {
#             'form': form
#         })

#     def post(self, request):
#         form = ReviewForm(request.POST)

#         if form.is_valid():

#             # review = Review(
#             #     user_name = form.cleaned_data['user_name'],
#             #     review_text = form.cleaned_data['review_text'],
#             #     rating = form.cleaned_data['rating']
#             #     )
#             # review.save()

#             form.save() #using Modelform
#             return HttpResponseRedirect("/thank-you")

#         return render(request, "reviews_app/review.html", {
#             'form': form
#         })


#Normal way to connect with FORM and models

# def review(request):
#     if request.method == 'POST':

#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             # review = Review(
#             #     user_name = form.cleaned_data['user_name'],
#             #     review_text = form.cleaned_data['review_text'],
#             #     rating = form.cleaned_data['rating']
#             #     )
#             # review.save()

#             form.save() #using Modelform
#             return HttpResponseRedirect("/thank-you")
    
#     else:
#         form = ReviewForm()

#     return render(request, "reviews_app/review.html", {
#         'form': form
#     })


#Using  "FormView" to handle form
class ReviewView(FormView):
    form_class = ReviewForm #Accessing Form in forms.py
    template_name = "reviews_app/review.html" #Adding template_name where review.html
    success_url = "/thank-you" #redirecting when  form submission is successful

    def form_valid(self, form): #checking if form is valid
        form.save()             #saving details that have been posted
        return super().form_valid(form) 

    #~~~~~~~~~~~~~~~~~~~~~~~~~ no need get()
    # def get(self, request):

    #     form = ReviewForm()

    #     return render(request, "reviews_app/review.html", {
    #         'form': form
    #     })
    #~~~~~~~~~~~~~~~~~~~~~~~~~~ Django automatic handles post() or posting
    # def post(self, request):
    #     form = ReviewForm(request.POST)

    #     if form.is_valid():

    #         # review = Review(
    #         #     user_name = form.cleaned_data['user_name'],
    #         #     review_text = form.cleaned_data['review_text'],
    #         #     rating = form.cleaned_data['rating']
    #         #     )
    #         # review.save()

    #         form.save() #using Modelform
    #         return HttpResponseRedirect("/thank-you")

    #     return render(request, "reviews_app/review.html", {
    #         'form': form
    #     })

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Class-base view TemplateView

# def thankyou(request):
#     return render(request, "reviews_app/thank_you.html")

#code above converted to Class-base views
# class ThankyouView(View):
#     def get(self,request):
#         return render(request, "reviews_app/thank_you.html")

class ThankyouView(TemplateView):
    template_name = "reviews_app/thank_you.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message']= "This Works!"
        return context



###~~~~~~~~~~~~~~~~~~Fetching Items in database using TemplateView

# class ReviewsListView(TemplateView):
#     template_name = "reviews_app/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] =  reviews
#         return context

###~~~~~~~~~~~~~~~~~~Fetching a list of data or Items in database using ListView
class ReviewsListView(ListView):
    template_name = "reviews_app/review_list.html"
    model = Review #you can access the model by using "object_list"
    context_object_name = "reviews" #changing "object_list" to "reviews"
    

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gte=4)
        return data


###~~~~~~~~~~~~~~~~~~Fetching datas in database using Template View
# class SingleReviewView(TemplateView):
#     template_name = "reviews_app/single_review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
        
#         context["review"] = selected_review
#         return context
    

###~~~~~~~~~~~~~~~~~~Fetching single items or data in database using DetailView
class SingleReviewView(DetailView):
    template_name = "reviews_app/single_review.html"
    model = Review




