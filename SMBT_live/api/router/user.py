from fastapi import Depends,APIRouter
from starlette.responses import JSONResponse
from mongoengine import *
import json
from api.models import *
from mongoengine import *
from api.schema import *
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime
from jose import jwt
router=APIRouter(tags=["Singup"])
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
# ,expires_delta=timedelta
def create_access_token(data:dict):
    to_encode=data.copy()
    # expire=datetime.utcnow()+expires_delta
    # to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt
    
# def authenticate_user(Employee_id, password):
#     try:    
#         u = Usercreate.objects(Employee_id=Employee_id, Active_Status="Active").to_json()
#         user = json.loads(u)[0]
#         password_check = pwd_context.verify(password, user.get('password'))
#         return password_check
#     except (Usercreate.DoesNotExist, IndexError):
#         return False
def authenticate_user(Employee_id, password):
    try:
        user = Usercreate.objects(Employee_id=Employee_id, Active_Status="Active").only('password').first()
        if user:
            user_dict = json.loads(user.to_json())
            password_check = pwd_context.verify(password,user_dict.get('password'))
            return password_check
        else:
            return False
    except Usercreate.DoesNotExist:
        return False

@router.post("/token")
async def login(from_data:OAuth2PasswordRequestForm=Depends()):
    username=from_data.username
    password=from_data.password
    try:
        password_check = authenticate_user(username, password)
        if not password_check:
            raise ValueError("Credentials not valid")
        access_token = create_access_token(data={"sub": username})
        user = Usercreate.objects(Employee_id=username).only('Employee_id', 'User_name', 'Department', 'Branch', 'Desigination', 'Role_Code').first()
        if not user:
            raise ValueError("Employee ID not Exist")
        data = {"Error": "False","Message": "Login Successfully", "access_token": access_token,"token_type": "bearer","Empid": user.Employee_id,"Name": user.User_name,"Department": user.Department,"Branch": user.Branch,"Desigination": user.Desigination,"Role": user.Role_Code}
        return data
    except ValueError as e:
        data = {
            "Error": "True",
            "Message": str(e)
        }
        return JSONResponse(content=data, status_code=401)
def get_password(password):
    s=pwd_context.hash(password)
    
    return s
# ,token:str=Depends(oauth2_scheme)
@router.post("/User/data/list")
def sign_up(new_user:Don6):
    # in_tz = pytz.timezone('Asia/Kolkata')
    # in_time = datetime.now(in_tz)
    # in_time_str = in_time.strftime('%Y-%m-%d %H:%M')
    now = datetime.now()
    result = Usercreate.objects.order_by("-Employee_id").first()
    if result:
        Employee_id = result.Employee_id + 1
    else:
        Employee_id = 1001
    try:
        b1= new_user.Branch[:1].upper() + new_user.Branch[1:]
        user=Usercreate(UserID=Usercreate.objects.count()+1,Employee_id=Employee_id,password=get_password("Smbt@2023"),User_name=new_user.User_name,mobile_number=new_user.Mobile_number,Desigination=new_user.Desigination,Email_id=new_user.Email_id,Branch=b1,Created_by=new_user.Created_by,Modified_by=new_user.Modified_by,Source=new_user.Source,Country=new_user.Country,Country_code=new_user.Country_code,State=new_user.State,State_code=new_user.State_code,City=new_user.City,Pincode=new_user.Pincode,Allowance_Per_Day=new_user.Allowance_Per_Day,Multi_Branch_Access=new_user.Multi_Branch_Access,Active_Status=new_user.Active_Status,Department=new_user.Department,Reporting_Manager=new_user.Reporting_Manager,Bank_Account_No=new_user.Bank_Account_No,Bank_Name=new_user.Bank_Name,IFSC_Code=new_user. IFSC_Code,PAN_Number=new_user.PAN_Number,ID_Proof_No=new_user.ID_Proof_No,Role_Code=new_user.Role_Code,Location="",Location_address="",Created_on=now)
        user.save()
    except NotUniqueError:
        # return "Employe_id is alredy Existed"
        data1={"Error":"True","Message":"Employe_id is alredy Existed"}
        return JSONResponse(content=data1, status_code=400)
    except ValidationError:
        data1={"Error":"True","Message":"Please Enter valid Email_id"}
        return JSONResponse(content=data1, status_code=400)
        # return "Please enter valied Email_id"
        
    a="Successfully Executed"
    b=user.Employee_id

    if a:
            return {"Error":"False","Message":a,"Employee_id":b}
    else:
        d= {"Error":"True","Message":"Data not found"}
        # raise HTTPException(status_code=400,detail=d)
        data1={"Error":"True","Message":"Employe_id is Alredy Existed"}
        return JSONResponse(content=d, status_code=400)
@router.post("/get/user/list")
async def get_usercreate_list(me:get_userlist,token:str=Depends(oauth2_scheme)):
    data={"Error":"False","Message":"Data found","Userlist":[]}
    r=Usercreate.objects(Created_by=me.emp_id,Active_Status="Active").to_json()
    # return r
    data_list=json.loads(r)
    if data_list:
        for i in data_list:
            de={"UserName":i["User_name"],"EmployeeID":i["Employee_id"],"Email_id":i["Email_id"],"Designation":i["Desigination"],"Branch":i["Branch"],"ActiveStatus":i["Active_Status"],"City":i["City"],"ReportingManager":i["Reporting_Manager"],"Multi_Branch_Access":i["Multi_Branch_Access"],"Allowance_Per_Day":i["Allowance_Per_Day"],"mobile":i["mobile_number"],"Country":i["Country"],"State":i["State"],"Department":i["Department"],"Pincode":i["Pincode"],"Bank_Account_No":i["Bank_Account_No"],"Bank_Name":i["Bank_Name"],"IFSC_Code":i["IFSC_Code"],"PAN_Number":i["PAN_Number"],"ID_Proof_No":i["ID_Proof_No"],"Role_Code":i["Role_Code"]}
            # return {"Error":"False","Message":"Data Found","Details":de}
            data["Userlist"].append(de)
        return data
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.post("/search/user/data")
async def search_usercreate_list(me:search_user_list):
    data={"Error":"False","Message":"Data found","Userlist":[]}
    r=Usercreate.objects(Employee_id=int(me.Employee_id),Active_Status="Active").to_json()
    data_list=json.loads(r)
    if data_list:
        for i in data_list:
            de={"UserName":i["User_name"],"EmployeeID":i["Employee_id"],"Email_id":i["Email_id"],"Designation":i["Desigination"],"Branch":i["Branch"],"ActiveStatus":i["Active_Status"],"City":i["City"],"ReportingManager":i["Reporting_Manager"],"Multi_Branch_Access":i["Multi_Branch_Access"],"Allowance_Per_Day":i["Allowance_Per_Day"],"mobile":i["mobile_number"],"Country":i["Country"],"State":i["State"],"Department":i["Department"],"Pincode":i["Pincode"],"Bank_Account_No":i["Bank_Account_No"],"Bank_Name":i["Bank_Name"],"IFSC_Code":i["IFSC_Code"],"PAN_Number":i["PAN_Number"],"ID_Proof_No":i["ID_Proof_No"],"Role_Code":i["Role_Code"]}
            # return {"Error":"False","Message":"Data Found","Details":de}
            data["Userlist"].append(de)
        return data
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.post("/add_role_master_list")
def create_role_master(me:role):
    ad=Rolemaster(sno=Rolemaster.objects.count()+1,Role=me.Role)
    ad.save()
    a="Successfully Executed"
    if ad:
            return {"Error":"False","Message":a}
    else:
        d= {"Error":"True","Message":"Data not found"}
        return JSONResponse(content=d, status_code=400)
@router.get("/get_role_master_list")
def get_role_list():
    aa=Rolemaster.objects().to_json()
    b=json.loads(aa)
    data={"Error":"False","Message":"Data found","Rolelist":[]}
    for c in b:
        ro={"Role":c["Role"]}
        data["Rolelist"].append(ro)
    return data

@router.put("/change_employe_password")
def change_password(me:change_password_em):
    new=Usercreate.objects(Employee_id=me.Employee_id).to_json()
    new1=json.loads(new)
    if new1:
            if me.new_password==me.confirm_password:
                a= Usercreate.objects(Employee_id=me.Employee_id).update_one(set__password=get_password(me.new_password))
                b="Successfully Updated"
                if a:
                    return {"Error":"False","Message":b}
                else:
                    a={"Error":"True","Message":"Your password and confirmation password do not match"}
                return JSONResponse(content=a, status_code=400)
            else:
                a={"Error":"True","Message":"Your password and confirmation password do not match"}
                return JSONResponse(content=a, status_code=400)
    else:
         a={"Error":"True","Message":"Your password is wrong"}
         return JSONResponse(content=a, status_code=400)
@router.put("/delete_usermaster_emp_id")
def get_delete1(me:get_delete):
    if me.emp_id!="" and me.status!="":
        a= Usercreate.objects(Employee_id=me.emp_id).update_one(set__Active_Status=me.status)
        b="Successfully Updated"
        if a:
                return {"Error":"False","Message":"Data Found","Details":b}
        else:
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)
    else:
        a={"Error":"True","Message":"please enter employe_Id and status"}
        return JSONResponse(content=a, status_code=400)
@router.post("/emp_id_status_check")
def status_emp(me:emp_id_status):
    new=Usercreate.objects(Employee_id=int(me.emp_id)).to_json()
    new1=json.loads(new)
    if new1:
        for dd in new1:
            d=dd["Active_Status"]
            a={"Error":"False","Message":d}
        return JSONResponse(content=a, status_code=200)
    else:   
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.post("/add_department_details")
def add_department(me:add_depart):
    new=Add_depart(sno=Add_depart.objects.count()+1,department_name=me.department_name)
    new.save()
    a="Successfully Exicuted"
    if a:
            return {"Error":"False","Message":a}
    else:
        d= {"Error":"True","Message":"Data not found"}
        data1={"Error":"True","Message":"Employe_id is alredy Existed"}
        return JSONResponse(content=d, status_code=400)
@router.post("/add_Designation_details")
def add_Designation(me:add_designation):
    new=Add_Designation(sno=Add_Designation.objects.count()+1,Designation_name=me.Designation_name)
    new.save()
    a="Successfully Exicuted"
    if a:
            return {"Error":"False","Message":a}
    else:
        d={"Error":"True","Message":"Data not found"}
        data1={"Error":"True","Message":"Employe_id is alredy Existed"}
        return JSONResponse(content=d, status_code=400)
@router.get("/get_usercreate_department")
def get_department():
    new=Add_depart.objects().to_json()
    new1=json.loads(new)
    data={"Error":"False","Message":"Data found","Department":[]}
    if new1:
        for n in new1:
            a={"Department":n["department_name"]}
            data["Department"].append(a)
        return data
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.get("/get_usercreate_designation")
def get_designation():
    new=Add_Designation.objects().to_json()
    new1=json.loads(new)
    data={"Error":"False","Message":"Data found","Designation":[]}
    if new1:
        for n in new1:
            a={"Designation":n["Designation_name"]}
            data["Designation"].append(a)
        return data
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
 

@router.put("/update_user_master_details")
def update_user_list(me:update_user_master_list_using_emp_id):
    try:
        new=Usercreate.objects(Employee_id=me.Employee_id).to_json()
        new1=json.loads(new)
        if new1:
            try:
                b1= me.Branch[:1].upper() + me.Branch[1:]
                new1=Usercreate.objects(Employee_id=int(me.Employee_id)).update_one(set__User_name=me.User_name,set__mobile_number=int(me.mobile_number),set__Desigination=me.Desigination,set__Email_id=me.Email_id,set__Country=me.Country,set__State=me.State,set__City=me.City,set__Pincode=int(me.Pincode),set__Allowance_Per_Day=int(me.Allowance_Per_Day),set__Multi_Branch_Access=me.Multi_Branch_Access,set__Department=me.Department,set__Reporting_Manager=me.Reporting_Manager,set__Bank_Account_No=int(me.Bank_Account_No),set__Bank_Name=me.Bank_Name,set__IFSC_Code=me.IFSC_Code,set__PAN_Number=me.PAN_Number,set__ID_Proof_No=me.ID_Proof_No,set__Role_Code=me.Role_Code,set__Branch=b1)
                b="Successfully Updated"
                if b:
                        return {"Error":"False","Message":b}
                else:
                    a={"Error":"True","Message":"Data not found"}
                    return JSONResponse(content=a, status_code=400)
            except ValidationError:
                a={"Error":"True","Message":"please enter valid email_Id"}
                return JSONResponse(content=a, status_code=400)
        else:
                a={"Error":"True","Message":"please enter valid Employee_id"}
                return JSONResponse(content=a, status_code=400)
    except ValueError:
        a={"Error":"True","Message":"please enter valid Employe_id"}
        return JSONResponse(content=a, status_code=400)
    
    