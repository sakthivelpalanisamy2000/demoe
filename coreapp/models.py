from django.db import models

# Create your models here.
# trial
from django.db import models
from django.contrib.auth.models import User

# demo

# class Demoskill(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)

#     name = models.CharField(max_length=50)

# class Demoperson(models.Model):
#     skills = models.ManyToManyField(Demoskill, blank=True, null=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        db_table = "TrialProcut"

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    class Meta:
        db_table = "TrialSubcription"


# end trial

class Programminglan(models.Model):
    language = models.CharField(max_length=200)

    def __str__(self):
        return self.language
    class Meta:
        db_table = "Programming_languages"




    
class Toutput(models.Model):
   
    toutputs = models.TextField()

    def __str__(self):
        return self.toutputs

class demooutput(models.Model):
   
    demooutputs = models.TextField()

    def __str__(self):
        return self.demooutputs

class Demoquestions(models.Model):
    questions = models.TextField()
   
    def __str__(self):
        return self.questions

    class Meta:
        db_table = "Demoquestions"





class Uploademployee(models.Model):
    topice = models.TextField()
    upload = models.TextField()
    class Meta:
        db_table = "Uploademployee"

class Aptitudeone(models.Model):
    topice = models.TextField()
    upload = models.TextField()
    class Meta:
        db_table = "Aptitudeone"

class Ctwo(models.Model):
    topice = models.TextField()
    upload = models.TextField()
    class Meta:
        db_table = "Ctwo"

class Javathree(models.Model):
    topice = models.TextField()
    upload = models.TextField()
    class Meta:
        db_table = "Javathree"
    
class Pythonfour(models.Model):
    topice = models.TextField()
    upload = models.TextField()
    class Meta:
        db_table = "Pythonfour"

class Cppfive(models.Model):
    topice = models.TextField()
    upload = models.TextField()
    class Meta:
        db_table = "Cppfive"
        
class Englishsix(models.Model):
    topice = models.TextField()
    upload = models.TextField()
    class Meta:
        db_table = "Englishsix"
        
class Intershipseven(models.Model):
    topice = models.TextField()
    upload = models.TextField()
    class Meta:
        db_table = "Intershipseven"
        
class Workshopeight(models.Model):
    topice = models.TextField()
    upload = models.TextField()
    class Meta:
        db_table = "Workshopeight"
        
class Pdnine(models.Model):
    topice = models.TextField()
    upload = models.TextField()
    class Meta:
        db_table = "Pdnine"
        
class Jobten(models.Model):
    topice = models.TextField()
    upload = models.TextField()
    class Meta:
        db_table = "Jobten"

class TenX(models.Model):
    programming = models.TextField()
    main = models.TextField()
    class Meta:
        db_table = "tenX"

class Userpermistionupload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aptitude = models.ForeignKey(Aptitudeone, on_delete=models.CASCADE,blank=True, null=True)
    c = models.ForeignKey(Ctwo, on_delete=models.CASCADE,blank=True, null=True)
    java = models.ForeignKey(Javathree, on_delete=models.CASCADE,blank=True, null=True)
    python = models.ForeignKey(Pythonfour, on_delete=models.CASCADE,blank=True, null=True)
    cpp = models.ForeignKey(Cppfive, on_delete=models.CASCADE,blank=True, null=True)
    english = models.ForeignKey(Englishsix, on_delete=models.CASCADE,blank=True, null=True)
    intership = models.ForeignKey(Intershipseven, on_delete=models.CASCADE,blank=True, null=True)
    workshop = models.ForeignKey(Workshopeight, on_delete=models.CASCADE,blank=True, null=True)
    pd = models.ForeignKey(Pdnine, on_delete=models.CASCADE,blank=True, null=True)
    job = models.ForeignKey(Jobten, on_delete=models.CASCADE,blank=True, null=True)
    tenx = models.ForeignKey(TenX, on_delete=models.CASCADE,blank=True, null=True)


    class Meta:
        db_table = "Userpermistionupload"

class Userpermistionuploademployee(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aptitude = models.BooleanField(default=False ,blank=True , null=True)
    c = models.BooleanField(default=False  ,blank=True , null=True)
    java = models.BooleanField(default=False  ,blank=True , null=True)
    python = models.BooleanField(default=False  ,blank=True , null=True)
    cpp = models.BooleanField(default=False  ,blank=True , null=True)
    english =models.BooleanField(default=False  ,blank=True , null=True)
    intership = models.BooleanField(default=False  ,blank=True , null=True)
    workshop = models.BooleanField(default=False  ,blank=True , null=True)
    pd = models.BooleanField(default=False  ,blank=True , null=True)
    job = models.BooleanField(default=False  ,blank=True , null=True)

    class Meta:
        db_table = "Userpermistionuploademployee"







class Employement(models.Model):
    jobtitle = models.TextField(null=True, blank=True)
    employer = models.TextField(null=True, blank=True)
    startdate = models.TextField(null=True, blank=True)
    enddate = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    description=models.TextField(null=True, blank=True)
   
    def __str__(self):
        return self.jobtitle
class Educations(models.Model):
    school = models.TextField(null=True, blank=True)
    degree = models.TextField(null=True, blank=True)
    startdate = models.TextField(null=True, blank=True)
    enddate = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
   
    def __str__(self):
        return self.school
    
class SocialLink(models.Model):
    lable = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
   
   
    def __str__(self):
        return self.lable
class Skill(models.Model):
    skill = models.TextField(null=True, blank=True)
    level = models.TextField(null=True, blank=True)
   
   
    def __str__(self):
        return self.skill
class Courses(models.Model):
    courses = models.TextField(null=True, blank=True)
    institution = models.TextField(null=True, blank=True)
    startdate = models.TextField(null=True, blank=True)
    enddate = models.TextField(null=True, blank=True)
   
   
    def __str__(self):
        return self.courses
class Interships(models.Model):
    jobtitle = models.TextField(null=True, blank=True)
    employer = models.TextField(null=True, blank=True)
    startdate = models.TextField(null=True, blank=True)
    enddate = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    description=models.TextField(null=True, blank=True)
   
   
    def __str__(self):
        return self.jobtitle

class ExtraCurricular(models.Model):
    functiontype = models.TextField(null=True, blank=True)
    employer = models.TextField(null=True, blank=True)
    startdate = models.TextField(null=True, blank=True)
    enddate = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    description=models.TextField(null=True, blank=True)
   
   
    def __str__(self):
        return self.functiontype
class Reference(models.Model):
    name = models.TextField(null=True, blank=True)
    company = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    
   
   
    def __str__(self):
        return self.name
    
class Hobbies(models.Model):
    hobbielist = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.hobbielist
    
# template
class TemplatedesignImage(models.Model):
    image=models.ImageField(upload_to='images/')
    link=models.TextField(null=True, blank=True)

class Userclick(models.Model):
    userclickid = models.IntegerField(null=True, blank=True)

class Templatedesign(models.Model):
    template = models.TextField(null=True, blank=True)

    image = models.ForeignKey(TemplatedesignImage, on_delete=models.CASCADE ,null=True, blank=True)

    def __str__(self):
        return self.template
    




# testcase
class Practicelevels(models.Model):
    title = models.CharField(max_length=1000 , null=True, blank=True )

   
    def __str__(self):
        return self.title

class Practicetitle(models.Model):
    title = models.CharField(max_length=1000 , null=True, blank=True )

   
    def __str__(self):
        return self.title


# c language start
    
    # c traning
class Ctraingclick(models.Model):

    click = models.CharField(max_length=1000 , null=True, blank=True )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Cuserclick"

class Ctraingtitle(models.Model):

    title = models.CharField(max_length=1000 , null=True, blank=True )
    selecttype = models.CharField(max_length=100 , null=True, blank=True )
    mcqscore = models.CharField(max_length=100 , null=True, blank=True )
    mcqtotal = models.CharField(max_length=100 , null=True, blank=True )
    test = models.CharField(max_length=100 , null=True, blank=True )
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True, blank=True )

    def __str__(self):
        return self.title
class Ctraningreport(models.Model):

    titleid=models.ForeignKey(Ctraingtitle, on_delete=models.CASCADE ,null=True, blank=True )
    status = models.CharField(max_length=100 , null=True, blank=True )
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True, blank=True )

    class Meta:
        db_table = "ctraningreport"

    
class Cuploadvideosections(models.Model):
    titleone = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    content = models.TextField(null=True, blank=True)
    title = models.ForeignKey(Ctraingtitle, on_delete=models.CASCADE ,null=True, blank=True)
    def __str__(self):
        return self.titleone
    
class Cquiz(models.Model):
	question = models.CharField(max_length = 1000, null=True, blank=True )
	option1 = models.CharField(max_length = 1000, null=True, blank=True )
	option2 = models.CharField(max_length = 1000, null=True, blank=True )
	option3 = models.CharField(max_length = 1000, null=True, blank=True )
	option4 = models.CharField(max_length = 1000, null=True, blank=True )
	answer = models.CharField(max_length = 1000, null=True, blank=True )
	answer1 = models.CharField(max_length = 100, null=True, blank=True )
	answer2 = models.CharField(max_length = 100, null=True, blank=True )
	answer3 = models.CharField(max_length = 100, null=True, blank=True )
	answer4 = models.CharField(max_length = 100, null=True, blank=True )
	title = models.ForeignKey(Ctraingtitle, on_delete=models.CASCADE ,null=True, blank=True)
	def __str__(self):
            return self.question
    
class Ctraningcodeingquestions(models.Model):
    questions = models.TextField()
    sinput = models.TextField()
    soutput = models.TextField()
    tinput = models.TextField()
    toutput = models.TextField()
    samplecode=models.TextField(null=True, blank=True)
    title = models.ForeignKey(Ctraingtitle, on_delete=models.CASCADE ,null=True, blank=True)
    def __str__(self):
        return self.questions



   
class Ctitlepractices(models.Model):
    title = models.CharField(max_length=1000 , null=True, blank=True )
    level = models.CharField(max_length=30 , null=True, blank=True )
    def __str__(self):
        return self.title 
    
class Cquestionpractices(models.Model):
    content = models.TextField(null=True, blank=True)
    title = models.ForeignKey(Ctitlepractices, on_delete=models.CASCADE ,null=True, blank=True)

class Ctitletestcase(models.Model):
    title = models.CharField(max_length=1000 , null=True, blank=True )
    level = models.CharField(max_length=30 , null=True, blank=True )
    def __str__(self):
        return self.title 
class CtechnicalQuestionsTestcase(models.Model):
    questions = models.TextField()
    sinput = models.TextField()
    soutput = models.TextField()
    tinput = models.TextField()
    toutput = models.TextField()
    samplecode=models.TextField(null=True, blank=True)
    title = models.ForeignKey(Ctitletestcase, on_delete=models.CASCADE ,null=True, blank=True)
    def __str__(self):
        return self.questions
    
class Ctestcasereport(models.Model):
    success=models.CharField(max_length=1000 , null=True, blank=True )
    failed=models.CharField(max_length=1000 , null=True, blank=True )
    title = models.ForeignKey(Ctitletestcase, on_delete=models.CASCADE ,null=True, blank=True)
    testcase = models.ForeignKey(CtechnicalQuestionsTestcase, on_delete=models.CASCADE ,null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True, blank=True)



    

# c language end
    

# python start
    
class Pythontraingclick(models.Model):

    click = models.CharField(max_length=1000 , null=True, blank=True )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Python_userclick"

class Pythontraingtitle(models.Model):

    title = models.CharField(max_length=1000 , null=True, blank=True )
    selecttype = models.CharField(max_length=100 , null=True, blank=True )
    def __str__(self):
        return self.title
    
class Pythonuploadvideosections(models.Model):
    titleone = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    content = models.TextField(null=True, blank=True)
    title = models.ForeignKey(Pythontraingtitle, on_delete=models.CASCADE ,null=True, blank=True)
    def __str__(self):
        return self.titleone
    
class Pythonquiz(models.Model):
	question = models.CharField(max_length = 1000, null=True, blank=True )
	option1 = models.CharField(max_length = 1000, null=True, blank=True )
	option2 = models.CharField(max_length = 1000, null=True, blank=True )
	option3 = models.CharField(max_length = 1000, null=True, blank=True )
	option4 = models.CharField(max_length = 1000, null=True, blank=True )
	answer = models.CharField(max_length = 1000, null=True, blank=True )
	answer1 = models.CharField(max_length = 100, null=True, blank=True )
	answer2 = models.CharField(max_length = 100, null=True, blank=True )
	answer3 = models.CharField(max_length = 100, null=True, blank=True )
	answer4 = models.CharField(max_length = 100, null=True, blank=True )
	title = models.ForeignKey(Pythontraingtitle, on_delete=models.CASCADE ,null=True, blank=True)
	def __str__(self):
            return self.question
    
class Pythontraningcodeingquestions(models.Model):
    questions = models.TextField()
    sinput = models.TextField()
    soutput = models.TextField()
    tinput = models.TextField()
    toutput = models.TextField()
    samplecode=models.TextField(null=True, blank=True)
    title = models.ForeignKey(Pythontraingtitle, on_delete=models.CASCADE ,null=True, blank=True)
    def __str__(self):
        return self.questions
    


class Ptitlepractices(models.Model):
    title = models.CharField(max_length=1000 , null=True, blank=True )
    level = models.CharField(max_length=30 , null=True, blank=True )
    def __str__(self):
        return self.title 
    
class Pquestionpractices(models.Model):
    content = models.TextField(null=True, blank=True)
    title = models.ForeignKey(Ptitlepractices, on_delete=models.CASCADE ,null=True, blank=True)

class Ptitletestcase(models.Model):
    title = models.CharField(max_length=1000 , null=True, blank=True )
    level = models.CharField(max_length=30 , null=True, blank=True )
    def __str__(self):
        return self.title 
class PtechnicalQuestionsTestcase(models.Model):
    questions = models.TextField()
    sinput = models.TextField()
    soutput = models.TextField()
    tinput = models.TextField()
    toutput = models.TextField()
    samplecode=models.TextField(null=True, blank=True)
    title = models.ForeignKey(Ptitletestcase, on_delete=models.CASCADE ,null=True, blank=True)



    def __str__(self):
        return self.questions
    
class Ptestcasereport(models.Model):
    success=models.CharField(max_length=1000 , null=True, blank=True )
    failed=models.CharField(max_length=1000 , null=True, blank=True )
    title = models.ForeignKey(Ptitletestcase, on_delete=models.CASCADE ,null=True, blank=True)
    testcase = models.ForeignKey(PtechnicalQuestionsTestcase, on_delete=models.CASCADE ,null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True, blank=True)

# python end


# cpp start
    # cpp traning
class Cpptraingclick(models.Model):

    click = models.CharField(max_length=1000 , null=True, blank=True )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "cpp_userclick"
        
class Cpptraingtitle(models.Model):

    title = models.CharField(max_length=1000 , null=True, blank=True )
    selecttype = models.CharField(max_length=100 , null=True, blank=True )
    def __str__(self):
        return self.title
    
class Cppuploadvideosections(models.Model):
    titleone = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    content = models.TextField(null=True, blank=True)
    title = models.ForeignKey(Cpptraingtitle, on_delete=models.CASCADE ,null=True, blank=True)
    def __str__(self):
        return self.titleone
    
class Cppquiz(models.Model):
	question = models.CharField(max_length = 1000, null=True, blank=True )
	option1 = models.CharField(max_length = 1000, null=True, blank=True )
	option2 = models.CharField(max_length = 1000, null=True, blank=True )
	option3 = models.CharField(max_length = 1000, null=True, blank=True )
	option4 = models.CharField(max_length = 1000, null=True, blank=True )
	answer = models.CharField(max_length = 1000, null=True, blank=True )
	answer1 = models.CharField(max_length = 100, null=True, blank=True )
	answer2 = models.CharField(max_length = 100, null=True, blank=True )
	answer3 = models.CharField(max_length = 100, null=True, blank=True )
	answer4 = models.CharField(max_length = 100, null=True, blank=True )
	title = models.ForeignKey(Cpptraingtitle, on_delete=models.CASCADE ,null=True, blank=True)
	def __str__(self):
            return self.question
    
class Cpptraningcodeingquestions(models.Model):
    questions = models.TextField()
    sinput = models.TextField()
    soutput = models.TextField()
    tinput = models.TextField()
    toutput = models.TextField()
    samplecode=models.TextField(null=True, blank=True)
    title = models.ForeignKey(Cpptraingtitle, on_delete=models.CASCADE ,null=True, blank=True)
    def __str__(self):
        return self.questions




class Cpponetitlepractices(models.Model):
    title = models.CharField(max_length=1000 , null=True, blank=True )
    level = models.CharField(max_length=30 , null=True, blank=True )
    def __str__(self):
        return self.title 
    
class Cpponepquestionpractices(models.Model):
    content = models.TextField(null=True, blank=True)
    title = models.ForeignKey(Ptitlepractices, on_delete=models.CASCADE ,null=True, blank=True)

class Cpponetitletestcase(models.Model):
    title = models.CharField(max_length=1000 , null=True, blank=True )
    level = models.CharField(max_length=30 , null=True, blank=True )
    def __str__(self):
        return self.title 
class CpponetechnicalQuestionsTestcase(models.Model):
    questions = models.TextField()
    sinput = models.TextField()
    soutput = models.TextField()
    tinput = models.TextField()
    toutput = models.TextField()
    samplecode=models.TextField(null=True, blank=True)
    title = models.ForeignKey(Cpponetitletestcase, on_delete=models.CASCADE ,null=True, blank=True)



    def __str__(self):
        return self.questions
    
class Cpptestcasereport(models.Model):
    success=models.CharField(max_length=1000 , null=True, blank=True )
    failed=models.CharField(max_length=1000 , null=True, blank=True )
    title = models.ForeignKey(Cpponetitletestcase, on_delete=models.CASCADE ,null=True, blank=True)
    testcase = models.ForeignKey(CpponetechnicalQuestionsTestcase, on_delete=models.CASCADE ,null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True, blank=True)
# python end
# cpp end


      
class Titlepractices(models.Model):
    title = models.CharField(max_length=1000 , null=True, blank=True )
    level = models.CharField(max_length=30 , null=True, blank=True )


   
    def __str__(self):
        return self.title


    
class Questionpractices(models.Model):
    level = models.CharField(max_length=100 , null=True, blank=True )
    content = models.TextField(null=True, blank=True)
    title = models.ForeignKey(Titlepractices, on_delete=models.CASCADE ,null=True, blank=True)


    
    def __str__(self):
        return self.content


class Titletestcase(models.Model):

    title = models.CharField(max_length=1000 , null=True, blank=True )
    level = models.CharField(max_length=30 , null=True, blank=True )


   
    def __str__(self):
        return self.title
class Javatraingtitle(models.Model):

    title = models.CharField(max_length=1000 , null=True, blank=True )
    selecttype = models.CharField(max_length=100 , null=True, blank=True )


    def __str__(self):
        return self.title
    
class Titleclick(models.Model):
    title = models.CharField(max_length=1000 , null=True, blank=True )

    cliknum=models.CharField(max_length=1000 , null=True, blank=True )
    def __str__(self):
        return self.title
   
class Mcqjavatraning(models.Model):

    questions = models.TextField(null=True, blank=True)
    optiona = models.TextField(null=True, blank=True)
    optionb = models.TextField(null=True, blank=True)
    optionc = models.TextField(null=True, blank=True)
    optiond = models.TextField(null=True, blank=True)
    correctans = models.TextField(null=True, blank=True)
    title = models.ForeignKey(Titlepractices, on_delete=models.CASCADE ,null=True, blank=True)

    def __str__(self):
        return self.questions


class Demovideo(models.Model):
    titl = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    content = models.TextField(null=True, blank=True)
   

    def __str__(self):
        return self.title
class Uploadvideosections(models.Model):
    titleone = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    content = models.TextField(null=True, blank=True)
    title = models.ForeignKey(Javatraingtitle, on_delete=models.CASCADE ,null=True, blank=True)

    
    def __str__(self):
        return self.titleone
    
class Videosection(models.Model):

    url = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    title = models.ForeignKey(Titlepractices, on_delete=models.CASCADE ,null=True, blank=True)

    def __str__(self):
        return self.url
class Javatraingmcq(models.Model):

    questions = models.TextField(null=True, blank=True)
    optiona = models.TextField(null=True, blank=True)
    optionb = models.TextField(null=True, blank=True)
    optionc = models.TextField(null=True, blank=True)
    optiond = models.TextField(null=True, blank=True)
    correctans = models.TextField(null=True, blank=True)
    title = models.ForeignKey(Javatraingtitle, on_delete=models.CASCADE ,null=True, blank=True)
    def __str__(self):
        return self.questions
    
class TechnicalQuestionsTestcase(models.Model):
    questions = models.TextField()
    sinput = models.TextField()
    soutput = models.TextField()
    tinput = models.TextField()
    toutput = models.TextField()
    samplecode=models.TextField(null=True, blank=True)
    title = models.ForeignKey(Titletestcase, on_delete=models.CASCADE ,null=True, blank=True)
    def __str__(self):
        return self.questions
    

class Javatestcasereport(models.Model):
    success=models.CharField(max_length=1000 , null=True, blank=True )
    failed=models.CharField(max_length=1000 , null=True, blank=True )
    title = models.ForeignKey(Titletestcase, on_delete=models.CASCADE ,null=True, blank=True)
    testcase = models.ForeignKey(TechnicalQuestionsTestcase, on_delete=models.CASCADE ,null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True, blank=True)
    
class Traningcodeingquestions(models.Model):
    questions = models.TextField()
    sinput = models.TextField()
    soutput = models.TextField()
    tinput = models.TextField()
    toutput = models.TextField()
    samplecode=models.TextField(null=True, blank=True)
    title = models.ForeignKey(Javatraingtitle, on_delete=models.CASCADE ,null=True, blank=True)
    def __str__(self):
        return self.questions
    
class Traningupdateid(models.Model):
    updateid = models.CharField(max_length=1000 , null=True, blank=True )
    
    def __str__(self):
        return self.updateid

# resume

class Personaldetails(models.Model):
    jobtitle = models.TextField(null=True, blank=True)
    photo = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    lastname = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    phone=models.TextField(null=True, blank=True)
    country=models.TextField(null=True, blank=True)
    city=models.TextField(null=True, blank=True)
    address=models.TextField(null=True, blank=True)
    postcode=models.TextField(null=True, blank=True)
    nationality=models.TextField(null=True, blank=True)
    placeofbirth=models.TextField(null=True, blank=True)
    dateofbirth=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Profilesummary(models.Model):
    summary = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.summary
    
class Educationsresume(models.Model):

    ugname= models.CharField(max_length=200 ,null=True, blank=True)
    uglocations= models.CharField(max_length=200 , null=True, blank=True)
    ugstartdate=models.DateField(null=True, blank=True)
    ugenddate=models.DateField(null=True, blank=True)
    ugdegree= models.CharField(max_length=300 ,null=True, blank=True)
    ugfieldstudy= models.CharField(max_length=300 , null=True, blank=True)
    ugdegree= models.CharField(max_length=300 , null=True, blank=True)
    ugdescriptions=models.TextField(null=True, blank=True)
    # 
    xiiname= models.CharField(max_length=200 ,null=True, blank=True)
    xiilocations= models.CharField(max_length=200 , null=True, blank=True)
    xiistartdate=models.DateField(null=True, blank=True)
    xiienddate=models.DateField(null=True, blank=True)
    xiidegree= models.CharField(max_length=300 ,null=True, blank=True)
    xiifieldstudy= models.CharField(max_length=300 , null=True, blank=True)
    xiidegree= models.CharField(max_length=300 , null=True, blank=True)
    xiidescriptions=models.TextField(null=True, blank=True)
    # 
    xname= models.CharField(max_length=200 ,null=True, blank=True)
    xlocations= models.CharField(max_length=200 , null=True, blank=True)
    xstartdate=models.DateField(null=True, blank=True)
    xenddate=models.DateField(null=True, blank=True)
    xdegree= models.CharField(max_length=300 ,null=True, blank=True)
    xfieldstudy= models.CharField(max_length=300 , null=True, blank=True)
    xdegree= models.CharField(max_length=300 , null=True, blank=True)
    xdescriptions=models.TextField(null=True, blank=True)


    def __str__(self):
        return self.ugname
    
class Projectresume(models.Model):

    title = models.CharField(max_length=500 ,null=True, blank=True)
    
    descriptions=models.TextField(null=True, blank=True)
  
    def __str__(self):
        return self.title

# delete
class Quiz(models.Model):
	question = models.CharField(max_length = 1000, null=True, blank=True )
	option1 = models.CharField(max_length = 1000, null=True, blank=True )
	option2 = models.CharField(max_length = 1000, null=True, blank=True )
	option3 = models.CharField(max_length = 1000, null=True, blank=True )
	option4 = models.CharField(max_length = 1000, null=True, blank=True )
	answer = models.CharField(max_length = 1000, null=True, blank=True )
	answer1 = models.CharField(max_length = 100, null=True, blank=True )
	answer2 = models.CharField(max_length = 100, null=True, blank=True )
	answer3 = models.CharField(max_length = 100, null=True, blank=True )
	answer4 = models.CharField(max_length = 100, null=True, blank=True )
	title = models.ForeignKey(Javatraingtitle, on_delete=models.CASCADE ,null=True, blank=True)

	def __str__(self):
            return self.question
# aptitude

class Aptitudetitle(models.Model):

    title = models.CharField(max_length=1000 , null=True, blank=True )

    def __str__(self):
        return self.title

class Aptitudevideosections(models.Model):
    titleone = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='aptitudes/')
    content = models.TextField(null=True, blank=True)
    title = models.ForeignKey(Aptitudetitle, on_delete=models.CASCADE ,null=True, blank=True)

    
    def __str__(self):
        return self.titleone 

class Aptitudequiz(models.Model):
	question = models.CharField(max_length = 1000, null=True, blank=True )
	option1 = models.CharField(max_length = 1000, null=True, blank=True )
	option2 = models.CharField(max_length = 1000, null=True, blank=True )
	option3 = models.CharField(max_length = 1000, null=True, blank=True )
	option4 = models.CharField(max_length = 1000, null=True, blank=True )
	answer = models.CharField(max_length = 1000, null=True, blank=True )
	answer1 = models.CharField(max_length = 100, null=True, blank=True )
	answer2 = models.CharField(max_length = 100, null=True, blank=True )
	answer3 = models.CharField(max_length = 100, null=True, blank=True )
	answer4 = models.CharField(max_length = 100, null=True, blank=True )
	title = models.ForeignKey(Aptitudetitle, on_delete=models.CASCADE ,null=True, blank=True)

	def __str__(self):
            return self.question

    # aptitude practies
class Apptitle(models.Model):

    title = models.CharField(max_length=1000 , null=True, blank=True )

    def __str__(self):
        return self.title
    
class Appquiz(models.Model):
	question = models.CharField(max_length = 1000, null=True, blank=True )
	option1 = models.CharField(max_length = 1000, null=True, blank=True )
	option2 = models.CharField(max_length = 1000, null=True, blank=True )
	option3 = models.CharField(max_length = 1000, null=True, blank=True )
	option4 = models.CharField(max_length = 1000, null=True, blank=True )
	answer = models.CharField(max_length = 1000, null=True, blank=True )
	answer1 = models.CharField(max_length = 100, null=True, blank=True )
	answer2 = models.CharField(max_length = 100, null=True, blank=True )
	answer3 = models.CharField(max_length = 100, null=True, blank=True )
	answer4 = models.CharField(max_length = 100, null=True, blank=True )
	title = models.ForeignKey(Apptitle, on_delete=models.CASCADE ,null=True, blank=True)

	def __str__(self):
            return self.question





# pd start
    

class Pdtitle(models.Model):

    title = models.CharField(max_length=1000 , null=True, blank=True )

    def __str__(self):
        return self.title

class Pdvideosections(models.Model):
    titleone = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='pd/')
    content = models.TextField(null=True, blank=True)
    title = models.ForeignKey(Pdtitle, on_delete=models.CASCADE ,null=True, blank=True)

    
    def __str__(self):
        return self.titleone 



#delete end



# workshop start
    
class Workshoptitle(models.Model):

    title = models.CharField(max_length=1000 , null=True, blank=True )
    content = models.TextField(null=True, blank=True )
    image = models.ImageField(upload_to='imageworkshop/',null=True)


    def __str__(self):
        return self.title

class Workshopvideosections(models.Model):
    titleone = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='workshops/')
    content = models.TextField(null=True, blank=True)
    title = models.ForeignKey(Workshoptitle, on_delete=models.CASCADE ,null=True, blank=True)

    
    def __str__(self):
        return self.titleone 

class Workshopquiz(models.Model):
	question = models.CharField(max_length = 1000, null=True, blank=True )
	option1 = models.CharField(max_length = 1000, null=True, blank=True )
	option2 = models.CharField(max_length = 1000, null=True, blank=True )
	option3 = models.CharField(max_length = 1000, null=True, blank=True )
	option4 = models.CharField(max_length = 1000, null=True, blank=True )
	answer = models.CharField(max_length = 1000, null=True, blank=True )
	answer1 = models.CharField(max_length = 100, null=True, blank=True )
	answer2 = models.CharField(max_length = 100, null=True, blank=True )
	answer3 = models.CharField(max_length = 100, null=True, blank=True )
	answer4 = models.CharField(max_length = 100, null=True, blank=True )
	title = models.ForeignKey(Workshoptitle, on_delete=models.CASCADE ,null=True, blank=True)

	def __str__(self):
            return self.question
    


    # intership

        
class Intershiptitle(models.Model):

    title = models.CharField(max_length=1000 , null=True, blank=True )
    timer = models.CharField(max_length=1000 , null=True, blank=True )
    part = models.CharField(max_length=1000 , null=True, blank=True )
    code = models.CharField(max_length=1000 , null=True, blank=True )

    content = models.TextField(null=True, blank=True )
    image = models.ImageField(upload_to='Interships/',null=True)


    def __str__(self):
        return self.title

class Intershipvideosections(models.Model):
    titleone = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='Interships/')
    content = models.TextField(null=True, blank=True)
    title = models.ForeignKey(Intershiptitle, on_delete=models.CASCADE ,null=True, blank=True)

    
    def __str__(self):
        return self.titleone 

class Intershipquiz(models.Model):
	question = models.CharField(max_length = 1000, null=True, blank=True )
	option1 = models.CharField(max_length = 1000, null=True, blank=True )
	option2 = models.CharField(max_length = 1000, null=True, blank=True )
	option3 = models.CharField(max_length = 1000, null=True, blank=True )
	option4 = models.CharField(max_length = 1000, null=True, blank=True )
	answer = models.CharField(max_length = 1000, null=True, blank=True )
	answer1 = models.CharField(max_length = 100, null=True, blank=True )
	answer2 = models.CharField(max_length = 100, null=True, blank=True )
	answer3 = models.CharField(max_length = 100, null=True, blank=True )
	answer4 = models.CharField(max_length = 100, null=True, blank=True )
	title = models.ForeignKey(Intershiptitle, on_delete=models.CASCADE ,null=True, blank=True)

	def __str__(self):
            return self.question
    




    # technical

class Etechnicaltitle(models.Model):

    title = models.CharField(max_length=1000 , null=True, blank=True )
    subtitle = models.CharField(max_length=1000 , null=True, blank=True )
    
    def __str__(self):
        return self.title

class Etechnicalvideosections(models.Model):
    titleone = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='Etechnicals/')
    content = models.TextField(null=True, blank=True)
    title = models.ForeignKey(Etechnicaltitle, on_delete=models.CASCADE ,null=True, blank=True)
 
    def __str__(self):
        return self.titleone 

class Etechnicalquiz(models.Model):
	question = models.CharField(max_length = 1000, null=True, blank=True )
	option1 = models.CharField(max_length = 1000, null=True, blank=True )
	option2 = models.CharField(max_length = 1000, null=True, blank=True )
	option3 = models.CharField(max_length = 1000, null=True, blank=True )
	option4 = models.CharField(max_length = 1000, null=True, blank=True )
	answer = models.CharField(max_length = 1000, null=True, blank=True )
	answer1 = models.CharField(max_length = 100, null=True, blank=True )
	answer2 = models.CharField(max_length = 100, null=True, blank=True )
	answer3 = models.CharField(max_length = 100, null=True, blank=True )
	answer4 = models.CharField(max_length = 100, null=True, blank=True )
	title = models.ForeignKey(Etechnicaltitle, on_delete=models.CASCADE ,null=True, blank=True)

	def __str__(self):
            return self.question
    

# bussniss english
    

class Ebusinesstitle(models.Model):

    title = models.CharField(max_length=1000 , null=True, blank=True )
    subtitle = models.CharField(max_length=1000 , null=True, blank=True )
    
    def __str__(self):
        return self.title

class Ebusinessvideosections(models.Model):
    titleone = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='Ebusinesss/')
    content = models.TextField(null=True, blank=True)
    title = models.ForeignKey(Ebusinesstitle, on_delete=models.CASCADE ,null=True, blank=True)
 
    def __str__(self):
        return self.titleone 

class Ebusinessquiz(models.Model):
	question = models.CharField(max_length = 1000, null=True, blank=True )
	option1 = models.CharField(max_length = 1000, null=True, blank=True )
	option2 = models.CharField(max_length = 1000, null=True, blank=True )
	option3 = models.CharField(max_length = 1000, null=True, blank=True )
	option4 = models.CharField(max_length = 1000, null=True, blank=True )
	answer = models.CharField(max_length = 1000, null=True, blank=True )
	answer1 = models.CharField(max_length = 100, null=True, blank=True )
	answer2 = models.CharField(max_length = 100, null=True, blank=True )
	answer3 = models.CharField(max_length = 100, null=True, blank=True )
	answer4 = models.CharField(max_length = 100, null=True, blank=True )
	title = models.ForeignKey(Ebusinesstitle, on_delete=models.CASCADE ,null=True, blank=True)

	def __str__(self):
            return self.question


# spoken english
    

class Espokentitle(models.Model):

    title = models.CharField(max_length=1000 , null=True, blank=True )
    subtitle = models.CharField(max_length=1000 , null=True, blank=True )
    
    def __str__(self):
        return self.title

class Espokenvideosections(models.Model):
    titleone = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='Espokens/')
    content = models.TextField(null=True, blank=True)
    title = models.ForeignKey(Espokentitle, on_delete=models.CASCADE ,null=True, blank=True)
 
    def __str__(self):
        return self.titleone 

class Espokenquiz(models.Model):
	question = models.CharField(max_length = 1000, null=True, blank=True )
	option1 = models.CharField(max_length = 1000, null=True, blank=True )
	option2 = models.CharField(max_length = 1000, null=True, blank=True )
	option3 = models.CharField(max_length = 1000, null=True, blank=True )
	option4 = models.CharField(max_length = 1000, null=True, blank=True )
	answer = models.CharField(max_length = 1000, null=True, blank=True )
	answer1 = models.CharField(max_length = 100, null=True, blank=True )
	answer2 = models.CharField(max_length = 100, null=True, blank=True )
	answer3 = models.CharField(max_length = 100, null=True, blank=True )
	answer4 = models.CharField(max_length = 100, null=True, blank=True )
	title = models.ForeignKey(Espokentitle, on_delete=models.CASCADE ,null=True, blank=True)

	def __str__(self):
            return self.question
    
# listening

class Elisteningtitle(models.Model):
    titleone = models.CharField(max_length=100)

    title = models.CharField(max_length=1000 , null=True, blank=True )
    subtitle = models.CharField(max_length=1000 , null=True, blank=True )
    
    # def __str__(self):
    #     return self.titleone

class Elisteningreader(models.Model):
    
    content = models.TextField(null=True, blank=True)
    title = models.ForeignKey(Elisteningtitle, on_delete=models.CASCADE ,null=True, blank=True)
 
    def __str__(self):
        return self.content 

class Elisteningquiz(models.Model):
	question = models.CharField(max_length = 1000, null=True, blank=True )
	option1 = models.CharField(max_length = 1000, null=True, blank=True )
	option2 = models.CharField(max_length = 1000, null=True, blank=True )
	option3 = models.CharField(max_length = 1000, null=True, blank=True )
	option4 = models.CharField(max_length = 1000, null=True, blank=True )
	answer = models.CharField(max_length = 1000, null=True, blank=True )
	answer1 = models.CharField(max_length = 100, null=True, blank=True )
	answer2 = models.CharField(max_length = 100, null=True, blank=True )
	answer3 = models.CharField(max_length = 100, null=True, blank=True )
	answer4 = models.CharField(max_length = 100, null=True, blank=True )
	title = models.ForeignKey(Elisteningtitle, on_delete=models.CASCADE ,null=True, blank=True)

	def __str__(self):
            return self.question