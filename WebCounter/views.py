from django.shortcuts import render,HttpResponse

from WebCounter.counter import *


def index(request):
    return render(request, 'WebCounter/index.html')

def result(request):
    yourLogin = UesrLogin()
    yourLogin.UserInfoGet(request.POST['user'], request.POST['password'])
    yourLogin.UrpLogin()

    your_psI = psI()
    yourMessage=your_psI.PersonalInformation(yourLogin.UrpLogin()[0])


    your_pfI = pfI()
    your_pfI.PerformanceInformation(yourLogin.UrpLogin()[1])



    yourSumCredit=your_pfI.gpaCounter(yourLogin.UrpLogin()[1])[0]
    yourRequiredGPA = your_pfI.gpaCounter(yourLogin.UrpLogin()[1])[1]
    yourElectiveGPA = your_pfI.gpaCounter(yourLogin.UrpLogin()[1])[2]
    yourTotalGPA = your_pfI.gpaCounter(yourLogin.UrpLogin()[1])[3]

    yourLesson=your_pfI.PerformanceInformation(yourLogin.UrpLogin()[1])
    yourLessonList = []

    for i in range(len(yourLesson)):
        yourLessonList.append([])
        yourLessonList[i].append(yourLesson[i].CourseNumber1)
        yourLessonList[i].append(yourLesson[i].CourseName)
        yourLessonList[i].append(yourLesson[i].CourseCredit)
        yourLessonList[i].append(yourLesson[i].CourseAttribute)
        yourLessonList[i].append(yourLesson[i].CourseGrade)

    #print(yourLessonList)

    return render(request, 'WebCounter/result.html', {
        'yourName': yourMessage['yourName'],
        'yourClass': yourMessage['yourClass'],
        'totalGPA': yourTotalGPA,
        'requiredGPA': yourRequiredGPA,
        'electiveGPA': yourElectiveGPA,
        'sumCredit': yourSumCredit,
        'yourLesson': yourLessonList,
    })

    #return HttpResponse(yourLessonList)




