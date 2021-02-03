from django.shortcuts import render
from django.http import HttpResponse
from . models import mentors,m_team,main_project,related_project,all_research,all_blog,contact
# Create your views here.
def start_(request):
    details=mentors.objects.all()
    m_details=m_team.objects.all()
    p_details=main_project.objects.all()
    r_details=related_project.objects.all()
    a_research=all_research.objects.all()
    a_blog=all_blog.objects.all()
    return render(request,'index.html',{'details':details,'m_details':m_details,'p_details':p_details,'r_details':r_details,'all_research':a_research,'all_blogs':a_blog})

def contact_form(request):
    form_detail={}
    form_detail['name']=request.POST.get('name','Visitor')
    form_detail['email']=request.POST.get('email','off')
    form_detail['subject']=request.POST.get('subject','Nothing to show!!!')
    form_detail['message']=request.POST.get('message','off')
    user=contact(name=form_detail['name'],email=form_detail['email'],subject=form_detail['subject'],description=form_detail['message'])
    user.save()
    return render(request,'contact.html',{'form_detail':form_detail})

def blog_detail(request,myid):
    string_of_request=request
    page_section=str(string_of_request).split('/')[1]
    if page_section=='project':
        blog = main_project.objects.filter(number=myid)
        return render(request,'blog.html',{'blog': blog[0] })
    elif page_section=='blog':
        blog = all_blog.objects.filter(number=myid)
        return render(request,'blog.html',{'blog': blog[0] })
    elif page_section=='r_project':
        blog = related_project.objects.filter(number=myid)
        return render(request,'blog.html',{'blog': blog[0] })
    elif page_section=='research':
        blog = all_research.objects.filter(number=myid)
        return render(request,'blog.html',{'blog': blog[0]})

