from django.shortcuts import render, redirect
from django.views import View


from .models import Calendar, CalendarUser, Schedule
from .forms import CalendarForm, CalendarUserForm, ScheduleForm


# トップページ
class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {}

        # とりあえずここで表示
        context["calendars"]    = Calendar.objects.all()

        return render(request, "scheduler/index.html", context)


    def post(self, request, *args, **kwargs):



        return redirect("scheduler:index")

index   = IndexView.as_view()



class CalendarView(View):
    def get(self, request, pk, *args, **kwargs):
        context = {}

        context["calendar"]     = Calendar.objects.filter(id=pk).first()
        context["schedules"]    = Schedule.objects.filter(calendar=pk)

        return render(request, "scheduler/calendar.html", context)
    def post(self, request, pk, *args, **kwargs):
        # TODO:ここでカレンダーの投稿を受け付ける

        copied              = request.POST.copy()
        copied["user"]      = request.user
        copied["calendar"]  = pk

        form    = ScheduleForm(copied)

        if form.is_valid():
            form.save()
        else:
            print(form.errors)

        return redirect("scheduler:calendar", pk)

calendar    = CalendarView.as_view()


