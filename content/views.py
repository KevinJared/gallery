from django.http  import HttpResponse
from django.shortcuts import render
import datetime as dt

# Create your views here.
def welcome(request):
   return render(request, 'index.html')


def content_of_day(request):
    date = dt.date.today()
    return render(request, 'all-images/articles.html', {"date": date,})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day
def past_days_content(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        # Converts data from the string Url
    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'all-images/past.html', {"date": date})