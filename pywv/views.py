from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from .models import  Post,Comment
from .forms import PostForm,CommentForm
from django.core.mail import send_mail
from django.conf import settings


class HomeView(ListView):
    model= Post
    template_name='home.html'
    ordering=['-id']
    
    def get_context_data(self,*args, **kwargs):
        context=super(HomeView,self).get_context_data(*args, **kwargs)
        return context
   
class ArticleDetailView(DetailView):
    model=Post
    template_name= 'article_details.html'
    
    def get_context_data(self,*args, **kwargs):
        context=super(ArticleDetailView,self).get_context_data(*args, **kwargs)
        
        return context
    
class AddPostView(CreateView):
    model= Post
    form_class=PostForm
    template_name='addPost.html'
    
   
class AddCommentView(CreateView):
    model= Comment
    form_class=CommentForm
    template_name='add_comment.html'
    success_url=reverse_lazy('home')
    
    def form_valid(self,form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
   
class UpdatePostView(UpdateView):
    model=Post
    form_class=PostForm
    template_name='update_post.html'
    #fields=['title','title_tag','body']
    
class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('allPosts')
 
 

def Home(request):
        return render(request, "home.html")

class AllPosts(ListView):
    model= Post
    template_name='allPosts.html'
    ordering=['-id']
    
    def get_context_data(self,*args, **kwargs):
        context=super(AllPosts,self).get_context_data(*args, **kwargs)
        return context

def ContactUs(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phoneNumber = request.POST['phone']
        message = request.POST['message']

        # send mail
        send_mail(
            "Contact form submission at pywv.org",  # subject
            message + "\n" "\n" "\n" "Name : " + name + "\n" "Phone number : " + phoneNumber + "\n" "Email : " + email,  # message
            'info@pywv.org',  # from email
            ['info@pywv.org'],  # to email
        )
        return render(request, "contactUs.html", {
            "name": name
        })
    else:
        return render(request, "contactUs.html")

    
def AboutUs(request):
        return render(request, "aboutUs.html")

def AdoptAGirlsMonth(request):
        return render(request, "adoptAGirlsMonth.html")
    
def Flourish(request):
        return render(request, "flourish.html")
    
def LbqSupport(request):
        return render(request, "lbqSupport.html")
    
def Mens(request):
        return render(request, "mens.html")
    
def Pywv2022_2026StrategicPlan(request):
        return render(request, "pywv2022-2026StrategicPlan.html")
    
def Resources(request):
        return render(request, "resources.html")
    
def TheTeam(request):
        return render(request, "theTeam.html")

def LydiaOdipo(request):
        return render(request, "lydiaOdipo.html")

def AnneMugo(request):
        return render(request, "anneMugo.html")

def BerylWafula(request):
        return render(request, "berylWafula.html")

def ConsolataAkoth(request):
        return render(request, "consolataAkoth.html")

def CynthiaKatanu(request):
        return render(request, "CynthiaKatanu.html")

def EstherAoko(request):
        return render(request, "EstherAoko.html")

def FaheKerubo(request):
        return render(request, "FaheKerubo.html")

def MercyWanjiko(request):
        return render(request, "MercyWanjiko.html")

def RisperSarota(request):
        return render(request, "RisperSarota.html")

def LucyNjenga(request):
        return render(request, "lucyNjenga.html")

def Marylizz(request):
        return render(request, "marylizz.html")

def CynthiaBuchira(request):
        return render(request, "cynthiaBuchira.html")

def SharonNyakundi(request):
        return render(request, "sharonNyakundi.html")

def Terry(request):
        return render(request, "terry.html")

def Lizz(request):
        return render(request, "lizz.html")
    
def WhatWeDo(request):
        return render(request, "whatWeDo.html")

def Donate(request):
        return render(request, "donationPage.html")

def Scholarships(request):
        return render(request, "scholarships.html")

def Empowerment(request):
        return render(request, "empowerment.html")
    
def Healthcare(request):
        return render(request, "healthcare.html")

def Rights(request):
        return render(request, "rights.html")

def HIV(request):
        return render(request, "hivPrevention.html")
def MentalHealth(request):
        return render(request, "mentalHealth.html")
def DigitalMedia(request):
        return render(request, "digitalMedia.html")


    
def EndingViolence(request):
        return render(request, "endingViolence.html")
def GenderRights(request):
        return render(request, "genderRights.html")
def WeLead(request):
        return render(request, "weLead.html")
def CommunityEngagement(request):
        return render(request, "communityEngagement.html")