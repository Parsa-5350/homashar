from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *


# صفحه اصلی 
def home(request):
    return render(request, 'index.html')

#صفحه ادمین شهردار 
def home2(request):
    return render(request, 'index2.html')

# صفخه شهیدها 
def martyr_page(request):
    return render(request, 'martyr.html')

# صفحه شهردار 
def shahrdar(request):
    return render(request, 'shahrdar.html')

# صفخه شورا 
def shora(request):
    return render(request, 'shora.html')


# فرم ها: 
# -------------------------------------start-------------------------------------

# فرم تاریخچه 
def history(request):
    if request.method == 'POST':
        user = formHistory(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formHistory()

    return render(request, 'form-history.html', {'form':user})


# فرم اخبار 
def news(request):
    if request.method == 'POST':
        user = formNews(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formNews()

    return render(request, 'form-news.html', {'form':user})


# فرم پروژه ها 
def project(request):
    if request.method == 'POST':
        user = formProject(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formProject()

    return render(request, 'form-projects.html', {'form':user})


# فرم شوراها 
def councils(request):
    if request.method == 'POST':
        user = formCouncils(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formCouncils()

    return render(request, 'form-councils.html', {'form':user})


# فرم شهردار 
def mayor(request):
    if request.method == 'POST':
        user = formMayor(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formMayor()

    return render(request, 'form-mayor.html', {'form':user})


# فرم مشاهیر 
def celebrities(request):
    if request.method == 'POST':
        user = formCelebrities(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formCelebrities()

    return render(request, 'form-celebrities.html', {'form':user})


# فرم شهیدها 
def martyrs(request):
    if request.method == 'POST':
        user = formMartyrs(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formMartyrs()

    return render(request, 'form-martyrs.html', {'form':user})


# فرم پرسنل 
def personnel(request):
    if request.method == 'POST':
        user = formPersonnel(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formPersonnel()

    return render(request, 'form-personnel.html', {'form':user})


# فرم مشخصات هماشهر 
def municipality(request):
    if request.method == 'POST':
        user = formMunicipality(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formMunicipality()

    return render(request, 'form-municipality-info.html', {'form':user})

# -------------------------------------end-------------------------------------



# لیست ها: 
# -------------------------------------start-------------------------------------

# لیست مشاهیر 
def list_celebrities(request):
    return render(request,'list-celebrities.html')

# لیست تاریخچه ها 
def list_history(request):
    return render(request,'list-history.html')

# لیست شهردار 
def list_mayor(request):
    return render(request,'list-mayor.html')

# لیست مشخصات هماشهر 
def list_municipality(request):
    return render(request,'list-municipality-info.html')

# لیست پرسنل 
def list_personnel(request):
    return render(request,'list-personnel.html')

# لیست پروژه ها 
def list_project(request):
    return render(request,'list-project.html')

# لیست شوراها 
def list_councils(request):
    return render(request,'list-councils.html')

# لیست خبرها 
def list_news(request):
    return render(request,'list-news.html')

# لیست شهیدها 
def list_martyrs(request):
    return render(request,'list-martyrs.html')

# -------------------------------------end-------------------------------------



def history_delete(request,id):
    item=History.objects.get(id=id)
    item.delete()
    return render(request,'list-history.html',{'item':item})


def news_delete(request,id):
    item=News.objects.get(id=id)
    item.delete()
    return render(request,'list-news.html',{'item':item})    

                               
def project_delete(request,id):
    item=Project.objects.get(id=id)
    item.delete()
    return render(request,'list-project.html',{'item':item})


def councils_delete(request,id):
    item=Councils.objects.get(id=id)
    item.delete()
    return render(request,'list-councils.html',{'item':item})


def mayor_delete(request,id):
    item=Mayor.objects.get(id=id)
    item.delete()
    return render(request,'list-mayor.html',{'item':item})


def celebrities_delete(request,id):
    item=Celebrities.objects.get(id=id)
    item.delete()
    return render(request,'list-celebrities.html',{'item':item}) 


def martyrs_delete(request,id):
    item=Martyrs.objects.get(id=id)
    item.delete()
    return render(request,'list-martyrs.html',{'item':item})  


def personnel_delete(request,id):
    item=Personnel.objects.get(id=id)
    item.delete()
    return render(request,'list-personnel.html',{'item':item}) 


def municipality_delete(request,id):
    item=Municipality.objects.get(id=id)
    item.delete()
    return render(request,'list-municipality.html',{'item':item})    








def history_form(request,id):
    if request.method == 'POST':
        user = formHistory(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formHistory()
    item=History.objects.get(id=id)
    return render(request,'list-history.html',{'item':item})


def councils_form(request,id):
    if request.method == 'POST':
        user = formCouncils(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formCouncils()
    item=Councils.objects.get(id=id)
    return render(request,'list-councils.html',{'item':item})


def news_form(request,id):
    if request.method == 'POST':
        user = formNews(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formNews()
    item=News.objects.get(id=id)
    return render(request,'list-news.html',{'item':item})


def project_form(request,id):
    if request.method == 'POST':
        user = formProject(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formProject()
    item=Project.objects.get(id=id)
    return render(request,'list-project.html',{'item':item})


def mayor_form(request,id):
    if request.method == 'POST':
        user = formMayor(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formMayor()
    item=Mayor.objects.get(id=id)
    return render(request,'list-mayor.html',{'item':item})


def celebrities_form(request,id):
    if request.method == 'POST':
        user = formCelebrities(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formCelebrities()
    item=Celebrities.objects.get(id=id)
    return render(request,'list-celebrities.html',{'item':item})

def martyrs_form(request,id):
    if request.method == 'POST':
        user = formMartyrs(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formMartyrs()
    item=Martyrs.objects.get(id=id)
    return render(request,'list-martyrs.html',{'item':item})


def personnel_form(request,id):
    if request.method == 'POST':
        user = formPersonnel(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formPersonnel()
    item=Personnel.objects.get(id=id)
    return render(request,'list-personnel.html',{'item':item})


def municipality_form(request,id):
    if request.method == 'POST':
        user = formMunicipality(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formMunicipality()
    item=Municipality.objects.get(id=id)
    return render(request,'list-municipality-info.html',{'item':item})




# فرم تاریخچه 
def history(request):
    if request.method == 'POST':
        user = formHistory(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formHistory()

    return render(request, 'form-history.html', {'form':user})


# فرم اخبار 
def news(request):
    if request.method == 'POST':
        user = formNews(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formNews()

    return render(request, 'form-news.html', {'form':user})


# فرم پروژه ها 
def project(request):
    if request.method == 'POST':
        user = formProject(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formProject()

    return render(request, 'form-projects.html', {'form':user})


# فرم شوراها 
def councils(request):
    if request.method == 'POST':
        user = formCouncils(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formCouncils()

    return render(request, 'form-councils.html', {'form':user})


# فرم شهردار 
def mayor(request):
    if request.method == 'POST':
        user = formMayor(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formMayor()

    return render(request, 'form-mayor.html', {'form':user})


# فرم مشاهیر 
def celebrities(request):
    if request.method == 'POST':
        user = formCelebrities(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formCelebrities()

    return render(request, 'form-celebrities.html', {'form':user})


# فرم شهیدها 
def martyrs(request):
    if request.method == 'POST':
        user = formMartyrs(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formMartyrs()

    return render(request, 'form-martyrs.html', {'form':user})


# فرم پرسنل 
def personnel(request):
    if request.method == 'POST':
        user = formPersonnel(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formPersonnel()

    return render(request, 'form-personnel.html', {'form':user})


# فرم مشخصات هماشهر 
def municipality(request):
    if request.method == 'POST':
        user = formMunicipality(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formMunicipality()

    return render(request, 'form-municipality-info.html', {'form':user})









def detail_form(requset,item_id):
    product=History.objects.get(id=item_id)
    
    if requset.method == 'POST':
        user = formMartyrs(requset.POST,instance=product)
        if user.is_valid():
            user.save()
            messages.success(requset, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formMartyrs(instance=product)

    return render(requset,'list-history.html',{'index':product})


def detail1_form(requset,item_id):
    product=News.objects.get(id=item_id)
    
    if requset.method == 'POST':
        user = formNews(requset.POST,instance=product)
        if user.is_valid():
            user.save()
            messages.success(requset, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formNews(instance=product)

    return render(requset,'list-news.html',{'index':product})


def detail2_form(requset,item_id):
    product=Project.objects.get(id=item_id)
    if requset.method == 'POST':
        user = formProject(requset.POST,instance=product)
        if user.is_valid():
            user.save()
            messages.success(requset, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formProject(instance=product)
    return render(requset,'list-project.html',{'index':product})


def detail3_form(requset,item_id):
    product=Councils.objects.get(id=item_id)
    if requset.method == 'POST':
        user = formCouncils(requset.POST,instance=product)
        if user.is_valid():
            user.save()
            messages.success(requset, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formCouncils(instance=product)

    return render(requset,'list-councils.html',{'index':product})


def detail4_form(requset,item_id):
    product=Mayor.objects.get(id=item_id)
    if requset.method == 'POST':
        user = formMayor(requset.POST,instance=product)
        if user.is_valid():
            user.save()
            messages.success(requset, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formMayor(instance=product)
    return render(requset,'list-mayor.html',{'index':product})


def detail5_form(requset,item_id):
    product=Celebrities.objects.get(id=item_id)
    if requset.method == 'POST':
        user = formCelebrities(requset.POST,instance=product)
        if user.is_valid():
            user.save()
            messages.success(requset, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formCelebrities(instance=product)
    return render(requset,'list-celebrities.html',{'index':product})


def detail6_form(requset,item_id):
    product=Martyrs.objects.get(id=item_id)
    if requset.method == 'POST':
        user = formMartyrs(requset.POST,instance=product)
        if user.is_valid():
            user.save()
            messages.success(requset, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formMartyrs(instance=product)
    return render(requset,'list-martyrs.html',{'index':product})


def detail7_form(requset,item_id):
    product=Personnel.objects.get(id=item_id)
    if requset.method == 'POST':
        user = formPersonnel(requset.POST,instance=product)
        if user.is_valid():
            user.save()
            messages.success(requset, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formPersonnel(instance=product)
    return render(requset,'list-personnel.html',{'index':product})



def detail8_form(requset,item_id):
    product=Municipality.objects.get(id=item_id)
    if requset.method == 'POST':
        user = formMunicipality(requset.POST,instance=product)
        if user.is_valid():
            user.save()
            messages.success(requset, 'فرم ثبت شد', extra_tags='site')
            return redirect('homashahr:home2')
    else:
        user = formMunicipality(instance=product)
    return render(requset,'list-municipality.html',{'index':product})