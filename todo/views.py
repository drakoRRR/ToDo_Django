from django.shortcuts import render

# Create your views here.
def main_page(request):
    '''Main page with the tasks'''

    return render(request, 'todo/mainpage.html')


def create_task(request):
    '''Page of creating tasks'''

    return render(request, 'todo/addtask.html')