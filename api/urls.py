from django.urls import path, include
from api.models import CourseResource, CategoryResourse
from tastypie.api import Api

api = Api(api_name='v1')
course_resourse = CourseResource()
category_resourse = CategoryResourse()

api.register(course_resourse)
api.register(category_resourse)

urlpatterns = [
    path('', include(api.urls), name='index')
]