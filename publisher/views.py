from django.shortcuts import render,redirect,HttpResponse
from .models import Book,Writer,Publisher
from login.views import check_login
# Create your views here.

#出版社
@check_login
def publisher_list(request):
    data = Publisher.objects.all()
    print("==============1")
    return render(request,"publisher/publisher_list.html",{"publisher_list":data,})
@check_login
def add_publisher(request):
    if request.method == 'POST':
        publisher_name = request.POST.get("publisher_name")
        publisher_addr = request.POST.get("publisher_addr")
        publisher_obj = Publisher.objects.create(name=publisher_name,addr=publisher_addr)
        return redirect("/publisher_list/")
    return render(request,"publisher/add_publisher.html")
@check_login
def delete_publisher(request):
    delete_id = request.GET.get("id")
    Publisher.objects.get(id=delete_id).delete()
    return redirect("/publisher_list/")
@check_login
def edit_publisher(request):
    edit_id = request.GET.get("id")
    publisher_obj = Publisher.objects.get(id=edit_id)
    print("==============3")
    if request.method == "POST":
        new_name = request.POST.get("publisher_name")
        new_addr = request.POST.get("publisher_addr")
        publisher_obj.name = new_name
        publisher_obj.addr = new_addr
        publisher_obj.save()
        return redirect("/publisher_list/")

    return render(request,"publisher/edit_publisher.html",{"publisher":publisher_obj})

#书籍
@check_login
def book_list(request):
    data = Book.objects.all()
    return render(request,"publisher/book_list.html",{"book_list":data,})

@check_login
def add_book(request):
    if request.method == "POST":
        new_name = request.POST.get("book_name")
        new_date = request.POST.get("book_date")
        new_publisher = request.POST.get("publisher_id")
        # new_writer = request.POST.get("writer_id")
        Book.objects.create(name=new_name,date=new_date,publisher_id=new_publisher)
        return redirect("/book_list/")
    # data2 = Writer.objects.all()
    data = Publisher.objects.all()
    return render(request,"publisher/add_book.html",{"publisher_list":data,})
@check_login
def delete_book(request):
    delete_id = request.GET.get("id")
    Book.objects.get(id=delete_id).delete()
    return redirect("/book_list/")
@check_login
def edit_book(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        book_name = request.POST.get("book_name")
        book_date = request.POST.get("book_date")
        book_publisher = request.POST.get("publisher_id")
        book_obj = Book.objects.get(id=book_id)
        book_obj.name = book_name
        book_obj.date = book_date
        book_obj.publisher_id = book_publisher
        book_obj.save()
        return redirect("/book_list/")
    book_id = request.GET.get("id")
    book_obj = Book.objects.get(id=book_id)
    data = Publisher.objects.all()
    return render(request,"publisher/edit_book.html",{"book":book_obj,"publisher_list":data,})
#作者
@check_login
def writer_list(request):
    date = Writer.objects.all()
    return render(request,"publisher/writer_list.html",{"writer_list":date,})

@check_login
def delete_writer(request):
    delete_id = request.GET.get("id")
    Writer.objects.get(id=delete_id).delete()
    return redirect("/writer_list/")

@check_login
def add_writer(request):
    if request.method == "POST":
        new_name = request.POST.get("writer_name")
        new_birthday = request.POST.get("writer_birthday")
        new_boooks = request.POST.getlist("book_id")
        writer_obj = Writer.objects.create(name=new_name,birthday=new_birthday,)
        writer_obj.books.set(new_boooks)
        writer_obj.save()
        return redirect("/writer_list/")
    data = Book.objects.all()
    return render(request,"publisher/add_writer.html",{"book_list":data,})
@check_login
def edit_writer(request):
    edit_id = request.GET.get("id")
    writer_obj = Writer.objects.get(id=edit_id)
    data = Book.objects.all()
    if request.method == "POST":
        new_name = request.POST.get("writer_name")
        new_birthday = request.POST.get("writer_birthday")
        new_books = request.POST.getlist("book_id")
        edit_obj = Writer.objects.get(id=edit_id)
        edit_obj.name = new_name
        edit_obj.birthday = new_birthday
        edit_obj.books.set(new_books)
        edit_obj.save()
        return redirect("/writer_list/")

    return render(request,"publisher/edit_writer.html",{"writer":writer_obj,"book_list":data,})