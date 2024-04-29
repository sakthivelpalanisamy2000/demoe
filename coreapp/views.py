
from json import dumps 
from django.views.decorators.csrf import csrf_exempt
from coreapp.models import Userpermistionuploademployee,Userpermistionupload,Javatestcasereport,Cpptraingclick,Ptestcasereport,Cpptestcasereport,Cpptestcasereport,Ctestcasereport,Ctraningreport,Pythontraingclick,Ctraingclick,Cpptraningcodeingquestions,Cppquiz,Cppuploadvideosections,Cpptraingtitle , Ctraningcodeingquestions,Cquiz,Cuploadvideosections,Ctraingtitle , Pythontraningcodeingquestions,Pythonquiz,Pythonuploadvideosections,Pythontraingtitle , CpponetechnicalQuestionsTestcase,Cpponetitletestcase,Cpponepquestionpractices,Cpponetitlepractices, Ptitlepractices,Ptitletestcase,PtechnicalQuestionsTestcase,Pquestionpractices, Ctitlepractices,Ctitletestcase,CtechnicalQuestionsTestcase,Cquestionpractices, Demoquestions,Quiz,Projectresume,Elisteningreader,Elisteningtitle,Elisteningquiz,Ebusinessquiz,Espokenquiz,Espokenvideosections,Espokentitle,Ebusinessvideosections,Ebusinesstitle,Etechnicaltitle,Etechnicalvideosections,Etechnicalquiz,Intershiptitle,Intershipquiz,Intershipvideosections,Appquiz,Apptitle,Pdvideosections,Pdtitle,Titleclick,Workshopquiz,Workshopvideosections,Workshoptitle,Traningupdateid,Aptitudetitle,Aptitudevideosections,Aptitudequiz,Javatraingmcq,Videosection,Traningcodeingquestions,Practicelevels,Questionpractices,Titlepractices,Javatraingtitle,Titletestcase,TechnicalQuestionsTestcase,Toutput,Programminglan,demooutput,Templatedesign,Personaldetails,Profilesummary,TemplatedesignImage,Educationsresume
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
import json


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User  # Import the User model

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User  # Import the User model


# trial product

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from .models import Product, Subscription 


from datetime import timedelta
from django.utils import timezone





# chatgpt 
# In myrecipe_app/views.py

from django.shortcuts import render
from django.http import HttpResponse
from dotenv import load_dotenv
import os
import openai

# Initialize environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv('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')

def amain(request):

    return render(request, 'amain/index.html')
def celebrate(request):

    return render(request, 'amain/celebrate.html')

def indexchatgpt1(request):
    # Display the main ingredient input page
    return render(request, 'chatgpt/index.html')

def generate_recipe(request):
    if request.method == 'POST':
        # Extract the three ingredients from the user's input
        ingredients = request.POST.getlist('ingredient')

        if len(ingredients) != 3:
            return HttpResponse("Kindly provide exactly 3 ingredients.")

        # Craft a conversational prompt for ChatGPT, specifying our needs
        prompt = f"Craft a recipe in HTML using {', '.join(ingredients)}. Ensure the recipe ingredients appear at the top, followed by the step-by-step instructions."

        # Engage ChatGPT to receive the desired recipe
        response = openai.Completion.create(
            engine="text-davinci-002",  # Choose the appropriate engine
            prompt=prompt,
            max_tokens=500,  # Adjust as needed
        )

        # Extract the recipe from ChatGPT's response
        recipe = response["choices"][0]["text"]

        # Showcase the recipe on a new page
        return render(request, 'recipe.html', {'recipe': recipe})

    else:
        return HttpResponse("Method not allowed.")



# chatgpt end

from openai import OpenAI



openai.api_key = os.getenv('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')

load_dotenv()



def indexchatgpt(request):


    user_input = "what is fullstack Developement"
        # Make sure to replace 'your-openai-api-key' with your actual OpenAI API key
    openai.api_key = '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'
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=100
    )
    bot_response = response.choices[0].text.strip()
    print(bot_response)
def job(request):

    return render(request, 'design/dashborad/jobs/jobs.html')

def areport(request):

    if 'username' in request.session:
        usernameget=request.user.username

        try:
            template="design/dashborad/areport/index.html"
            return render(request ,template,{"username":usernameget} )
            # session = Session.objects.get(session_key=session_id)
            # user_id = session.get_decoded().get('_auth_user_id')
            # print("session user id:", user_id)

           
            # current_user = request.user

            # data = Ctraingtitle.objects.all()
           


           
            # results = Ctraingtitle.objects.prefetch_related(
            # Prefetch('ctraningreport_set', queryset=Ctraningreport.objects.filter(user_id=1))
            # ).values_list( 'id','title', 'selecttype', 'ctraningreport__user__username', 'ctraningreport__status')
            # print(results)
            # iduser=request.user.username
            # if results is not None:
            #     converted_results = []
            #     for item in results:
            #         if item is not None:
            #             result_dict = {
            #                 'check':iduser,
            #                 'id': item[0],
            #                 'title': item[1],
            #                 'selecttype': item[2],
            #                 'username':item[3],
                           

            #                 'status': item[4],
            #             }
            #             converted_results.append(result_dict)
            #     print("converted_results", converted_results)
            # else:
            #     print("results is None")
            # filtered_data = [dict(t) for t in {tuple(d.items()) for d in converted_results if d['id'] is not None}]
            # print("filtered_data is None" ,filtered_data)


            # data2 = Ctraingtitle.objects.all()
            # print("data2",data2)

   
            # template = "design/dashborad/c_language/traning/view.html"

            # return render(request, template, {"data": converted_results, "data2": data2})

         
        except Session.DoesNotExist:
            return HttpResponse("Invalid session ID")
        except User.DoesNotExist:
            return HttpResponse("User not found")
    else:
        # User not logged in, redirect to login page
        return redirect('login')

    



def start_trial(user, product):
    end_date = timezone.now() + timedelta(days=14)
    Subscription.objects.create(user=user, product=product, end_date=end_date)


@login_required
def subscribe_to_product(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)

    # Check if the user is already subscribed
    if Subscription.objects.filter(user=user, product=product).exists():
        return render(request, 'trial/already_subscribed.html', {'product': product})

    # Start a 14-day trial
    end_date = timezone.now() + timedelta(days=14)
    Subscription.objects.create(user=user, product=product, end_date=end_date)

    return render(request, 'trial/subscription_success.html', {'product': product})

@login_required
def check_trial_status(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)

    try:
        subscription = Subscription.objects.get(user=user, product=product)
    except Subscription.DoesNotExist:
        return render(request, 'trial/not_subscribed.html', {'product': product})

    current_date = timezone.now().date()

    if subscription.end_date >= current_date:
        days_left = (subscription.end_date - current_date).days
        return render(request, 'trial/trial_status.html', {'days_left': days_left, 'product': product})
    else:
        return render(request, 'trial/trial_expired.html', {'product': product})



# end trial
def outputvalue(request):
    if request.method == 'POST':
        output_value = request.POST.get('data')
        print(output_value)
        # Process the output_value as needed
        # ...

        return JsonResponse({'status': 'success'})
    
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
def check(request):
     if request.method == 'POST':
        output_value = request.POST.get('data')
        print(output_value)

     return render(request, "check.html", {})
    

def resumedemo(request):
    # data = File.objects.all()
    # print(data)
    return render(request, "resumedemo.html", {})
def compiler(request):
    # data = File.objects.all()
    # print(data)
    return render(request, "compiler.html", {})

def pythoncompiler(request):
    # data = File.objects.all()
    # print(data)
    return render(request, "pythoncompiler.html", {})
def ccode(request):
    return render(request, "ccode.html", {})
def testing(request):
    codevalue="#include <iostream>\nusing namespace std;\n        \nint main() {\n    cout << \"Write Your code\";\n    return 0;\n"
    dataDictionary = { 
        'amp': 'data', 
         
    } 

    data_from_django = {'codevalue': '#include <iostream>\nusing namespace std;\n        \nint main() {\n    cout << \"Write Your code\";\n    return 0;\n'}
    # dump data 
    dataJSON = dumps(dataDictionary) 
    return render(request, "cpp.html", {'data': dataJSON , 'codevalue':codevalue ,'data_from_django':data_from_django })
@csrf_exempt
def javatesting(request):
    # value=TechnicalQuestionsTestcase.objects.()
    
    if 'username' in request.session:


        
        if request.method == 'POST':
            output_value = request.POST.get('data')
            # obj=demooutput()
            # obj.demooutputs=output_value
            # obj.save()
            valuedemo="Write a Code"
            valuedemo2="Write a Code"
            # myitem=Toutput.objects.last().toutputs
            myitem=demooutput.objects.last().demooutputs

            # print(Toutput.objects.last().toutputs)
            # for item in Toutput.objects.all():
            #     myitem=item.toutputs
            for i in demooutput.objects.all():
                demova=i.demooutputs
            

            # output_old = [5, 1, 6]
            # print(myitem)
            print("code",myitem)
            print("outpuyval",output_value)
            print("deme",valuedemo)
            # status_code = 200 

            # for item in TechnicalQuestionsTestcase.objects.all():
            #     myitem=item.soutput
            
            if output_value == myitem:

                print("++++++++sucess rate ") 
                response_data = {'success': True, 'message': 'Datasdfsadf processed successfully'}
                status_code = 200 

                print(demova)
                print(myitem)
            elif output_value != myitem :
                
                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500  
            # print(myitem)
            # if myitem == output_value :
                
            #     response_data = {'success': True, 'message': 'Datasdfsadf processed successfully'}
            #     status_code = 200 
            #     # print(output_old)
            #     print("suuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuccccccccccccccceeeeeeeeeeeeeeessssssssss")
            # else:
            

            #     response_data = {'success': False, 'message':'error_message'}
            #     status_code = 500  
            #     print("errrrrrrrrrrr")

                # HTTP status code for server error
            # HTTP status code for success
            
            # If there's an error, handle it
            # response_data = {'success': False, 'error_message': str(e)}
            # status_code = 500  # HTTP status code for server error

            return JsonResponse(response_data, status=status_code)
        
       
        return render(request, 'java.html', {'username': request.session['username']})
    else:
        return redirect('login')

def pythontesting(request):
    
    return render(request, "python.html", {})

def ctesting(request):
    return render(request, "c.html", {})
@csrf_exempt
def addquestions(request):
    template="questions.html"
    if request.method == "POST":
        questions = request.POST["technicalquestions"]
        sinput = request.POST["sinput"]
        soutput = request.POST["soutput"]
        tinput = request.POST["tinput"]
        toutput = request.POST["toutput"]
        languageselecte = request.POST["languageselecte"]
        print("*****************")
        print(questions,sinput,soutput,tinput,toutput,languageselecte)
        return render(request,template,{'data':questions})



    return render(request,template,{})


def postadddemo(request):
    if request.method == "POST":
        # textvalue = request.POST["textvalue"]
        languageselecte = request.POST["languageselecte"]

        sectextvalue = request.POST["sectextvalue"]
        # areatextpost = request.POST["areatextpost"]
        # obj = Demoquestions()
        # obj.questions=areatextpost
        # obj.save()

        print("*****************************")
        print( languageselecte,sectextvalue)
    return render(request,"democheck/postadd.html",{})

def demoquestiondisplay(request):
    data_list =Demoquestions.objects.all()
    

    paginator = Paginator(data_list , 1)  # Show 10 items per page

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        data = paginator.page(paginator.num_pages)

    return render(request,"democheck/democpp.html",{'data':data})



def sent(request):
    template="democheck/multipledatasent.html"

    # if request.method == 'POST':
    #     questions = request.POST.get('data1')
    #     userinput = request.POST.get('data2')
    #     useroutput = request.POST.get('data3')
    #     testcaseinput = request.POST.get('data4')
    #     testcaseoutput = request.POST.get('data5')

    #     print(questions,userinput,useroutput,testcaseinput,testcaseoutput)
    return render(request ,template,{} )

@csrf_exempt
def sentadd(request):
    template="democheck/multipledatasent.html"
    print("entet the sentadd")
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        data1 = data.get('data1')
        data2 = data.get('data2')
        data3 = data.get('data3')
        data4 = data.get('data4')
        data5 = data.get('data5')
        print("SDL")

        print(data1,data2,data3,data4,data5)

        # Process the received data as needed

        return JsonResponse({'status': 'success', 'message': 'Data received successfully'})

    # return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
    return render(request ,template,{} )



@csrf_exempt
def javaaddpage(request):
    template="democheck/javaaddpage.html"
    
   
    return render(request ,template,{} )




# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def custom_login(request):
    print("enter usr")
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return JsonResponse({'success': False, 'message': 'Username and password are required.'})

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'message': 'Account is not active.'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid username or password.'})

    return render(request, 'loginform/login.html')




from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

# def home(request):
#     return render(request, 'authenticate/home.html')

def home(request):
    if 'username' in request.session:
        return render(request, 'authenticate/home.html', {'username': request.session['username']})
    else:
        return redirect('login')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, 'You have been logged in successfully')
            request.session['username'] = username
            return redirect('areport')
        else:
            messages.warning(request, "Username or Password is incorrect !!")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html')




def logout_user(request):
    request.session.flush()
    return redirect('login')

def new(request):
    if 'username' in request.session:


        if request.method == 'POST':
            inputData = request.POST.get('inputData')
            sampleCode = request.POST.get('sampleCode')
            sampleinput = request.POST.get('sampleinput')
            sampleoutput = request.POST.get('sampleoutput')
            textcaseInput = request.POST.get('textcaseInput')
            textcaseOutput = request.POST.get('textcaseOutput')


            obj=TechnicalQuestionsTestcase()
            obj.questions= inputData
            obj.sinput= sampleinput
            obj.soutput=sampleoutput 
            obj.tinput= textcaseInput
            obj.toutput=textcaseOutput
            obj.samplecode=sampleCode
            obj.save()
            
            # print("id is ",itemId)

            # password = request.POST.get('password')
            print(inputData,sampleCode , textcaseOutput,textcaseInput,sampleoutput,sampleinput)

        return render(request, 'democheck/new.html')
    else:
            return redirect('login')
def taketest(request):
        if 'username' in request.session:
            
            data_list =TechnicalQuestionsTestcase.objects.all()
            

            paginator = Paginator(data_list , 1)  # Show 10 items per page

            page = request.GET.get('page')
            try:
                data = paginator.page(page)
                
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                data = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g., 9999), deliver last page.
                data = paginator.page(paginator.num_pages)

            if request.method == 'POST':
                    output_value = request.POST.get('data')
                    matchvalue = request.POST.get('data2')
                    print("matchvalue",matchvalue)
                    myitem=TechnicalQuestionsTestcase.objects.get(id=matchvalue ).toutput
                    print(myitem)
                    print("code",myitem)
                    print("outpuyval",output_value)
                    if output_value == myitem:
                        print("++++++++sucess rate ") 
                        response_data = {'success': True, 'message': 'Datasdfsadf processed successfully'}
                        status_code = 200 
                        print(myitem)
                    elif output_value != myitem :
                        print("failer")
                        response_data = {'success': False, 'message':'error_message'}
                        status_code = 500
                    return JsonResponse(response_data, status=status_code)

            return render(request,"democheck/java.html",{'data':data})
        else:
            return redirect('login')

# myapp/views.py
from django.shortcuts import render
from django.http import JsonResponse

def my_view(request, my_id):
    if request.method == 'POST':
        submitted_id = request.POST.get('my_id', '')
        return JsonResponse({'message': f'Received ID from AJAX request: {submitted_id}'})
    else:
        return render(request, 'democheck/id.html')



# def resume(request):
#     template="resume2.html"
    
   
#     return render(request ,template,{} )

def personaldetails(request):
    template="resume/editresume.html"

    if request.method == 'POST':
        print("enter")
        data = json.loads(request.body.decode('utf-8'))

        jobtitle = data.get('data1')
        fullName = data.get('data2')
        Email = data.get('data3')
        Phone = data.get('data4')
        Country = data.get('data5')
        city = data.get('data6')
        Address = data.get('data7')



        obj=Personaldetails()
        obj.jobtitle= jobtitle
        obj.name= fullName
        obj.email=Email 
        obj.phone= Phone
        obj.country=Country
        obj.city=city
        obj.address=Address

        obj.save()


        print("job titile",jobtitle)

            

        return render(request,template, {'data':data})

    # else:
    #     print("not come")
    return render(request,template, '')


# template
def choosetempale(request):
    template="design/choosetemplate.html"
  
    return render (request,template,{})


def desgincode(request):
    template="design/index.html"


    
    useridpass=Userclick.objects.last().userclickid

    print("useridpass",useridpass)
        
    display=Personaldetails.objects.last()
    summarydata=Profilesummary.objects.last()
    image=TemplatedesignImage.objects.all()
    data1=Templatedesign.objects.get(id=1 ).template
    print("data sent")
    print("enter")
    job_title = request.POST.get('jobtitle')
    full_name = request.POST.get('fullName')
    email = request.POST.get('Email')
    phone = request.POST.get('Phone')
    country = request.POST.get('Country')
    city = request.POST.get('city')
    address = request.POST.get('Address')
    summary = request.POST.get('summary')
    obj=Personaldetails()
    obj.jobtitle= job_title
    obj.name= full_name
    obj.email=email 
    obj.phone= phone
    obj.country=country
    obj.city=city
    obj.address=address

    obj.save()

    obj=Profilesummary()
    obj.summary=summary
    obj.save()


    display=Personaldetails.objects.last()
    summarydata=Profilesummary.objects.last()
    print("job titile",job_title)
    return render (request,template,{'data':display,'summary':summarydata,'image':image ,"data1":data1  })

    



def savevalue(request):
    template="design/templateone.html"
    if request.method == 'POST':
        job_title = request.POST.get('jobtitle')
        full_name = request.POST.get('fullName')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        country = request.POST.get('Country')
        city = request.POST.get('city')
        address = request.POST.get('Address')
        summary = request.POST.get('summary')
        obj=Personaldetails()
        obj.jobtitle= job_title
        obj.name= full_name
        obj.email=email 
        obj.phone= phone
        obj.country=country
        obj.city=city
        obj.address=address

        obj.save()

        obj=Profilesummary()
        obj.summary=summary
        obj.save()


    return render (request,template,{})


def templateone(request):
    template="design/templateone.html"
    
    if request.method == 'POST':
        job_title = request.POST.get('jobtitle')
        full_name = request.POST.get('fullName')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        country = request.POST.get('Country')
        city = request.POST.get('city')
        address = request.POST.get('Address')
        summary = request.POST.get('summary')
        obj=Personaldetails()
        obj.jobtitle= job_title
        obj.name= full_name
        obj.email=email 
        obj.phone= phone
        obj.country=country
        obj.city=city
        obj.address=address

        obj.save()

        obj=Profilesummary()
        obj.summary=summary
        obj.save()
    

        
    display=Personaldetails.objects.last()
    summarydata=Profilesummary.objects.last()
    image=TemplatedesignImage.objects.all()
    # display=Personaldetails.objects.get(id=59 )
    print("data sent")
    print("enter")
    


    display=Personaldetails.objects.last()
    summarydata=Profilesummary.objects.last()
    # print("job titile",job_title)
    return render (request,template,{'data':display,'summary':summarydata,'image':image  })

def templatetwo(request):
    template="design/templatetwo.html"
    
    if request.method == 'POST':
        job_title = request.POST.get('jobtitle')
        full_name = request.POST.get('fullName')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        country = request.POST.get('Country')
        city = request.POST.get('city')
        address = request.POST.get('Address')
        summary = request.POST.get('summary')
        obj=Personaldetails()
        obj.jobtitle= job_title
        obj.name= full_name
        obj.email=email 
        obj.phone= phone
        obj.country=country
        obj.city=city
        obj.address=address

        obj.save()

        obj=Profilesummary()
        obj.summary=summary
        obj.save()

        
    display=Personaldetails.objects.last()
    summarydata=Profilesummary.objects.last()
    image=TemplatedesignImage.objects.all()
    # display=Personaldetails.objects.get(id=59 )
    print("data sent")
    print("enter")
    


    display=Personaldetails.objects.last()
    summarydata=Profilesummary.objects.last()
    # print("job titile",job_title)
    return render (request,template,{'data':display,'summary':summarydata,'image':image  })


def templatethree(request):
    template="design/templatethree.html"
    
    if request.method == 'POST':
        job_title = request.POST.get('jobtitle')
        full_name = request.POST.get('fullName')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        country = request.POST.get('Country')
        city = request.POST.get('city')
        address = request.POST.get('Address')
        summary = request.POST.get('summary')
        obj=Personaldetails()
        obj.jobtitle= job_title
        obj.name= full_name
        obj.email=email 
        obj.phone= phone
        obj.country=country
        obj.city=city
        obj.address=address

        obj.save()

        obj=Profilesummary()
        obj.summary=summary
        obj.save()
    

        
    display=Personaldetails.objects.last()
    summarydata=Profilesummary.objects.last()
    image=TemplatedesignImage.objects.all()
    # display=Personaldetails.objects.get(id=59 )
    print("data sent")
    print("enter")
    


    display=Personaldetails.objects.last()
    summarydata=Profilesummary.objects.last()
    # print("job titile",job_title)
    return render (request,template,{'data':display,'summary':summarydata,'image':image  })


def templatefour(request):
    template="design/templatefour.html"
    
    if request.method == 'POST':
        job_title = request.POST.get('jobtitle')
        full_name = request.POST.get('fullName')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        country = request.POST.get('Country')
        city = request.POST.get('city')
        address = request.POST.get('Address')
        summary = request.POST.get('summary')
        obj=Personaldetails()
        obj.jobtitle= job_title
        obj.name= full_name
        obj.email=email 
        obj.phone= phone
        obj.country=country
        obj.city=city
        obj.address=address

        obj.save()

        obj=Profilesummary()
        obj.summary=summary
        obj.save()

        
    display=Personaldetails.objects.last()
    summarydata=Profilesummary.objects.last()
    image=TemplatedesignImage.objects.all()
    # display=Personaldetails.objects.get(id=59 )
    print("data sent")
    print("enter")
    


    display=Personaldetails.objects.last()
    summarydata=Profilesummary.objects.last()
    # print("job titile",job_title)
    return render (request,template,{'data':display,'summary':summarydata,'image':image  })


def resume(request):
    template="resume/editresume.html"
    data =Templatedesign.objects.all()
    display=Personaldetails.objects.last()
    summarydata=Profilesummary.objects.last()

    if request.method == 'POST':
        print("data sent")
        print("enter")

        
        job_title = request.POST.get('jobtitle')
        full_name = request.POST.get('fullName')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        country = request.POST.get('Country')
        city = request.POST.get('city')
        address = request.POST.get('Address')
        summary = request.POST.get('summary')




        obj=Personaldetails()
        obj.jobtitle= job_title
        obj.name= full_name
        obj.email=email 
        obj.phone= phone
        obj.country=country
        obj.city=city
        obj.address=address

        obj.save()

        obj=Profilesummary()
        obj.summary=summary
        obj.save()


        display=Personaldetails.objects.last()
        summarydata=Profilesummary.objects.last()
        print("job titile",job_title)

            

        return render(request,template, {'data':display,'summary':summarydata})
    return render (request,template,{})


# java 

def bumlaaddcss(request):
            
        data_list =TechnicalQuestionsTestcase.objects.all()
        

        paginator = Paginator(data_list , 1)  # Show 10 items per page

        page = request.GET.get('page')
        try:
            data = paginator.page(page)
            
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver last page.
            data = paginator.page(paginator.num_pages)

        if request.method == 'POST':
                output_value = request.POST.get('data')
                matchvalue = request.POST.get('data2')
                print("matchvalue",matchvalue)

                obj=demooutput()
                obj.demooutputs=output_value
                obj.save()
                print("enter")
                valuedemo="Write a Code"
                valuedemo2="Write a Code"
                # myitem=Toutput.objects.last().toutputs
                myitem=TechnicalQuestionsTestcase.objects.get(id=matchvalue ).toutput
                
                print(myitem)

                # print(Toutput.objects.last().toutputs)
                # for item in Toutput.objects.all():
                #     myitem=item.toutputs

                
                
                

                # output_old = [5, 1, 6]
                # print(myitem)
                print("code",myitem)
                print("outpuyval",output_value)
                print("deme",valuedemo)
                # status_code = 200 

                # for item in TechnicalQuestionsTestcase.objects.all():
                #     myitem=item.soutput
                
                if output_value == myitem:

                    print("++++++++sucess rate ") 
                    response_data = {'success': True, 'message': 'Datasdfsadf processed successfully'}
                    status_code = 200 

                    print(myitem)
                elif output_value != myitem :
                    
                    print("failer")
                    response_data = {'success': False, 'message':'error_message'}
                    status_code = 500
                return JsonResponse(response_data, status=status_code)

        return render(request,"democheck/javacopy.html",{'data':data})
    



def showdesign(request):
    template="resume/experience.html"
    
   
    return render(request ,template,{} )




# full design page
# python language start


#  python traning

@login_required
def preportpage(request):
    template="design/dashborad/python_language/index.html"
    userid = request.user.id

    total_question = PtechnicalQuestionsTestcase.objects.count()
    success = Ptestcasereport.objects.filter(user_id=userid).count()
    success_percentage = (success / total_question) * 100 if total_question > 0 else 0
    success_percentage_rounded ="{:.1f}".format(success_percentage)
    showsuccess = Ptestcasereport.objects.filter(user_id=userid).all()

    for instance in showsuccess:
        print(instance.id)

    failed =(total_question - success)
    failed_percentage = (failed / total_question) * 100 if total_question > 0 else 0
    failed_percentage_rounded ="{:.1f}".format(failed_percentage)

    print("total_question",total_question,success,failed)
    context = {

        'total': total_question,
        'success': success,
        'failed': failed,
        'success_percentage':success_percentage_rounded,
        'failed_percentage':failed_percentage_rounded



   
    }

    return render(request ,template,{'report':context,"showsuccess":showsuccess} )

@login_required
def ptraningclick(request):
    template="design/dashborad/python_language/traning/upload/title.html"
    user=request.user
    click=user.id
    print()
    if request.method == 'POST':
        data = request.POST.get('data2')
        obj=Pythontraingclick()
        obj.click=data
        obj.user_id=click
        obj.save()
        return redirect('ptraningmcq')
    return redirect('ptraningmcq')

@login_required
def ptraningchecktest(request):
    template="design/dashborad/python_language/testcase/upload/title.html"
    username=request.user.username
    username_cap = username.capitalize()
    if request.method == 'POST':
            
            data = request.POST.get('data2')
            data3 = request.POST.get('data3')
            print("data sented",data3)        
            check=Pythontraningcodeingquestions.objects.get(id=data ).toutput
            print("check2",data)
            print("check3",data3)
            if check==data3:
                response_data = {'success': True, 'message': 'test case has been executed successfully',"username":username_cap}
                status_code = 200                 
            else:
                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500
            return JsonResponse(response_data, status=status_code)
    return render(request ,template,{} )

@login_required
def ptraningview(request):
    template="design/dashborad/python_language/traning/view.html"
    data=Pythontraingtitle.objects.all()
    user=request.user
    print("print",user.id)

    return render(request ,template,{"data":data} )
def ptraningvideo(request,id):
    template="design/dashborad/python_language/traning/video.html"
    data2 =Pythonuploadvideosections.objects.filter(title_id=id)
    return render(request ,template,{"data":data2} )

@login_required
def ptraningmcq(request):
    template="design/dashborad/python_language/traning/mcq.html"
    user_id = request.user.id
    last_click = Pythontraingclick.objects.filter(user_id=user_id).last()
    if last_click is not None:
        myitem = last_click.click
        print("Last click for current user:", myitem)

        data =Pythonquiz.objects.filter(title_id=myitem)
        count =Pythonquiz.objects.filter(title_id=myitem).count()

    questions = [
    {   'id':quiz.id,
        'question': quiz.question,
        'answers': [
            {'text': quiz.option1, 'correct': quiz.answer1},
            {'text': quiz.option2, 'correct': quiz.answer2},
            {'text': quiz.option3, 'correct': quiz.answer3},
            {'text': quiz.option4, 'correct': quiz.answer4}
        ]
    }
    for quiz in data
   ]
    return render(request ,template,{"questions":questions ,"count":count} )

def ptraningcompiler(request):
    template="design/dashborad/python_language/traning/compiler.html"
    
    return render(request ,template,{} )

@login_required
def ptraningtest(request):
    template="design/dashborad/python_language/traning/test.html"
    user_id = request.user.id
    last_click = Pythontraingclick.objects.filter(user_id=user_id).last()
    if last_click is not None:
        myitem = last_click.click
        print("Last click for current user:", myitem)
    
    data1=Pythontraningcodeingquestions.objects.filter(title_id=myitem)
    
    paginator = Paginator(data1 , 1)  

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    

    return render(request ,template,{"data":data} )


# upload traning c
def ptraningviewupload(request):
    template="design/dashborad/python_language/traning/upload/title.html"
    data=Pythontraingtitle.objects.all()

    if request.method == 'POST':
        title = request.POST.get('data2')
        chapter = request.POST.get('data3')
        obj =Pythontraingtitle()
        obj.title=title
        obj.selecttype=chapter
        obj.save()
        return redirect('ptraningvideoupload')
       
    return render(request ,template,{"data":data} )
def ptraningvideoupload(request):
    template="design/dashborad/python_language/traning/upload/video.html"

    data=Pythontraingtitle.objects.all()

    if request.method == 'POST' and request.FILES.get('video_file'):
        demoone="c"
        title = request.POST.get('type')
        video_file = request.FILES['video_file']
        con = request.POST.get('content')
        Pythonuploadvideosections.objects.create(titleone=demoone ,title_id=title, video_file=video_file , content= con)
        return redirect("ptraningmcqupload")
     
    
    return render(request ,template,{"data":data} )

def ptraningmcqupload(request):
    template="design/dashborad/python_language/traning/upload/mcq.html"
    
    data=Pythontraingtitle.objects.all()
    if request.method == 'POST':
        type = request.POST.get('type')

        question = request.POST.get('question')
        option1 = request.POST.get('optionone')
        option2 = request.POST.get('optiontwo')
        option3 = request.POST.get('optionthree')
        option4 = request.POST.get('optionfour')
        answer1 = request.POST.get('answerone')
        answer2 = request.POST.get('answertwo')
        answer3 = request.POST.get('answerthree')
        answer4 = request.POST.get('answerfour')
        obj=Pythonquiz()
        obj.question=question
        obj.option1=option1
        obj.option2=option2
        obj.option3=option3
        obj.option4=option4
        obj.answer1=answer1
        obj.answer2=answer2
        obj.answer3=answer3
        obj.answer4=answer4
        obj.title_id=type
        obj.save()

        # return redirect("apptitleupload")

       
    return render(request, template, {"data":data})

def ptraningtestupload(request):
    template="design/dashborad/python_language/traning/upload/test.html"
    data=Pythontraingtitle.objects.all()

    if request.method == 'POST':
            inputData = request.POST.get('inputData')
            sampleCode = request.POST.get('sampleCode')
            sampleinput = request.POST.get('sampleinput')
            sampleoutput = request.POST.get('sampleoutput')
            textcaseInput = request.POST.get('textcaseInput')
            textcaseOutput = request.POST.get('textcaseOutput')
            type = request.POST.get('selectedtype')

            obj=Pythontraningcodeingquestions()
            obj.questions= inputData
            obj.sinput= sampleinput
            obj.soutput=sampleoutput 
            obj.tinput= textcaseInput
            obj.toutput=textcaseOutput
            obj.samplecode=sampleCode
            obj.title_id=type

            obj.save()
            print(inputData,sampleCode , textcaseOutput,textcaseInput,sampleoutput,sampleinput)

    return render(request ,template,{"data":data} )

# edit traning c
    # -- > view
def ptraningvieweditview(request):
    template="design/dashborad/python_language/traning/edit/view.html"
    data=Pythontraingtitle.objects.all()
    user=request.user
    print("print",user.id)

    return render(request ,template,{"data":data} )

def ptraningvideoeditview(request,id):
    template="design/dashborad/python_language/traning/edit/videoview.html"
    data2 =Pythonuploadvideosections.objects.filter(title_id=id)
    return render(request ,template,{"data":data2} )


def ptraningmcqeditview(request,id):
    template="design/dashborad/python_language/traning/edit/mcqview.html"
    data2 =Pythonquiz.objects.filter(title_id=id)
    paginator = Paginator(data2 , 1)  # Show 10 items per page

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        data = paginator.page(paginator.num_pages)


    return render(request ,template,{"data":data , } )


    #  --> edit
def ptraningviewedit(request,id):
    template="design/dashborad/python_language/traning/editupload/titleupload.html"
    data = get_object_or_404(Pythontraingtitle, id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        data.title=title
        data.save()
        return redirect("ptraningvieweditview")
    return render(request ,template,{"data":data} )

def ptraningvideoedit(request,id):
    template="design/dashborad/python_language/traning/editupload/video.html"
    data = get_object_or_404(Pythonuploadvideosections, id=id)

    if request.method == 'POST':
        video_file = request.FILES['video_file']
        con = request.POST.get('content')
        data.titleone="edione"
        data.video_file=video_file
        data.content= con
        data.save()

        return redirect("ptraningvieweditview")
    return render(request ,template,{"data":data} )

def ptraningmcqedit(request,id):
    template="design/dashborad/python_language/traning/editupload/mcq.html"
    data = get_object_or_404(Pythonquiz, id=id)
    id_value = data.title_id
    if request.method == 'POST':
        question = request.POST.get('question')
        option1 = request.POST.get('optionone')
        option2 = request.POST.get('optiontwo')
        option3 = request.POST.get('optionthree')
        option4 = request.POST.get('optionfour')
        answer1 = request.POST.get('answerone')
        answer2 = request.POST.get('answertwo')
        answer3 = request.POST.get('answerthree')
        answer4 = request.POST.get('answerfour')
        data.question=question
        data.option1=option1
        data.option2=option2
        data.option3=option3
        data.option4=option4
        data.answer1=answer1
        data.answer2=answer2
        data.answer3=answer3
        data.answer4=answer4
        data.save()
        return redirect(reverse('ptraningmcqeditview', kwargs={'id': id_value}))
    return render(request ,template,{"data":data} )
    # delete
def ptraningviewdelete(request,id):
    template="design/dashborad/python_language/traning/upload/title.html"
    data = get_object_or_404(Pythontraingtitle, id=id)

    if request.method == 'POST':
        data.delete()
        return redirect("ptraningvieweditview")
    return render(request ,template,{"data":data} ) 

def ptraningvideodelete(request,id):
    template="design/dashborad/python_language/traning/upload/video.html"
    data = get_object_or_404(Pythonuploadvideosections, id=id)

    if request.method == 'POST':
        data.delete()
        return redirect("ptraningvieweditview")
    return render(request ,template,{"data":data} )

def ptraningmcqdelete(request,id):
    template="design/dashborad/python_language/traning/upload/mcq.html"
    data = get_object_or_404(Pythonquiz, id=id)
    id_value = data.title_id
    if request.method == 'POST':
        data.delete()
        return redirect(reverse('ptraningmcqeditview', kwargs={'id': id_value}))
    return render(request ,template,{"data":data } )

def ptraningtestdelete(request,id):
    template="design/dashborad/python_language/traning/edit/test.html"
    count = Pythontraningcodeingquestions.objects.filter(title_id=id).count()

    somevalue=Pythontraingtitle.objects.filter(id=id)
    data1=Pythontraningcodeingquestions.objects.filter(title_id=id)
    
    paginator = Paginator(data1 , 1)  

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
        
    return render(request ,template,{"data":data,"somevalue":somevalue ,"count":count} )
    



# end edit traning python







# start edit practis

def pythonpracticeeditview(request):
    template="design/dashborad/python_language/practices/edit/view.html"
    data=Ptitlepractices.objects.all()
    data2=Ptitlepractices.objects.count()
    easy = Ptitlepractices.objects.filter(level="Easy").count()
    hard = Ptitlepractices.objects.filter(level="Hard").count()
    medium =Ptitlepractices.objects.filter(level="Medium").count()
    print(data)
    
    return render(request ,template,{"data":data,"count":data2,"easy":easy,"hard":hard,"medium":medium} )


def pythonpedittitle(request, titleid):
    
    template="design/dashborad/python_language/practices/edit/title.html"
    data=Ptitlepractices.objects.filter(id=titleid)
    edit = get_object_or_404(Ptitlepractices, id=titleid)
    if request.method == 'POST':
        title = request.POST.get('title')
        edit.title=title
        edit.save()

        return redirect('pythonpracticeeditview')
    return render(request, template, {'data': edit})

def pythonpdeletetitle(request, titleid):
    
    template="design/dashborad/cpp_language/practices/edit/title.html"
    data=Ptitlepractices.objects.filter(id=titleid)
    edit = get_object_or_404(Ptitlepractices, id=titleid)
    if request.method == 'POST':
       
        edit.delete()

        return redirect('pythonpracticeeditview')
    return render(request, template, {'data': edit})

def pythonpquestionview(request ,compiler_id):
    template="design/dashborad/python_language/practices/edit/questionview.html"


    data1=Pquestionpractices.objects.filter(title_id=compiler_id)
    count = Pquestionpractices.objects.filter(title_id=compiler_id).count()
    print("Count", count)
    
    paginator = Paginator(data1 , 1)  # Show 10 items per page

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        data = paginator.page(paginator.num_pages)
    
 
    return render(request ,template,{"data":data,"count":count} )

def pythonpquestionedit(request, questionupdate):
    data = get_object_or_404(Pquestionpractices, id=questionupdate)
    template="design/dashborad/python_language/practices/edit/editquestion.html"
    if request.method == 'POST':
        content = request.POST.get('content')
        data.content=content
        data.save()
        return redirect('pythonpracticeeditview')
    return render(request, template, {'data': data})

def pythonpdeletequestion(request, questiondelete_id):
    data = get_object_or_404(Pquestionpractices, id=questiondelete_id)
    template="design/dashborad/javatrainee/pquestionedit.html"
    if request.method == 'POST':
        data.delete()
        return redirect('pythonpracticeeditview')
    return render(request, template, {'data': data})
# end edit


# start edit testcas



def pythonptestcaseditview(request):
    template="design/dashborad/python_language/testcase/edit/view.html"
    data=Ptitletestcase.objects.all()
    data2=Ptitletestcase.objects.count()
    easy = Ptitletestcase.objects.filter(level="Easy").count()
    hard = Ptitletestcase.objects.filter(level="Hard").count()
    medium = Ptitletestcase.objects.filter(level="Medium").count()
    print(data)
    
    return render(request ,template,{"data":data,"count":data2,"easy":easy,"hard":hard,"medium":medium} )


def pythonptedittitle(request, titleid):
    
    template="design/dashborad/python_language/testcase/edit/title.html"
    data=Ptitletestcase.objects.filter(id=titleid)
    edit = get_object_or_404(Ptitletestcase, id=titleid)
    if request.method == 'POST':
        title = request.POST.get('title')
        edit.title=title
        edit.save()

        return redirect('pythonptestcaseditview')
    return render(request, template, {'data': edit})

def pythonptdeletetitle(request, titleid):
    
    template="design/dashborad/python_language/testcase/edit/title.html"
    data=Ptitletestcase.objects.filter(id=titleid)
    edit = get_object_or_404(Ptitletestcase, id=titleid)
    if request.method == 'POST':
       
        edit.delete()

        return redirect('pythonptestcaseditview')
    return render(request, template, {'data': edit})

def pythonptquestionview(request ,id):
    template="design/dashborad/python_language/testcase/edit/editquestion.html"


    data1=PtechnicalQuestionsTestcase.objects.filter(title_id=id)
    
    paginator = Paginator(data1 , 1)  

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    

 
    return render(request ,template,{"data":data} )

# def cppptquestionedit(request, questionupdate):
#     data = get_object_or_404(CtechnicalQuestionsTestcase, id=questionupdate)
#     template="design/dashborad/cpp_language/testcase/edit/editquestion.html"
#     if request.method == 'POST':
#         content = request.POST.get('content')
#         data.content=content
#         data.save()
#         return redirect('cppptestcaseditview')
#     return render(request, template, {'data': data})

def pythonptdeletequestion(request, questiondelete_id):
    data = get_object_or_404(PtechnicalQuestionsTestcase, id=questiondelete_id)
    template="design/dashborad/javatrainee/pquestionedit.html"
    if request.method == 'POST':
        data.delete()
        return redirect('pythonptestcaseditview')
    return render(request, template, {'data': data})
# end testcase edit

def ppracticeview(request):
    template="design/dashborad/python_language/practices/title.html"
    data=Ptitlepractices.objects.all()
    data2=Ptitlepractices.objects.count()
    easy = Ptitlepractices.objects.filter(level="Easy").count()
    hard = Ptitlepractices.objects.filter(level="Hard").count()
    medium = Ptitlepractices.objects.filter(level="Medium").count()
    print(data)
    
    return render(request ,template,{"data":data,"count":data2,"easy":easy,"hard":hard,"medium":medium} )
    # return render(request ,template,{} )

def ppcompiler(request,id):
    template="design/dashborad/python_language/practices/compiler.html"
    
    data1=Pquestionpractices.objects.filter(title_id=id)
    
    paginator = Paginator(data1 , 1)  

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    return render(request ,template,{"data":data} )

@login_required
def ptview(request):
    template="design/dashborad/python_language/testcase/index.html"
    data=Ptitletestcase.objects.all()
    data2=Ptitletestcase.objects.count()
    easy = Ptitletestcase.objects.filter(level="Easy").count()
    hard = Ptitletestcase.objects.filter(level="Hard").count()
    medium = Ptitletestcase.objects.filter(level="Medium").count()
    userid = request.user.id

    total_question = PtechnicalQuestionsTestcase.objects.count()
    success = Ptestcasereport.objects.filter(user_id=userid).count()
    success_percentage = (success / total_question) * 100 if total_question > 0 else 0
    success_percentage_rounded ="{:.0f}".format(success_percentage)
    print(data)
    print(data)
    
    return render(request ,template,{"data":data,"count":data2,"easy":easy,"hard":hard,"medium":medium,"report":success_percentage_rounded} )

def ptcompiler(request,id):
    template="design/dashborad/python_language/testcase/compiler.html"
    
    data1=PtechnicalQuestionsTestcase.objects.filter(title_id=id)
    
    paginator = Paginator(data1 , 1)  

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    

    return render(request ,template,{"data":data} )

def pttitleupload(request):
    template="design/dashborad/python_language/testcase/upload/title.html"
    if request.method == 'POST':
            
            data = request.POST.get('data2')
            data3 = request.POST.get('data3')
            print("data sented",data3)

            obj=Ptitletestcase()
            obj.title=data
            obj.level=data3
            obj.save()
            value="code"
            value2="code"

            if value==value2:
                response_data = {'success': True, 'message': 'Datasdfsadf processed successfully'}
                status_code = 200 
                 
            else:
                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500
            return JsonResponse(response_data, status=status_code)
    return render(request ,template,{} )
def ptestud(request):
    template="design/dashborad/python_language/testcase/upload/question.html"
    data=Ptitletestcase.objects.all()

    if request.method == 'POST':
            inputData = request.POST.get('inputData')
            sampleCode = request.POST.get('sampleCode')
            sampleinput = request.POST.get('sampleinput')
            sampleoutput = request.POST.get('sampleoutput')
            textcaseInput = request.POST.get('textcaseInput')
            textcaseOutput = request.POST.get('textcaseOutput')
            type = request.POST.get('selectedtype')

            obj=PtechnicalQuestionsTestcase()
            obj.questions= inputData
            obj.sinput= sampleinput
            obj.soutput=sampleoutput 
            obj.tinput= textcaseInput
            obj.toutput=textcaseOutput
            obj.samplecode=sampleCode
            obj.title_id=type

            obj.save()
            print(inputData,sampleCode , textcaseOutput,textcaseInput,sampleoutput,sampleinput)

    return render(request ,template,{"data":data} )

@login_required
def ptchecktest(request):
    template="design/dashborad/python_language/testcase/upload/title.html"
    userid = request.user.id
    if request.method == 'POST':
            
            data = request.POST.get('data2')
            data3 = request.POST.get('data3')
            data4 = request.POST.get('data4')
            print("data4",data4)

            print("data sented",data3)
            username=request.user.username
            
            check=PtechnicalQuestionsTestcase.objects.get(id=data ).toutput
            print("check2",data)
            print("check3",data3)

            if check==data3:
                       
                existing_obj = Ptestcasereport.objects.filter(testcase_id=data, user_id=userid).first()

                if existing_obj:
                    existing_obj.success = "success"
                    existing_obj.title_id = data4
                    existing_obj.save()
                    print("Sample output check compiler data", data, data4)
                else:
                    
                    obj = Ptestcasereport.objects.create(success="success", testcase_id=data, title_id=data4, user_id=userid)
                    print("New object created with testcase_id:", data)

                response_data = {'success': True, 'message': 'Test case has been executed successfully', "username": username}
                status_code = 200
                 
            else:
                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500
            return JsonResponse(response_data, status=status_code)
    return render(request ,template,{} )
    
    

def ptitleupload(request):
    template="design/dashborad/python_language/practices/upload/title.html"
    if request.method == 'POST':
            
            data = request.POST.get('data2')
            data3 = request.POST.get('data3')
            print("data sented",data3)

            obj=Ptitlepractices()
            obj.title=data
            obj.level=data3
            obj.save()
            value="code"
            value2="code"
            if value==value2:
                response_data = {'success': True, 'message': 'Datasdfsadf processed successfully'}
                status_code = 200 
            else:
                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500
            return JsonResponse(response_data, status=status_code)
    return render(request ,template,{} )

def ppracticeupload(request):
    template="design/dashborad/python_language/practices/upload/title.html"
    data=Ptitlepractices.objects.all()
    # print(data)
    if request.method == 'POST':
            type = request.POST.get('type')
            content = request.POST.get('content')
           
            obj=Pquestionpractices()
            obj.content=content
            obj.title_id=type
            obj.save()
        
   
    return render(request ,template,{"data":data} )

    # testcase

# end python language











# c language start

#  c traning
@login_required
def creportpage(request):
    template="design/dashborad/c_language/index.html"
    userid = request.user.id
    # totalquestion =CtechnicalQuestionsTestcase.objects.count()
    total_question = CtechnicalQuestionsTestcase.objects.count()
    success = Ctestcasereport.objects.filter(user_id=userid).count()
    success_percentage = (success / total_question) * 100 if total_question > 0 else 0
    success_percentage_rounded ="{:.1f}".format(success_percentage)
    showsuccess = Ctestcasereport.objects.filter(user_id=userid).all()

# Iterate over each instance in the queryset and print its id
    for instance in showsuccess:
        print(instance.id)

    failed =(total_question - success)
    failed_percentage = (failed / total_question) * 100 if total_question > 0 else 0
    failed_percentage_rounded ="{:.1f}".format(failed_percentage)

    print("total_question",total_question,success,failed)
    context = {

        'total': total_question,
        'success': success,
        'failed': failed,
        'success_percentage':success_percentage_rounded,
        'failed_percentage':failed_percentage_rounded



   
    }

    return render(request ,template,{'report':context,"showsuccess":showsuccess } )

@login_required
def ctraingmcqscore(request):
    template="design/dashborad/c_language/index.html"
    userid = request.user.id
    last_click = Ctraingclick.objects.filter(user_id=userid).last().click
    print("last_click" , last_click)
    # if last_click is not None:
    #     myitem = last_click.click
    #     print("Last click for current user:", myitem)

    try:
        dataget = get_object_or_404(Ctraningreport, titleid_id=last_click,user_id=userid)
        content = "Completed"
        dataget.status = content
        dataget.user_id = userid
        dataget.save()
    except:
        content = "Completed"
        obj = Ctraningreport()
        obj.titleid_id=last_click
        obj.status=content
        obj.user_id=userid
        obj.save()
    return render(request ,template,{} )


@login_required
def ctraningclick(request):
    template="design/dashborad/c_language/traning/upload/title.html"
    user=request.user
    click=user.id
    print()
    if request.method == 'POST':
        data = request.POST.get('data2')
        obj=Ctraingclick()
        obj.click=data
        obj.user_id=click
        obj.save()
        return redirect('ctraningmcq')
    return redirect('ctraningmcq')

@login_required
def ctraningchecktest(request):
    template="design/dashborad/c_language/testcase/upload/title.html"
    username=request.user.username
    username_cap = username.capitalize()
    if request.method == 'POST':
            
            data = request.POST.get('data2')
            data3 = request.POST.get('data3')
            print("data sented",data3)        
            check=Ctraningcodeingquestions.objects.get(id=data ).toutput
            print("check2",data)
            print("check3",data3)
            if check==data3:
                response_data = {'success': True, 'message': 'test case has been executed successfully',"username":username_cap}
                status_code = 200                 
            else:
                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500
            return JsonResponse(response_data, status=status_code)
    return render(request ,template,{} )
from django.contrib.sessions.models import Session
from django.db.models import Prefetch
@login_required
def ctraningview(request,session_id):
    if 'username' in request.session:
        session_id = request.session.session_key

        try:
            session = Session.objects.get(session_key=session_id)
            user_id = session.get_decoded().get('_auth_user_id')
            print("session user id:", user_id)

            # Retrieve the currently logged-in user
            current_user = request.user.id

            data = Ctraingtitle.objects.all()
           


            # Assuming Ctraingtitle and Ctraningreport are your Django models

            # Perform the left join and select distinct rows
            # queryset = Ctraingtitle.objects.filter(id__isnull=False).select_related('Ctrainingreport',user_id=current_user).distinct()
            # results = Ctraingtitle.objects.filter(ctraningreport__isnull=False).values_list('user', 'status', 'selecttype', 'title')

            # results = Ctraingtitle.objects.filter(ctraningreport__isnull=False).values_list('title', 'selecttype' , 'user__username', 'ctraningreport__status')
            results1 = Ctraingtitle.objects.all()
            resultss = Ctraningreport.objects.filter(user=current_user)
            merged_list = list(results1) + list(resultss)
            print("+++++++++++++++++++++++++++++++++++++++++++==")
            print("merged_list",merged_list)
            
            results = Ctraingtitle.objects.prefetch_related(
            Prefetch('ctraningreport_set', queryset=Ctraningreport.objects.filter(user_id=current_user))
            ).values_list( 'id','title', 'selecttype', 'ctraningreport__user__username', 'ctraningreport__status')
            print(results.query)

            iduser=request.user.username
            if results is not None:
                converted_results = []
                for item in results:
                    if item is not None:
                        result_dict = {
                            'check':iduser,
                            'id': item[0],
                            'title': item[1],
                            'selecttype': item[2],
                            'username':item[3],
                           

                            'status': item[4],
                        }
                        converted_results.append(result_dict)
                print("converted_results", converted_results)
            else:
                print("results is None")
            filtered_data = [dict(t) for t in {tuple(d.items()) for d in converted_results if d['id'] is not None}]
            print("filtered_data is None" ,filtered_data)


            data2 = Ctraingtitle.objects.all()
            print("data2",data2)

   
            template = "design/dashborad/c_language/traning/view.html"

            return render(request, template, {"data": merged_list, "data2": data2})

         
        except Session.DoesNotExist:
            return HttpResponse("Invalid session ID")
        except User.DoesNotExist:
            return HttpResponse("User not found")
    else:
        # User not logged in, redirect to login page
        return redirect('login')
    
def ctraningvideo(request,session_id,id):
    if 'username' in request.session:
        template="design/dashborad/c_language/traning/video.html"
        session = Session.objects.get(session_key=session_id)
        user_id = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=user_id)
        data2 =Cuploadvideosections.objects.filter(title_id=id)
        return render(request ,template,{"data":data2} )
    else:
        return redirect('login')

@login_required
def ctraningmcq(request):
    template="design/dashborad/c_language/traning/mcq.html"
    user_id = request.user.id
    last_click = Ctraingclick.objects.filter(user_id=user_id).last()
    if last_click is not None:
        myitem = last_click.click
        print("Last click for current user:", myitem)

        data =Cquiz.objects.filter(title_id=myitem)
        count =Cquiz.objects.filter(title_id=myitem).count()

    questions = [
    {   'id':quiz.id,
        'question': quiz.question,
        'answers': [
            {'text': quiz.option1, 'correct': quiz.answer1},
            {'text': quiz.option2, 'correct': quiz.answer2},
            {'text': quiz.option3, 'correct': quiz.answer3},
            {'text': quiz.option4, 'correct': quiz.answer4}
        ]
    }
    for quiz in data
   ]
    return render(request ,template,{"questions":questions ,"count":count} )

def ctraningcompiler(request):
    template="design/dashborad/c_language/traning/compiler.html"
    
    return render(request ,template,{} )

@login_required
def ctraningtest(request):
    template="design/dashborad/c_language/traning/test.html"
    user_id = request.user.id
    last_click = Ctraingclick.objects.filter(user_id=user_id).last()
    if last_click is not None:
        myitem = last_click.click
        print("Last click for current user:", myitem)
    
    data1=Ctraningcodeingquestions.objects.filter(title_id=myitem)
    
    paginator = Paginator(data1 , 1)  

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    

    return render(request ,template,{"data":data} )


# upload traning c
def ctraningviewupload(request):
    template="design/dashborad/c_language/traning/upload/title.html"
    data=Ctraingtitle.objects.all()

    if request.method == 'POST':
        title = request.POST.get('data2')
        chapter = request.POST.get('data3')
        obj =Ctraingtitle()
        obj.title=title
        obj.selecttype=chapter
        obj.save()
        return redirect('ctraningvideoupload')
       
    return render(request ,template,{"data":data} )
def ctraningvideoupload(request):
    template="design/dashborad/c_language/traning/upload/video.html"

    data=Ctraingtitle.objects.all()

    if request.method == 'POST' and request.FILES.get('video_file'):
        demoone="c"
        title = request.POST.get('type')
        video_file = request.FILES['video_file']
        con = request.POST.get('content')
        Cuploadvideosections.objects.create(titleone=demoone ,title_id=title, video_file=video_file , content= con)
        return redirect("ctraningmcqupload")
     
    
    return render(request ,template,{"data":data} )

def ctraningmcqupload(request):
    template="design/dashborad/c_language/traning/upload/mcq.html"
    
    data=Ctraingtitle.objects.all()
    if request.method == 'POST':
        type = request.POST.get('type')

        question = request.POST.get('question')
        option1 = request.POST.get('optionone')
        option2 = request.POST.get('optiontwo')
        option3 = request.POST.get('optionthree')
        option4 = request.POST.get('optionfour')
        answer1 = request.POST.get('answerone')
        answer2 = request.POST.get('answertwo')
        answer3 = request.POST.get('answerthree')
        answer4 = request.POST.get('answerfour')
        obj=Cquiz()
        obj.question=question
        obj.option1=option1
        obj.option2=option2
        obj.option3=option3
        obj.option4=option4
        obj.answer1=answer1
        obj.answer2=answer2
        obj.answer3=answer3
        obj.answer4=answer4
        obj.title_id=type
        obj.save()

        # return redirect("apptitleupload")

       
    return render(request, template, {"data":data})

def ctraningtestupload(request):
    template="design/dashborad/c_language/traning/upload/test.html"
    data=Ctraingtitle.objects.all()

    if request.method == 'POST':
            inputData = request.POST.get('inputData')
            sampleCode = request.POST.get('sampleCode')
            sampleinput = request.POST.get('sampleinput')
            sampleoutput = request.POST.get('sampleoutput')
            textcaseInput = request.POST.get('textcaseInput')
            textcaseOutput = request.POST.get('textcaseOutput')
            type = request.POST.get('selectedtype')

            obj=Ctraningcodeingquestions()
            obj.questions= inputData
            obj.sinput= sampleinput
            obj.soutput=sampleoutput 
            obj.tinput= textcaseInput
            obj.toutput=textcaseOutput
            obj.samplecode=sampleCode
            obj.title_id=type

            obj.save()
            print(inputData,sampleCode , textcaseOutput,textcaseInput,sampleoutput,sampleinput)

    return render(request ,template,{"data":data} )

# edit traning c
    # -- > view
def ctraningvieweditview(request):
    template="design/dashborad/c_language/traning/edit/view.html"
    data=Ctraingtitle.objects.all()
    user=request.user
    print("print",user.id)

    return render(request ,template,{"data":data} )

def ctraningvideoeditview(request,id):
    template="design/dashborad/c_language/traning/edit/videoview.html"
    data2 =Cuploadvideosections.objects.filter(title_id=id)
    return render(request ,template,{"data":data2} )


def ctraningmcqeditview(request,id):
    template="design/dashborad/c_language/traning/edit/mcqview.html"
    data2 =Cquiz.objects.filter(title_id=id)
    paginator = Paginator(data2 , 1)  # Show 10 items per page

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        data = paginator.page(paginator.num_pages)


    return render(request ,template,{"data":data , } )


    #  --> edit
def ctraningviewedit(request,id):
    template="design/dashborad/c_language/traning/editupload/titleupload.html"
    data = get_object_or_404(Ctraingtitle, id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        data.title=title
        data.save()
        return redirect("ctraningviewupload")
    return render(request ,template,{"data":data} )

def ctraningvideoedit(request,id):
    template="design/dashborad/c_language/traning/editupload/video.html"
    data = get_object_or_404(Cuploadvideosections, id=id)

    if request.method == 'POST':
        video_file = request.FILES['video_file']
        con = request.POST.get('content')
        data.titleone="edione"
        data.video_file=video_file
        data.content= con
        data.save()

        return redirect("ctraningviewupload")
    return render(request ,template,{"data":data} )

def ctraningmcqedit(request,id):
    template="design/dashborad/c_language/traning/editupload/mcq.html"
    data = get_object_or_404(Cquiz, id=id)
    id_value = data.title_id
    if request.method == 'POST':
        question = request.POST.get('question')
        option1 = request.POST.get('optionone')
        option2 = request.POST.get('optiontwo')
        option3 = request.POST.get('optionthree')
        option4 = request.POST.get('optionfour')
        answer1 = request.POST.get('answerone')
        answer2 = request.POST.get('answertwo')
        answer3 = request.POST.get('answerthree')
        answer4 = request.POST.get('answerfour')
        data.question=question
        data.option1=option1
        data.option2=option2
        data.option3=option3
        data.option4=option4
        data.answer1=answer1
        data.answer2=answer2
        data.answer3=answer3
        data.answer4=answer4
        data.save()
        return redirect(reverse('ctraningmcqeditview', kwargs={'id': id_value}))
    return render(request ,template,{"data":data} )
    # delete
def ctraningviewdelete(request,id):
    template="design/dashborad/c_language/traning/upload/title.html"
    data = get_object_or_404(Ctraingtitle, id=id)

    if request.method == 'POST':
        data.delete()
        return redirect("ctraningviewupload")
    return render(request ,template,{"data":data} ) 

def ctraningvideodelete(request,id):
    template="design/dashborad/c_language/traning/upload/video.html"
    data = get_object_or_404(Cuploadvideosections, id=id)

    if request.method == 'POST':
        data.delete()
        return redirect("ctraningviewupload")
    return render(request ,template,{"data":data} )

def ctraningmcqdelete(request,id):
    template="design/dashborad/c_language/traning/upload/mcq.html"
    data = get_object_or_404(Cquiz, id=id)
    id_value = data.title_id
    if request.method == 'POST':
        data.delete()
        return redirect(reverse('ctraningmcqeditview', kwargs={'id': id_value}))
    return render(request ,template,{"data":data } )

def ctraningtestdelete(request,id):
    template="design/dashborad/c_language/traning/edit/test.html"
    count = Ctraningcodeingquestions.objects.filter(title_id=id).count()

    somevalue=Ctraingtitle.objects.filter(id=id)
    data1=Ctraningcodeingquestions.objects.filter(title_id=id)
    
    paginator = Paginator(data1 , 1)  

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    return render(request ,template,{"data":data,"somevalue":somevalue ,"count":count} )
    



# end edit traning c


# start edit practis

def cpracticeeditview(request):
    template="design/dashborad/c_language/practices/edit/view.html"
    data=Ctitlepractices.objects.all()
    data2=Ctitlepractices.objects.count()
    easy = Ctitlepractices.objects.filter(level="Easy").count()
    hard = Ctitlepractices.objects.filter(level="Hard").count()
    medium = Ctitlepractices.objects.filter(level="Medium").count()
    print(data)
    
    return render(request ,template,{"data":data,"count":data2,"easy":easy,"hard":hard,"medium":medium} )


def cpedittitle(request, titleid):
    
    template="design/dashborad/c_language/practices/edit/title.html"
    data=Ctitlepractices.objects.filter(id=titleid)
    edit = get_object_or_404(Ctitlepractices, id=titleid)
    if request.method == 'POST':
        title = request.POST.get('title')
        edit.title=title
        edit.save()

        return redirect('cpracticeeditview')
    return render(request, template, {'data': edit})

def cpdeletetitle(request, titleid):
    
    template="design/dashborad/cpp_language/practices/edit/title.html"
    data=Ctitlepractices.objects.filter(id=titleid)
    edit = get_object_or_404(Ctitlepractices, id=titleid)
    if request.method == 'POST':
       
        edit.delete()

        return redirect('cpracticeeditview')
    return render(request, template, {'data': edit})

def cpquestionview(request ,compiler_id):
    template="design/dashborad/c_language/practices/edit/questionview.html"


    data1=Cquestionpractices.objects.filter(title_id=compiler_id)
    count = Cquestionpractices.objects.filter(title_id=compiler_id).count()
    print("Count", count)
    
    paginator = Paginator(data1 , 1)  # Show 10 items per page

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        data = paginator.page(paginator.num_pages)
    
 
    return render(request ,template,{"data":data,"count":count} )

def cpquestionedit(request, questionupdate):
    data = get_object_or_404(Cquestionpractices, id=questionupdate)
    template="design/dashborad/c_language/practices/edit/editquestion.html"
    if request.method == 'POST':
        content = request.POST.get('content')
        data.content=content
        data.save()
        return redirect('cpracticeeditview')
    return render(request, template, {'data': data})

def cpdeletequestion(request, questiondelete_id):
    data = get_object_or_404(Cquestionpractices, id=questiondelete_id)
    template="design/dashborad/javatrainee/pquestionedit.html"
    if request.method == 'POST':
        data.delete()
        return redirect('cpracticeeditview')
    return render(request, template, {'data': data})
# end edit

# c start
# start edit testcas





def cptestcaseditview(request):
    template="design/dashborad/c_language/testcase/edit/view.html"
    # data=Ctitletestcase.objects.all()
    data=CtechnicalQuestionsTestcase.objects.all()

    data2=Ctitletestcase.objects.count()
    easy = Ctitletestcase.objects.filter(level="Easy").count()
    hard = Ctitletestcase.objects.filter(level="Hard").count()
    medium = Ctitletestcase.objects.filter(level="Medium").count()
    
    print(data)
    
    return render(request ,template,{"data":data,"count":data2,"easy":easy,"hard":hard,"medium":medium} )


def cptedittitle(request, titleid):
    
    template="design/dashborad/c_language/testcase/edit/title.html"
    data=Ctitletestcase.objects.filter(id=titleid)
    edit = get_object_or_404(Ctitletestcase, id=titleid)
    if request.method == 'POST':
        title = request.POST.get('title')
        edit.title=title
        edit.save()

        return redirect('cptestcaseditview')
    return render(request, template, {'data': edit})

def cptdeletetitle(request, titleid):
    
    template="design/dashborad/c_language/testcase/edit/title.html"
    data=Ctitletestcase.objects.filter(id=titleid)
    edit = get_object_or_404(Ctitletestcase, id=titleid)
    if request.method == 'POST':
       
        edit.delete()

        return redirect('cptestcaseditview')
    return render(request, template, {'data': edit})

def cptquestionview(request ,id):
    template="design/dashborad/c_language/testcase/edit/editquestion.html"


    data1=CtechnicalQuestionsTestcase.objects.filter(title_id=id)
    
    paginator = Paginator(data1 , 1)  

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    

 
    return render(request ,template,{"data":data} )

# def cppptquestionedit(request, questionupdate):
#     data = get_object_or_404(CtechnicalQuestionsTestcase, id=questionupdate)
#     template="design/dashborad/cpp_language/testcase/edit/editquestion.html"
#     if request.method == 'POST':
#         content = request.POST.get('content')
#         data.content=content
#         data.save()
#         return redirect('cppptestcaseditview')
#     return render(request, template, {'data': data})

def cptdeletequestion(request, questiondelete_id):
    data = get_object_or_404(CtechnicalQuestionsTestcase, id=questiondelete_id)
    template="design/dashborad/javatrainee/pquestionedit.html"
    if request.method == 'POST':
        data.delete()
        return redirect('cptestcaseditview')
    return render(request, template, {'data': data})
# end testcase edit

def cpracticeview(request):
    template="design/dashborad/c_language/practices/title.html"
    data=Ctitlepractices.objects.all()
    data2=Ctitlepractices.objects.count()
    easy = Ctitlepractices.objects.filter(level="Easy").count()
    hard = Ctitlepractices.objects.filter(level="Hard").count()
    medium = Ctitlepractices.objects.filter(level="Medium").count()
    print(data)
    
    return render(request ,template,{"data":data,"count":data2,"easy":easy,"hard":hard,"medium":medium} )
    # return render(request ,template,{} )

def cpcompiler(request,id):
    template="design/dashborad/c_language/practices/compiler.html"
    
    data1=Cquestionpractices.objects.filter(title_id=id)
    
    paginator = Paginator(data1 , 1)  

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    return render(request ,template,{"data":data} )
@login_required
def ctview(request):
    template="design/dashborad/c_language/testcase/index.html"
    data=Ctitletestcase.objects.all()
    data2=Ctitletestcase.objects.count()
    easy = Ctitletestcase.objects.filter(level="Easy").count()
    hard = Ctitletestcase.objects.filter(level="Hard").count()
    medium = Ctitletestcase.objects.filter(level="Medium").count()
    userid = request.user.id
    # totalquestion =CtechnicalQuestionsTestcase.objects.count()
    total_question = CtechnicalQuestionsTestcase.objects.count()
    success = Ctestcasereport.objects.filter(user_id=userid).count()
    success_percentage = (success / total_question) * 100 if total_question > 0 else 0
    success_percentage_rounded ="{:.1f}".format(success_percentage)
    print(data)
    
    return render(request ,template,{"data":data,"count":data2,"easy":easy,"hard":hard,"medium":medium ,"report":success_percentage_rounded} )

def ctcompiler(request,id):
    template="design/dashborad/c_language/testcase/compiler.html"
    
    data1=CtechnicalQuestionsTestcase.objects.filter(title_id=id)
    
    paginator = Paginator(data1 , 1)  

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    

    return render(request ,template,{"data":data} )

def cttitleupload(request):
    template="design/dashborad/c_language/testcase/upload/title.html"
    if request.method == 'POST':
            
            data = request.POST.get('data2')
            data3 = request.POST.get('data3')
            print("data sented",data3)

            obj=Ctitletestcase()
            obj.title=data
            obj.level=data3
            obj.save()
            value="code"
            value2="code"

            if value==value2:
                response_data = {'success': True, 'message': 'Datasdfsadf processed successfully'}
                status_code = 200 
                 
            else:
                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500
            return JsonResponse(response_data, status=status_code)
    return render(request ,template,{} )
def ctestud(request):
    template="design/dashborad/c_language/testcase/upload/question.html"
    data=Ctitletestcase.objects.all()

    if request.method == 'POST':
            inputData = request.POST.get('inputData')
            sampleCode = request.POST.get('sampleCode')
            sampleinput = request.POST.get('sampleinput')
            sampleoutput = request.POST.get('sampleoutput')
            textcaseInput = request.POST.get('textcaseInput')
            textcaseOutput = request.POST.get('textcaseOutput')
            type = request.POST.get('selectedtype')

            obj=CtechnicalQuestionsTestcase()
            obj.questions= inputData
            obj.sinput= sampleinput
            obj.soutput=sampleoutput 
            obj.tinput= textcaseInput
            obj.toutput=textcaseOutput
            obj.samplecode=sampleCode
            obj.title_id=type

            obj.save()
            print(inputData,sampleCode , textcaseOutput,textcaseInput,sampleoutput,sampleinput)

    return render(request ,template,{"data":data} )
@login_required
def ctchecktest(request):
    template="design/dashborad/c_language/testcase/upload/title.html"
    userid = request.user.id
    if request.method == 'POST':
            
            data = request.POST.get('data2')
            data3 = request.POST.get('data3')
            data4 = request.POST.get('data4')
            print("data4",data4)

            print("data sented",data3)
            username=request.user.username
            
            check=CtechnicalQuestionsTestcase.objects.get(id=data ).toutput
            print("check2",data)
            print("check3",data3)

            if check==data3:
                       
                existing_obj = Ctestcasereport.objects.filter(testcase_id=data, user_id=userid).first()

                if existing_obj:
                    existing_obj.success = "success"
                    existing_obj.title_id = data4
                    existing_obj.save()
                    print("Sample output check compiler data", data, data4)
                else:
                    
                    obj = Ctestcasereport.objects.create(success="success", testcase_id=data, title_id=data4, user_id=userid)
                    print("New object created with testcase_id:", data)

                response_data = {'success': True, 'message': 'Test case has been executed successfully', "username": username}
                status_code = 200
                 
            else:
                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500
            return JsonResponse(response_data, status=status_code)
    return render(request ,template,{} )
    

def ctitleupload(request):
    template="design/dashborad/c_language/practices/upload/title.html"
    if request.method == 'POST':
            
            data = request.POST.get('data2')
            data3 = request.POST.get('data3')
            print("data sented",data3)

            obj=Ctitlepractices()
            obj.title=data
            obj.level=data3
            obj.save()
            value="code"
            value2="code"
            if value==value2:
                response_data = {'success': True, 'message': 'Datasdfsadf processed successfully'}
                status_code = 200 
            else:
                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500
            return JsonResponse(response_data, status=status_code)
    return render(request ,template,{} )

def cpracticeupload(request):
    template="design/dashborad/c_language/practices/upload/title.html"
    data=Ctitlepractices.objects.all()
    data2=Ctitlepractices.objects.count()
    easy = Ctitlepractices.objects.filter(level="Easy").count()
    hard = Ctitlepractices.objects.filter(level="Hard").count()
    medium = Ctitlepractices.objects.filter(level="Medium").count()
    
    uploaddata=Ctitlepractices.objects.all()
    # print(data)
    if request.method == 'POST':
            type = request.POST.get('type')
            content = request.POST.get('content')
           
            obj=Cquestionpractices()
            obj.content=content
            obj.title_id=type
            obj.save()
        
   
    return render(request ,template,{"uploaddata":uploaddata,"data":data,"count":data2,"easy":easy,"hard":hard,"medium":medium} )

    # testcase

# end c language



# c++ start
# start edit practis


# python language start


#  python traning
@login_required
def cppreportpage(request):
    template="design/dashborad/cpp_language/index.html"
    userid = request.user.id
    # totalquestion =CtechnicalQuestionsTestcase.objects.count()
    total_question = CpponetechnicalQuestionsTestcase.objects.count()
    success = Cpptestcasereport.objects.filter(user_id=userid).count()
    success_percentage = (success / total_question) * 100 if total_question > 0 else 0
    success_percentage_rounded ="{:.1f}".format(success_percentage)
    showsuccess = Cpptestcasereport.objects.filter(user_id=userid).all()

# Iterate over each instance in the queryset and print its id
    for instance in showsuccess:
        print(instance.id)

    failed =(total_question - success)
    failed_percentage = (failed / total_question) * 100 if total_question > 0 else 0
    failed_percentage_rounded ="{:.1f}".format(failed_percentage)

    print("total_question",total_question,success,failed)
    context = {

        'total': total_question,
        'success': success,
        'failed': failed,
        'success_percentage':success_percentage_rounded,
        'failed_percentage':failed_percentage_rounded



   
    }

    return render(request ,template,{'report':context,"showsuccess":showsuccess} )


@login_required
def cpptraningclick(request):
    template="design/dashborad/cpp_language/traning/upload/title.html"
    user=request.user
    click=user.id
    print()
    if request.method == 'POST':
        data = request.POST.get('data2')
        obj=Cpptraingclick()
        obj.click=data
        obj.user_id=click
        obj.save()
        return redirect('cpptraningmcq')
    return redirect('cpptraningmcq')

@login_required
def cpptraningchecktest(request):
    template="design/dashborad/cpp_language/testcase/upload/title.html"
    username=request.user.username
    username_cap = username.capitalize()
    if request.method == 'POST':
            
            data = request.POST.get('data2')
            data3 = request.POST.get('data3')
            print("data sented",data3)        
            check=Cpptraningcodeingquestions.objects.get(id=data ).toutput
            print("check2",data)
            print("check3",data3)
            if check==data3:
                response_data = {'success': True, 'message': 'test case has been executed successfully',"username":username_cap}
                status_code = 200                 
            else:
                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500
            return JsonResponse(response_data, status=status_code)
    return render(request ,template,{} )

@login_required
def cpptraningview(request):
    template="design/dashborad/cpp_language/traning/view.html"
    data=Cpptraingtitle.objects.all()
    user=request.user
    print("print",user.id)

    return render(request ,template,{"data":data} )
def cpptraningvideo(request,id):
    template="design/dashborad/cpp_language/traning/video.html"
    data2 =Cppuploadvideosections.objects.filter(title_id=id)
    return render(request ,template,{"data":data2} )

@login_required
def cpptraningmcq(request):
    template="design/dashborad/cpp_language/traning/mcq.html"
    user_id = request.user.id
    last_click = Cpptraingclick.objects.filter(user_id=user_id).last()
    if last_click is not None:
        myitem = last_click.click
        print("Last click for current user:", myitem)

        data =Cppquiz.objects.filter(title_id=myitem)
        count =Cppquiz.objects.filter(title_id=myitem).count()

    questions = [
    {   'id':quiz.id,
        'question': quiz.question,
        'answers': [
            {'text': quiz.option1, 'correct': quiz.answer1},
            {'text': quiz.option2, 'correct': quiz.answer2},
            {'text': quiz.option3, 'correct': quiz.answer3},
            {'text': quiz.option4, 'correct': quiz.answer4}
        ]
    }
    for quiz in data
   ]
    return render(request ,template,{"questions":questions ,"count":count} )

def cpptraningcompiler(request):
    template="design/dashborad/cpp_language/traning/compiler.html"
    
    return render(request ,template,{} )

@login_required
def cpptraningtest(request):
    template="design/dashborad/cpp_language/traning/test.html"
    user_id = request.user.id
    last_click = Cpptraingclick.objects.filter(user_id=user_id).last()
    if last_click is not None:
        myitem = last_click.click
        print("Last click for current user:", myitem)
    
    data1=Cpptraningcodeingquestions.objects.filter(title_id=myitem)
    
    paginator = Paginator(data1 , 1)  

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    

    return render(request ,template,{"data":data} )


# upload traning c
def cpptraningviewupload(request):
    template="design/dashborad/cpp_language/traning/upload/title.html"
    data=Cpptraingtitle.objects.all()

    if request.method == 'POST':
        title = request.POST.get('data2')
        chapter = request.POST.get('data3')
        obj =Cpptraingtitle()
        obj.title=title
        obj.selecttype=chapter
        obj.save()
        return redirect('cpptraningvideoupload')
       
    return render(request ,template,{"data":data} )
def cpptraningvideoupload(request):
    template="design/dashborad/cpp_language/traning/upload/video.html"

    data=Cpptraingtitle.objects.all()

    if request.method == 'POST' and request.FILES.get('video_file'):
        demoone="c"
        title = request.POST.get('type')
        video_file = request.FILES['video_file']
        con = request.POST.get('content')
        Cppuploadvideosections.objects.create(titleone=demoone ,title_id=title, video_file=video_file , content= con)
        return redirect("cpptraningmcqupload")
     
    
    return render(request ,template,{"data":data} )

def cpptraningmcqupload(request):
    template="design/dashborad/cpp_language/traning/upload/mcq.html"
    
    data=Cpptraingtitle.objects.all()
    if request.method == 'POST':
        type = request.POST.get('type')

        question = request.POST.get('question')
        option1 = request.POST.get('optionone')
        option2 = request.POST.get('optiontwo')
        option3 = request.POST.get('optionthree')
        option4 = request.POST.get('optionfour')
        answer1 = request.POST.get('answerone')
        answer2 = request.POST.get('answertwo')
        answer3 = request.POST.get('answerthree')
        answer4 = request.POST.get('answerfour')
        obj=Cppquiz()
        obj.question=question
        obj.option1=option1
        obj.option2=option2
        obj.option3=option3
        obj.option4=option4
        obj.answer1=answer1
        obj.answer2=answer2
        obj.answer3=answer3
        obj.answer4=answer4
        obj.title_id=type
        obj.save()

        # return redirect("apptitleupload")

       
    return render(request, template, {"data":data})

def cpptraningtestupload(request):
    template="design/dashborad/cpp_language/traning/upload/test.html"
    data=Cpptraingtitle.objects.all()

    if request.method == 'POST':
            inputData = request.POST.get('inputData')
            sampleCode = request.POST.get('sampleCode')
            sampleinput = request.POST.get('sampleinput')
            sampleoutput = request.POST.get('sampleoutput')
            textcaseInput = request.POST.get('textcaseInput')
            textcaseOutput = request.POST.get('textcaseOutput')
            type = request.POST.get('selectedtype')

            obj=Cpptraningcodeingquestions()
            obj.questions= inputData
            obj.sinput= sampleinput
            obj.soutput=sampleoutput 
            obj.tinput= textcaseInput
            obj.toutput=textcaseOutput
            obj.samplecode=sampleCode
            obj.title_id=type

            obj.save()
            print(inputData,sampleCode , textcaseOutput,textcaseInput,sampleoutput,sampleinput)

    return render(request ,template,{"data":data} )

# edit traning c
    # -- > view
def cpptraningvieweditview(request):
    template="design/dashborad/cpp_language/traning/edit/view.html"
    data=Cpptraingtitle.objects.all()
    user=request.user
    print("print",user.id)

    return render(request ,template,{"data":data} )

def cpptraningvideoeditview(request,id):
    template="design/dashborad/cpp_language/traning/edit/videoview.html"
    data2 =Cppuploadvideosections.objects.filter(title_id=id)
    return render(request ,template,{"data":data2} )


def cpptraningmcqeditview(request,id):
    template="design/dashborad/cpp_language/traning/edit/mcqview.html"
    data2 =Cppquiz.objects.filter(title_id=id)
    paginator = Paginator(data2 , 1)  # Show 10 items per page

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        data = paginator.page(paginator.num_pages)


    return render(request ,template,{"data":data , } )


    #  --> edit
def cpptraningviewedit(request,id):
    template="design/dashborad/cpp_language/traning/editupload/titleupload.html"
    data = get_object_or_404(Cpptraingtitle, id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        data.title=title
        data.save()
        return redirect("cpptraningvieweditview")
    return render(request ,template,{"data":data} )

def cpptraningvideoedit(request,id):
    template="design/dashborad/cpp_language/traning/editupload/video.html"
    data = get_object_or_404(Cppuploadvideosections, id=id)

    if request.method == 'POST':
        video_file = request.FILES['video_file']
        con = request.POST.get('content')
        data.titleone="edione"
        data.video_file=video_file
        data.content= con
        data.save()

        return redirect("cpptraningvieweditview")
    return render(request ,template,{"data":data} )

def cpptraningmcqedit(request,id):
    template="design/dashborad/cpp_language/traning/editupload/mcq.html"
    data = get_object_or_404(Cppquiz, id=id)
    id_value = data.title_id
    if request.method == 'POST':
        question = request.POST.get('question')
        option1 = request.POST.get('optionone')
        option2 = request.POST.get('optiontwo')
        option3 = request.POST.get('optionthree')
        option4 = request.POST.get('optionfour')
        answer1 = request.POST.get('answerone')
        answer2 = request.POST.get('answertwo')
        answer3 = request.POST.get('answerthree')
        answer4 = request.POST.get('answerfour')
        data.question=question
        data.option1=option1
        data.option2=option2
        data.option3=option3
        data.option4=option4
        data.answer1=answer1
        data.answer2=answer2
        data.answer3=answer3
        data.answer4=answer4
        data.save()
        return redirect(reverse('cpptraningmcqeditview', kwargs={'id': id_value}))
    return render(request ,template,{"data":data} )
    # delete
def cpptraningviewdelete(request,id):
    template="design/dashborad/cpp_language/traning/upload/title.html"
    data = get_object_or_404(Cpptraingtitle, id=id)

    if request.method == 'POST':
        data.delete()
        return redirect("cpptraningvieweditview")
    return render(request ,template,{"data":data} ) 

def cpptraningvideodelete(request,id):
    template="design/dashborad/cpp_language/traning/upload/video.html"
    data = get_object_or_404(Cppuploadvideosections, id=id)

    if request.method == 'POST':
        data.delete()
        return redirect("cpptraningvieweditview")
    return render(request ,template,{"data":data} )

def cpptraningmcqdelete(request,id):
    template="design/dashborad/cpp_language/traning/upload/mcq.html"
    data = get_object_or_404(Cppquiz, id=id)
    id_value = data.title_id
    if request.method == 'POST':
        data.delete()
        return redirect(reverse('cpptraningmcqeditview', kwargs={'id': id_value}))
    return render(request ,template,{"data":data } )

def cpptraningtestdelete(request,id):
    template="design/dashborad/cpp_language/traning/edit/test.html"
    count = Cpptraningcodeingquestions.objects.filter(title_id=id).count()

    somevalue=Cpptraingtitle.objects.filter(id=id)
    data1=Cpptraningcodeingquestions.objects.filter(title_id=id)
    
    paginator = Paginator(data1 , 1)  

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
        
    return render(request ,template,{"data":data,"somevalue":somevalue ,"count":count} )
    



# end edit traning c++






def cpppracticeeditview(request):
    template="design/dashborad/cpp_language/practices/edit/view.html"
    data=Cpponetitlepractices.objects.all()
    data2=Cpponetitlepractices.objects.count()
    easy = Cpponetitlepractices.objects.filter(level="Easy").count()
    hard = Cpponetitlepractices.objects.filter(level="Hard").count()
    medium = Cpponetitlepractices.objects.filter(level="Medium").count()
    print(data)
    
    return render(request ,template,{"data":data,"count":data2,"easy":easy,"hard":hard,"medium":medium} )


def cpppedittitle(request, titleid):
    
    template="design/dashborad/cpp_language/practices/edit/title.html"
    data=Cpponetitlepractices.objects.filter(id=titleid)
    edit = get_object_or_404(Cpponetitlepractices, id=titleid)
    if request.method == 'POST':
        title = request.POST.get('title')
        edit.title=title
        edit.save()

        return redirect('cpppracticeeditview')
    return render(request, template, {'data': edit})

def cpppdeletetitle(request, titleid):
    
    template="design/dashborad/cpp_language/practices/edit/title.html"
    data=Cpponetitlepractices.objects.filter(id=titleid)
    edit = get_object_or_404(Cpponetitlepractices, id=titleid)
    if request.method == 'POST':
       
        edit.delete()

        return redirect('cpppracticeeditview')
    return render(request, template, {'data': edit})

def cpppquestionview(request ,compiler_id):
    template="design/dashborad/cpp_language/practices/edit/questionview.html"


    data1=Cpponepquestionpractices.objects.filter(title_id=compiler_id)
    count = Cpponepquestionpractices.objects.filter(title_id=compiler_id).count()
    print("Count", count)
    
    paginator = Paginator(data1 , 1)  # Show 10 items per page

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        data = paginator.page(paginator.num_pages)
    
 
    return render(request ,template,{"data":data,"count":count} )

def cpppquestionedit(request, questionupdate):
    data = get_object_or_404(Cpponepquestionpractices, id=questionupdate)
    template="design/dashborad/cpp_language/practices/edit/editquestion.html"
    if request.method == 'POST':
        content = request.POST.get('content')
        data.content=content
        data.save()
        return redirect('cpppracticeeditview')
    return render(request, template, {'data': data})

def cpppdeletequestion(request, questiondelete_id):
    data = get_object_or_404(Cpponepquestionpractices, id=questiondelete_id)
    template="design/dashborad/javatrainee/pquestionedit.html"
    if request.method == 'POST':
        data.delete()
        return redirect('cpppracticeeditview')
    return render(request, template, {'data': data})
# end edit

# c++ start
# start edit testcase

def cppptestcaseditview(request):
    template="design/dashborad/cpp_language/testcase/edit/view.html"
    data=Cpponetitletestcase.objects.all()
    data2=Cpponetitletestcase.objects.count()
    easy = Cpponetitletestcase.objects.filter(level="Easy").count()
    hard = Cpponetitletestcase.objects.filter(level="Hard").count()
    medium = Cpponetitletestcase.objects.filter(level="Medium").count()
    print(data)
    
    return render(request ,template,{"data":data,"count":data2,"easy":easy,"hard":hard,"medium":medium} )


def cppptedittitle(request, titleid):
    
    template="design/dashborad/cpp_language/testcase/edit/title.html"
    data=Cpponetitletestcase.objects.filter(id=titleid)
    edit = get_object_or_404(Cpponetitletestcase, id=titleid)
    if request.method == 'POST':
        title = request.POST.get('title')
        edit.title=title
        edit.save()

        return redirect('cppptestcaseditview')
    return render(request, template, {'data': edit})

def cppptdeletetitle(request, titleid):
    
    template="design/dashborad/cpp_language/testcase/edit/title.html"
    data=Cpponetitletestcase.objects.filter(id=titleid)
    edit = get_object_or_404(Cpponetitletestcase, id=titleid)
    if request.method == 'POST':
       
        edit.delete()

        return redirect('cppptestcaseditview')
    return render(request, template, {'data': edit})

def cppptquestionview(request ,id):
    template="design/dashborad/cpp_language/testcase/edit/editquestion.html"


    data1=CpponetechnicalQuestionsTestcase.objects.filter(title_id=id)
    
    paginator = Paginator(data1 , 1)  

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    

 
    return render(request ,template,{"data":data} )

# def cppptquestionedit(request, questionupdate):
#     data = get_object_or_404(CpponetechnicalQuestionsTestcase, id=questionupdate)
#     template="design/dashborad/cpp_language/testcase/edit/editquestion.html"
#     if request.method == 'POST':
#         content = request.POST.get('content')
#         data.content=content
#         data.save()
#         return redirect('cppptestcaseditview')
#     return render(request, template, {'data': data})

def cppptdeletequestion(request, questiondelete_id):
    data = get_object_or_404(CpponetechnicalQuestionsTestcase, id=questiondelete_id)
    template="design/dashborad/javatrainee/pquestionedit.html"
    if request.method == 'POST':
        data.delete()
        return redirect('cppptestcaseditview')
    return render(request, template, {'data': data})
# end edit

def cpppracticeview(request):
    template="design/dashborad/cpp_language/practices/title.html"
    data=Cpponetitlepractices.objects.all()
    data2=Cpponetitlepractices.objects.count()
    easy = Cpponetitlepractices.objects.filter(level="Easy").count()
    hard = Cpponetitlepractices.objects.filter(level="Hard").count()
    medium = Cpponetitlepractices.objects.filter(level="Medium").count()
    print(data)
    
    return render(request ,template,{"data":data,"count":data2,"easy":easy,"hard":hard,"medium":medium} )
    # return render(request ,template,{} )

def cpppcompiler(request,id):
    template="design/dashborad/cpp_language/practices/compiler.html"
    
    data1=Cpponepquestionpractices.objects.filter(title_id=id)
    
    paginator = Paginator(data1 , 1)  

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    return render(request ,template,{"data":data} )
@login_required
def cpptview(request):
    template="design/dashborad/cpp_language/testcase/index.html"
    data=Cpponetitletestcase.objects.all()
    data2=Cpponetitletestcase.objects.count()
    easy = Cpponetitletestcase.objects.filter(level="Easy").count()
    hard = Cpponetitletestcase.objects.filter(level="Hard").count()
    medium = Cpponetitletestcase.objects.filter(level="Medium").count()
    userid = request.user.id
    # totalquestion =CtechnicalQuestionsTestcase.objects.count()
    total_question = CpponetechnicalQuestionsTestcase.objects.count()
    success = Cpptestcasereport.objects.filter(user_id=userid).count()
    success_percentage = (success / total_question) * 100 if total_question > 0 else 0
    success_percentage_rounded ="{:.0f}".format(success_percentage)
    print(data)
    
    return render(request ,template,{"data":data,"count":data2,"easy":easy,"hard":hard,"medium":medium,"report":success_percentage_rounded} )

def cpptcompiler(request,id):
    template="design/dashborad/cpp_language/testcase/compiler.html"
    
    data1=CpponetechnicalQuestionsTestcase.objects.filter(title_id=id)
    
    paginator = Paginator(data1 , 1)  

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    

    return render(request ,template,{"data":data} )

def cppttitleupload(request):
    template="design/dashborad/cpp_language/testcase/upload/title.html"
    if request.method == 'POST':
            
            data = request.POST.get('data2')
            data3 = request.POST.get('data3')
            print("data sented",data3)

            obj=Cpponetitletestcase()
            obj.title=data
            obj.level=data3
            obj.save()
            value="code"
            value2="code"

            if value==value2:
                response_data = {'success': True, 'message': 'Datasdfsadf processed successfully'}
                status_code = 200 
                 
            else:
                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500
            return JsonResponse(response_data, status=status_code)
    return render(request ,template,{} )
def cpptestud(request):
    template="design/dashborad/cpp_language/testcase/upload/question.html"
    data=Cpponetitletestcase.objects.all()

    if request.method == 'POST':
            inputData = request.POST.get('inputData')
            sampleCode = request.POST.get('sampleCode')
            sampleinput = request.POST.get('sampleinput')
            sampleoutput = request.POST.get('sampleoutput')
            textcaseInput = request.POST.get('textcaseInput')
            textcaseOutput = request.POST.get('textcaseOutput')
            type = request.POST.get('selectedtype')

            obj=CpponetechnicalQuestionsTestcase()
            obj.questions= inputData
            obj.sinput= sampleinput
            obj.soutput=sampleoutput 
            obj.tinput= textcaseInput
            obj.toutput=textcaseOutput
            obj.samplecode=sampleCode
            obj.title_id=type

            obj.save()
            print(inputData,sampleCode , textcaseOutput,textcaseInput,sampleoutput,sampleinput)

    return render(request ,template,{"data":data} )
@login_required
def cpptchecktest(request):
    template="design/dashborad/cpp_language/testcase/upload/title.html"
    userid = request.user.id
    if request.method == 'POST':
            
            data = request.POST.get('data2')
            data3 = request.POST.get('data3')
            data4 = request.POST.get('data4')
            print("data4",data4)

            print("data sented",data3)
            username=request.user.username
            
            check=CpponetechnicalQuestionsTestcase.objects.get(id=data ).toutput
            print("check2",data)
            print("check3",data3)

            if check==data3:
                       
                existing_obj = Cpptestcasereport.objects.filter(testcase_id=data, user_id=userid).first()

                if existing_obj:
                    existing_obj.success = "success"
                    existing_obj.title_id = data4
                    existing_obj.save()
                    print("Sample output check compiler data", data, data4)
                else:
                    
                    obj = Cpptestcasereport.objects.create(success="success", testcase_id=data, title_id=data4, user_id=userid)
                    print("New object created with testcase_id:", data)

                response_data = {'success': True, 'message': 'Test case has been executed successfully', "username": username}
                status_code = 200
                 
            else:
                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500
            return JsonResponse(response_data, status=status_code)
    return render(request ,template,{} )
    
    

def cpptitleupload(request):
    template="design/dashborad/cpp_language/practices/upload/title.html"
    data=Cpponetitlepractices.objects.all()

    if request.method == 'POST':
            data = request.POST.get('data2')
            data3 = request.POST.get('data3')
            print("data sented",data3)

            obj=Cpponetitlepractices()
            obj.title=data
            obj.level=data3
            obj.save()
            value="code"
            value2="code"
            if value==value2:
                response_data = {'success': True, 'message': 'Datasdfsadf processed successfully'}
                status_code = 200 
            else:
                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500
            return JsonResponse(response_data, status=status_code)
    return render(request ,template,{"data":data} )

def cpppracticeupload(request):
    template="design/dashborad/cpp_language/practices/upload/title.html"
    data=Cpponetitlepractices.objects.all()
    # print(data)
    if request.method == 'POST':
            type = request.POST.get('type')
            content = request.POST.get('content')
           
            obj=Cpponepquestionpractices()
            obj.content=content
            obj.title_id=type
            obj.save()
        
   
    return render(request ,template,{"data":data} )

    # testcase

    # c++ Traning

def cpptraning(request):
   
    template="design/dashborad/cpp_language/traning/index.html"
    titlehead=Javatraingtitle.objects.all()
   
    return render(request ,template,{"data":titlehead} )

# end c++ language

###################start testcase ####################
def javapracticeview(request):
    template="design/dashborad/compiler/javapractice.html"
    data=Titlepractices.objects.all()
    data2=Titlepractices.objects.count()
    easy = Titlepractices.objects.filter(level="Easy").count()
    hard = Titlepractices.objects.filter(level="Hard").count()
    medium = Titlepractices.objects.filter(level="Medium").count()
    print(data)
    
    return render(request ,template,{"data":data,"count":data2,"easy":easy,"hard":hard,"medium":medium} )


def javapracticelevel(request):
    template="design/dashborad/javatrainee/javapracticeupload.html"
    if request.method == 'POST':
            
            data = request.POST.get('data2')
            data3 = request.POST.get('data3')
            print("data sented",data3)

            obj=Titlepractices()
            obj.title=data
            obj.level=data3
            obj.save()
            value="code"
            value2="code"
            if value==value2:

                
                response_data = {'success': True, 'message': 'Datasdfsadf processed successfully'}
                status_code = 200 

                
            else:
                
                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500
            return JsonResponse(response_data, status=status_code)
    return render(request ,template,{} )
def javatestcaselevel(request):
    template="design/dashborad/javatrainee/uploadjava.html"

    if request.method == 'POST':
            
            data = request.POST.get('data2')
            data3 = request.POST.get('data3')
            print("data sented",data3)

            obj=Titletestcase()
            obj.title=data
            obj.level=data3
            obj.save()
            value="code"
            value2="code"
            if value==value2:

                
                response_data = {'success': True, 'message': 'Datasdfsadf processed successfully'}
                status_code = 200 

                
            else:
                
                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500
            return JsonResponse(response_data, status=status_code)
    return render(request ,template,{} )
def uploadjava(request):
    template="design/dashborad/javatrainee/uploadjava.html"
    data=Titletestcase.objects.all()

    if request.method == 'POST':
            inputData = request.POST.get('inputData')
            sampleCode = request.POST.get('sampleCode')
            sampleinput = request.POST.get('sampleinput')
            sampleoutput = request.POST.get('sampleoutput')
            textcaseInput = request.POST.get('textcaseInput')
            textcaseOutput = request.POST.get('textcaseOutput')
            type = request.POST.get('selectedtype')

            obj=TechnicalQuestionsTestcase()
            obj.questions= inputData
            obj.sinput= sampleinput
            obj.soutput=sampleoutput 
            obj.tinput= textcaseInput
            obj.toutput=textcaseOutput
            obj.samplecode=sampleCode
            obj.title_id=type

            obj.save()
            print(inputData,sampleCode , textcaseOutput,textcaseInput,sampleoutput,sampleinput)

    return render(request ,template,{"data":data} )
def javapracticeupload(request):
    template="design/dashborad/javatrainee/javapracticeupload.html"
    data=Titlepractices.objects.all()
    # print(data)
    if request.method == 'POST':
            type = request.POST.get('type')
            content = request.POST.get('content')
           
            obj=Questionpractices()
            obj.content=content
            obj.title_id=type
            obj.save()
        
   
    return render(request ,template,{"data":data} )


def javacompiler(request ,compiler_id):
    template="design/dashborad/compiler/java.html"


    data1=Questionpractices.objects.filter(title_id=compiler_id)
    
    paginator = Paginator(data1 , 1)  # Show 10 items per page

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        data = paginator.page(paginator.num_pages)
    
 
    return render(request ,template,{"data":data} )



@login_required
def javatestcaseview(request):
    template="design/dashborad/compiler/javatestcaseview.html"
    data=Titletestcase.objects.all()
    data2=Titletestcase.objects.count()
    easy = Titletestcase.objects.filter(level="Easy").count()
    hard = Titletestcase.objects.filter(level="Hard").count()
    medium = Titletestcase.objects.filter(level="Medium").count()
    userid = request.user.id

    total_question = TechnicalQuestionsTestcase.objects.count()
    success = Javatestcasereport.objects.filter(user_id=userid).count()
    success_percentage = (success / total_question) * 100 if total_question > 0 else 0
    success_percentage_rounded ="{:.0f}".format(success_percentage)
    print(data)



    print(data)
    
    return render(request ,template,{"data":data,"count":data2,"easy":easy,"hard":hard,"medium":medium,"report":success_percentage_rounded} )

@login_required
def javareportpage(request):
    template="design/dashborad/areport/javatreport.html"
    userid = request.user.id
    # totalquestion =CtechnicalQuestionsTestcase.objects.count()
    total_question = TechnicalQuestionsTestcase.objects.count()
    success = Javatestcasereport.objects.filter(user_id=userid).count()
    success_percentage = (success / total_question) * 100 if total_question > 0 else 0
    success_percentage_rounded ="{:.1f}".format(success_percentage)
    showsuccess = Javatestcasereport.objects.filter(user_id=userid).all()

# Iterate over each instance in the queryset and print its id
    for instance in showsuccess:
        print(instance.id)

    failed =(total_question - success)
    failed_percentage = (failed / total_question) * 100 if total_question > 0 else 0
    failed_percentage_rounded ="{:.1f}".format(failed_percentage)

    print("total_question",total_question,success,failed)
    context = {

        'total': total_question,
        'success': success,
        'failed': failed,
        'success_percentage':success_percentage_rounded,
        'failed_percentage':failed_percentage_rounded 

    }
    
    return render(request ,template,{'report':context,"showsuccess":showsuccess} )


@login_required
def javatchecktest(request):
    template="design/dashborad/cpp_language/testcase/upload/title.html"
    userid = request.user.id
    if request.method == 'POST':
            
            data = request.POST.get('data2')
            data3 = request.POST.get('data3')
            data4 = request.POST.get('data4')
            print("data4",data4)

            print("data sented",data3)
            username=request.user.username
            
            check=TechnicalQuestionsTestcase.objects.get(id=data ).toutput
            print("check2",data)
            print("check3",data3)

            if check==data3:
                       
                existing_obj = Javatestcasereport.objects.filter(testcase_id=data, user_id=userid).first()

                if existing_obj:
                    existing_obj.success = "success"
                    existing_obj.title_id = data4
                    existing_obj.save()
                    print("Sample output check compiler data", data, data4)
                else:
                    
                    obj = Javatestcasereport.objects.create(success="success", testcase_id=data, title_id=data4, user_id=userid)
                    print("New object created with testcase_id:", data)

                response_data = {'success': True, 'message': 'Test case has been executed successfully', "username": username}
                status_code = 200
                 
            else:
                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500
            return JsonResponse(response_data, status=status_code)
    return render(request ,template,{} )
    

def javatestcase(request,testcase_id):
    template="design/dashborad/testcase/java.html"


    data_list =TechnicalQuestionsTestcase.objects.filter(title_id=testcase_id)


    paginator = Paginator(data_list , 1)  # Show 10 items per page

    page = request.GET.get('page')
    try:
        data = paginator.page(page)

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        data = paginator.page(paginator.num_pages)

    if request.method == 'POST':
            output_value = request.POST.get('data')
            matchvalue = request.POST.get('data2')
            print("matchvalue",matchvalue)

            # obj=demooutput()
            # obj.demooutputs=output_value
            # obj.save()
            print("enter")
            valuedemo="Write a Code"
            valuedemo2="Write a Code"
            # myitem=Toutput.objects.last().toutputs
            myitem=TechnicalQuestionsTestcase.objects.get(id=matchvalue ).toutput

            print(myitem)

            # print(Toutput.objects.last().toutputs)
            # for item in Toutput.objects.all():
            #     myitem=item.toutputs





            # output_old = [5, 1, 6]
            # print(myitem)
            print("code",myitem)
            print("outpuyval",output_value)
            print("deme",valuedemo)
            # status_code = 200

            # for item in TechnicalQuestionsTestcase.objects.all():
            #     myitem=item.soutput

            if output_value == myitem:

                print("++++++++sucess rate ")
                response_data = {'success': True, 'message': 'Datasdfsadf processed successfully'}
                status_code = 200

                print(myitem)
            elif output_value != myitem :

                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500
            return JsonResponse(response_data, status=status_code)

    return render(request,template,{'data':data})
    



def practiceview(request):
   
    template="design/dashborad/javatrainee/practiceview.html"

    return render(request ,template,{} )

def topicupload(request):
   
    template="design/dashborad/javatrainee/topicupload.html"
    titlehead=Javatraingtitle.objects.all()


    return render(request ,template,{"data":titlehead} )

def codingtestupload(request):
   
    template="design/dashborad/javatrainee/codingtestupload.html"
    titlehead=Javatraingtitle.objects.all()
    if request.method == 'POST':
        inputData = request.POST.get('inputData')
        sampleCode = request.POST.get('sampleCode')
        sampleinput = request.POST.get('sampleinput')
        sampleoutput = request.POST.get('sampleoutput')
        textcaseInput = request.POST.get('textcaseInput')
        textcaseOutput = request.POST.get('textcaseOutput')
        type = request.POST.get('selectedtype')

        obj=Traningcodeingquestions()
        obj.questions= inputData
        obj.sinput= sampleinput
        obj.soutput=sampleoutput 
        obj.tinput= textcaseInput
        obj.toutput=textcaseOutput
        obj.samplecode=sampleCode
        obj.title_id=type

        obj.save()
        print(inputData,sampleCode , textcaseOutput,textcaseInput,sampleoutput,sampleinput , type)




    return render(request ,template,{"data":titlehead} )

def mcqupload(request):
   
    template="design/dashborad/javatrainee/mcqupload.html"
    titlehead=Javatraingtitle.objects.all()


    return render(request ,template,{"data":titlehead} )




def javatraning(request):
   
    template="design/dashborad/traning/javatraning.html"
    titlehead=Javatraingtitle.objects.all()
   
    return render(request ,template,{"data":titlehead} )




def titleupdateid(request):
   
    template="design/dashborad/javatrainee/javatraning.html"
    titlehead=Javatraingtitle.objects.all()
    if request.method == 'POST':
        updateid = request.POST.get('data2')
        updateid2 = request.POST.get('data3')

        print(updateid , "updateid")

        obj=Titleclick()
        obj.title=updateid2
        obj.cliknum= updateid
        obj.save()
   
    return render(request ,template,{"data":titlehead} )
# edit Start
def javatraningtranieeview(request):
   
    template="design/dashborad/javatrainee/javatraning.html"
    titlehead=Javatraingtitle.objects.all()
    show=Titleclick.objects.last().cliknum
    print(show)
    data=Javatraingtitle.objects.filter(id=show)
   
    return render(request ,template,{"data":titlehead ,"data2":data} )


def edittopic(request,pk):
   
    template="design/dashborad/javatrainee/edittopic.html"

    item = get_object_or_404(Javatraingtitle, id=pk)
    if request.method == 'POST':
        item.title = request.POST.get('title') 
        print(item.title)  
        item.save()
        return redirect('javatraningtranieeview')
    
    return render(request ,template,{'data': item} )


def updatetopic(request,pk):
   
    template="design/dashborad/javatrainee/edittopic.html"

    item = get_object_or_404(Javatraingtitle, id=pk)
    if request.method == 'POST':
        item.title = request.POST.get('title')   
        item.save()
        return redirect('javatraningtranieeview')
    
   
    return render(request ,template,{'data': item} )

def traningtitle_delete(request, pk):
    data = get_object_or_404(Javatraingtitle, id=pk)
    template="design/dashborad/javatrainee/javatraning.html"
    if request.method == 'POST':
        data.delete()
        return redirect('javatraningtranieeview')
    return render(request, template, {'data': data})


def editvideo(request,editvideo_id):
    template="design/dashborad/javatrainee/editvideo.html"
    data =Videosection.objects.filter(title_id=editvideo_id)
    data2 =Uploadvideosections.objects.filter(title_id=editvideo_id)
    print("data2", data2)

    somevalue=Javatraingtitle.objects.filter(id=editvideo_id)
    print(data)
    
    return render(request ,template,{"data":data,"somevalue":somevalue ,"data2":data2} )

def editvideopart(request,editvideopart_id):
    template="design/dashborad/javatrainee/editvideopart2.html"
    data2 =Uploadvideosections.objects.filter(id=editvideopart_id)
    somecolletion=Uploadvideosections.objects.filter(id=editvideopart_id)
    
 
    for i in somecolletion:
        print("Titleit",i.title_id)
        datatitle=i.title_id
   
    somevalue=Javatraingtitle.objects.filter(id=datatitle)   
    return render(request ,template,{"somevalue":somevalue ,"data2":data2} )


def updateeditvideopart(request,updatevideo):
    template="design/dashborad/javatrainee/editvideopart2.html"
    item = get_object_or_404(Uploadvideosections, id=updatevideo) 
    print("updatevideo",updatevideo)
    if request.method == 'POST' or request.FILES.get('video_file'):
        # print("33333333333333333333333333333333333333333333333332423423423")
        # print("enter to the post")
        # dad=request.POST.get('type')
        # data2=request.POST.get('content')
        # file=request.FILES['video_file']
        # print(dad,"data", "data3",data2 , file )
        item.title_id = request.POST.get('type')
        item.video_file= request.FILES['video_file']
        item.content= request.POST.get('content')
        item.save()

        return redirect("javatraningtranieeview")
    # else:
    #     return redirect("javatraningtranieeview")

        
    
    return render(request ,template,{} )


def editcodeingview(request, editcoding):
    template="design/dashborad/javatrainee/editcodeing.html"

   
    data_list =Traningcodeingquestions.objects.filter(title_id=editcoding)
    count = Traningcodeingquestions.objects.filter(title_id=editcoding).count()

    somevalue=Javatraingtitle.objects.filter(id=editcoding)
    
    print('somevalue',somevalue)


    paginator = Paginator(data_list , 1)  # Show 10 items per page

    page = request.GET.get('page')
    try:
        data = paginator.page(page)

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        data = paginator.page(paginator.num_pages)

    if request.method == 'POST':
            output_value = request.POST.get('data')
            matchvalue = request.POST.get('data2')
            print("matchvalue",matchvalue)

            # obj=demooutput()
            # obj.demooutputs=output_value
            # obj.save()
            print("enter")
            valuedemo="Write a Code"
            valuedemo2="Write a Code"
            # myitem=Toutput.objects.last().toutputs
            myitem=Traningcodeingquestions.objects.get(id=matchvalue ).toutput
            print(myitem)
            # print(Toutput.objects.last().toutputs)
            # for item in Toutput.objects.all():
            #     myitem=item.toutputs
            # output_old = [5, 1, 6]
            # print(myitem)
            print("code",myitem)
            print("outpuyval",output_value)
            print("deme",valuedemo)
            # status_code = 200

            # for item in TechnicalQuestionsTestcase.objects.all():
            #     myitem=item.soutput

            if output_value == myitem:

                print("++++++++sucess rate ")
                response_data = {'success': True, 'message': 'Datasdfsadf processed successfully'}
                status_code = 200

                print(myitem)
            elif output_value != myitem :

                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500
            return JsonResponse(response_data, status=status_code)
   
    return render(request ,template,{"data":data ,"somevalue":somevalue ,"count":count} )

def editupdatecodeing(request,codeupadate_id):
    template="design/dashborad/javatrainee/editupatecode.html"
    code =Traningcodeingquestions.objects.filter(id=codeupadate_id)
    print("codeupdateid",codeupadate_id)
    print("code ",code)
    for i in code:
        print("Titleit",i.title_id)
        datatitle=i.title_id
   
    data=Javatraingtitle.objects.filter(id=datatitle)

    if request.method == 'POST':
        inputData = request.POST.get('inputData')
        sampleCode = request.POST.get('sampleCode')
        sampleinput = request.POST.get('sampleinput')
        sampleoutput = request.POST.get('sampleoutput')
        textcaseInput = request.POST.get('textcaseInput')
        textcaseOutput = request.POST.get('textcaseOutput')
        type = request.POST.get('selectedtype')

        obj=Traningcodeingquestions()
        obj.questions= inputData
        obj.sinput= sampleinput
        obj.soutput=sampleoutput 
        obj.tinput= textcaseInput
        obj.toutput=textcaseOutput
        obj.samplecode=sampleCode
        obj.title_id=type

        obj.save()

        return redirect("javatraningtranieeview")


   
    return render(request ,template,{"code":code,"data":data} )

def editdeletecodeing(request, codedelete_id):
    data = get_object_or_404(Traningcodeingquestions, id=codedelete_id)
    template="design/dashborad/javatrainee/editupatecode.html"
    if request.method == 'POST':
        data.delete()
        return redirect('javatraningtranieeview')
    return render(request, template, {'data': data})

def viewpracties(request):
    template="design/dashborad/javatrainee/viewpracties.html"
    data=Titlepractices.objects.all()
    print(data)
    
    return render(request ,template,{"data":data} )

def titlepractiesedit(request ,ptitle_id):
    template="design/dashborad/javatrainee/ptitleedit.html"
    data = get_object_or_404(Titlepractices, id=ptitle_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        data.title=title
        data.save()
        return redirect("viewpracties")
    
    
    return render(request ,template,{"data":data} )



def titlepractiedelete(request, titledelete):
    template="design/dashborad/javatrainee/ptitleedit.html"
    data = get_object_or_404(Titlepractices, id=titledelete)
    if request.method == 'POST':
        data.delete()
        return redirect('viewpracties')
    return render(request, template, {'data': data})
def pquestionedit(request ,compiler_id):
    template="design/dashborad/javatrainee/pquestionedit.html"


    data1=Questionpractices.objects.filter(title_id=compiler_id)
    count = Questionpractices.objects.filter(title_id=compiler_id).count()
    print("Count", count)
    
    paginator = Paginator(data1 , 1)  # Show 10 items per page

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        data = paginator.page(paginator.num_pages)
    
 
    return render(request ,template,{"data":data,"count":count} )


def pquestioneditview(request, questionupdate):
    data = get_object_or_404(Questionpractices, id=questionupdate)
    template="design/dashborad/javatrainee/pquestionupload.html"
    if request.method == 'POST':
        content = request.POST.get('content')
        data.content=content
        data.save()
        return redirect('viewpracties')
    return render(request, template, {'data': data})


def pdeletequestion(request, questiondelete_id):
    data = get_object_or_404(Questionpractices, id=questiondelete_id)
    template="design/dashborad/javatrainee/pquestionedit.html"
    if request.method == 'POST':
        data.delete()
        return redirect('viewpracties')
    return render(request, template, {'data': data})

def ptitleedit(request, questiondelete_id):
    data = get_object_or_404(Questionpractices, id=questiondelete_id)
    template="design/dashborad/javatrainee/pquestionedit.html"
    if request.method == 'POST':
        data.delete()
        return redirect('viewpracties')
    return render(request, template, {'data': data})



def testtitleview(request):
    template="design/dashborad/javatrainee/testtitle.html"
    data=Titletestcase.objects.all()
    print(data)
    
    return render(request ,template,{"data":data} )


def testtitleupdate(request, title_id):
    data = get_object_or_404(Titletestcase, id=title_id)
    template="design/dashborad/javatrainee/testtitleupdate.html"
    if request.method == 'POST':
        content = request.POST.get('title')
        data.title=content
        data.save()
        return redirect('testtitleview')
    return render(request, template, {'data': data})

def testtitledelete(request, title_id):
    data = get_object_or_404(Titletestcase, id=title_id)
    template="design/dashborad/javatrainee/testtitleupdate.html"
    if request.method == 'POST':
        data.delete()
        return redirect('testtitleview')
    return render(request, template, {'data': data})


def testquestionview(request, testcase):
    template="design/dashborad/javatrainee/testquestion.html"

   
    data_list =TechnicalQuestionsTestcase.objects.filter(title_id=testcase)
    count = TechnicalQuestionsTestcase.objects.filter(title_id=testcase).count()

    somevalue=Titletestcase.objects.filter(id=testcase)
    
    print('somevalue',somevalue)


    paginator = Paginator(data_list , 1)  # Show 10 items per page

    page = request.GET.get('page')
    try:
        data = paginator.page(page)

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        data = paginator.page(paginator.num_pages)

    if request.method == 'POST':
            output_value = request.POST.get('data')
            matchvalue = request.POST.get('data2')
            print("matchvalue",matchvalue)

            # obj=demooutput()
            # obj.demooutputs=output_value
            # obj.save()
            print("enter")
            valuedemo="Write a Code"
            valuedemo2="Write a Code"
            # myitem=Toutput.objects.last().toutputs
            myitem=TechnicalQuestionsTestcase.objects.get(id=matchvalue ).toutput
            print(myitem)
            # print(Toutput.objects.last().toutputs)
            # for item in Toutput.objects.all():
            #     myitem=item.toutputs
            # output_old = [5, 1, 6]
            # print(myitem)
            print("code",myitem)
            print("outpuyval",output_value)
            print("deme",valuedemo)
            # status_code = 200

            # for item in TechnicalQuestionsTestcase.objects.all():
            #     myitem=item.soutput

            if output_value == myitem:

                print("++++++++sucess rate ")
                response_data = {'success': True, 'message': 'Datasdfsadf processed successfully'}
                status_code = 200

                print(myitem)
            elif output_value != myitem :

                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500
            return JsonResponse(response_data, status=status_code)
   
    return render(request ,template,{"data":data ,"somevalue":somevalue ,"count":count} )



def testdeletequestion(request, testcase_id):
    data = get_object_or_404(TechnicalQuestionsTestcase, id=testcase_id)
    template="design/dashborad/javatrainee/editupatecode.html"
    if request.method == 'POST':
        data.delete()
        return redirect('testtitleview')
    return render(request, template, {'data': data})


# quiz start
def mcqtest(request):
    template="design/dashborad/traning/mcqtest.html"
    # quiz_data = Quiz.objects.all()
    update_id=Traningupdateid.objects.last().updateid

    quiz_data = Quiz.objects.filter(title_id=update_id)

    # Structure the data for use in the template
    # questions = [
    #              {    'demo': quiz.answer, 
    #                   'options': [{'option': quiz.option1, 'option': quiz.option3}, {'option': quiz.option2}], 
    #                   'question_text': quiz.question} for quiz in quiz_data]

   
    # quiz_data = Quiz.objects.all()

    questions = [
    {   'id':quiz.id,
        'question': quiz.question,
        'answers': [
            {'text': quiz.option1, 'correct': quiz.answer1},
            {'text': quiz.option2, 'correct': quiz.answer2},
            {'text': quiz.option3, 'correct': quiz.answer3},
            {'text': quiz.option4, 'correct': quiz.answer4}
        ]
    }
    for quiz in quiz_data
   ]
    print(questions)
    update_id=Traningupdateid.objects.last().updateid
    somevalue=Javatraingtitle.objects.filter(id=update_id)
   
    return render(request ,template,{"somevalue":somevalue ,"questions":questions} )
def quizupload(request):
    # data = get_object_or_404(Quiz)
    
    data=Javatraingtitle.objects.all()
    template="design/dashborad/quiz/upload.html"
    if request.method == 'POST':
        type = request.POST.get('type')

        question = request.POST.get('question')
        option1 = request.POST.get('optionone')
        option2 = request.POST.get('optiontwo')
        option3 = request.POST.get('optionthree')
        option4 = request.POST.get('optionfour')
        answer1 = request.POST.get('answerone')
        answer2 = request.POST.get('answertwo')
        answer3 = request.POST.get('answerthree')
        answer4 = request.POST.get('answerfour')
        obj=Quiz()
        obj.question=question
        obj.option1=option1
        obj.option2=option2
        obj.option3=option3
        obj.option4=option4
        obj.answer1=answer1
        obj.answer2=answer2
        obj.answer3=answer3
        obj.answer4=answer4
        obj.title_id=type
        obj.save()

        
        # print("question", question)
        # print("option1", option1)
        # print("option2", option2)
        # print("option3", option3)
        # print("option4", option4)
        # print("answer1", answer1)
        # print("answer2", answer2)
        # print("answer3", answer3)
        # print("answer4", answer4)
        # print("type", type)

       
    return render(request, template, {"data":data})


    
# edit quiz end


# aptitude start


def aptitudestart(request):

    if 'username' in request.session:
        session_id = request.session.session_key

        try:
            template="design/dashborad/aptitude/index.html"
            data=Aptitudetitle.objects.all()
            return render(request ,template,{"data":data} )

        except Session.DoesNotExist:
            return HttpResponse("Invalid session ID")
        except User.DoesNotExist:
            return HttpResponse("User not found")
    else:
       
        return redirect('login')

   
   

def aptitudevideo(request,appvideoid):
    if 'username' in request.session:
        session_id = request.session.session_key

        try:
            template="design/dashborad/aptitude/videosection.html"
            data2 =Aptitudevideosections.objects.filter(title_id=appvideoid)
            return render(request ,template,{"data":data2} )

        except Session.DoesNotExist:
            return HttpResponse("Invalid session ID")
        except User.DoesNotExist:
            return HttpResponse("User not found")
    else:
       
        return redirect('login')
   


def aptitudemcq(request,app_id):
    if 'username' in request.session:
        session_id = request.session.session_key

        
        template="design/dashborad/aptitude/mcq.html"
        data =Aptitudequiz.objects.filter(title_id=app_id)
        

        data2=Aptitudequiz.objects.count()
        questions = [
        {   'id':quiz.id,
            'video':app_id,
            'question': quiz.question,
            'answers': [
                {'text': quiz.option1, 'correct': quiz.answer1},
                {'text': quiz.option2, 'correct': quiz.answer2},
                {'text': quiz.option3, 'correct': quiz.answer3},
                {'text': quiz.option4, 'correct': quiz.answer4}
            ]
        }
        for quiz in data
    ]
        return render(request ,template,{"questions":questions ,"data":data,"count":data2} )

        
    else:
       
        return redirect('login')
   
    

def aptitudetitleupload(request):
    if 'username' in request.session:
        template="design/dashborad/aptitude/upload/title.html"
        data=Aptitudetitle.objects.all()
        if request.method == 'POST':
            title = request.POST.get('title')
            obj=Aptitudetitle()
            obj.title=title
            obj.save()
            return redirect("aptitudevideoupload")
        return render(request ,template,{"data":data} )
        
    else:
       
        return redirect('login')

   

def aptitudevideoupload(request):
    if 'username' in request.session:
   
        template="design/dashborad/aptitude/upload/video.html"
        data=Aptitudetitle.objects.all()

        if request.method == 'POST' and request.FILES.get('video_file'):
            demoone="aptitude"
            title = request.POST.get('type')
            video_file = request.FILES['video_file']
            con = request.POST.get('content')
            Aptitudevideosections.objects.create(titleone=demoone ,title_id=title, video_file=video_file , content= con)
            return redirect("aptitudemcqupload")

        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def aptitudemcqupload(request):
    if 'username' in request.session:
   
        template="design/dashborad/aptitude/upload/mcq.html"

        # data = get_object_or_404(Quiz)
        
        data=Aptitudetitle.objects.all()
        if request.method == 'POST':
            type = request.POST.get('type')

            question = request.POST.get('question')
            option1 = request.POST.get('optionone')
            option2 = request.POST.get('optiontwo')
            option3 = request.POST.get('optionthree')
            option4 = request.POST.get('optionfour')
            answer1 = request.POST.get('answerone')
            answer2 = request.POST.get('answertwo')
            answer3 = request.POST.get('answerthree')
            answer4 = request.POST.get('answerfour')
            obj=Aptitudequiz()
            obj.question=question
            obj.option1=option1
            obj.option2=option2
            obj.option3=option3
            obj.option4=option4
            obj.answer1=answer1
            obj.answer2=answer2
            obj.answer3=answer3
            obj.answer4=answer4
            obj.title_id=type
            obj.save()

            # return redirect("aptitudestart")

       
        return render(request, template, {"data":data})
    
    else:
       
        return redirect('login')




# aptitude Practices


def appview(request):
    if 'username' in request.session:
   
        template="design/dashborad/aptitude/appview/title.html"
        data=Apptitle.objects.all()
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def appmcqview(request,app_id):
    if 'username' in request.session:
   
        template="design/dashborad/aptitude/appview/mcq.html"
        data =Appquiz.objects.filter(title_id=app_id)
        count =Appquiz.objects.filter(title_id=app_id).count()

        data2=get_object_or_404(Apptitle,id=app_id)
        questions = [
        {   'id':quiz.id,
            'question': quiz.question,
            'answers': [
                {'text': quiz.option1, 'correct': quiz.answer1},
                {'text': quiz.option2, 'correct': quiz.answer2},
                {'text': quiz.option3, 'correct': quiz.answer3},
                {'text': quiz.option4, 'correct': quiz.answer4}
            ]
        }
        for quiz in data
        ]
        return render(request ,template,{"questions":questions ,"data":data2 ,"count":count} )
    else:
       
        return redirect('login')
# app=aptitude practies
# app upload
def apptitleupload(request):
    if 'username' in request.session:   
        template="design/dashborad/aptitude/appupload/title.html"
        data=Apptitle.objects.all() 
        if request.method == 'POST':
            title = request.POST.get('title')
            obj=Apptitle()
            obj.title=title
            obj.save()
            return redirect("appmcqupload")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')


def appmcqupload(request):
    if 'username' in request.session:
   
        template="design/dashborad/aptitude/appupload/mcq.html"

        # data = get_object_or_404(Quiz)
        
        data=Apptitle.objects.all()
        if request.method == 'POST':
            type = request.POST.get('type')

            question = request.POST.get('question')
            option1 = request.POST.get('optionone')
            option2 = request.POST.get('optiontwo')
            option3 = request.POST.get('optionthree')
            option4 = request.POST.get('optionfour')
            answer1 = request.POST.get('answerone')
            answer2 = request.POST.get('answertwo')
            answer3 = request.POST.get('answerthree')
            answer4 = request.POST.get('answerfour')
            obj=Appquiz()
            obj.question=question
            obj.option1=option1
            obj.option2=option2
            obj.option3=option3
            obj.option4=option4
            obj.answer1=answer1
            obj.answer2=answer2
            obj.answer3=answer3
            obj.answer4=answer4
            obj.title_id=type
            obj.save()

            # return redirect("apptitleupload")

        
        return render(request, template, {"data":data})
    else:
       
        return redirect('login')


# start traing apps

def apptetview(request):
    if 'username' in request.session:
   
        template="design/dashborad/aptitude/edit/view.html"
        data=Aptitudetitle.objects.all()
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def apptetitle(request,id):
    if 'username' in request.session:
        template="design/dashborad/aptitude/edit/title.html"
        data = get_object_or_404(Aptitudetitle, id=id)

        if request.method == 'POST':
            title = request.POST.get('title')
            data.title=title
            data.save()
            return redirect("apptetview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def apptetitledelet(request,id):
    if 'username' in request.session:
        template="design/dashborad/aptitude/edit/title.html"
        data = get_object_or_404(Aptitudetitle, id=id)

        if request.method == 'POST':
            data.delete()
            return redirect("apptetview")
        return render(request ,template,{"data":data} ) 
    else:
       
        return redirect('login')


def appvideoview(request,appvideoid):
    if 'username' in request.session:
   
        template="design/dashborad/aptitude/edit/videov.html"
        data2 =Aptitudevideosections.objects.filter(title_id=appvideoid)
        return render(request ,template,{"data":data2} )
    else:
       
        return redirect('login')

def appvideoedit(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/aptitude/edit/video.html"
        data = get_object_or_404(Aptitudevideosections, id=id)

        if request.method == 'POST':
            video_file = request.FILES['video_file']
            con = request.POST.get('content')
            data.titleone="edione"
            data.video_file=video_file
            data.content= con
            data.save()

            return redirect("apptetview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')
def appvideodelete(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/aptitude/edit/video.html"
        data = get_object_or_404(Aptitudevideosections, id=id)

        if request.method == 'POST':
            data.delete()
            return redirect("apptetview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def apptemcqedit(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/aptitude/edit/mcq.html"
        data2 =Aptitudequiz.objects.filter(title_id=id)
        paginator = Paginator(data2 , 1)  # Show 10 items per page

        page = request.GET.get('page')
        try:
            data = paginator.page(page)
            
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver last page.
            data = paginator.page(paginator.num_pages)


        return render(request ,template,{"data":data , } )
    else:
       
        return redirect('login')


def apptemcqeditpart(request,id):
    if 'username' in request.session:
        template="design/dashborad/aptitude/edit/editmcq.html"
        data = get_object_or_404(Aptitudequiz, id=id)
        id_value = data.title_id
        if request.method == 'POST':
            question = request.POST.get('question')
            option1 = request.POST.get('optionone')
            option2 = request.POST.get('optiontwo')
            option3 = request.POST.get('optionthree')
            option4 = request.POST.get('optionfour')
            answer1 = request.POST.get('answerone')
            answer2 = request.POST.get('answertwo')
            answer3 = request.POST.get('answerthree')
            answer4 = request.POST.get('answerfour')
            data.question=question
            data.option1=option1
            data.option2=option2
            data.option3=option3
            data.option4=option4
            data.answer1=answer1
            data.answer2=answer2
            data.answer3=answer3
            data.answer4=answer4
            data.save()
            return redirect(reverse('apptemcqedit', kwargs={'id': id_value}))
        return render(request ,template,{"data":data } )
    else:
       
        return redirect('login')


def appmtecqdeletepart(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/aptitude/edit/editmcq.html"
        
        data = get_object_or_404(Aptitudequiz, id=id)
        id_value = data.title_id
        if request.method == 'POST':
            data.delete()
            return redirect(reverse('apptemcqedit', kwargs={'id': id_value}))
        return render(request ,template,{"data":data } )
    else:
        
        return redirect('login')
# end traing apps




    # app edit
def appeeditview(request):
    if 'username' in request.session:
   
        template="design/dashborad/aptitude/appedit/view.html"
        data=Apptitle.objects.all()
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def apptitleedit(request,id):
    if 'username' in request.session:
        template="design/dashborad/aptitude/appedit/title.html"
        data = get_object_or_404(Apptitle, id=id)

        if request.method == 'POST':
            title = request.POST.get('title')
            data.title=title
            data.save()
            return redirect("appeeditview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def apptitledelet(request,id):
    if 'username' in request.session:
        template="ddesign/dashborad/aptitude/appedit/title.html"
        data = get_object_or_404(Apptitle, id=id)

        if request.method == 'POST':
            data.delete()
            return redirect("appeeditview")
        return render(request ,template,{"data":data} ) 
    else:
       
        return redirect('login')

def appmcqedit(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/aptitude/appedit/mcq.html"
        data2 =Appquiz.objects.filter(title_id=id)
        
                

        paginator = Paginator(data2 , 1)  # Show 10 items per page

        page = request.GET.get('page')
        try:
            data = paginator.page(page)
            
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver last page.
            data = paginator.page(paginator.num_pages)


        return render(request ,template,{"data":data , } )
    else:
       
        return redirect('login')

from django.urls import reverse

def appmcqeditpart(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/aptitude/appedit/editmcq.html"
        data = get_object_or_404(Appquiz, id=id)
        id_value = data.title_id
        if request.method == 'POST':
            question = request.POST.get('question')
            option1 = request.POST.get('optionone')
            option2 = request.POST.get('optiontwo')
            option3 = request.POST.get('optionthree')
            option4 = request.POST.get('optionfour')
            answer1 = request.POST.get('answerone')
            answer2 = request.POST.get('answertwo')
            answer3 = request.POST.get('answerthree')
            answer4 = request.POST.get('answerfour')
            data.question=question
            data.option1=option1
            data.option2=option2
            data.option3=option3
            data.option4=option4
            data.answer1=answer1
            data.answer2=answer2
            data.answer3=answer3
            data.answer4=answer4
            data.save()
            return redirect(reverse('appmcqedit', kwargs={'id': id_value}))
        return render(request ,template,{"data":data } )
    else:
       
        return redirect('login')

def appmcqdeletepart(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/aptitude/appedit/editmcq.html"
        
        data = get_object_or_404(Appquiz, id=id)
        id_value = data.title_id
        if request.method == 'POST':
            data.delete()
            return redirect(reverse('appmcqedit', kwargs={'id': id_value}))
        return render(request ,template,{"data":data } )
    else:
       
        return redirect('login')


# aptitude end


# pd start
def pdview(request):
    if 'username' in request.session:
   
        template="design/dashborad/PD/index.html"
        data=Pdtitle.objects.all()
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')
    
    

def pdvideo(request,pdvideoid):
    if 'username' in request.session:
   
        template="design/dashborad/PD/video.html"
        data2 =Pdvideosections.objects.filter(title_id=pdvideoid)
        return render(request ,template,{"data":data2} )
    else:
       
        return redirect('login')


def pdtitleupload(request):
    if 'username' in request.session:
   
        template="design/dashborad/PD/upload/title.html"
        data=Pdtitle.objects.all()
        if request.method == 'POST':
            title = request.POST.get('title')
            obj=Pdtitle()
            obj.title=title
            obj.save()
            return redirect("pdvideoupload")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def pdvideoupload(request):
    if 'username' in request.session:
        template="design/dashborad/PD/upload/video.html"
        data=Pdtitle.objects.all()

        if request.method == 'POST' and request.FILES.get('video_file'):
            demoone="pd"
            title = request.POST.get('type')
            video_file = request.FILES['video_file']
            con = request.POST.get('content')
            Pdvideosections.objects.create(titleone=demoone ,title_id=title, video_file=video_file , content= con)
            return redirect("pdtitleupload")

        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

    # pd edit view and edit
def pdeditview(request):
    if 'username' in request.session:
   
        template="design/dashborad/PD/edit/view.html"
        data=Pdtitle.objects.all()
    
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def pdvideoview(request,pdeditid):
    if 'username' in request.session:
        template="design/dashborad/PD/edit/videoview.html"
        data=get_object_or_404(Pdvideosections,title_id=pdeditid)
        if request.method == 'POST':
            title = request.POST.get('type')
            video_file = request.FILES['video_file']
            con = request.POST.get('content')
            data
            return redirect("pdeditview")

        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def pdtitleedit(request,id):
    if 'username' in request.session:
        template="design/dashborad/PD/edit/edittitle.html"
        data = get_object_or_404(Pdtitle, id=id)

        if request.method == 'POST':
            title = request.POST.get('title')
            data.title=title
            data.save()
            return redirect("pdeditview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def pdtitledelet(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/PD/edit/edittitle.html"
        data = get_object_or_404(Pdtitle, id=id)

        if request.method == 'POST':
            data.delete()
            return redirect("pdeditview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def pdeditvieo(request,pdeditid):
    if 'username' in request.session:
        template="design/dashborad/PD/edit/editvideo.html"
        data=get_object_or_404(Pdvideosections,id=pdeditid)
        if request.method == 'POST':
            video_file = request.FILES['video_file']
            con = request.POST.get('content')
            data.video_file=video_file
            data.content=con
            data.save()
            return redirect("pdeditview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def pdvideodelete(request,id):
    if 'username' in request.session:
        template="design/dashborad/PD/edit/editvideo.html"
        data = get_object_or_404(Pdvideosections, id=id)

        if request.method == 'POST':
            data.delete()
            return redirect("pdeditview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')
# end pd

def javacomplete(request,globel_id):
   
    template="design/dashborad/traning/javacomplete.html"

    data_list =Javatraingmcq.objects.filter(title_id=globel_id)


    paginator = Paginator(data_list , 1)  # Show 10 items per page

    page = request.GET.get('page')
    try:
        data = paginator.page(page)

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        data = paginator.page(paginator.num_pages)

   
   

    
   
    return render(request ,template,{"data":data} )

def video(request,video_id):
    template="design/dashborad/traning/videosection.html"
    data =Videosection.objects.filter(title_id=video_id)
    data2 =Uploadvideosections.objects.filter(title_id=video_id)
    print("data2", data2)

    somevalue=Javatraingtitle.objects.filter(id=video_id)
    print(data)
    for i in data:
        print(i.url)
    traingid=video_id
    compailerdata={
        "id":traingid
    }
    return render(request ,template,{"data":data,"traingid":compailerdata ,"somevalue":somevalue ,"data2":data2} )

def traningcompiler(request):
    template="design/dashborad/traning/compilerjava.html"
    if request.method == 'POST':
        updateid = request.POST.get('data2')
        print(updateid , "updateid")

        obj=Traningupdateid()
        obj.updateid= updateid
        obj.save()





    update_id=Traningupdateid.objects.last().updateid
    somevalue=Javatraingtitle.objects.filter(id=update_id)
    return render(request ,template,{"somevalue":somevalue} )
def examdetails(request):
    template="design/dashborad/traning/examdetails.html"
   
    return render(request ,template,{} )

def javatrainingtest(request):
    template="design/dashborad/traning/javatrainingtest.html"

    update_id=Traningupdateid.objects.last().updateid

    

    data_list =Traningcodeingquestions.objects.filter(title_id=update_id)

    somevalue=Javatraingtitle.objects.filter(id=update_id)
    
    print('somevalue',somevalue)


    paginator = Paginator(data_list , 1)  # Show 10 items per page

    page = request.GET.get('page')
    try:
        data = paginator.page(page)

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        data = paginator.page(paginator.num_pages)

    if request.method == 'POST':
            output_value = request.POST.get('data')
            matchvalue = request.POST.get('data2')
            print("matchvalue",matchvalue)

            # obj=demooutput()
            # obj.demooutputs=output_value
            # obj.save()
            print("enter")
            valuedemo="Write a Code"
            valuedemo2="Write a Code"
            # myitem=Toutput.objects.last().toutputs
            myitem=Traningcodeingquestions.objects.get(id=matchvalue ).toutput

            print(myitem)

            # print(Toutput.objects.last().toutputs)
            # for item in Toutput.objects.all():
            #     myitem=item.toutputs





            # output_old = [5, 1, 6]
            # print(myitem)
            print("code",myitem)
            print("outpuyval",output_value)
            print("deme",valuedemo)
            # status_code = 200

            # for item in TechnicalQuestionsTestcase.objects.all():
            #     myitem=item.soutput

            if output_value == myitem:

                print("++++++++sucess rate ")
                response_data = {'success': True, 'message': 'Datasdfsadf processed successfully'}
                status_code = 200

                print(myitem)
            elif output_value != myitem :

                print("failer")
                response_data = {'success': False, 'message':'error_message'}
                status_code = 500
            return JsonResponse(response_data, status=status_code)
   
    return render(request ,template,{"data":data ,"somevalue":somevalue} )


def uploadjavatraing(request):
    template="design/dashborad/javatrainee/uploadjavatraing.html"
    titlehead=Javatraingtitle.objects.all()
    if request.method == 'POST':
        
        data = request.POST.get('data2')
        typeselected = request.POST.get('data3')
        # mcq
        questiontypeselected = request.POST.get('questiontypeselected')
        questionmcq = request.POST.get('questionmcq')

        optionamcq = request.POST.get('optionamcq')
        optionbmcq = request.POST.get('optionbmcq')
        optioncmcq = request.POST.get('optioncmcq')
        correctansmcq = request.POST.get('correctansmcq')
        optiondmcq = request.POST.get('optiondmcq')


        print("questiontypeselected",questiontypeselected )
        print("optionamcq",optionamcq )
        print("  optionbmcq",optionbmcq )
        print("  optioncmcq",optioncmcq )
        print("  optiondmcq",optiondmcq )
        print("  correctansmcq",correctansmcq )
        print("  questionmcq",questionmcq )

       

        obj=Javatraingtitle()
        obj.title=data
        obj.selecttype=typeselected
        obj.save()

        value="code"
        value2="code"
        if value==value2:

            
            response_data = {'success': True, 'message': 'Datasdfsadf processed successfully'}
            status_code = 200 

            
        else:
            
            print("failer")
            response_data = {'success': False, 'message':'error_message'}
            status_code = 500
        return JsonResponse(response_data, status=status_code)
  
    return render (request,template,{"data":titlehead})


def uploadjavatraingmcq(request):
    template="design/dashborad/javatrainee/uploadjavatraing.html"
    titlehead=Javatraingtitle.objects.all()
    if request.method == 'POST':
      
        questiontypeselected = request.POST.get('questiontypeselected')
        questionmcq = request.POST.get('questionmcq')

        optionamcq = request.POST.get('optionamcq')
        optionbmcq = request.POST.get('optionbmcq')
        optioncmcq = request.POST.get('optioncmcq')
        correctansmcq = request.POST.get('correctansmcq')
        optiondmcq = request.POST.get('optiondmcq')


        print("questiontypeselected",questiontypeselected )
        print("optionamcq",optionamcq )
        print("  optionbmcq",optionbmcq )
        print("  optioncmcq",optioncmcq )
        print("  optiondmcq",optiondmcq )
        print("  correctansmcq",correctansmcq )
        print("  questionmcq",questionmcq )

       

        obj=Javatraingmcq()
        obj.questions=questionmcq
        obj.optiona=optionamcq
        obj.optionb=optionbmcq
        obj.optionc=optioncmcq
        obj.optiond=optiondmcq
        obj.correctans=correctansmcq
        obj.title_id=questiontypeselected
        
        obj.save()
        
        
    return render (request,template,{"data":titlehead})




def quiz(request):
    template="design/dashborad/quiz/index.html"
    quiz_data = Quiz.objects.all()

    # Structure the data for use in the template
    # questions = [
    #              {    'demo': quiz.answer, 
    #                   'options': [{'option': quiz.option1, 'option': quiz.option3}, {'option': quiz.option2}], 
    #                   'question_text': quiz.question} for quiz in quiz_data]

    # print(questions)
    # quiz_data = Quiz.objects.all()

    questions = [
    {
        'question_text': quiz.question,
        'answers': [
            {'text': quiz.option1, 'correct': True},
            {'text': quiz.option2, 'correct': False},
            {'text': quiz.option3, 'correct': False},
            {'text': quiz.option4, 'correct': False}
        ]
    }
    for quiz in quiz_data
   ]
    
    print("down",questions)
    return render (request,template,{"questions":questions})




# intership



def intershipstart(request):
    if 'username' in request.session:
   
        template="design/dashborad/intership/index.html"
        data=Intershiptitle.objects.all()
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def intershipvideo(request,appvideoid):
    if 'username' in request.session:
        template="design/dashborad/intership/videosection.html"
        data2 =Intershipvideosections.objects.filter(title_id=appvideoid)
        return render(request ,template,{"data":data2} )
    else:
       
        return redirect('login')

def intershipmcq(request,app_id):
    if 'username' in request.session:
        template="design/dashborad/intership/mcq.html"
        data =Intershipquiz.objects.filter(title_id=app_id)
        questions = [
        {   'id':quiz.id,
            'question': quiz.question,
            'answers': [
                {'text': quiz.option1, 'correct': quiz.answer1},
                {'text': quiz.option2, 'correct': quiz.answer2},
                {'text': quiz.option3, 'correct': quiz.answer3},
                {'text': quiz.option4, 'correct': quiz.answer4}
            ]
        }
        for quiz in data
    ]
        return render(request ,template,{"questions":questions ,"data":data} )
    else:
       
        return redirect('login')

def intershiptitleupload(request):
    if 'username' in request.session:
        data=Intershiptitle.objects.all()
        
        template="design/dashborad/intership/upload/title.html"
        if request.method == 'POST':
            print("enter")
            title = request.POST.get('title')
            timer = request.POST.get('timer')
            part = request.POST.get('part')
            code = request.POST.get('code')
            obj=Intershiptitle()
            obj.title=title
            obj.timer=timer
            obj.part=part
            obj.code=code
            obj.save()
            return redirect("intershipvideoupload")
        return render(request ,template,{'data':data} )
    else:
       
        return redirect('login')
def intershipvideoupload(request):
    if 'username' in request.session:
   
        template="design/dashborad/intership/upload/video.html"
        data=Intershiptitle.objects.all()

        if request.method == 'POST' and request.FILES.get('video_file'):
            demoone="intership"
            title = request.POST.get('type')
            video_file = request.FILES['video_file']
            con = request.POST.get('content')
            Intershipvideosections.objects.create(titleone=demoone ,title_id=title, video_file=video_file , content= con)
            return redirect("intershipmcqupload")

        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def intershipmcqupload(request):
    if 'username' in request.session:
    
        template="design/dashborad/intership/upload/mcq.html"

        # data = get_object_or_404(Quiz)
        
        data=Intershiptitle.objects.all()
        if request.method == 'POST':
            type = request.POST.get('type')

            question = request.POST.get('question')
            option1 = request.POST.get('optionone')
            option2 = request.POST.get('optiontwo')
            option3 = request.POST.get('optionthree')
            option4 = request.POST.get('optionfour')
            answer1 = request.POST.get('answerone')
            answer2 = request.POST.get('answertwo')
            answer3 = request.POST.get('answerthree')
            answer4 = request.POST.get('answerfour')
            obj=Intershipquiz()
            obj.question=question
            obj.option1=option1
            obj.option2=option2
            obj.option3=option3
            obj.option4=option4
            obj.answer1=answer1
            obj.answer2=answer2
            obj.answer3=answer3
            obj.answer4=answer4
            obj.title_id=type
            obj.save()

            return redirect("intershipstart")

        
        return render(request, template, {"data":data})
    else:
       
        return redirect('login')

# workshop edit
# start traing apps

def intershipteview(request):
    if 'username' in request.session:
   
        template="design/dashborad/intership/edit/view.html"
        data=Intershiptitle.objects.all()
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def intershiptetitle(request,id):
    if 'username' in request.session:
        template="design/dashborad/intership/edit/title.html"
        data = get_object_or_404(Intershiptitle, id=id)

        if request.method == 'POST':
            title = request.POST.get('title')
            timer = request.POST.get('timer')
            part = request.POST.get('part')
            code = request.POST.get('code')
            data.title=title
            data.timer=timer
            data.part=part
            data.code=code
            data.save()
            return redirect("intershiptitleupload")
        
        return render(request ,template,{"data":data} ) 
    else:
       
        return redirect('login')

def intershiptdelete(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/intership/edit/title.html"
        data = get_object_or_404(Intershiptitle, id=id)

        if request.method == 'POST':
            data.delete()
            return redirect("intershiptetview")
        return render(request ,template,{"data":data} ) 
    else:
       
        return redirect('login')


def intershipvideoview(request,appvideoid):
    if 'username' in request.session:
   
        template="design/dashborad/intership/edit/videov.html"
        data2 =Intershipvideosections.objects.filter(title_id=appvideoid)
        return render(request ,template,{"data":data2} )
    else:
       
        return redirect('login')

def intershipvideoedit(request,id):
    if 'username' in request.session:
        template="design/dashborad/intership/edit/video.html"
        data = get_object_or_404(Intershipvideosections, id=id)

        if request.method == 'POST':
            video_file = request.FILES['video_file']
            con = request.POST.get('content')
            data.titleone="edione"
            data.video_file=video_file
            data.content= con
            data.save()

            return redirect("intershiptitleupload")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')
def intershipvideodelete(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/intership/edit/video.html"
        data = get_object_or_404(Intershipvideosections, id=id)

        if request.method == 'POST':
            data.delete()
            return redirect("intershiptetview")
        return render(request ,template,{"data":data} ) 
    else:
       
        return redirect('login')

def intershiptemcqedit(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/intership/edit/mcq.html"
        data2 =Intershipquiz.objects.filter(title_id=id)
        paginator = Paginator(data2 , 1)  # Show 10 items per page

        page = request.GET.get('page')
        try:
            data = paginator.page(page)
            
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver last page.
            data = paginator.page(paginator.num_pages)


        return render(request ,template,{"data":data , } )
    else:
       
        return redirect('login')


def intershiptemcqeditpart(request,id):
    if 'username' in request.session:
        template="design/dashborad/intership/edit/editmcq.html"
        data = get_object_or_404(Intershipquiz, id=id)
        id_value = data.title_id
        if request.method == 'POST':
            question = request.POST.get('question')
            option1 = request.POST.get('optionone')
            option2 = request.POST.get('optiontwo')
            option3 = request.POST.get('optionthree')
            option4 = request.POST.get('optionfour')
            answer1 = request.POST.get('answerone')
            answer2 = request.POST.get('answertwo')
            answer3 = request.POST.get('answerthree')
            answer4 = request.POST.get('answerfour')
            data.question=question
            data.option1=option1
            data.option2=option2
            data.option3=option3
            data.option4=option4
            data.answer1=answer1
            data.answer2=answer2
            data.answer3=answer3
            data.answer4=answer4
            data.save()
            return redirect(reverse('intershiptemcqedit', kwargs={'id': id_value}))
        return render(request ,template,{"data":data } )
    else:
       
        return redirect('login')


def intershiptecqdeletepart(request,id):
    if 'username' in request.session:
        template="design/dashborad/intership/edit/editmcq.html"
        
        data = get_object_or_404(Intershipquiz, id=id)
        id_value = data.title_id
        if request.method == 'POST':
            data.delete()
            return redirect(reverse('intershiptemcqedit', kwargs={'id': id_value}))
        return render(request ,template,{"data":data } )
    else:
       
        return redirect('login')

def intershipcertificate(request):
    if 'username' in request.session:
        template="design/dashborad/intership/certificate.html"
    
        return render(request ,template,{} )
    else:
       
        return redirect('login')
    
def intershipannouncement(request):
    if 'username' in request.session:
        template="design/dashborad/intership/announment.html"
    
        return render(request ,template,{} )
    else:
       
        return redirect('login')

# end intership


# Workshop start

def workoshopcertificate(request):
    if 'username' in request.session:
        template="design/dashborad/workshop/certificate.html"
    
        return render(request ,template,{} )
    else:
       
        return redirect('login')

def workoshopannouncement(request):
    if 'username' in request.session:
        template="design/dashborad/workshop/announment.html"
    
        return render(request ,template,{} )
    else:
       
        return redirect('login')



def workshopstart(request):
    if 'username' in request.session:
    
        template="design/dashborad/workshop/index.html"
        data=Workshoptitle.objects.all()
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def workshopvideo(request,appvideoid):
    if 'username' in request.session:
        template="design/dashborad/workshop/videosection.html"
        data2 =Workshopvideosections.objects.filter(title_id=appvideoid)
        return render(request ,template,{"data":data2} )
    else:
       
        return redirect('login')

def workshopmcq(request,app_id):
    if 'username' in request.session:
    
        template="design/dashborad/workshop/mcq.html"
        data =Workshopquiz.objects.filter(title_id=app_id)
        questions = [
        {   'id':quiz.id,
            'question': quiz.question,
            'answers': [
                {'text': quiz.option1, 'correct': quiz.answer1},
                {'text': quiz.option2, 'correct': quiz.answer2},
                {'text': quiz.option3, 'correct': quiz.answer3},
                {'text': quiz.option4, 'correct': quiz.answer4}
            ]
        }
        for quiz in data
    ]
        return render(request ,template,{"questions":questions ,"data":data} )
    else:
       
        return redirect('login')

def workshoptitleupload(request):
    if 'username' in request.session:
        template="design/dashborad/workshop/upload/title.html"
        if request.method == 'POST':
            print("enter")
            title = request.POST.get('title')
    

            obj=Workshoptitle()
            obj.title=title


            obj.save()
            return redirect("workshopvideoupload")
        return render(request ,template,{} )
    else:
       
        return redirect('login')

def workshopvideoupload(request):
    if 'username' in request.session:
   
        template="design/dashborad/workshop/upload/video.html"
        data=Workshoptitle.objects.all()

        if request.method == 'POST' and request.FILES.get('video_file'):
            demoone="workshop"
            title = request.POST.get('type')
            video_file = request.FILES['video_file']
            con = request.POST.get('content')
            Workshopvideosections.objects.create(titleone=demoone ,title_id=title, video_file=video_file , content= con)
            return redirect("workshopmcqupload")

        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def workshopmcqupload(request):
    if 'username' in request.session:
   
        template="design/dashborad/workshop/upload/mcq.html"

        # data = get_object_or_404(Quiz)
        
        data=Workshoptitle.objects.all()
        if request.method == 'POST':
            type = request.POST.get('type')

            question = request.POST.get('question')
            option1 = request.POST.get('optionone')
            option2 = request.POST.get('optiontwo')
            option3 = request.POST.get('optionthree')
            option4 = request.POST.get('optionfour')
            answer1 = request.POST.get('answerone')
            answer2 = request.POST.get('answertwo')
            answer3 = request.POST.get('answerthree')
            answer4 = request.POST.get('answerfour')
            obj=Workshopquiz()
            obj.question=question
            obj.option1=option1
            obj.option2=option2
            obj.option3=option3
            obj.option4=option4
            obj.answer1=answer1
            obj.answer2=answer2
            obj.answer3=answer3
            obj.answer4=answer4
            obj.title_id=type
            obj.save()

            return redirect("workshopstart")

        
        return render(request, template, {"data":data})
    else:
       
        return redirect('login')



# workshop edit
# start traing apps

def workshopteview(request):
    if 'username' in request.session:
        template="design/dashborad/workshop/edit/view.html"
        data=Workshoptitle.objects.all()
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def workshoptetitle(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/workshop/edit/title.html"
        data = get_object_or_404(Workshoptitle, id=id)

        if request.method == 'POST':
            title = request.POST.get('title')
            timer = request.POST.get('timer')
            part = request.POST.get('part')
            code = request.POST.get('code')
            data.title=title
            data.timer=timer
            data.part=part
            data.code=code
            data.save()
            return redirect("workshopteview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def workshoptdelete(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/workshop/edit/title.html"
        data = get_object_or_404(Workshoptitle, id=id)

        if request.method == 'POST':
            data.delete()
            return redirect("workshopteview")
        return render(request ,template,{"data":data} ) 
    else:
       
        return redirect('login')


def workshopvideoview(request,appvideoid):
    if 'username' in request.session:
        template="design/dashborad/workshop/edit/videov.html"
        data2 =Workshopvideosections.objects.filter(title_id=appvideoid)
        return render(request ,template,{"data":data2} )
    else:
       
        return redirect('login')

def workshopvideoedit(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/workshop/edit/video.html"
        data = get_object_or_404(Workshopvideosections, id=id)

        if request.method == 'POST':
            video_file = request.FILES['video_file']
            con = request.POST.get('content')
            data.titleone="edione"
            data.video_file=video_file
            data.content= con
            data.save()

            return redirect("workshopteview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')
def workshopvideodelete(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/workshop/edit/video.html"
        data = get_object_or_404(Workshopvideosections, id=id)

        if request.method == 'POST':
            data.delete()
            return redirect("workshoptetview")
        return render(request ,template,{"data":data} ) 
    else:
       
        return redirect('login')

def workshoptemcqedit(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/workshop/edit/mcq.html"
        data2 =Workshopquiz.objects.filter(title_id=id)
        paginator = Paginator(data2 , 1)  # Show 10 items per page

        page = request.GET.get('page')
        try:
            data = paginator.page(page)
            
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver last page.
            data = paginator.page(paginator.num_pages)


        return render(request ,template,{"data":data , } )
    else:
       
        return redirect('login')


def workshoptemcqeditpart(request,id):
    if 'username' in request.session:
        template="design/dashborad/workshop/edit/editmcq.html"
        data = get_object_or_404(Workshopquiz, id=id)
        id_value = data.title_id
        if request.method == 'POST':
            question = request.POST.get('question')
            option1 = request.POST.get('optionone')
            option2 = request.POST.get('optiontwo')
            option3 = request.POST.get('optionthree')
            option4 = request.POST.get('optionfour')
            answer1 = request.POST.get('answerone')
            answer2 = request.POST.get('answertwo')
            answer3 = request.POST.get('answerthree')
            answer4 = request.POST.get('answerfour')
            data.question=question
            data.option1=option1
            data.option2=option2
            data.option3=option3
            data.option4=option4
            data.answer1=answer1
            data.answer2=answer2
            data.answer3=answer3
            data.answer4=answer4
            data.save()
            return redirect(reverse('workshoptemcqedit', kwargs={'id': id_value}))
        return render(request ,template,{"data":data } )
    else:
       
        return redirect('login')


def workshoptecqdeletepart(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/workshop/edit/editmcq.html"
        
        data = get_object_or_404(Workshopquiz, id=id)
        id_value = data.title_id
        if request.method == 'POST':
            data.delete()
            return redirect(reverse('workshoptemcqedit', kwargs={'id': id_value}))
        return render(request ,template,{"data":data } )
    else:
       
        return redirect('login')

# end workshop

# english start


def englishtraing(request):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/traning.html"
        
    
        return render(request ,template,{} )
    else:
       
        return redirect('login')
def technicalenglish(request):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/technical/index.html"
        data=Etechnicaltitle.objects.all()
    
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')


def etechnicalvideo(request,appvideoid):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/technical/videosection.html"
        data2 =Etechnicalvideosections.objects.filter(title_id=appvideoid)
        return render(request ,template,{"data":data2} )
    else:
       
        return redirect('login')

def etechnicalmcq(request,app_id):
    if 'username' in request.session:
        template="design/dashborad/english/traning/technical/mcq.html"
        data =Etechnicalquiz.objects.filter(title_id=app_id)
        questions = [
        {   'id':quiz.id,
            'question': quiz.question,
            'answers': [
                {'text': quiz.option1, 'correct': quiz.answer1},
                {'text': quiz.option2, 'correct': quiz.answer2},
                {'text': quiz.option3, 'correct': quiz.answer3},
                {'text': quiz.option4, 'correct': quiz.answer4}
            ]
        }
        for quiz in data
    ]
        return render(request ,template,{"questions":questions ,"data":data} )
    else:
       
        return redirect('login')

def etechnicaltitleupload(request):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/technical/upload/title.html"
        if request.method == 'POST':
            print("enter")
            title = request.POST.get('title')
            subtitle = request.POST.get('subtitle')
    
            obj=Etechnicaltitle()
            obj.title=title
            obj.subtitle=subtitle
        
            obj.save()
            return redirect("etechnicalvideoupload")
        return render(request ,template,{} )
    else:
       
        return redirect('login')

def etechnicalvideoupload(request):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/technical/upload/video.html"
        data=Etechnicaltitle.objects.all()

        if request.method == 'POST' and request.FILES.get('video_file'):
            demoone="intership"
            title = request.POST.get('type')
            video_file = request.FILES['video_file']
            con = request.POST.get('content')
            Etechnicalvideosections.objects.create(titleone=demoone ,title_id=title, video_file=video_file , content= con)
            return redirect("etechnicalmcqupload")

        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def etechnicalmcqupload(request):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/technical/upload/mcq.html"

        # data = get_object_or_404(Quiz)
        
        data=Etechnicaltitle.objects.all()
        if request.method == 'POST':
            type = request.POST.get('type')

            question = request.POST.get('question')
            option1 = request.POST.get('optionone')
            option2 = request.POST.get('optiontwo')
            option3 = request.POST.get('optionthree')
            option4 = request.POST.get('optionfour')
            answer1 = request.POST.get('answerone')
            answer2 = request.POST.get('answertwo')
            answer3 = request.POST.get('answerthree')
            answer4 = request.POST.get('answerfour')
            obj=Etechnicalquiz()
            obj.question=question
            obj.option1=option1
            obj.option2=option2
            obj.option3=option3
            obj.option4=option4
            obj.answer1=answer1
            obj.answer2=answer2
            obj.answer3=answer3
            obj.answer4=answer4
            obj.title_id=type
            obj.save()

            # return redirect("technicalenglish")

        
        return render(request, template, {"data":data})
    else:
       
        return redirect('login')


# technical english edit


def etechnicaltview(request):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/technical/edit/view.html"
        data=Etechnicaltitle.objects.all()
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def etechnicaltitle(request,id):
    if 'username' in request.session:
        template="design/dashborad/english/traning/technical/edit/title.html"
        data = get_object_or_404(Etechnicaltitle, id=id)

        if request.method == 'POST':
            title = request.POST.get('title')
            data.title=title
            data.save()
            return redirect("etechnicaltview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def etechnicaltitledelet(request,id):
    if 'username' in request.session:
        template="design/dashborad/english/traning/technical/edit/title.html"
        data = get_object_or_404(Etechnicaltitle, id=id)

        if request.method == 'POST':
            data.delete()
            return redirect("etechnicaltview")
        return render(request ,template,{"data":data} ) 
    else:
       
        return redirect('login')


def etechnicalvideoview(request,appvideoid):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/technical/edit/videov.html"
        data2 =Etechnicalvideosections.objects.filter(title_id=appvideoid)
        return render(request ,template,{"data":data2} )
    else:
       
        return redirect('login')

def etechnicalvideoedit(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/technical/edit/video.html"
        data = get_object_or_404(Etechnicalvideosections, id=id)

        if request.method == 'POST':
            video_file = request.FILES['video_file']
            con = request.POST.get('content')
            data.titleone="edione"
            data.video_file=video_file
            data.content= con
            data.save()

            return redirect("etechnicaltview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')
def etechnicalvideodelete(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/technical/edit/video.html"
        data = get_object_or_404(Etechnicalvideosections, id=id)

        if request.method == 'POST':
            data.delete()
            return redirect("etechnicaltview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def etechnicalmcqedit(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/technical/edit/mcq.html"
        data2 =Etechnicalquiz.objects.filter(title_id=id)
        paginator = Paginator(data2 , 1)  # Show 10 items per page

        page = request.GET.get('page')
        try:
            data = paginator.page(page)
            
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver last page.
            data = paginator.page(paginator.num_pages)


        return render(request ,template,{"data":data , } )
    else:
       
        return redirect('login')


def etechnicalmcqeditpart(request,id):
    if 'username' in request.session:
        template="design/dashborad/english/traning/technical/edit/editmcq.html"
        data = get_object_or_404(Etechnicalquiz, id=id)
        id_value = data.title_id
        if request.method == 'POST':
            question = request.POST.get('question')
            option1 = request.POST.get('optionone')
            option2 = request.POST.get('optiontwo')
            option3 = request.POST.get('optionthree')
            option4 = request.POST.get('optionfour')
            answer1 = request.POST.get('answerone')
            answer2 = request.POST.get('answertwo')
            answer3 = request.POST.get('answerthree')
            answer4 = request.POST.get('answerfour')
            data.question=question
            data.option1=option1
            data.option2=option2
            data.option3=option3
            data.option4=option4
            data.answer1=answer1
            data.answer2=answer2
            data.answer3=answer3
            data.answer4=answer4
            data.save()
            return redirect(reverse('etechnicalmcqedit', kwargs={'id': id_value}))
        return render(request ,template,{"data":data } )
    else:
       
        return redirect('login')


def etechnicaltecqdeletepart(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/technical/edit/editmcq.html"
        
        data = get_object_or_404(Etechnicalquiz, id=id)
        id_value = data.title_id
        if request.method == 'POST':
            data.delete()
            return redirect(reverse('etechnicalmcqedit', kwargs={'id': id_value}))
        return render(request ,template,{"data":data } )
    else:
        
        return redirect('login')
# end traing technical english




# business english

def businessenglish(request):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/business/index.html"
        data=Ebusinesstitle.objects.all()
    
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')


def ebusinessvideo(request,appvideoid):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/business/videosection.html"
        data2 =Ebusinessvideosections.objects.filter(title_id=appvideoid)
        return render(request ,template,{"data":data2} )
    else:
       
        return redirect('login')

def ebusinessmcq(request,app_id):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/business/mcq.html"
        data =Ebusinessquiz.objects.filter(title_id=app_id)
        questions = [
        {   'id':quiz.id,
            'question': quiz.question,
            'answers': [
                {'text': quiz.option1, 'correct': quiz.answer1},
                {'text': quiz.option2, 'correct': quiz.answer2},
                {'text': quiz.option3, 'correct': quiz.answer3},
                {'text': quiz.option4, 'correct': quiz.answer4}
            ]
        }
        for quiz in data
    ]
        return render(request ,template,{"questions":questions ,"data":data} )
    else:
       
        return redirect('login')

def ebusinesstitleupload(request):

    if 'username' in request.session:
        template="design/dashborad/english/traning/business/upload/title.html"
        if request.method == 'POST':
            print("enter")
            title = request.POST.get('title')
            subtitle = request.POST.get('subtitle')
    
            obj=Ebusinesstitle()
            obj.title=title
            obj.subtitle=subtitle
        
            obj.save()
            return redirect("ebusinessvideoupload")
        return render(request ,template,{} )
    else:
       
        return redirect('login')

def ebusinessvideoupload(request):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/business/upload/video.html"
        data=Ebusinesstitle.objects.all()

        if request.method == 'POST' and request.FILES.get('video_file'):
            demoone="intership"
            title = request.POST.get('type')
            video_file = request.FILES['video_file']
            con = request.POST.get('content')
            Ebusinessvideosections.objects.create(titleone=demoone ,title_id=title, video_file=video_file , content= con)
            return redirect("ebusinessmcqupload")

        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def ebusinessmcqupload(request):
    if 'username' in request.session:
        template="design/dashborad/english/traning/business/upload/mcq.html"

        # data = get_object_or_404(Quiz)
        
        data=Ebusinesstitle.objects.all()
        if request.method == 'POST':
            type = request.POST.get('type')

            question = request.POST.get('question')
            option1 = request.POST.get('optionone')
            option2 = request.POST.get('optiontwo')
            option3 = request.POST.get('optionthree')
            option4 = request.POST.get('optionfour')
            answer1 = request.POST.get('answerone')
            answer2 = request.POST.get('answertwo')
            answer3 = request.POST.get('answerthree')
            answer4 = request.POST.get('answerfour')
            obj=Ebusinessquiz()
            obj.question=question
            obj.option1=option1
            obj.option2=option2
            obj.option3=option3
            obj.option4=option4
            obj.answer1=answer1
            obj.answer2=answer2
            obj.answer3=answer3
            obj.answer4=answer4
            obj.title_id=type
            obj.save()

            # return redirect("businessenglish")

        
        return render(request, template, {"data":data})
    else:
       
        return redirect('login')
    


# bussiness english edit


def ebusinesstview(request):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/business/edit/view.html"
        data=Ebusinesstitle.objects.all()
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def ebusinesstitle(request,id):
    if 'username' in request.session:
        template="design/dashborad/english/traning/business/edit/title.html"
        data = get_object_or_404(Ebusinesstitle, id=id)

        if request.method == 'POST':
            title = request.POST.get('title')
            data.title=title
            data.save()
            return redirect("ebusinesstview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def ebusinesstitledelet(request,id):
    if 'username' in request.session:
        template="design/dashborad/english/traning/business/edit/title.html"
        data = get_object_or_404(Ebusinesstitle, id=id)

        if request.method == 'POST':
            data.delete()
            return redirect("ebusinesstview")
        return render(request ,template,{"data":data} ) 
    else:
       
        return redirect('login')


def ebusinessvideoview(request,appvideoid):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/business/edit/videov.html"
        data2 =Ebusinessvideosections.objects.filter(title_id=appvideoid)
        return render(request ,template,{"data":data2} )
    else:
       
        return redirect('login')

def ebusinessvideoedit(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/business/edit/video.html"
        data = get_object_or_404(Ebusinessvideosections, id=id)

        if request.method == 'POST':
            video_file = request.FILES['video_file']
            con = request.POST.get('content')
            data.titleone="edione"
            data.video_file=video_file
            data.content= con
            data.save()

            return redirect("ebusinesstview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')
def ebusinessvideodelete(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/business/edit/video.html"
        data = get_object_or_404(Ebusinessvideosections, id=id)

        if request.method == 'POST':
            data.delete()
            return redirect("ebusinesstview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def ebusinessmcqedit(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/business/edit/mcq.html"
        data2 =Ebusinessquiz.objects.filter(title_id=id)
        paginator = Paginator(data2 , 1)  # Show 10 items per page

        page = request.GET.get('page')
        try:
            data = paginator.page(page)
            
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver last page.
            data = paginator.page(paginator.num_pages)


        return render(request ,template,{"data":data , } )
    else:
       
        return redirect('login')


def ebusinessmcqeditpart(request,id):
    if 'username' in request.session:
        template="design/dashborad/english/traning/business/edit/editmcq.html"
        data = get_object_or_404(Ebusinessquiz, id=id)
        id_value = data.title_id
        if request.method == 'POST':
            question = request.POST.get('question')
            option1 = request.POST.get('optionone')
            option2 = request.POST.get('optiontwo')
            option3 = request.POST.get('optionthree')
            option4 = request.POST.get('optionfour')
            answer1 = request.POST.get('answerone')
            answer2 = request.POST.get('answertwo')
            answer3 = request.POST.get('answerthree')
            answer4 = request.POST.get('answerfour')
            data.question=question
            data.option1=option1
            data.option2=option2
            data.option3=option3
            data.option4=option4
            data.answer1=answer1
            data.answer2=answer2
            data.answer3=answer3
            data.answer4=answer4
            data.save()
            return redirect(reverse('ebusinessmcqedit', kwargs={'id': id_value}))
        return render(request ,template,{"data":data } )
    else:
       
        return redirect('login')


def ebusinesstecqdeletepart(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/business/edit/editmcq.html"
        
        data = get_object_or_404(Ebusinessquiz, id=id)
        id_value = data.title_id
        if request.method == 'POST':
            data.delete()
            return redirect(reverse('ebusinessmcqedit', kwargs={'id': id_value}))
        return render(request ,template,{"data":data } )
    else:
        
        return redirect('login')
# end traing bussiness english



# spoken English


def spokenenglish(request):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/spoken/index.html"
        data=Espokentitle.objects.all()
    
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')


def espokenvideo(request,appvideoid):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/spoken/videosection.html"
        data2 =Espokenvideosections.objects.filter(title_id=appvideoid)
        return render(request ,template,{"data":data2} )
    else:
       
        return redirect('login')

def espokenmcq(request,app_id):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/spoken/mcq.html"
        data =Espokenquiz.objects.filter(title_id=app_id)
        questions = [
        {   'id':quiz.id,
            'question': quiz.question,
            'answers': [
                {'text': quiz.option1, 'correct': quiz.answer1},
                {'text': quiz.option2, 'correct': quiz.answer2},
                {'text': quiz.option3, 'correct': quiz.answer3},
                {'text': quiz.option4, 'correct': quiz.answer4}
            ]
        }
        for quiz in data
    ]
        return render(request ,template,{"questions":questions ,"data":data} )
    else:
       
        return redirect('login')

def espokentitleupload(request):
    if 'username' in request.session:
    
        template="design/dashborad/english/traning/spoken/upload/title.html"
        if request.method == 'POST':
            print("enter")
            title = request.POST.get('title')
            subtitle = request.POST.get('subtitle')
    
            obj=Espokentitle()
            obj.title=title
            obj.subtitle=subtitle
        
            obj.save()
            return redirect("espokenvideoupload")
        return render(request ,template,{} )
    else:
       
        return redirect('login')

def espokenvideoupload(request):
    if 'username' in request.session:
    
        template="design/dashborad/english/traning/spoken/upload/video.html"
        data=Espokentitle.objects.all()

        if request.method == 'POST' and request.FILES.get('video_file'):
            demoone="intership"
            title = request.POST.get('type')
            video_file = request.FILES['video_file']
            con = request.POST.get('content')
            Espokenvideosections.objects.create(titleone=demoone ,title_id=title, video_file=video_file , content= con)
            return redirect("espokenmcqupload")

        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def espokenmcqupload(request):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/spoken/upload/mcq.html"

        # data = get_object_or_404(Quiz)
        
        data=Espokentitle.objects.all()
        if request.method == 'POST':
            type = request.POST.get('type')

            question = request.POST.get('question')
            option1 = request.POST.get('optionone')
            option2 = request.POST.get('optiontwo')
            option3 = request.POST.get('optionthree')
            option4 = request.POST.get('optionfour')
            answer1 = request.POST.get('answerone')
            answer2 = request.POST.get('answertwo')
            answer3 = request.POST.get('answerthree')
            answer4 = request.POST.get('answerfour')
            obj=Espokenquiz()
            obj.question=question
            obj.option1=option1
            obj.option2=option2
            obj.option3=option3
            obj.option4=option4
            obj.answer1=answer1
            obj.answer2=answer2
            obj.answer3=answer3
            obj.answer4=answer4
            obj.title_id=type
            obj.save()

            # return redirect("spokenenglish")

        
        return render(request, template, {"data":data})
    else:
       
        return redirect('login')




# spoken english edit


def espokentview(request):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/spoken/edit/view.html"
        data=Espokentitle.objects.all()
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def espokentitle(request,id):
    if 'username' in request.session:
        template="design/dashborad/english/traning/spoken/edit/title.html"
        data = get_object_or_404(Espokentitle, id=id)

        if request.method == 'POST':
            title = request.POST.get('title')
            data.title=title
            data.save()
            return redirect("espokentview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def espokentitledelet(request,id):
    if 'username' in request.session:
        template="design/dashborad/english/traning/spoken/edit/title.html"
        data = get_object_or_404(Espokentitle, id=id)

        if request.method == 'POST':
            data.delete()
            return redirect("espokentview")
        return render(request ,template,{"data":data} ) 
    else:
       
        return redirect('login')


def espokenvideoview(request,appvideoid):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/spoken/edit/videov.html"
        data2 =Espokenvideosections.objects.filter(title_id=appvideoid)
        return render(request ,template,{"data":data2} )
    else:
       
        return redirect('login')

def espokenvideoedit(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/spoken/edit/video.html"
        data = get_object_or_404(Espokenvideosections, id=id)

        if request.method == 'POST':
            video_file = request.FILES['video_file']
            con = request.POST.get('content')
            data.titleone="edione"
            data.video_file=video_file
            data.content= con
            data.save()

            return redirect("espokentview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')
def espokenvideodelete(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/spoken/edit/video.html"
        data = get_object_or_404(Espokenvideosections, id=id)

        if request.method == 'POST':
            data.delete()
            return redirect("espokentview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def espokenmcqedit(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/spoken/edit/mcq.html"
        data2 =Espokenquiz.objects.filter(title_id=id)
        paginator = Paginator(data2 , 1)  # Show 10 items per page

        page = request.GET.get('page')
        try:
            data = paginator.page(page)
            
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver last page.
            data = paginator.page(paginator.num_pages)


        return render(request ,template,{"data":data , } )
    else:
       
        return redirect('login')


def espokenmcqeditpart(request,id):
    if 'username' in request.session:
        template="design/dashborad/english/traning/spoken/edit/editmcq.html"
        data = get_object_or_404(Espokenquiz, id=id)
        id_value = data.title_id
        if request.method == 'POST':
            question = request.POST.get('question')
            option1 = request.POST.get('optionone')
            option2 = request.POST.get('optiontwo')
            option3 = request.POST.get('optionthree')
            option4 = request.POST.get('optionfour')
            answer1 = request.POST.get('answerone')
            answer2 = request.POST.get('answertwo')
            answer3 = request.POST.get('answerthree')
            answer4 = request.POST.get('answerfour')
            data.question=question
            data.option1=option1
            data.option2=option2
            data.option3=option3
            data.option4=option4
            data.answer1=answer1
            data.answer2=answer2
            data.answer3=answer3
            data.answer4=answer4
            data.save()
            return redirect(reverse('espokenmcqedit', kwargs={'id': id_value}))
        return render(request ,template,{"data":data } )
    else:
       
        return redirect('login')


def espokentecqdeletepart(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/spoken/edit/editmcq.html"
        
        data = get_object_or_404(Espokenquiz, id=id)
        id_value = data.title_id
        if request.method == 'POST':
            data.delete()
            return redirect(reverse('espokenmcqedit', kwargs={'id': id_value}))
        return render(request ,template,{"data":data } )
    else:
        
        return redirect('login')
# end traing spoken english



# text - speech
from django.http import HttpResponse
from gtts import gTTS
import tempfile
import os

def text_to_audio(request):
    if request.method == 'POST':
        text_to_convert = request.POST.get('text_to_convert', '')
        language = 'en'
        
        # Convert text to speech
        tts = gTTS(text=text_to_convert, lang=language, slow=False)
        
        # Save the audio file
        audio_file = "output_audio.mp3"
        tts.save(audio_file)

        # Play the audio file using system command
        os.system("mpg123 " + audio_file)  # Make sure you have mpg123 installed
        
        # Optionally, you can return a response or redirect to another page
        return HttpResponse("Text converted to speech and played successfully!")
    else:
        return render(request, 'aatext.html')




# listening

def listening(request):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/listening/index.html"
        
        return render(request ,template,{} )
    else:
       
        return redirect('login')



def listeningenglish(request):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/listening/view/one.html"
        data=Elisteningtitle.objects.all()
    
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')


def elisteningreder(request,appvideoid):
    if 'username' in request.session:
        template="design/dashborad/english/traning/listening/view/reader.html"
        data2 =Elisteningreader.objects.filter(title_id=appvideoid)
        return render(request ,template,{"data":data2} )
    else:
       
        return redirect('login')

def elisteningmcq(request,app_id):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/listening/view/mcq.html"
        data =Elisteningquiz.objects.filter(title_id=app_id)
        questions = [
        {   'id':quiz.id,
            'question': quiz.question,
            'answers': [
                {'text': quiz.option1, 'correct': quiz.answer1},
                {'text': quiz.option2, 'correct': quiz.answer2},
                {'text': quiz.option3, 'correct': quiz.answer3},
                {'text': quiz.option4, 'correct': quiz.answer4}
            ]
        }
        for quiz in data
    ]
        return render(request ,template,{"questions":questions ,"data":data} )
    else:
       
        return redirect('login')

def elisteningtitleupload(request):
    if 'username' in request.session:
        template="design/dashborad/english/traning/listening/upload/title.html"
        if request.method == 'POST':
            print("enter")
            title = request.POST.get('title')
            subtitle = request.POST.get('subtitle')
    
            obj=Elisteningtitle()
            obj.title=title
            obj.subtitle=subtitle
        
            obj.save()
            return redirect("elisteningreaderupload")
        return render(request ,template,{} )
    else:
       
        return redirect('login')
def elisteningreaderupload(request):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/listening/upload/video.html"
        data=Elisteningtitle.objects.all()

        if request.method == 'POST' :
            # demoone="list"
            con = request.POST.get('content')
            title = request.POST.get('type')
            Elisteningreader.objects.create( content= con,title_id=title)
            return redirect("elisteningmcqupload")

        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def elisteningmcqupload(request):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/listening/upload/mcq.html"

        # data = get_object_or_404(Quiz)
        
        data=Elisteningtitle.objects.all()
        if request.method == 'POST':
            type = request.POST.get('type')

            question = request.POST.get('question')
            option1 = request.POST.get('optionone')
            option2 = request.POST.get('optiontwo')
            option3 = request.POST.get('optionthree')
            option4 = request.POST.get('optionfour')
            answer1 = request.POST.get('answerone')
            answer2 = request.POST.get('answertwo')
            answer3 = request.POST.get('answerthree')
            answer4 = request.POST.get('answerfour')
            obj=Elisteningquiz()
            obj.question=question
            obj.option1=option1
            obj.option2=option2
            obj.option3=option3
            obj.option4=option4
            obj.answer1=answer1
            obj.answer2=answer2
            obj.answer3=answer3
            obj.answer4=answer4
            obj.title_id=type
            obj.save()

            # return redirect("listeningenglish")

        
        return render(request, template, {"data":data})
    else:
       
        return redirect('login')



# listening english edit


def elisteningtview(request):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/listening/edit/view.html"
        data=Elisteningtitle.objects.all()
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def elisteningtitle(request,id):
    if 'username' in request.session:
        template="design/dashborad/english/traning/listening/edit/title.html"
        data = get_object_or_404(Elisteningtitle, id=id)

        if request.method == 'POST':
            title = request.POST.get('title')
            data.title=title
            data.save()
            return redirect("elisteningtview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def elisteningtitledelet(request,id):
    if 'username' in request.session:
        template="design/dashborad/english/traning/listening/edit/title.html"
        data = get_object_or_404(Elisteningtitle, id=id)

        if request.method == 'POST':
            data.delete()
            return redirect("elisteningtview")
        return render(request ,template,{"data":data} ) 
    else:
       
        return redirect('login')


def elisteningvideoview(request,appvideoid):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/listening/edit/videov.html"
        data2 =Elisteningvideosections.objects.filter(title_id=appvideoid)
        return render(request ,template,{"data":data2} )
    else:
       
        return redirect('login')

def elisteningvideoedit(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/listening/edit/video.html"
        data = get_object_or_404(Elisteningvideosections, id=id)

        if request.method == 'POST':
            video_file = request.FILES['video_file']
            con = request.POST.get('content')
            data.titleone="edione"
            data.video_file=video_file
            data.content= con
            data.save()

            return redirect("elisteningtview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')
def elisteningvideodelete(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/listening/edit/video.html"
        data = get_object_or_404(Elisteningvideosections, id=id)

        if request.method == 'POST':
            data.delete()
            return redirect("elisteningtview")
        return render(request ,template,{"data":data} )
    else:
       
        return redirect('login')

def elisteningmcqedit(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/listening/edit/mcq.html"
        data2 =Elisteningquiz.objects.filter(title_id=id)
        paginator = Paginator(data2 , 1)  # Show 10 items per page

        page = request.GET.get('page')
        try:
            data = paginator.page(page)
            
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver last page.
            data = paginator.page(paginator.num_pages)


        return render(request ,template,{"data":data , } )
    else:
       
        return redirect('login')


def elisteningmcqeditpart(request,id):
    if 'username' in request.session:
        template="design/dashborad/english/traning/listening/edit/editmcq.html"
        data = get_object_or_404(Elisteningquiz, id=id)
        id_value = data.title_id
        if request.method == 'POST':
            question = request.POST.get('question')
            option1 = request.POST.get('optionone')
            option2 = request.POST.get('optiontwo')
            option3 = request.POST.get('optionthree')
            option4 = request.POST.get('optionfour')
            answer1 = request.POST.get('answerone')
            answer2 = request.POST.get('answertwo')
            answer3 = request.POST.get('answerthree')
            answer4 = request.POST.get('answerfour')
            data.question=question
            data.option1=option1
            data.option2=option2
            data.option3=option3
            data.option4=option4
            data.answer1=answer1
            data.answer2=answer2
            data.answer3=answer3
            data.answer4=answer4
            data.save()
            return redirect(reverse('elisteningmcqedit', kwargs={'id': id_value}))
        return render(request ,template,{"data":data } )
    else:
       
        return redirect('login')


def elisteningtecqdeletepart(request,id):
    if 'username' in request.session:
   
        template="design/dashborad/english/traning/listening/edit/editmcq.html"
        
        data = get_object_or_404(Elisteningquiz, id=id)
        id_value = data.title_id
        if request.method == 'POST':
            data.delete()
            return redirect(reverse('elisteningmcqedit', kwargs={'id': id_value}))
        return render(request ,template,{"data":data } )
    else:
        
        return redirect('login')
# end traing listening english











































































def pythontestcase(request):
   
    template="design/dashborad/testcase/python.html"
    
   
    return render(request ,template,{} )
# RESUME BUILD
def resumebuild(request):
    if 'username' in request.session:
    
        template="design/dashborad/resumebuild/choose.html"
        
        return render(request ,template,{} )
    else:
       
        return redirect('login')


def rone(request):
    if 'username' in request.session:
        template="design/dashborad/resumebuild/one.html"
        
        if request.method == 'POST':
            job_title = request.POST.get('jobtitle')
            full_name = request.POST.get('fullName')
            email = request.POST.get('Email')
            phone = request.POST.get('Phone')
            country = request.POST.get('Country')
            city = request.POST.get('city')
            address = request.POST.get('Address')
            summary = request.POST.get('summary')

            # 
            xiiname = request.POST.get('xiiname')
            xiilocation = request.POST.get('xiilocation')
            xiistartdate = request.POST.get('xiistartdate')
            xiienddate = request.POST.get('xiienddate')
            xiidegree = request.POST.get('xiidegree')
            xiifieldstudy = request.POST.get('xiifieldstudy')
            xiidescription = request.POST.get('xiidescription')
            # 
            xname = request.POST.get('xname')
            xlocation = request.POST.get('xlocation')
            xstartdate = request.POST.get('xstartdate')
            xenddate = request.POST.get('xenddate')
            xdegree = request.POST.get('xdegree')
            xfieldstudy = request.POST.get('xfieldstudy')
            xdescription = request.POST.get('xdescription')
            # 
            ugname = request.POST.get('ugname')
            uglocation = request.POST.get('uglocation')
            ugstartdate = request.POST.get('ugstartdate')
            ugenddate = request.POST.get('ugenddate')
            ugdegree = request.POST.get('ugdegree')
            ugfieldstudy = request.POST.get('ugfieldstudy')
            ugdescription = request.POST.get('ugdescription')

            # Project
            projecttitle = request.POST.get('projecttitle')
            projectdescription = request.POST.get('projectdescription')

            # skill
            skilstag = request.POST.get('skilstag')

            print("skill",skilstag)


            obj=Projectresume()
            obj.title=projecttitle
            obj.descriptions=projectdescription
            obj.save()

            obj=Educationsresume()
            obj.xiiname=xiiname
            obj.xiilocations=xiilocation
            obj.xiistartdate=xiistartdate
            obj.xiienddate=xiienddate
            obj.xiidegree=xiidegree
            obj.xiifieldstudy=xiifieldstudy
            obj.xiidescriptions=xiidescription

            obj.xname=xname
            obj.xlocations=xlocation
            obj.xstartdate=xstartdate
            obj.xenddate=xenddate
            obj.xdegree=xdegree
            obj.xfieldstudy=xfieldstudy
            obj.xdescriptions=xdescription

            obj.ugname=ugname
            obj.uglocations=uglocation
            obj.ugstartdate=ugstartdate
            obj.ugenddate=ugenddate
            obj.ugdegree=ugdegree
            obj.ugfieldstudy=ugfieldstudy
            obj.ugdescriptions=ugdescription
            obj.save()


            obj=Personaldetails()
            obj.jobtitle= job_title
            obj.name= full_name
            obj.email=email 
            obj.phone= phone
            obj.country=country
            obj.city=city
            obj.address=address
            obj.save()

            obj=Profilesummary()
            obj.summary=summary
            obj.save()
    
            
        display=Personaldetails.objects.last()
        summarydata=Profilesummary.objects.last()
        image=TemplatedesignImage.objects.all()
        # display=Personaldetails.objects.get(id=59 )
        print("data sent")
        print("enter")
        
        project=Projectresume.objects.last()
        education=Educationsresume.objects.last()
        display=Personaldetails.objects.last()
        summarydata=Profilesummary.objects.last()
        # print("job titile",job_title)
        return render (request,template,{'data':display,'summary':summarydata,'image':image,'education':education , 'project':project })
    else:
       
        return redirect('login')

def rtwo(request):
    if 'username' in request.session:
    
        template="design/dashborad/resumebuild/two.html"
        
        if request.method == 'POST':
            job_title = request.POST.get('jobtitle')
            full_name = request.POST.get('fullName')
            email = request.POST.get('Email')
            phone = request.POST.get('Phone')
            country = request.POST.get('Country')
            city = request.POST.get('city')
            address = request.POST.get('Address')
            summary = request.POST.get('summary')

            # 
            xiiname = request.POST.get('xiiname')
            xiilocation = request.POST.get('xiilocation')
            xiistartdate = request.POST.get('xiistartdate')
            xiienddate = request.POST.get('xiienddate')
            xiidegree = request.POST.get('xiidegree')
            xiifieldstudy = request.POST.get('xiifieldstudy')
            xiidescription = request.POST.get('xiidescription')
            # 
            xname = request.POST.get('xname')
            xlocation = request.POST.get('xlocation')
            xstartdate = request.POST.get('xstartdate')
            xenddate = request.POST.get('xenddate')
            xdegree = request.POST.get('xdegree')
            xfieldstudy = request.POST.get('xfieldstudy')
            xdescription = request.POST.get('xdescription')
            # 
            ugname = request.POST.get('ugname')
            uglocation = request.POST.get('uglocation')
            ugstartdate = request.POST.get('ugstartdate')
            ugenddate = request.POST.get('ugenddate')
            ugdegree = request.POST.get('ugdegree')
            ugfieldstudy = request.POST.get('ugfieldstudy')
            ugdescription = request.POST.get('ugdescription')

            # Project
            projecttitle = request.POST.get('projecttitle')
            projectdescription = request.POST.get('projectdescription')

            # skill
            skilstag = request.POST.get('skilstag')

            print("skill",skilstag)


            obj=Projectresume()
            obj.title=projecttitle
            obj.descriptions=projectdescription
            obj.save()

            obj=Educationsresume()
            obj.xiiname=xiiname
            obj.xiilocations=xiilocation
            obj.xiistartdate=xiistartdate
            obj.xiienddate=xiienddate
            obj.xiidegree=xiidegree
            obj.xiifieldstudy=xiifieldstudy
            obj.xiidescriptions=xiidescription

            obj.xname=xname
            obj.xlocations=xlocation
            obj.xstartdate=xstartdate
            obj.xenddate=xenddate
            obj.xdegree=xdegree
            obj.xfieldstudy=xfieldstudy
            obj.xdescriptions=xdescription

            obj.ugname=ugname
            obj.uglocations=uglocation
            obj.ugstartdate=ugstartdate
            obj.ugenddate=ugenddate
            obj.ugdegree=ugdegree
            obj.ugfieldstudy=ugfieldstudy
            obj.ugdescriptions=ugdescription
            obj.save()


            obj=Personaldetails()
            obj.jobtitle= job_title
            obj.name= full_name
            obj.email=email 
            obj.phone= phone
            obj.country=country
            obj.city=city
            obj.address=address
            obj.save()

            obj=Profilesummary()
            obj.summary=summary
            obj.save()

            
        display=Personaldetails.objects.last()
        summarydata=Profilesummary.objects.last()
        image=TemplatedesignImage.objects.all()
        # display=Personaldetails.objects.get(id=59 )
        print("data sent")
        print("enter")
        
        project=Projectresume.objects.last()
        education=Educationsresume.objects.last()
        display=Personaldetails.objects.last()
        summarydata=Profilesummary.objects.last()
        # print("job titile",job_title)
        return render (request,template,{'data':display,'summary':summarydata,'image':image,'education':education , 'project':project })
    else:
       
        return redirect('login')

def rthree(request):
    if 'username' in request.session:
   
        template="design/dashborad/resumebuild/three.html"

        if request.method == 'POST':
            job_title = request.POST.get('jobtitle')
            full_name = request.POST.get('fullName')
            email = request.POST.get('Email')
            phone = request.POST.get('Phone')
            country = request.POST.get('Country')
            city = request.POST.get('city')
            address = request.POST.get('Address')
            summary = request.POST.get('summary')

            # 
            xiiname = request.POST.get('xiiname')
            xiilocation = request.POST.get('xiilocation')
            xiistartdate = request.POST.get('xiistartdate')
            xiienddate = request.POST.get('xiienddate')
            xiidegree = request.POST.get('xiidegree')
            xiifieldstudy = request.POST.get('xiifieldstudy')
            xiidescription = request.POST.get('xiidescription')
            # 
            xname = request.POST.get('xname')
            xlocation = request.POST.get('xlocation')
            xstartdate = request.POST.get('xstartdate')
            xenddate = request.POST.get('xenddate')
            xdegree = request.POST.get('xdegree')
            xfieldstudy = request.POST.get('xfieldstudy')
            xdescription = request.POST.get('xdescription')
            # 
            ugname = request.POST.get('ugname')
            uglocation = request.POST.get('uglocation')
            ugstartdate = request.POST.get('ugstartdate')
            ugenddate = request.POST.get('ugenddate')
            ugdegree = request.POST.get('ugdegree')
            ugfieldstudy = request.POST.get('ugfieldstudy')
            ugdescription = request.POST.get('ugdescription')

            # Project
            projecttitle = request.POST.get('projecttitle')
            projectdescription = request.POST.get('projectdescription')

            # skill
            skilstag = request.POST.get('skilstag')

            print("skill",skilstag)


            obj=Projectresume()
            obj.title=projecttitle
            obj.descriptions=projectdescription
            obj.save()

            obj=Educationsresume()
            obj.xiiname=xiiname
            obj.xiilocations=xiilocation
            obj.xiistartdate=xiistartdate
            obj.xiienddate=xiienddate
            obj.xiidegree=xiidegree
            obj.xiifieldstudy=xiifieldstudy
            obj.xiidescriptions=xiidescription

            obj.xname=xname
            obj.xlocations=xlocation
            obj.xstartdate=xstartdate
            obj.xenddate=xenddate
            obj.xdegree=xdegree
            obj.xfieldstudy=xfieldstudy
            obj.xdescriptions=xdescription

            obj.ugname=ugname
            obj.uglocations=uglocation
            obj.ugstartdate=ugstartdate
            obj.ugenddate=ugenddate
            obj.ugdegree=ugdegree
            obj.ugfieldstudy=ugfieldstudy
            obj.ugdescriptions=ugdescription
            obj.save()


            obj=Personaldetails()
            obj.jobtitle= job_title
            obj.name= full_name
            obj.email=email 
            obj.phone= phone
            obj.country=country
            obj.city=city
            obj.address=address
            obj.save()

            obj=Profilesummary()
            obj.summary=summary
            obj.save()
        

            
        display=Personaldetails.objects.last()
        summarydata=Profilesummary.objects.last()
        image=TemplatedesignImage.objects.all()
        # display=Personaldetails.objects.get(id=59 )
        print("data sent")
        print("enter")
        
        project=Projectresume.objects.last()
        education=Educationsresume.objects.last()
        display=Personaldetails.objects.last()
        summarydata=Profilesummary.objects.last()
        # print("job titile",job_title)
        return render (request,template,{'data':display,'summary':summarydata,'image':image,'education':education , 'project':project })
    else:
       
        return redirect('login')

def rfour(request):
    if 'username' in request.session:
        template="design/dashborad/resumebuild/four.html"
        
        if request.method == 'POST':
            job_title = request.POST.get('jobtitle')
            full_name = request.POST.get('fullName')
            email = request.POST.get('Email')
            phone = request.POST.get('Phone')
            country = request.POST.get('Country')
            city = request.POST.get('city')
            address = request.POST.get('Address')
            summary = request.POST.get('summary')

            # 
            xiiname = request.POST.get('xiiname')
            xiilocation = request.POST.get('xiilocation')
            xiistartdate = request.POST.get('xiistartdate')
            xiienddate = request.POST.get('xiienddate')
            xiidegree = request.POST.get('xiidegree')
            xiifieldstudy = request.POST.get('xiifieldstudy')
            xiidescription = request.POST.get('xiidescription')
            # 
            xname = request.POST.get('xname')
            xlocation = request.POST.get('xlocation')
            xstartdate = request.POST.get('xstartdate')
            xenddate = request.POST.get('xenddate')
            xdegree = request.POST.get('xdegree')
            xfieldstudy = request.POST.get('xfieldstudy')
            xdescription = request.POST.get('xdescription')
            # 
            ugname = request.POST.get('ugname')
            uglocation = request.POST.get('uglocation')
            ugstartdate = request.POST.get('ugstartdate')
            ugenddate = request.POST.get('ugenddate')
            ugdegree = request.POST.get('ugdegree')
            ugfieldstudy = request.POST.get('ugfieldstudy')
            ugdescription = request.POST.get('ugdescription')

            # Project
            projecttitle = request.POST.get('projecttitle')
            projectdescription = request.POST.get('projectdescription')

            # skill
            skilstag = request.POST.get('skilstag')

            print("skill",skilstag)


            obj=Projectresume()
            obj.title=projecttitle
            obj.descriptions=projectdescription
            obj.save()

            obj=Educationsresume()
            obj.xiiname=xiiname
            obj.xiilocations=xiilocation
            obj.xiistartdate=xiistartdate
            obj.xiienddate=xiienddate
            obj.xiidegree=xiidegree
            obj.xiifieldstudy=xiifieldstudy
            obj.xiidescriptions=xiidescription

            obj.xname=xname
            obj.xlocations=xlocation
            obj.xstartdate=xstartdate
            obj.xenddate=xenddate
            obj.xdegree=xdegree
            obj.xfieldstudy=xfieldstudy
            obj.xdescriptions=xdescription

            obj.ugname=ugname
            obj.uglocations=uglocation
            obj.ugstartdate=ugstartdate
            obj.ugenddate=ugenddate
            obj.ugdegree=ugdegree
            obj.ugfieldstudy=ugfieldstudy
            obj.ugdescriptions=ugdescription
            obj.save()


            obj=Personaldetails()
            obj.jobtitle= job_title
            obj.name= full_name
            obj.email=email 
            obj.phone= phone
            obj.country=country
            obj.city=city
            obj.address=address
            obj.save()

            obj=Profilesummary()
            obj.summary=summary
            obj.save()
        

            
        display=Personaldetails.objects.last()
        summarydata=Profilesummary.objects.last()
        image=TemplatedesignImage.objects.all()
        # display=Personaldetails.objects.get(id=59 )
        print("data sent")
        print("enter")
        
        project=Projectresume.objects.last()
        education=Educationsresume.objects.last()
        display=Personaldetails.objects.last()
        summarydata=Profilesummary.objects.last()
        # print("job titile",job_title)
        return render (request,template,{'data':display,'summary':summarydata,'image':image,'education':education , 'project':project })
    else:
       
        return redirect('login')


# END RESUME BUILD

# video

from .models import Demovideo,Uploadvideosections

def uploadvideo(request):
    if request.method == 'POST' and request.FILES.get('video_file'):
        title = request.POST.get('title')
        video_file = request.FILES['video_file']
        Demovideo.objects.create(title=title, video_file=video_file)
        return redirect('video_list')  # Assuming you have a URL named 'video_list'
    return render(request, 'ademovideo.html')

def video_list(request):
    videos = Demovideo.objects.all()
    return render(request, 'avideo_list.html', {'videos': videos})

def videoupload(request):
   
    template="design/dashborad/javatrainee/videoupload.html"
    titlehead=Javatraingtitle.objects.all()

    if request.method == 'POST' and request.FILES.get('video_file'):
        title = request.POST.get('type')
        video_file = request.FILES['video_file']
        con = request.POST.get('content')



        Uploadvideosections.objects.create(title_id=title, video_file=video_file , content= con)


    return render(request ,template,{"data":titlehead} )



# sidebar
@login_required
def sidebar(request):
    userid = request.user.id
    success = Userpermistionupload.objects.filter(user_id=userid)
    # success = "hello"
    
    return {'sidebar_data': success}


from django.contrib.auth.hashers import make_password


def employeenext(request):
    template="design/dashborad/access/employeenext.html"
    employee=User.objects.filter(first_name="employee")
    print("employee",employee)
    if request.method == 'POST':
        emid = request.POST.get('emp')
        
        data1 = request.POST.get('data1')
        data2 = request.POST.get('data2')
        data3 = request.POST.get('data3')
        data4 = request.POST.get('data4')
        data5 = request.POST.get('data5')
        data6 = request.POST.get('data6')
        data7 = request.POST.get('data7')
        data8 = request.POST.get('data8')
        data9 = request.POST.get('data9')
        data10 = request.POST.get('data10')
        
        print("emp",emid)
        print("data1",data1)
        print("data2",data2)
        print("data3",data3)
        print("data3",data3)
        print("data4",data4)
        print("data5",data5)
        print("data6",data6)
        print("data7",data7)
        print("data8",data8)
        print("data9",data9)
        print("data10",data10)
     
        # # if User.objects.filter(email=email).exists():
        # #     return render(request,template, {'error_message': 'Email already exists'})

        # encrypted_password = make_password(password)
        Userpermistionupload.objects.create(job_id=data10,pd_id=data9,workshop_id=data8,intership_id=data7,english_id=data6,cpp_id=data5,python_id=data4,java_id=data3,c_id=data2,aptitude_id=data1,user_id=emid )
        # return redirect('login')

    return render(request,template, {'user':employee})

def employeeupload(request):
    template="design/dashborad/access/employee.html"
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        
        email = request.POST.get('email')
        password = request.POST.get('password')
        # if User.objects.filter(email=email).exists():
        #     return render(request,template, {'error_message': 'Email already exists'})

        encrypted_password = make_password(password)



        User.objects.create( first_name="employee", username=fullname, email=email , password= encrypted_password , is_active = 1)
        return redirect('employeenext')

    return render(request,template, {})


def studentnext(request):
    template="design/dashborad/access/studentnext.html"
    student=User.objects.filter(first_name="student")

    if request.method == 'POST':
        emid = request.POST.get('emp')
        
        data1 = request.POST.get('data1')
        
        
       
        Userpermistionupload.objects.create(tenx_id=data1 ,user_id=emid)
        # return redirect(dsd'lodsgin')

    return render(request,template, {'user':student})

def studentupload(request):
    template="design/dashborad/access/student.html"
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        
        email = request.POST.get('email')
        password = request.POST.get('password')
      
        encrypted_password = make_password(password)



        User.objects.create( first_name="student", username=fullname, email=email , password= encrypted_password , is_active = 1)
        return redirect('studentnext')

    return render(request,template, {})

# demo



