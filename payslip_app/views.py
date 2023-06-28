import calendar
from django.shortcuts import render ,HttpResponse,redirect
from .models import Employeesdetails

# Create your views here.


def login(request):
    return render(request,'login.html')


def home(request):
    return render(request,'home.html')


def edit(request,id):
    emp = Employeesdetails.objects.get(id=id)
    return render(request,'edit.html',{"emp":emp})


def update(request,id):
    employee_id = request.POST['employee_id']
    employee_name = request.POST['employee_name']
    gender = request.POST['gender']
    date_of_birth = request.POST['date_of_birth']
    department = request.POST['department']
    designation = request.POST['designation']
    bank = request.POST['bank']
    ifsc_code = request.POST['ifsc_code']
    pan_card_number = request.POST['pan_card_number']
    uan_number = request.POST['uan_number']
    pf_number =  request.POST['pf_number']
    paid_days =  request.POST['paid_days']
    paid_leaves =  request.POST['paid_leaves']
    date_of_jioning =  request.POST['dateofjoining']
    account_number =  request.POST['account_number']
    location =  request.POST['location']
    basic =  request.POST['basic']

    emp = Employeesdetails.objects.get(id=id)

    emp.employee_id = employee_id
    emp.employee_name=employee_name
    emp.gender=gender
    emp.date_of_birth=date_of_birth
    emp.department=department
    emp.designation=designation
    emp.bank=bank
    emp.ifsc_code=ifsc_code
    emp.pan_card_number=pan_card_number
    emp.uan_number=uan_number
    emp.pf_number=pf_number
    emp.paid_days=paid_days
    emp.paid_leaves=paid_leaves
    emp.date_of_jioning=date_of_jioning
    emp.account_number=account_number
    emp.location=location
    emp.basic=basic

    emp.save()
    return redirect("/get")
    


def view(request):
    emps = Employeesdetails.objects.all()
    result = {
        'emps': emps
    }
    #print(result)
    return render(request ,'view.html',result)




def view_all(request):
    emps = Employeesdetails.objects.all()
    result = {
        'emps':emps
    }
    return render(request,'view_all.html',result)



def add(request):
    if request.method == 'POST':
        employee_id = request.POST['employee_id']
        employee_name = request.POST['employee_name']
        gender = request.POST['gender']
        date_of_birth = request.POST['date_of_birth']
        department = request.POST['department']
        designation = request.POST['designation']
        bank = request.POST['bank']
        ifsc_code = request.POST['ifsc_code']
        pan_card_number = request.POST['pan_card_number']
        uan_number = request.POST['uan_number']
        pf_number =  request.POST['pf_number']
        paid_days =  request.POST['paid_days']
        paid_leaves =  request.POST['paid_leaves']
        date_of_jioning =  request.POST['dateofjoining']
        account_number =  request.POST['account_number']
        location =  request.POST['location']
        basic =  request.POST['basic']
        house_rent_allowances = request.POST['house_rent_allowances']
        medical_allowance = request.POST['medical_allowance']
        conveyance = request.POST['conveyance']
        special_allowance = request.POST['spical_allowance']
        phone_allowance = request.POST['phone_allowance']
        salary_arrears = request.POST['salary_arrears']
        employee_referral_scheme = request.POST['e_r_s']
        bonus = request.POST['bonus']
        professional_tax = request.POST['professional_tax']
        provident_fund = request.POST['provident']
        t_d_s = request.POST['t_d_s']
        loss_of_pay = request.POST['loss_of_pay']
        add_emp = Employeesdetails(employee_id = employee_id,employee_name=employee_name,gender=gender,date_of_birth=date_of_birth,department=department,designation=designation,
                                   bank=bank,ifsc_code=ifsc_code,pan_card_number=pan_card_number,uan_number=uan_number,pf_number=pf_number,
                                   paid_days=paid_days,paid_leaves=paid_leaves,date_of_jioning=date_of_jioning,account_number=account_number,location=location,basic=basic,
                                   house_rent_allowances=house_rent_allowances,medical_allowance=medical_allowance,conveyance=conveyance,special_allowance=special_allowance,phone_allowance=phone_allowance,
                                   salary_arrears=salary_arrears,employee_referral_scheme=employee_referral_scheme,bonus=bonus,professional_tax=professional_tax,provident_fund=provident_fund,
                                   t_d_s=t_d_s,loss_of_pay=loss_of_pay)
        add_emp.save()
        return redirect("/get")
    elif request.method == "GET":
        return render(request,'add_emp.html')
    else:
        return HttpResponse("ERROR")
    # return render(request,'add_emp.html')



def filter(request):
    if request.method == 'POST':
        # id = request.POST['employee_id']
        name = request.POST['employee_name']
        month = request.POST['month']
        month_name = list(calendar.month_name).index(month.capitalize())
        _, total_days = calendar.monthrange(2023, month_name)
        absent_days = request.POST['absent']
        emps = Employeesdetails.objects.all()
        # if id:
        #     emps = emps.filter(employee_id = id)
        if name:
            emps = emps.filter(employee_name = name)

        result = {
        'emps': emps,
        'month':month,
        'total_days':total_days,
        'absent': absent_days,
          }
        return render(request,'one_emp.html',result)
    elif request.method == 'GET':
        return render(request ,'filter_emp.html')
    else:
        return HttpResponse("ERROR")   

