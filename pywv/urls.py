from django.urls import path
from .views import  AddPostView,AddCommentView, AllPosts, DeletePostView, HomeView,ArticleDetailView, UpdatePostView
from . import views
#from django import views

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    
    path('allPosts',AllPosts.as_view(),name="allPosts"),
    

    path('article/<int:pk>',ArticleDetailView.as_view(),name='article-details'),
    
    path('add-post/',AddPostView.as_view(),name='add-post'),
        
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    
    path('article/<int:pk>/delete',DeletePostView.as_view(),name='delete_post'),
                
    path('article/<int:pk>/comment',AddCommentView.as_view(),name='add_comment'),
   
   
    path('', views.Home, name="home"),
    path('contactUs', views.ContactUs, name="contactUs"),
    path('aboutUs', views.AboutUs, name="aboutUs"),
    path('adoptAGirlsMonth', views.AdoptAGirlsMonth, name="adoptAGirlsMonth"),
    path('flourish', views.Flourish, name="flourish"),
    path('lbqSupport', views.LbqSupport, name="lbqSupport"),
    path('menstruation-health-and-mentorship-pywv', views.Mens, name="menstruation-health-and-mentorship-pywv"),
    path('pywv2022_2026StrategicPlan', views.Pywv2022_2026StrategicPlan, name="pywv2022_2026StrategicPlan"),
    path('resources', views.Resources, name="resources"),
    path('theTeam', views.TheTeam, name="theTeam"),
    path('whatWeDo', views.WhatWeDo, name="whatWeDo"),
    path('Donate', views.Donate, name="Donate"),
    
    path('LydiaOdipo', views.LydiaOdipo, name="LydiaOdipo"),
    path('AnneMugo', views.AnneMugo, name="AnneMugo"),
    path('BerylWafula', views.BerylWafula, name="BerylWafula"),
    path('ConsolataAkoth', views.ConsolataAkoth, name="ConsolataAkoth"),
    path('CynthiaKatanu', views.CynthiaKatanu, name="CynthiaKatanu"),
    path('EstherAoko', views.EstherAoko, name="EstherAoko"),
    path('FaheKerubo', views.FaheKerubo, name="FaheKerubo"),
    path('MercyWanjiko', views.MercyWanjiko, name="MercyWanjiko"),
    path('RisperSarota', views.RisperSarota, name="RisperSarota"),
    path('LucyNjenga', views.LucyNjenga, name="LucyNjenga"),
    path('Marylizz', views.Marylizz, name="Marylizz"),
    path('CynthiaBuchira', views.CynthiaBuchira, name="CynthiaBuchira"),
    path('SharonNyakundi', views.SharonNyakundi, name="SharonNyakundi"),
    path('Terry', views.Terry, name="Terry"),
    path('Lizz', views.Lizz, name="Lizz"),
    
    path('Scholarships', views.Scholarships, name="Scholarships"),
    path('Empowerment', views.Empowerment, name="Empowerment"),
    path('Healthcare', views.Healthcare, name="Healthcare"),
    path('Rights', views.Rights, name="Rights"),
    
    path('HIV-prevention-and-care-pywv', views.HIV, name="HIV-prevention-and-care-pywv"),
    path('mental-health-pywv', views.MentalHealth, name="mental-health-pywv"),
    
    path('prevention-and-ending-violence-against-women-and-girls', views.EndingViolence, name="prevention-and-ending-violence-against-women-and-girls"),
    path('gender-rights-promotion', views.GenderRights, name="gender-rights-promotion"),
    path('we-lead-project-pywv', views.WeLead, name="we-lead-project-pywv"),
    path('community-engagement', views.CommunityEngagement, name="community-engagement"),
    path('degital-media-advocacy', views.DigitalMedia, name="digital-media-advocacy"),
    
]
