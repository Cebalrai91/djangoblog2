from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import *
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.shortcuts import render, redirect



# class Image(TemplateView):
#     form = HotelForm
#     template_name = 'blog/image.html'
#
#     def post(self, request, *args, **kwargs):
#         form = HotelForm(request.POST, request.FILES)
#         if form.is_valid():
#             obj = form.save()
#             return HttpResponseRedirect(reverse_lazy('image_display', kwargs={'pk': obj.id}))
#
#         context = self.get_context_data(form=form)
#         return self.render_to_response(context)
#
#     def get(self,request, *args, **kwargs):
#         return self.post(request,*args,**kwargs)
#
#
# class ImageDisplay(DetailView):
#     model = Post
#     template_name = 'blog/image_display.html'
#     context_object_name = 'image'


def hotel_image_view(request):

    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
        return render(request, 'blog/image.html', {'form': form})

# Python program to view
# for displaying images


def display_hotel_images(request):

    if request.method == 'GET':

        Hotels = Hotel.objects.all()
        return render(request, 'blog/display_hotel_images.html',{'hotel_images': Hotels})




def success(request):
    return HttpResponse('successfully uploaded')


def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by("publish_date")
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def error_404_view(request,exception):
    data={"name": 'Blog dla programistów'}
    return render(request,'blog/404.html',data)

