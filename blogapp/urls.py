from django.urls import path
from .views import MainView, PostDetailView, SignUpView, SignInView, \
    FeedBackView, SuccessView, SearchResultView
from django.contrib.auth.views import LogoutView
from .views import sign_out


urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('blog/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', sign_out, name='signout'),
    path('contact/', FeedBackView.as_view(), name='contact'),
    path('contact/success/', SuccessView.as_view(), name='success'),
    path('search/', SearchResultView.as_view(), name='search_results'),
]
