from tastypie.resources import ModelResource
from shop.models import Category, Course

class CategoryResourse(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resourse_name = 'categories'
        allowed_methods = ['get']

class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resourse_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']