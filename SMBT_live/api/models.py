from mongoengine import Document,StringField,IntField,FileField,DateField,EmailField,DateTimeField,FloatField,SequenceField,BinaryField
import datetime
from starlette.responses import JSONResponse
from datetime import datetime
def validate_name(value):
    if not value.isalpha():
     a={"Error":"True","Message":"please enter vailed sno"}
     return JSONResponse(content=a, status_code=400)
def validate_mobile(value):
    if not value.isdigit() or len(value) != 10:
        a={"Error":"True","Message":"Mobile number must be 10 digits"}
        return JSONResponse(content=a, status_code=400)
class Usercreate(Document):
    UserID=IntField(unique=True)
    Employee_id=IntField(unique=True)
    password=StringField()
    User_name=StringField(max_length=20)
    mobile_number=IntField()
    Desigination=StringField()
    Email_id=EmailField()
    Branch=StringField()
    Created_on=DateTimeField()
    Created_by=StringField()
    Modified_by=StringField()
    Modified_On=DateField()
    Source=StringField()
    Location=StringField()
    Location_address=StringField()
    Country=StringField()
    Country_code=StringField()
    State=StringField()
    State_code=StringField()
    City=StringField()
    Pincode=IntField()
    Allowance_Per_Day=IntField()
    Multi_Branch_Access=StringField()
    Active_Status=StringField()
    Department=StringField()
    Reporting_Manager=StringField()
    Bank_Account_No=IntField()
    Bank_Name=StringField()
    IFSC_Code=StringField()
    PAN_Number=StringField()
    ID_Proof_No=StringField()
    Role_Code=StringField()
class Rolemaster(Document):
    sno=IntField(unique=True)
    Role=StringField()
class Add_depart(Document):
    sno=IntField(unique=True)
    department_name=StringField()
class Add_Designation(Document):
    sno=IntField(unique=True)
    Designation_name=StringField()
class uploa(Document):
    name=StringField()
    bank=FileField()
class country_state(Document):
    _id =StringField()
    id=StringField()
    state_name=StringField()
    country_code=StringField()
    country_status=StringField()
    country_name=StringField()
    state_code=StringField()
    state_status=StringField()
class country_state2(Document):
    sno=IntField()
    StateName=StringField()
    Capital=StringField()
    TotalDistricts=StringField()
    status=StringField()
    Statecode=StringField()
class country_state3(Document):
    sno=IntField()
    Capital=StringField()
    Capital_code=StringField()
    status=StringField()
# class Unit_Master(Document):
#     sno=IntField(unique=True)
#     unit_code=StringField(unique=True)
#     unit_name=StringField()
#     cluster_name=StringField()
#     address=StringField()
#     status=StringField()
#     file_name = StringField(required=True)
#     data = BinaryField(required=True)
#     meta = {'strict': False}
class Addunitmaster_mobile(Document):
    sno=IntField(unique=True)
    unit_code=SequenceField(sequence_name='user_id_seq', value_decorator=lambda x: f"UN{int(x):03d}")
    unit_name=StringField(unique=True)
    cluster_name=StringField(required=True)
    address=StringField(required=True)
    status=StringField()
    file_name=BinaryField()
# class AddMaster(Document):
#     sno=IntField()
#     emp_id=StringField(unique=True)
#     Ucid_id=StringField(unique=True)
#     Agent_name=StringField()
#     mobile=StringField(max_length=10)
#     Qualification=StringField()
#     Designation=StringField()
#     Bank_Account_No=IntField()
#     Bank_Name=StringField()
#     IFSC_Code=StringField()
#     PAN_Number=StringField()
#     location=StringField()
#     Lattitide=StringField()
#     Logitude=StringField()
#     area=StringField()
#     city=StringField()
#     pincode=IntField()
#     district=StringField()
#     state=StringField()
#     created_by=StringField()
#     created_on=StringField()
#     branch=StringField()
#     source=StringField()
#     bank_attach= StringField(max_length=200000000)
#     data =FileField()
#     pan_attach= StringField(max_length=200000000)
#     data1 = FileField()
#     status=StringField()
class AddMaster1(Document):
    sno=IntField(unique=True)
    created_by=StringField()
    Ucid_id=StringField(unique=True)
    Agent_name=StringField()
    mobile=StringField(max_length=10,unique=True)
    Qualification=StringField()
    Designation=StringField()
    Bank_Account_No=IntField()
    Bank_Name=StringField()
    IFSC_Code=StringField()
    PAN_Number=StringField()
    location=StringField()
    Longitude=StringField()
    Latitude=StringField()
    area=StringField()
    city=StringField()
    pincode=IntField()
    district=StringField()
    state=StringField()
    created_on=DateTimeField()
    source=StringField()
    # bank_attach_file_name=StringField()
    bank_attach_path=StringField()
    pan_attach_path=StringField()
    status=StringField()
    branch=StringField()
class Active11(Document):
    sno=IntField(unique=True)
    camp=StringField(required=True,unique=True)
    status=StringField()
    created_on=DateTimeField()
    created_by=StringField()
    Modified_on=StringField()
    Modified_by=StringField()
class Callreport(Document):
    sno=IntField(unique=True)
    created_by=StringField()
    emp_id=StringField()
    Ucid_id=StringField()
    name=StringField()
    Designation=StringField()
    mobilenumber=StringField(max_length=10)
    created_on=DateTimeField()
    location=StringField()
    Lattitide=StringField(required=True)
    Logitude=StringField(required=True)
    area=StringField()
    city=StringField()
    pincode=IntField()
    district=StringField()
    state=StringField()
    station=StringField()
    catagery=StringField()
    remarks=StringField()
    groupcall=StringField(required=False)
    branch=StringField(required=False)
    source=StringField()
    camp=StringField()
    campdetails=StringField()
    type=StringField()
    status=StringField()
class AddRe(Document):
    sno=IntField(unique=True)
    unit_name=StringField()
    unicode=StringField(uniique=True)
    month_year=StringField()
    target=FloatField()
    Incroces=FloatField()
    Inlaks=FloatField()
    Inthousands=FloatField()
    created_by=StringField()
    created_on=StringField()
    modified_by=StringField()
    modified_on=StringField()
    status=StringField()
class AddRe11(Document):
    sno=IntField(unique=True)
    unit_name=StringField()
    unicode=StringField(unique=True)
    month_year=StringField()
    target=FloatField()
    Incroces=FloatField()
    Inlaks=FloatField()
    Inthousands=FloatField()
    created_by=StringField()
    created_on=DateTimeField()
    modified_by=StringField()
    modified_on=StringField()
    status=StringField()
class AddAD(Document):
    sno=IntField(unique=True)
    unit_name=StringField()
    unicode=StringField(uniique=True)
    Date=StringField()
    target=IntField()
    created_by=StringField()
    created_on=DateField()
    modified_by=StringField()
    modified_on=StringField()
    status=StringField()
class Camp(Document):
    sno=IntField(unique=True)
    TransID=StringField(unique=True)
    state=StringField()
    # statecode=StringField()
    city=StringField()
    # citycode=StringField()
    Area=StringField()
    # Areacode=StringField()
    location=StringField()
    campname=StringField()
    created_by=StringField()
    created_on=DateTimeField()
    modified_by=StringField()
    modified_on=StringField()
    status=StringField()


class Enrol(Document):
    sno=IntField(unique=True)
    TransID=StringField()
    Patient_name=StringField()
    Age=IntField()
    mobile=StringField()
    Remarks=StringField()
    created_by=StringField()
    created_on=DateTimeField()
    status=StringField()

class Areas(Document):
    Location=StringField()
    Pincode=IntField()
    State=StringField()
    District=StringField()
    areacode=StringField()

class Cluster(Document):
    sno=IntField()
    cluster_code=StringField()
    cluster_name=StringField()
    address=StringField()
    status=StringField()
class Cluster1(Document):
    sno=IntField()
    cluster_code=StringField()
    cluster_name=StringField(unique=True)
    address=StringField()
    status=StringField()
class Referpatient(Document):
    sno=IntField()
    patient_name=StringField()
    patient_mobile=StringField(max_length=10)
    executive_name=StringField()
    Ucid=StringField()
    Ucid_name=StringField()
    conslutant=StringField()
    speciality=StringField()
    remarks=StringField()
    Ipno=StringField()
    mapped_by=StringField()
    mapped_on=StringField()
    status=StringField()
    created_by=StringField()
    created_on=DateField()
    branch=StringField()
    agent_mobile=StringField(max_length=10)
    executive_mobile=IntField()
class Cityes(Document):
    sno=IntField()
    State=StringField()
    City=StringField()
    city_code=StringField()
class Cityes2(Document):
    sno=IntField()
    State=StringField()
    City=StringField()
    city_code=StringField()
class Consultant(Document):
    sno=IntField()
    consultant=StringField()
    department=StringField()
class Myteamre(Document):
    sno=IntField()
    emp_id=StringField()
    reporting_manager=StringField()
    first_haif=IntField()
    second_haif=IntField()
    created_on=DateTimeField()
    callscount=IntField()
    activitycount=IntField()
class Teamcoverage(Document):
    sno=IntField()
    year_month=StringField()
    name=StringField()
    emp_id=StringField()
    counts=IntField()
    total_counts=IntField()
class Greet(Document):
    sno=IntField(unique=True)
    Greet_id=StringField()
    title=StringField()
    message=StringField()
    catagory=StringField()
    image=StringField()
    image_name=StringField()
    target_link=StringField()
    share=StringField()
    employe_name=StringField()
    desigation=StringField()
    status=StringField()
    created_by=StringField()
    created_on=DateTimeField()
    modified_by=StringField()
    modified_on=DateTimeField()
class News(Document):
    sno=IntField(unique=True)
    news_id=StringField()
    title=StringField()
    message=StringField()
    Attachment=StringField()
    Attachment_name=StringField()
    share=StringField()
    # employe_name=StringField()
    # desigation=StringField()
    status=StringField()
    created_by=StringField()
    created_on=DateTimeField()
    modified_by=StringField()
    modified_on=DateTimeField()
class Image(Document):
    name=StringField()
    image=StringField()
    path_image=BinaryField()
