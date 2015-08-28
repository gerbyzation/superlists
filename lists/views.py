from django.shortcuts import render


def home_page(request):
    # data = request.POST.get('item_text', '')
    # print("data: " + data)
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })
