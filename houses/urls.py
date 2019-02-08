# from django.urls import path
# from houses import views

# urlpatterns = [
#     path('houses/', views.house_list),
#     path('houses/<int:pk>/', views.house_detail),
# ]

# -- --
# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from houses import views

# urlpatterns = [
#     path('houses/', views.house_list),
#     path('houses/<int:pk>', views.house_detail),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)


# -- For Class-based Views --
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from houses import views

urlpatterns = [
    path('houses/', views.HouseList.as_view()),
    path('houses/<int:pk>/', views.HouseDetail.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
