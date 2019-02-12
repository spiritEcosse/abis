from api import views

from django.conf.urls import url

urlpatterns = [
    url(r'^person/verification/$', views.VerificationViews.as_view({'get': 'retrieve'})),
    url(r'^person/identification$', views.IdentificationViews.as_view({'get': 'list', 'post': 'post'})),
    url(r'^person/enroll/$', views.CreateViews.as_view({'get': 'retrieve', 'post': 'post'})),
    url(r'^person/enroll_xyt/$', views.CreateViews.as_view({'get': 'retrieve', 'post': 'post'})),
    url(r'^person/remove/$', views.DeleteViews.as_view()),
    url(r'^rnokpp/rejection/$', views.RnokppRejectionViews.as_view({'post': 'post'})),
    url(r'^rnokpp/info/$', views.RnokppRejectionViews.as_view({'post': 'post'})),
]
