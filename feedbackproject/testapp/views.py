from django.shortcuts import render
from . import forms

# Create your views here.
def feedbackview(request):
    form=forms.FeedbackForm()
    my_dict={'form': form}
    if request.method == "POST":
        form=forms.FeedbackForm(request.POST)
    if form.is_valid():
        print ('Form validation sucess and priniting feedback info')
        print ('Student name:', form.cleaned_data['name'])
        print ('Student roll no:', form.cleaned_data['rollno'])
        print ('Student mail id:' ,form.cleaned_data['email'])
        print ('Student Feedback:', form.cleaned_data['feedback'])
        return render(request,'testapp/thanks.html',{'name':form.cleaned_data['name']})

    return render(request,'testapp/feedback.html', context=my_dict)
