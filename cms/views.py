from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from cms.models import Book
from cms.forms import BookForm


# Create your views here.
def book_list(request):
	"""書籍の一覧"""
	# return HttpResponse("書籍の一覧")
	books = Book.objects.all().order_by("id")
	return render(request, "cms/book_list.html", {"books": books})




def book_edit(request, book_id=None):
	"""書籍の編集"""
	# return HttpResponse("書籍の編集")
	if book_id: #book_id が指定されている(フォーム修正時)
		book = get_object_or_404(Book, pk=book_id)
	else: # book_idが指定されていない(フォームに追加時)
		book = Book()

	if request.method=="POST": # POSTの時
		form = BookForm(request.POST, instance=book)  # POSTされたrequestデータからフォームを生成
		if form.is_valid():
			book = form.save(commit=False)
			book.save()
			return redirect("cms:book_list")
	else: # GETの時
		form = BookForm(instance=book) # bookインスタンスからフォームを生成

	return render(request, "cms/book_edit.html", dict(form=form, book_id=book_id))




def book_del(request,book_id):
	"""書籍の削除"""
	# return HttpResponse("書籍の削除")
	book = get_object_or_404(Book, pk=book_id)
	book.delete()
	return redirect("cms:book_list")


