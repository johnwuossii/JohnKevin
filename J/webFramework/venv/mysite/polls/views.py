from django.http import HttpResponse

def index(request):
    return HttpResponse('嗨 這是Poll的網頁喔')

def detail(request, poll_id):
    return HttpResponse('你在看的是 Poll {id} 的頁面'.format(id = poll_id) )

def results(request, poll_id):
    return HttpResponse('你在看的是 Poll {id} 的結果'.format(id = poll_id) )

def vote(request, poll_id):
    return HttpResponse('你在看的是 投票 Poll {id} 的頁面'.format(id = poll_id) )


