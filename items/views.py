from django.shortcuts import render, redirect
from .models import Item, Comment
from django.contrib.auth.decorators import login_required
from .forms import ItemForm, CommentForm
from django.contrib import messages

# Create your views here.



# Report lost/found item
@login_required
def create_item_view(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            messages.success(request, "Item reported successfully!")
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'items/create_item.html', {'form': form})



# View items (list)
def item_list_view(request):
    items = Item.objects.all()
    return render(request, 'items/item_list.html', {'items': items})



# Mark item as recovered
@login_required
def mark_as_recovered_view(request, item_id):
    item = Item.objects.get(id=item_id)
    if item.user == request.user:
        item.resolved = True
        item.save()
        messages.success(request, "Item marked as recovered!")
    return redirect('item_list')

    

# Add comment to an item
@login_required
def add_comment_view(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.item = item
            comment.user = request.user
            comment.save()
            messages.success(request, "Comment added!")
            return redirect('item_list')
    else:
        form = CommentForm()
    return render(request, 'items/add_comment.html', {'form': form, 'item': item})
