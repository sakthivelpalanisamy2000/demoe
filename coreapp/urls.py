"""adminproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from coreapp import views

urlpatterns = [

#  chat gpt
    path('b263ec24-57bd-424c-9dd1-90863f467dea', views.amain, name='amain'),
    path('celebrate', views.celebrate, name='celebrate'),
    path('job', views.job, name='job'),


    
    path('generate_recipe', views.generate_recipe, name='generate_recipe'),
    path('indexchatgpt', views.indexchatgpt, name='indexchatgpt'),
    


    # trial


    path('subscribe/<int:product_id>/', views.subscribe_to_product, name='subscribe_to_product'),
    path('trial_status/<int:product_id>/', views.check_trial_status, name='check_trial_status'),


    # endtrilal
    path("demoresumecheck", views.resumedemo, name="resume"),
    path("compiler", views.compiler, name="compiler"),

    path("pythoncompiler", views.pythoncompiler, name="compiler"),
    path("c", views.ccode, name="c"),
    path("testing", views.testing, name="testing"),
    path("javat", views.javatesting, name="javat"),
    path("pythont", views.pythontesting, name="testing"),
    path("ct", views.ctesting, name="downloadexcel"),
    path("javat",views.outputvalue, name="outputvalue"),



    path("addquestions", views.addquestions, name="addquestions"),
    path("post", views.postadddemo, name="post"),
    path("display", views.demoquestiondisplay, name="display"),
    path("check", views.check, name="check"),

    # path("sent",views.sent, name="sent"),
    path("sent",views.sentadd, name="sentadd"),
    path("javaaddpage",views.javaaddpage, name="javaadd"),

# 
    path('home', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('Upload_Question/', views.new, name='new'),
    path('Test/', views.taketest, name='taketest'),
    path('my-view/<int:my_id>/', views.my_view, name='id'),

    path('resume', views.resume, name='resume'),

    path('desgin', views.desgincode, name='desgin'),
    path('choosetemplatedesign', views.choosetempale, name='choosetemplatedesign'),


# RESUME

    path("personaldetails",views.personaldetails, name="personaldetails"),
    path("bumlaaddcss",views.bumlaaddcss, name="bumlaaddcss"),
    path("showdesign",views.showdesign, name="showdesign"),
    path('classical', views.templateone, name='templateone'),
    path('classical-2', views.templatetwo, name='templatetwo'),
    path('modern_Resume', views.templatethree, name='templatethree'),
    path('modern_Resume-2', views.templatefour, name='templatefour'),

    path('savevalue', views.savevalue, name='savevalue'),
    # javatestcase
    path('javatestcase/<int:testcase_id>', views.javatestcase, name='javatestcase'),
    path('javatestcaseview', views.javatestcaseview, name='javatestcaseview'),
    path('javareportpage', views.javareportpage, name='javareportpage'),


    path('uploadjava', views.uploadjava, name='uploadjava'),
    path('javacompiler/<int:compiler_id>', views.javacompiler, name='javacompiler'),
    path('javapracticeview', views.javapracticeview, name='javapracticeview'),
    path('javapracticeupload', views.javapracticeupload, name='javapracticeupload'),
    # no use only share add data
    path('javapracticelevel', views.javapracticelevel, name='javapracticelevel'),
    path('javatestcaselevel', views.javatestcaselevel, name='javatestcaselevel'),
    path('javatraning', views.javatraning, name='javatraning'),
    path('javacomplete/<int:globel_id>', views.javacomplete, name='javacomplete'),
    path('practiceview', views.practiceview, name='practiceview'),
    path('uploadjavatraing', views.uploadjavatraing, name='uploadjavatraing'),
    path('uploadjavatraingmcq', views.uploadjavatraingmcq, name='uploadjavatraingmcq'),
    path('video/<int:video_id>', views.video, name='video'),
    path('traningcompiler', views.traningcompiler, name='traningcompiler'),
    path('examdetails', views.examdetails, name='examdetails'),
    path('javatrainingtest', views.javatrainingtest, name='javatrainingtest'),
    path('topicupload', views.topicupload, name='topicupload'),
    path('videoupload', views.videoupload, name='videoupload'),
    path('mcqupload', views.mcqupload, name='mcqupload'),
    path('codingtestupload', views.codingtestupload, name='codingtestupload'),
    path('mcqtest', views.mcqtest, name='mcqtest'),
    path('upload', views.uploadvideo, name='uploadvideo'),
    path('video_list', views.video_list, name='video_list'),


    # 



    # edit delet java
    path('javatraningtranieeview', views.javatraningtranieeview, name='javatraningtranieeview'),

    path('item/<int:pk>/delete/', views.traningtitle_delete, name='item_delete'),
    path('titleupdateid', views.titleupdateid, name='titleupdateid'),
    path('item/<int:pk>', views.edittopic, name='item_update'),
    path('titleupdate/<int:pk>', views.updatetopic, name='titleupdate'),
    path('editvideo/<int:editvideo_id>', views.editvideo, name='aeditvideo'),
    path('editvideopart/<int:editvideopart_id>', views.editvideopart, name='editvideopart'),
    path('updatevideopart/<int:updatevideo>', views.updateeditvideopart, name='updatevideopart'),
    path('codeview/<int:editcoding>', views.editcodeingview, name='editcodeingview'),
    path('editcodeing/<int:codeupadate_id>', views.editupdatecodeing, name='codeupadate'),
    path('deletecodeing/<int:codedelete_id>', views.editdeletecodeing, name='codedelete'),
    path('viewpracties', views.viewpracties, name='viewpracties'),
    path('edit_title/<int:ptitle_id>', views.titlepractiesedit, name='titlepractice'),
    path('pquestionedit/<int:compiler_id>', views.pquestionedit, name='pquestionedit'),
    path('pdeletequestion/<int:questiondelete_id>', views.pdeletequestion, name='pdeletequestion'),
    path('pquestioneditview/<int:questionupdate>', views.pquestioneditview, name='pquestioneditview'),
    path('titlepractiedelete/<int:titledelete>', views.titlepractiedelete, name='titlepractiedelete'),
    path('testtitle', views.testtitleview, name='testtitleview'),
    path('testtitleupdate/<int:title_id>', views.testtitleupdate, name='testtitleupdate'),
    path('testtitledelete/<int:title_id>', views.testtitledelete, name='testtitledelete'),

    path('testcasequestion/<int:testcase>', views.testquestionview, name='testcasequestionview'),
    path('testdeletequestion/<int:testcase_id>', views.testdeletequestion, name='testdeletequestion'),
    path('quiz', views.quiz, name='quiz'),
    path('quizupload', views.quizupload, name='quizupload'),

    
    # end edit

# aptitude path
    path('bc09a074-eeb0-4779-8469-1d91a35dc5bb/aptitudestart', views.aptitudestart, name='aptitudestart'),
    path('aptitudevideo/3c5bdb06-9caf-432f-9192-42e54fb112bc<int:appvideoid>', views.aptitudevideo, name='aptitudevideo'),
    path('aptitudemcq/9668cdb2-2905-4d7c-bb3d-b1c0edecbbb4<int:app_id>', views.aptitudemcq, name='aptitudemcq'),

    # aptitude upload      
    path('aptitudetitleupload/e072538b-4f82-4bb6-adfb-bf743968db55', views.aptitudetitleupload, name='aptitudetitleupload'),
    path('aptitudevideoupload/c6b759e9-3680-487b-8b90-104cf4e60ec1', views.aptitudevideoupload, name='aptitudevideoupload'),
    path('aptitudemcqupload/825ccbeb-6d23-4577-bd52-723ec3e64a7a', views.aptitudemcqupload, name='aptitudemcqupload'),

    # APP UPLOAD
    path('appview/e656a34c-40cf-4e5c-864f-4629cbbd968a', views.appview, name='appview'),
    path('appmcqview/e7aaa674-37fc-4f03-9267-74b2cb6a8da5<int:app_id>', views.appmcqview, name='appmcqview'),

    path('appmcqupload/c5fea9ca-60af-4a77-bcaf-bffd1f746cc7', views.appmcqupload, name='appmcqupload'),
    path('apptitleupload/e9a89080-4cf0-417a-9550-b7dbc6b1bc6d', views.apptitleupload, name='apptitleupload'),

    path('appeeditview/a1d93938-cc61-4348-8e16-932e5fca4c49', views.appeeditview, name='appeeditview'),
    path('apptitleedit/c8ae9548-0174-48a9-8947-2430bec41025<int:id>', views.apptitleedit, name='apptitleedit'),
    path('apptitledelet/49f42b1d-fe91-45bf-9dd8-d12f1bc2884c<int:id>', views.apptitledelet, name='apptitledelete'),
    path('appmcqedit/2f677e34-b319-468f-b0aa-f8f55e54682d<int:id>', views.appmcqedit, name='appmcqedit'),
    path('appmcqeditpart/8f3bd371-a9f2-4023-82b7-f467a0988bab<int:id>', views.appmcqeditpart, name='appmcqeditpart'),
    path('appmcqdeletepart/d8f0d0fd-bc0c-44f0-9206-30c7511857a0<int:id>', views.appmcqdeletepart, name='appmcqdeletepart'),

    # traing app
    path('apptetview/f99dfd50-1eb9-4580-b2a7-7576072625fc', views.apptetview, name='apptetview'),
    path('apptetitle/d886d0bf-bf2b-43ad-be69-d835aafd2489<int:id>', views.apptetitle, name='apptetitle'),
    path('apptetitledelet/ff9af424-3196-4b47-a8f9-8dc2364fc568<int:id>', views.apptetitledelet, name='apptetitledelete'),
    path('apptemcqedit/0b4edc37-f55f-43fa-a778-d5effeab6882<int:id>', views.apptemcqedit, name='apptemcqedit'),
    path('apptemcqeditpart/9c555a20-079d-4ee3-91ef-0d766783fed1<int:id>', views.apptemcqeditpart, name='apptemcqeditpart'),
    path('appmtecqdeletepart/c4928474-9639-4641-895a-041b45d1915f<int:id>', views.appmtecqdeletepart, name='appmtecqdeletepart'),
    path('appvideoview/130d6b46-3e89-4410-9359-be2eb816bddd<int:appvideoid>', views.appvideoview, name='appvideoview'),
    path('appvideoedit/bb55403d-fd8e-49c9-8469-b56acc1daec6<int:id>', views.appvideoedit, name='appvideoedit'),
    path('appvideodelete/e0c19e7c-ef58-4f20-a045-23dfa361181f<int:id>', views.appvideodelete, name='appvideodelete'),





    

# pd start
    path('pdview/73d93c80-83d7-4c9f-ad44-31ccb71341dc', views.pdview, name='pdview'),
    path('pdvideo/f9585a0b-f79b-46e2-9d75-5360af732651<int:pdvideoid>', views.pdvideo, name='pdvideo'),
    path('pdtitleupload/0f5d39c8-9c6a-4476-9cb2-c278bbf7ea15', views.pdtitleupload, name='pdtitleupload'),
    path('pdvideoupload/f3257131-d795-47db-be14-9c9cc0c8ace8', views.pdvideoupload, name='pdvideoupload'),
    # pd edit and view
    path('pdeditview/2645361a-432e-4a83-97a9-4c153875e61d', views.pdeditview, name='pdeditview'),
    path('pdvideoview/9eff9d3f-9c1e-4acd-9da9-54a6eb5f7c25<int:pdeditid>', views.pdvideoview, name='pdvideoview'),
    path('pdtitleedit/801bd264-a7d6-43f4-ae66-913607c14d4f<int:id>', views.pdtitleedit, name='pdtitleedit'),
    path('pdtitledelet/9520df73-c51b-4cbe-a80e-8583f9c94e1c<int:id>', views.pdtitledelet, name='pdtitledelete'),
    path('pdeditvieo/3ba73be6-f797-43ce-8028-aa1643c8b31f<int:pdeditid>', views.pdeditvieo, name='pdeditvieo'),
    path('pdvideodelete/4f5d57e7-7e48-4e9b-880b-53ebd7f7d0bf<int:id>', views.pdvideodelete , name='pdvideodelete'),


# workshop start
    path('workoshopannouncement/7fa44937-f5c7-4ba2-9210-ccfc7c306711', views.workoshopannouncement, name='workoshopannouncement'),
    path('workoshopcertificate/2fe4717f-a82c-4b86-b09b-72ecb1f00861', views.workoshopcertificate, name='workoshopcertificate'),

    path('workshopstart/9ef2ef42-65ef-497d-a6bc-8990a726743f', views.workshopstart, name='workshopstart'),
    path('workshopvideo/abd776d3-0b4d-47bb-92e1-c2725853e454<int:appvideoid>', views.workshopvideo, name='workshopvideo'),
    path('workshopmcq/8b9a2600-c9d2-4a5e-9045-53cac0ebedf3<int:app_id>', views.workshopmcq, name='workshopmcq'),

    # workshop upload      
    path('workshoptitleupload/bed30ba3-5807-46d6-8a79-d6039e04827a', views.workshoptitleupload, name='workshoptitleupload'),
    path('workshopvideoupload/8a3d40c4-f654-4884-9bc6-3682c65cb42e', views.workshopvideoupload, name='workshopvideoupload'),
    path('workshopmcqupload/283529dd-40c9-4854-91e9-dcd7fd82060b', views.workshopmcqupload, name='workshopmcqupload'),

    # Workedit edi
    path('workshopteview/f66b327f-a1a4-4581-b32e-b2bbc2b182a7', views.workshopteview, name='workshopteview'),
    path('workshoptetitle/247e2cd6-e31b-4313-ba88-366797c98643<int:id>', views.workshoptetitle, name='workshoptetitle'),
    path('workshoptdelete/d1c3a917-c3c0-4300-a4db-3caaf84b4316<int:id>', views.workshoptdelete, name='workshoptdelete'),
    path('workshoptemcqedit/21f8fdab-681a-41fc-bafd-4ada487d9d2e<int:id>', views.workshoptemcqedit, name='workshoptemcqedit'),
    path('workshoptemcqeditpart/956500e9-d0b3-4190-8360-1ddf33b63d7c<int:id>', views.workshoptemcqeditpart, name='workshoptemcqeditpart'),
    path('workshoptecqdeletepart/776384ac-83c3-46d2-8b66-b79ba31fc153<int:id>', views.workshoptecqdeletepart, name='workshoptecqdeletepart'),
    path('workshopvideoview/8be59dcc-3e22-4a4d-ae74-a526dfac5dd9<int:appvideoid>', views.workshopvideoview, name='workshopvideoview'),
    path('workshopvideoedit/be442b43-2be4-4df1-b81d-8170e7c156a3<int:id>', views.workshopvideoedit, name='workshopvideoedit'),
    path('workshopvideodelete/3f2569db-8adf-486f-808e-17a7f5f3f1e2<int:id>', views.workshopvideodelete, name='workshopvideodelete'),


    # intership
    path('intershipannouncement/637a39cc-6b81-41b6-a58d-7222842b5e6b', views.intershipannouncement, name='intershipannouncement'),
    path('intershipcertificate/56b49f97-0e5f-437a-9a37-7855169adac3', views.intershipcertificate, name='intershipcertificate'),

    path('intershipstart/46998440-4a73-4128-87cb-e6dce645a49c', views.intershipstart, name='intershipstart'),
    path('intershipvideo/0b0a58de-d3b0-4b25-b8ff-4457c407c82b<int:appvideoid>', views.intershipvideo, name='intershipvideo'),
    path('intershipmcq/4a712a00-5718-4877-a2ee-5abf0ca06e7e<int:app_id>', views.intershipmcq, name='intershipmcq'),

    # intership upload      
    path('intershiptitleupload/37e890df-61cb-483b-875a-4960b9ebc8ff', views.intershiptitleupload, name='intershiptitleupload'),
    path('intershipvideoupload/617e6d28-de5b-4d31-a894-6dc8ad771417', views.intershipvideoupload, name='intershipvideoupload'),
    path('intershipmcqupload/feb8dc09-5392-4b96-a388-291ea61c8887', views.intershipmcqupload, name='intershipmcqupload'),

    # intership edi
    path('intershipteview/4d4ee842-c881-4d10-b99a-5444978f4cc5', views.intershipteview, name='intershipteview'),
    path('intershiptetitle/9425f19b-3198-44d6-a82d-f6eabe532f71<int:id>', views.intershiptetitle, name='intershiptetitle'),
    path('intershiptdelete/5e399de4-e667-42dd-9be3-33823c10cebf<int:id>', views.intershiptdelete, name='intershiptdelete'),
    path('intershiptemcqedit/be31e3df-7669-40e4-84b2-ddccbb716685<int:id>', views.intershiptemcqedit, name='intershiptemcqedit'),
    path('intershiptemcqeditpart/c723edbf-6e5c-4210-8212-24833cfb5709<int:id>', views.intershiptemcqeditpart, name='intershiptemcqeditpart'),
    path('intershiptecqdeletepart/1ca68382-7f29-472f-aa42-6b888228d667<int:id>', views.intershiptecqdeletepart, name='intershiptecqdeletepart'),
    path('intershipvideoview/3069431d-eabc-47b6-9bf0-76fcf7c1da52<int:appvideoid>', views.intershipvideoview, name='intershipvideoview'),
    path('intershipvideoedit/ad35b1ba-c495-44ea-977d-ef5a251b7655<int:id>', views.intershipvideoedit, name='intershipvideoedit'),
    path('intershipvideodelete/677b97e3-9b1a-4ab3-8d88-4f83235fae37<int:id>', views.intershipvideodelete, name='intershipvideodelete'),


# english traing
    path('englishtraing/e29b983e-710d-4f9d-b39b-72662a9f82a3', views.englishtraing, name='englishtraing'),
    path('technicalenglish/54ce8463-f6e4-46b4-994f-5ac591a4c777', views.technicalenglish, name='technicalenglish'),
    path('etechnicalvideo/236e2af9-bb43-4023-b6a8-a3ba19855ef8<int:appvideoid>', views.etechnicalvideo, name='etechnicalvideo'),
    path('etechnicalmcq/75b6054c-34ab-48a3-ac7b-af0f30447875<int:app_id>', views.etechnicalmcq, name='etechnicalmcq'),

    # etechnical upload      
    path('etechnicaltitleupload/e6464038-af32-45a0-a9db-4770346fa02a', views.etechnicaltitleupload, name='etechnicaltitleupload'),
    path('etechnicalvideoupload/ed822b62-92c8-4f25-8227-b47364248e21', views.etechnicalvideoupload, name='etechnicalvideoupload'),
    path('etechnicalmcqupload/2ee498db-067a-48a8-a90a-452fe8349988', views.etechnicalmcqupload, name='etechnicalmcqupload'),
 
    # etehnical 

    path('etechnicaltview', views.etechnicaltview, name='etechnicaltview'),
    path('etechnicaltitle/<int:id>', views.etechnicaltitle, name='etechnicaltitle'),
    path('etechnicaltitledelet/<int:id>', views.etechnicaltitledelet, name='etechnicaltitledelet'),
    path('etechnicalmcqedit/<int:id>', views.etechnicalmcqedit, name='etechnicalmcqedit'),
    path('etechnicalmcqeditpart/<int:id>', views.etechnicalmcqeditpart, name='etechnicalmcqeditpart'),
    path('etechnicaltecqdeletepart/<int:id>', views.etechnicaltecqdeletepart, name='etechnicaltecqdeletepart'),
    path('etechnicalvideoview/<int:appvideoid>', views.etechnicalvideoview, name='etechnicalvideoview'),
    path('etechnicalvideoedit/<int:id>', views.etechnicalvideoedit, name='etechnicalvideoedit'),
    path('etechnicalvideodelete/<int:id>', views.etechnicalvideodelete, name='etechnicalvideodelete'),






    


    # business english

    path('businessenglish/bc3ba6eb-4dcf-4632-860c-38ecb9e7b76f', views.businessenglish, name='businessenglish'),
    path('ebusinessvideo/ffb82536-4119-43dc-a287-229ee41d2bd8<int:appvideoid>', views.ebusinessvideo, name='ebusinessvideo'),
    path('ebusinessmcq/ea943342-45fd-4153-a849-9b9db090f5d4<int:app_id>', views.ebusinessmcq, name='ebusinessmcq'),

    # ebusiness upload      
    path('ebusinesstitleupload/ad01a77f-66b9-467e-9ac0-12e5dc3ca963', views.ebusinesstitleupload, name='ebusinesstitleupload'),
    path('ebusinessvideoupload/da72a1b5-065b-449e-bff9-ee7c27324bfd', views.ebusinessvideoupload, name='ebusinessvideoupload'),
    path('ebusinessmcqupload/eb87dfee-5aeb-46c5-b9ca-9389850fc202', views.ebusinessmcqupload, name='ebusinessmcqupload'),
# edit bussiness
    path('ebusinesstview', views.ebusinesstview, name='ebusinesstview'),
    path('ebusinesstitle/<int:id>', views.ebusinesstitle, name='ebusinesstitle'),
    path('ebusinesstitledelet/<int:id>', views.ebusinesstitledelet, name='ebusinesstitledelet'),
    path('ebusinessmcqedit/<int:id>', views.ebusinessmcqedit, name='ebusinessmcqedit'),
    path('ebusinessmcqeditpart/<int:id>', views.ebusinessmcqeditpart, name='ebusinessmcqeditpart'),
    path('ebusinesstecqdeletepart/<int:id>', views.ebusinesstecqdeletepart, name='ebusinesstecqdeletepart'),
    path('ebusinessvideoview/<int:appvideoid>', views.ebusinessvideoview, name='ebusinessvideoview'),
    path('ebusinessvideoedit/<int:id>', views.ebusinessvideoedit, name='ebusinessvideoedit'),
    path('ebusinessvideodelete/<int:id>', views.ebusinessvideodelete, name='ebusinessvideodelete'),


    # spoken english

    path('spokenenglish/fda589c7-c689-4c49-922a-463d4074c269', views.spokenenglish, name='spokenenglish'),
    path('espokenvideo/b5d84e8d-ecd3-4003-9c04-b1a29e952086<int:appvideoid>', views.espokenvideo, name='espokenvideo'),
    path('espokenmcq/cb43fe34-6d2c-4e38-9b91-c668c8562bdb<int:app_id>', views.espokenmcq, name='espokenmcq'),

    # espoken upload      
    path('espokentitleupload/ed33086e-2a54-45a8-b43a-bd1b66bc50ae', views.espokentitleupload, name='espokentitleupload'),
    path('espokenvideoupload/d035d127-b69c-47a3-9bf3-0497861ec0bf', views.espokenvideoupload, name='espokenvideoupload'),
    path('espokenmcqupload/9feb06aa-145c-4172-b48a-b4677df68129', views.espokenmcqupload, name='espokenmcqupload'),

    # edit espoken
    
    path('espokentview', views.espokentview, name='espokentview'),
    path('espokentitle/<int:id>', views.espokentitle, name='espokentitle'),
    path('espokentitledelet/<int:id>', views.espokentitledelet, name='espokentitledelet'),
    path('espokenmcqedit/<int:id>', views.espokenmcqedit, name='espokenmcqedit'),
    path('espokenmcqeditpart/<int:id>', views.espokenmcqeditpart, name='espokenmcqeditpart'),
    path('espokentecqdeletepart/<int:id>', views.espokentecqdeletepart, name='espokentecqdeletepart'),
    path('espokenvideoview/<int:appvideoid>', views.espokenvideoview, name='espokenvideoview'),
    path('espokenvideoedit/<int:id>', views.espokenvideoedit, name='espokenvideoedit'),
    path('espokenvideodelete/<int:id>', views.espokenvideodelete, name='espokenvideodelete'),

    # path('generate_audio', views.generate_audio, name='generate_audio'),
    path('text-to-audio/a534fed2-81ca-47da-a786-718eb7a7b594', views.text_to_audio, name='text_to_audio'),

    # listening

    path('onelist/beed3601-4ff2-404e-8c08-238421a0319d', views.listening, name='listening'),
    path('listeningenglish/73e3aa38-6402-4aa5-a4fe-512c4c6bbb04', views.listeningenglish, name='listeningenglish'),
    path('elisteningreder/2db53005-f33d-4ea3-8ade-befbbfa3cf0c<int:appvideoid>', views.elisteningreder, name='elisteningreder'),
    path('elisteningmcq/2d7de94c-5154-49b1-aaab-3ffb6f5600cb<int:app_id>', views.elisteningmcq, name='elisteningmcq'),

    # elistening upload      
    path('elisteningtitleupload/4d7d5b77-a34f-419f-b4e7-3b1ff86f0c9c', views.elisteningtitleupload, name='elisteningtitleupload'),
    path('elisteningreaderupload/885c2de1-b437-41d4-9594-922ac3203c19', views.elisteningreaderupload, name='elisteningreaderupload'),
    path('elisteningmcqupload/86faf37f-84a7-4e6a-afed-a2926a4cf234', views.elisteningmcqupload, name='elisteningmcqupload'),

    # listening edit
    
    path('elisteningtview', views.elisteningtview, name='elisteningtview'),
    path('elisteningtitle/<int:id>', views.elisteningtitle, name='elisteningtitle'),
    path('elisteningtitledelet/<int:id>', views.elisteningtitledelet, name='elisteningtitledelet'),
    path('elisteningmcqedit/<int:id>', views.elisteningmcqedit, name='elisteningmcqedit'),
    path('elisteningmcqeditpart/<int:id>', views.elisteningmcqeditpart, name='elisteningmcqeditpart'),
    path('elisteningtecqdeletepart/<int:id>', views.elisteningtecqdeletepart, name='elisteningtecqdeletepart'),
    path('elisteningvideoview/<int:appvideoid>', views.elisteningvideoview, name='elisteningvideoview'),
    path('elisteningvideoedit/<int:id>', views.elisteningvideoedit, name='elisteningvideoedit'),
    path('elisteningvideodelete/<int:id>', views.elisteningvideodelete, name='elisteningvideodelete'),






# c++ language start

    # C++ start

    # c++ traning view
    path('cppreportpage', views.cppreportpage, name='cppreportpage'),


    path('cpptraningclick', views.cpptraningclick, name='cpptraningclick'),
    path('cpptraningchecktest', views.cpptraningchecktest, name='cpptraningchecktest'),
    path('cpptraningview', views.cpptraningview, name='cpptraningview'),
    path('cpptraningvideo/<int:id>', views.cpptraningvideo, name='cpptraningvideo'),
    path('cpptraningcompiler', views.cpptraningcompiler, name='cpptraningcompiler'),
    path('cpptraningmcq', views.cpptraningmcq, name='cpptraningmcq'),
    path('cpptraningtest', views.cpptraningtest, name='cpptraningtest'),
    # c++ traning upload
    path('cpptraningviewupload', views.cpptraningviewupload, name='cpptraningviewupload'),
    path('cpptraningvideoupload', views.cpptraningvideoupload, name='cpptraningvideoupload'),
    path('cpptraningmcqupload', views.cpptraningmcqupload, name='cpptraningmcqupload'),
    path('cpptraningtestupload', views.cpptraningtestupload, name='cpptraningtestupload'),

    # c++ traning edit
        # ---> view 
    path('cpptraningvieweditview', views.cpptraningvieweditview, name='cpptraningvieweditview'),
    path('cpptraningvideoeditview/<int:id>', views.cpptraningvideoeditview, name='cpptraningvideoeditview'),
    path('cpptraningmcqeditview/<int:id>', views.cpptraningmcqeditview, name='cpptraningmcqeditview'),
        # -->edit

    path('cpptraningviewedit/<int:id>', views.cpptraningviewedit, name='cpptraningviewedit'),
    path('cpptraningvideoedit/<int:id>', views.cpptraningvideoedit, name='cpptraningvideoedit'),
    path('cpptraningmcqedit/<int:id>', views.cpptraningmcqedit, name='cpptraningmcqedit'),
        # ---> delete
    path('cpptraningviewdelete/<int:id>', views.cpptraningviewdelete, name='cpptraningviewdelete'),
    path('cpptraningvideodelete/<int:id>', views.cpptraningvideodelete, name='cpptraningvideodelete'),
    path('cpptraningmcqdelete/<int:id>', views.cpptraningmcqdelete, name='cpptraningmcqdelete'),
    path('cpptraningtestdelete/<int:id>', views.cpptraningtestdelete, name='cpptraningtestdelete'),

    # end c++ traning 




    # practieces
    path('cpppracticeview', views.cpppracticeview, name='cpppracticeview'),
    path('cpppcompiler/<int:id>', views.cpppcompiler, name='cpppcompiler'),
    path('cpptitleupload', views.cpptitleupload, name='cpptitleupload'),
    path('cpppracticeupload', views.cpppracticeupload, name='cpppracticeupload'),

    # testcase
    path('cpptview', views.cpptview, name='cpptview'),

    path('cpptcompiler/<int:id>', views.cpptcompiler, name='cpptcompiler'),
    path('cppttitleupload', views.cppttitleupload, name='cppttitleupload'),
    path('cpptestud', views.cpptestud, name='cpptestud'),
    path('cpptchecktest', views.cpptchecktest, name='cpptchecktest'),
    path('javatchecktest', views.javatchecktest, name='javatchecktest'),
    # edit practices
    path('cpppracticeeditview', views.cpppracticeeditview, name='cpppracticeeditview'),
    path('cpppquestionview/<int:compiler_id>', views.cpppquestionview, name='cpppquestionview'),
    path('cpppquestionedit/<int:questionupdate>', views.cpppquestionedit, name='cpppquestionedit'),
    path('cpppdeletequestion/<int:questiondelete_id>', views.cpppdeletequestion, name='cpppdeletequestion'),
    path('cpppedittitle/<int:titleid>', views.cpppedittitle, name='cpppedittitle'),
    path('cpppdeletetitle/<int:titleid>', views.cpppdeletetitle, name='cpppdeletetitle'),

    # edit testcase
    path('cppptestcaseditview', views.cppptestcaseditview, name='cppptestcaseditview'),
    path('cppptquestionview/<int:id>', views.cppptquestionview, name='cppptquestionview'),
    # path('cppptquestionedit/<int:questionupdate>', views.cpppquestionedit, name='cpppquestionedit'),
    path('cppptdeletequestion/<int:questiondelete_id>', views.cppptdeletequestion, name='cppptdeletequestion'),
    path('cppptedittitle/<int:titleid>', views.cppptedittitle, name='cppptedittitle'),
    path('cppptdeletetitle/<int:titleid>', views.cppptdeletetitle, name='cppptdeletetitle'),

    






# Traning view

    path('cpptraning', views.cpptraning, name='cpptraning'),





# c end




# c language start
    # practieces
    path('creportpage', views.creportpage, name='creportpage'),
    path('ctraingmcqscore', views.ctraingmcqscore, name='ctraingmcqscore'),


    path('cpracticeview', views.cpracticeview, name='cpracticeview'),
    path('cpcompiler/<int:id>', views.cpcompiler, name='cpcompiler'),
    path('ctitleupload', views.ctitleupload, name='ctitleupload'),
    path('cpracticeupload', views.cpracticeupload, name='cpracticeupload'),

    # testcase
    path('ctview', views.ctview, name='ctview'),

    path('ctcompiler/<int:id>', views.ctcompiler, name='ctcompiler'),
    path('cttitleupload', views.cttitleupload, name='cttitleupload'),
    path('ctestud', views.ctestud, name='ctestud'),
    path('ctchecktest', views.ctchecktest, name='ctchecktest'),
      # edit practices
    path('cpracticeeditview', views.cpracticeeditview, name='cpracticeeditview'),
    path('cpquestionview/<int:compiler_id>', views.cpquestionview, name='cpquestionview'),
    path('cpquestionedit/<int:questionupdate>', views.cpquestionedit, name='cpquestionedit'),
    path('cpdeletequestion/<int:questiondelete_id>', views.cpdeletequestion, name='cpdeletequestion'),
    path('cpedittitle/<int:titleid>', views.cpedittitle, name='cpedittitle'),
    path('cpdeletetitle/<int:titleid>', views.cpdeletetitle, name='cpdeletetitle'),

    # edit testcase
    path('cptestcaseditview', views.cptestcaseditview, name='cptestcaseditview'),
    path('cptquestionview/<int:id>', views.cptquestionview, name='cptquestionview'),
    # path('cppptquestionedit/<int:questionupdate>', views.cpppquestionedit, name='cpppquestionedit'),
    path('cptdeletequestion/<int:questiondelete_id>', views.cptdeletequestion, name='cptdeletequestion'),
    path('cptedittitle/<int:titleid>', views.cptedittitle, name='cptedittitle'),
    path('cptdeletetitle/<int:titleid>', views.cptdeletetitle, name='cptdeletetitle'),

    # c traning view
    path('ctraningclick', views.ctraningclick, name='ctraningclick'),
    path('ctraningchecktest', views.ctraningchecktest, name='ctraningchecktest'),
    path('ctraningview/<str:session_id>', views.ctraningview, name='ctraningview'),
    path('ctraningvidedsdfo/<str:session_id>/<int:id>', views.ctraningvideo, name='ctraningvideo'),
    path('ctraningcompiler', views.ctraningcompiler, name='ctraningcompiler'),
    path('ctraningmcq', views.ctraningmcq, name='ctraningmcq'),
    path('ctraningtest', views.ctraningtest, name='ctraningtest'),
    # c traning upload
    path('ctraningviewupload', views.ctraningviewupload, name='ctraningviewupload'),
    path('ctraningvideoupload', views.ctraningvideoupload, name='ctraningvideoupload'),
    path('ctraningmcqupload', views.ctraningmcqupload, name='ctraningmcqupload'),
    path('ctraningtestupload', views.ctraningtestupload, name='ctraningtestupload'),

    # c traning edit
        # ---> view 
    path('ctraningvieweditview', views.ctraningvieweditview, name='ctraningvieweditview'),
    path('ctraningvideoeditview/<int:id>', views.ctraningvideoeditview, name='ctraningvideoeditview'),
    path('ctraningmcqeditview/<int:id>', views.ctraningmcqeditview, name='ctraningmcqeditview'),
        # -->edit

    path('ctraningviewedit/<int:id>', views.ctraningviewedit, name='ctraningviewedit'),
    path('ctraningvideoedit/<int:id>', views.ctraningvideoedit, name='ctraningvideoedit'),
    path('ctraningmcqedit/<int:id>', views.ctraningmcqedit, name='ctraningmcqedit'),
        # ---> delete
    path('ctraningviewdelete/<int:id>', views.ctraningviewdelete, name='ctraningviewdelete'),
    path('ctraningvideodelete/<int:id>', views.ctraningvideodelete, name='ctraningvideodelete'),
    path('ctraningmcqdelete/<int:id>', views.ctraningmcqdelete, name='ctraningmcqdelete'),
    path('ctraningtestdelete/<int:id>', views.ctraningtestdelete, name='ctraningtestdelete'),

    # end c traning 

    

    






# c end

# python start

    # c traning view
    path('preportpage', views.preportpage, name='preportpage'),

    path('ptraningclick', views.ptraningclick, name='ptraningclick'),
    path('ptraningchecktest', views.ptraningchecktest, name='ptraningchecktest'),
    path('ptraningview', views.ptraningview, name='ptraningview'),
    path('ptraningvideo/<int:id>', views.ptraningvideo, name='ptraningvideo'),
    path('ptraningcompiler', views.ptraningcompiler, name='ptraningcompiler'),
    path('ptraningmcq', views.ptraningmcq, name='ptraningmcq'),
    path('ptraningtest', views.ptraningtest, name='ptraningtest'),
    # c traning upload
    path('ptraningviewupload', views.ptraningviewupload, name='ptraningviewupload'),
    path('ptraningvideoupload', views.ptraningvideoupload, name='ptraningvideoupload'),
    path('ptraningmcqupload', views.ptraningmcqupload, name='ptraningmcqupload'),
    path('ptraningtestupload', views.ptraningtestupload, name='ptraningtestupload'),

    # c traning edit
        # ---> view 
    path('ptraningvieweditview', views.ptraningvieweditview, name='ptraningvieweditview'),
    path('ptraningvideoeditview/<int:id>', views.ptraningvideoeditview, name='ptraningvideoeditview'),
    path('ptraningmcqeditview/<int:id>', views.ptraningmcqeditview, name='ptraningmcqeditview'),
        # -->edit

    path('ptraningviewedit/<int:id>', views.ptraningviewedit, name='ptraningviewedit'),
    path('ptraningvideoedit/<int:id>', views.ptraningvideoedit, name='ptraningvideoedit'),
    path('ptraningmcqedit/<int:id>', views.ptraningmcqedit, name='ptraningmcqedit'),
        # ---> delete
    path('ptraningviewdelete/<int:id>', views.ptraningviewdelete, name='ptraningviewdelete'),
    path('ptraningvideodelete/<int:id>', views.ptraningvideodelete, name='ptraningvideodelete'),
    path('ptraningmcqdelete/<int:id>', views.ptraningmcqdelete, name='ptraningmcqdelete'),
    path('ptraningtestdelete/<int:id>', views.ptraningtestdelete, name='ptraningtestdelete'),

    # end c traning 






  # practieces
    path('ppracticeview', views.ppracticeview, name='ppracticeview'),
    path('ppcompiler/<int:id>', views.ppcompiler, name='ppcompiler'),
    path('ptitleupload', views.ptitleupload, name='ptitleupload'),
    path('ppracticeupload', views.ppracticeupload, name='ppracticeupload'),


    # testcase

    path('ptview', views.ptview, name='ptview'),

    path('ptcompiler/<int:id>', views.ptcompiler, name='ptcompiler'),
    path('pttitleupload', views.pttitleupload, name='pttitleupload'),
    path('ptestud', views.ptestud, name='ptestud'),
    path('ptchecktest', views.ptchecktest, name='ptchecktest'),


        # edit practices
    path('pythonpracticeeditview', views.pythonpracticeeditview, name='pythonpracticeeditview'),
    path('pythonpquestionview/<int:compiler_id>', views.pythonpquestionview, name='pythonpquestionview'),
    path('pythonpquestionedit/<int:questionupdate>', views.pythonpquestionedit, name='pythonpquestionedit'),
    path('pythonpdeletequestion/<int:questiondelete_id>', views.pythonpdeletequestion, name='pythonpdeletequestion'),
    path('pythonpedittitle/<int:titleid>', views.pythonpedittitle, name='pythonpedittitle'),
    path('pythonpdeletetitle/<int:titleid>', views.pythonpdeletetitle, name='pythonpdeletetitle'),

    # edit testcase
    path('pythonptestcaseditview', views.pythonptestcaseditview, name='pythonptestcaseditview'),
    path('pythonptquestionview/<int:id>', views.pythonptquestionview, name='pythonptquestionview'),
    # path('cppptquestionedit/<int:questionupdate>', views.cpppquestionedit, name='cpppquestionedit'),
    path('pythonptdeletequestion/<int:questiondelete_id>', views.pythonptdeletequestion, name='pythonptdeletequestion'),
    path('pythonptedittitle/<int:titleid>', views.pythonptedittitle, name='pythonptedittitle'),
    path('pythonptdeletetitle/<int:titleid>', views.pythonptdeletetitle, name='pythonptdeletetitle'),

# end python

    path('04ae79b6-087b-416c-b9f7-c46bae3d1c71/areport', views.areport, name='areport'),
























    path('employeeupload', views.employeeupload, name='employeeupload'),
    path('employeenext', views.employeenext, name='employeenext'),
     path('studentupload', views.studentupload, name='studentupload'),
    path('studentnext', views.studentnext, name='studentnext'),



    path('sidebar', views.sidebar, name='sidebar'),

    path('pythontest', views.pythontestcase, name='pythontest'),
    path('resumebuild/218ed12f-ef00-4dbe-80da-9b3eef9d399f', views.resumebuild, name='resumebuild'),
    path('rone/676dbe93-c22c-446c-a3f0-c144f6e0684f', views.rone, name='rone'),
    path('rtwo/bb2b1c72-22da-4a98-8baf-68e4907240e7', views.rtwo, name='rtwo'),
    path('rthree/a2e0b836-d586-4905-aa69-1db53aeb00ec', views.rthree, name='rthree'),
    path('rfour/90ba9e97-d4ae-4c93-bada-ff7ce0c5b905', views.rfour, name='rfour'),









    




]
