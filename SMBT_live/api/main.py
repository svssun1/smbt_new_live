from fastapi import FastAPI,Depends,File,UploadFile,Form,Request,Query,status,Response,HTTPException
from starlette.responses import JSONResponse
from mongoengine import *
import json
from api.models import *
from mongoengine import *
from api.schema import *
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta,datetime,time
from jose import jwt
from geopy.geocoders import Nominatim
from fastapi.staticfiles import StaticFiles
import base64
from pathlib import Path
from fastapi.responses import FileResponse
from typing import Dict
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
import pytz
import io
import webbrowser
from api.router import user,unitmaster,addmaster,Activity,Createcall,Revenue,Addmission,Camp,Enrol,Cluster,patient,Reports,Greet,News,location,mobile
app=FastAPI()
app.mount("/static", StaticFiles(directory="./api/static"), name="static")
#connect("mongodb://api_user:mh%24cover%4047@ec2-13-127-65-92.ap-south-1.compute.amazonaws.com:27017/?authMechanism=DEFAULT")
#connect( db='SMBT', username='api-user', password='mh$cover@47', host='ec2-13-127-65-92.ap-south-1.compute.amazonaws.com:27017')
# client = pymongo.MongoClient("mongodb://api_user:mh%24cover%4047@ec2-13-127-65-92.ap-south-1.compute.amazonaws.com:27017/SMBT",authSource="admin") 
# db = client['SMBT']
connect(db="SMBT",host="Localhost",port=27017)
# "mongodb://api_user:mh%24cover%4047@ec2-13-127-65-92.ap-south-1.compute.amazonaws.com"
app.include_router(user.router)
app.include_router(unitmaster.router)
app.include_router(addmaster.router)
app.include_router(Activity.router)
app.include_router(Createcall.router)
app.include_router(Revenue.router)
app.include_router(Addmission.router)
app.include_router(Camp.router)
app.include_router(Enrol.router)
app.include_router(Cluster.router)
app.include_router(patient.router)
app.include_router(Reports.router)
app.include_router(Greet.router)
app.include_router(News.router)
app.include_router(location.router)
app.include_router(mobile.router)


#token
# SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

@app.get("/")
def index_page():
    return "Hey Listen, Hero's NEVER and EVER die :)"
import io
import os
@app.post("/mobile_image_set")
def image11(me:mobile_image_data):
     new=Image(name=me.name,path_image=me.file)
     FILEPATH="./api/static/{}_unit.jpg".format("name")
     filepath="./api/static/{}_unit.jpg".format("name")
     return_filepATH = "http://13.127.133.6"+filepath[5:]
     with open(FILEPATH, "wb") as f:
      decoded_image = base64.b64decode(me.file)
      f.write(decoded_image)
      new.image=return_filepATH
     new.save()
     b="Successfully Updated"
     if b:
            return {"Error":"False","Message":b}
     else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
###########importtant########################################################################################
# @app.get("/image/{image_id}")
# async def read_image(image_id: str):
#     image_obj = image.objects(name=image_id).first()
#     if image_obj:
#         image_data = image_obj.image
#         decoded_image = base64.b64decode(image_data)
#         return Response(content=decoded_image, media_type="image/jpeg")
#     else:
#         return {"error":"image not found"}
############importtant#######################################################################################
@app.get("/get_image_data{image_id}")
async def get_image(name:str):
    images=Image.objects(name=name).first()
    if images:
           name=images.name
           image_data=images.image
           ass={"Name":name,"path":image_data}
           return ass
        #    FILEPATH="./api/static/{}_unit.jpg".format(name)
        #    filepath="./api/static/{}_unit.jpg".format(name)
        #    return_filepATH = "http://13.127.133.6"+filepath[5:]
        #    with open(FILEPATH, "wb") as f:
        #     decoded_image = base64.b64decode(image_data)
        #     f.write(decoded_image)    
    else:
        raise HTTPException(status_code=404, detail="Image not found")
@app.put("/update_pic_")
def Update_photo(me:update_image_data):
     img=Image.objects(name=me.name).first()
     FILEPATH="./api/static/{}_unit.jpg".format("name")
     filepath="./api/static/{}_unit.jpg".format("name")
     return_filepATH = "http://13.127.133.6"+filepath[5:]
     with open(FILEPATH, "wb") as f:
      decoded_image = base64.b64decode(me.path_image)
      f.write(decoded_image)
      image45=return_filepATH
      path_image=me.path_image
      if img:
        img=Image.objects(name=me.name).update_one(set__name=me.change_name,set__image=image45,set__path_image=path_image)
        return "done"
      else:
          return "please check name"

# @app.get("/get/{image_id}")
# async def get_image(name:str):
#     image1=image.objects(image=name).first()
#     if image1:
#            FILEPATH=os.path.join("./api/static/{}.jpg".format("unit_code"))
#            filepath=os.path.join("./api/static/{}.jpg".format("unit_code"))
#            return_filepATH = "http://localhost:8000"+filepath[1:]
#            print(return_filepATH)
#            with open(FILEPATH, "wb") as f:
#              f.write(bson.Binary(image1.image))
#              return return_filepATH
#     else:
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)


# @app.get("/get_mobile_image_set")
# def imagess(name: str):
#     try:
#         image_obj = image.objects(name=name).first()
#         if image_obj:
#             image_data = image_obj.image
#             print(type(image_data))
#             decoded_image = base64.b64decode(image_data)
            
#             # Create a directory to store the images
#             if not os.path.exists("staic"):
#                 os.makedirs("static")
            
#             # Save the image to the "images" directory
#             image_path = f"images/{name}.jpg"
#             with open(image_path, "wb") as f:
#                 f.write(decoded_image)
#             # Set the path of the saved image as a variable, and return it as part of the response
#             image_url = f"http://13.127.133.6/{image_path}"
#             return {"image_path": image_path, "image_url": image_url}
#         else:
#             return {"error":"image not found"}
#     except:
#         a={"Error":"True","Message":"Image not found"}
#         return JSONResponse(content=a, status_code=400)
# ,expires_delta=timedelta
# def create_access_token(data:dict):
#     to_encode=data.copy()
#     # expire=datetime.utcnow()+expires_delta
#     # to_encode.update({"exp":expire})
#     encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
#     return encoded_jwt
    

# # authentication
# # def authenticate_user(Employee_id,password):
# #     try:    
# #         u=Usercreate.objects(Employee_id=Employee_id,Active_Status="Active").to_json()
# #         user=json.loads(u)
# #         if user:
# #             user=user[0]
# #             password_check=pwd_context.verify(password, user['password'])
# #             return password_check
# #     except Usercreate.DoesNotExist:
# #         return "False"
# def authenticate_user(Employee_id, password):
#     try:    
#         u = Usercreate.objects(Employee_id=Employee_id, Active_Status="Active").to_json()
#         user = json.loads(u)[0]
#         password_check = pwd_context.verify(password, user.get('password'))
#         return password_check
#     except (Usercreate.DoesNotExist, IndexError):
#         return False

# token for the data
# ,expires_delta=timedelta(minutes=15)


# @app.post("/token")
# async def login(from_data:OAuth2PasswordRequestForm=Depends()):
#     username=from_data.username
#     password=from_data.password
#     try:
#         password_check = authenticate_user(username, password)
#         print(password_check)
#         if not password_check:
#             raise ValueError("Credentials not valid")
#         access_token = create_access_token(data={"sub": username})
#         user = Usercreate.objects(Employee_id=username).first()
#         if not user:
#             raise ValueError("Employee ID not Exist")
#         data = {"Error": "False","Message": "Login Successfully", "access_token": access_token,"token_type": "bearer","Empid": user.Employee_id,"Name": user.User_name,"Department": user.Department,"Branch": user.Branch,"Desigination": user.Desigination,"Role": user.Role_Code}
#         return data
#     except ValueError as e:
#         data = {
#             "Error": "True",
#             "Message": str(e)
#         }
#         return JSONResponse(content=data, status_code=401)
# def get_password(password):
#     return pwd_context.hash(password)
# # ,token:str=Depends(oauth2_scheme)
# @app.post("/User/data/list")
# def sign_up(new_user:Don6):
#     # in_tz = pytz.timezone('Asia/Kolkata')
#     # in_time = datetime.now(in_tz)
#     # in_time_str = in_time.strftime('%Y-%m-%d %H:%M')
#     now = datetime.now()
#     result = Usercreate.objects.order_by("-Employee_id").first()
#     if result:
#         Employee_id = result.Employee_id + 1
#     else:
#         Employee_id = 1001
#     try:
#         b1= new_user.Branch[:1].upper() + new_user.Branch[1:]
#         user=Usercreate(UserID=Usercreate.objects.count()+1,Employee_id=Employee_id,password=get_password("Smbt@2023"),User_name=new_user.User_name,mobile_number=new_user.Mobile_number,Desigination=new_user.Desigination,Email_id=new_user.Email_id,Branch=b1,Created_by=new_user.Created_by,Modified_by=new_user.Modified_by,Source=new_user.Source,Country=new_user.Country,Country_code=new_user.Country_code,State=new_user.State,State_code=new_user.State_code,City=new_user.City,Pincode=new_user.Pincode,Allowance_Per_Day=new_user.Allowance_Per_Day,Multi_Branch_Access=new_user.Multi_Branch_Access,Active_Status=new_user.Active_Status,Department=new_user.Department,Reporting_Manager=new_user.Reporting_Manager,Bank_Account_No=new_user.Bank_Account_No,Bank_Name=new_user.Bank_Name,IFSC_Code=new_user. IFSC_Code,PAN_Number=new_user.PAN_Number,ID_Proof_No=new_user.ID_Proof_No,Role_Code=new_user.Role_Code,Location="",Location_address="",Created_on=now)
#         user.save()
#     except NotUniqueError:
#         # return "Employe_id is alredy Existed"
#         data1={"Error":"True","Message":"Employe_id is alredy Existed"}
#         return JSONResponse(content=data1, status_code=400)
#     except ValidationError:
#         data1={"Error":"True","Message":"Please Enter valid Email_id"}
#         return JSONResponse(content=data1, status_code=400)
#         # return "Please enter valied Email_id"
        
#     a="Successfully Executed"
#     b=user.Employee_id

#     if a:
#             return {"Error":"False","Message":a,"Employee_id":b}
#     else:
#         d= {"Error":"True","Message":"Data not found"}
#         # raise HTTPException(status_code=400,detail=d)
#         data1={"Error":"True","Message":"Employe_id is Alredy Existed"}
#         return JSONResponse(content=d, status_code=400)
    
# @app.post("/get/user/list")
# async def get_usercreate_list(me:get_userlist,token:str=Depends(oauth2_scheme)):
    
#     data={"Error":"False","Message":"Data found","Userlist":[]}
#     r=Usercreate.objects(Created_by=me.emp_id,Active_Status="Active").order_by("-Employee_id").to_json()
#     data_list=json.loads(r)
#     if data_list:
#         for i in data_list:
#             de={"UserName":i["User_name"],"EmployeeID":i["Employee_id"],"Email_id":i["Email_id"],"Designation":i["Desigination"],"Branch":i["Branch"],"ActiveStatus":i["Active_Status"],"City":i["City"],"ReportingManager":i["Reporting_Manager"],"Multi_Branch_Access":i["Multi_Branch_Access"],"Allowance_Per_Day":i["Allowance_Per_Day"],"mobile":i["mobile_number"],"Country":i["Country"],"State":i["State"],"Department":i["Department"],"Pincode":i["Pincode"],"Bank_Account_No":i["Bank_Account_No"],"Bank_Name":i["Bank_Name"],"IFSC_Code":i["IFSC_Code"],"PAN_Number":i["PAN_Number"],"ID_Proof_No":i["ID_Proof_No"],"Role_Code":i["Role_Code"]}
#             # return {"Error":"False","Message":"Data Found","Details":de}
#             data["Userlist"].append(de)
#         return data
#     else:
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/search/user/data")
# async def search_usercreate_list(me:search_user_list):
#     data={"Error":"False","Message":"Data found","Userlist":[]}
#     r=Usercreate.objects(Employee_id=int(me.Employee_id),Active_Status="Active").to_json()
#     data_list=json.loads(r)
#     if data_list:
#         for i in data_list:
#             de={"UserName":i["User_name"],"EmployeeID":i["Employee_id"],"Email_id":i["Email_id"],"Designation":i["Desigination"],"Branch":i["Branch"],"ActiveStatus":i["Active_Status"],"City":i["City"],"ReportingManager":i["Reporting_Manager"],"Multi_Branch_Access":i["Multi_Branch_Access"],"Allowance_Per_Day":i["Allowance_Per_Day"],"mobile":i["mobile_number"],"Country":i["Country"],"State":i["State"],"Department":i["Department"],"Pincode":i["Pincode"],"Bank_Account_No":i["Bank_Account_No"],"Bank_Name":i["Bank_Name"],"IFSC_Code":i["IFSC_Code"],"PAN_Number":i["PAN_Number"],"ID_Proof_No":i["ID_Proof_No"],"Role_Code":i["Role_Code"]}
#             # return {"Error":"False","Message":"Data Found","Details":de}
#             data["Userlist"].append(de)
#         return data
#     else:
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/add_role_master_list")
# def create_role_master(me:role):
#     ad=Rolemaster(sno=Rolemaster.objects.count()+1,Role=me.Role)
#     ad.save()
#     a="Successfully Executed"
#     if ad:
#             return {"Error":"False","Message":a}
#     else:
#         d= {"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=d, status_code=400)
# @app.get("/get_role_master_list")
# def get_role_list():
#     aa=Rolemaster.objects().to_json()
#     b=json.loads(aa)
#     data={"Error":"False","Message":"Data found","Rolelist":[]}
#     for c in b:
#         ro={"Role":c["Role"]}
#         data["Rolelist"].append(ro)
#     return data

# @app.put("/change_employe_password")
# def change_password(me:change_password_em):
#     # new=Usercreate.objects(Employee_id=me.Employee_id,password=me.old_password).to_json()
#     # new1=json.loads(new)
#     # if new1:
#             if me.new_password==me.confirm_password:
#                 a= Usercreate.objects(Employee_id=int(me.Employee_id)).update_one(set__password=get_password(me.new_password))
#                 b="Successfully Updated"
#                 if a:
#                     return {"Error":"False","Message":b}
#                 else:
#                     a={"Error":"True","Message":"Your password and confirmation password do not match"}
#                 return JSONResponse(content=a, status_code=400)
#             else:
#                 a={"Error":"True","Message":"Your password and confirmation password do not match"}
#                 return JSONResponse(content=a, status_code=400)

#     # else:
#     #      a={"Error":"True","Message":"Your password is wrong"}
#     #      return JSONResponse(content=a, status_code=400)
# @app.put("/delete_usermaster_emp_id")
# def get_delete1(me:get_delete):
#     if me.emp_id!="" and me.status!="":
#         a= Usercreate.objects(Employee_id=me.emp_id).update_one(set__Active_Status=me.status)
#         b="Successfully Updated"
#         if a:
#                 return {"Error":"False","Message":"Data Found","Details":b}
#         else:
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
#     else:
#         a={"Error":"True","Message":"please enter employe_Id and status"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/emp_id_status_check")
# def status_emp(me:emp_id_status):
#     new=Usercreate.objects(Employee_id=int(me.emp_id)).to_json()
#     new1=json.loads(new)
#     if new1:
#         for dd in new1:
#             d=dd["Active_Status"]
           
#             a={"Error":"False","Message":d}
#         return JSONResponse(content=a, status_code=200)
#     else:
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)

# @app.post("/add_department_details")
# def add_department(me:add_depart):
#     new=Add_depart(sno=Add_depart.objects.count()+1,department_name=me.department_name)
#     new.save()
#     a="Successfully Exicuted"
#     if a:
#             return {"Error":"False","Message":a}
#     else:
#         d= {"Error":"True","Message":"Data not found"}
#         data1={"Error":"True","Message":"Employe_id is alredy Existed"}
#         return JSONResponse(content=d, status_code=400)
# @app.post("/add_Designation_details")
# def add_Designation(me:add_designation):
#     new=Add_Designation(sno=Add_Designation.objects.count()+1,Designation_name=me.Designation_name)
#     new.save()
#     a="Successfully Exicuted"
#     if a:
#             return {"Error":"False","Message":a}
#     else:
#         d= {"Error":"True","Message":"Data not found"}
#         # raise HTTPException(status_code=400,detail=d)
#         data1={"Error":"True","Message":"Employe_id is alredy Existed"}
#         return JSONResponse(content=d, status_code=400)
# @app.get("/get_usercreate_department")
# def get_department():
#     new=Add_depart.objects().to_json()
#     new1=json.loads(new)
#     data={"Error":"False","Message":"Data found","Department":[]}
#     if new1:
#         for n in new1:
#             a={"Department":n["department_name"]}
#             data["Department"].append(a)
#         return data
#     else:
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.get("/get_usercreate_designation")
# def get_designation():
#     new=Add_Designation.objects().to_json()
#     new1=json.loads(new)
#     data={"Error":"False","Message":"Data found","Designation":[]}
#     if new1:
#         for n in new1:
#             a={"Designation":n["Designation_name"]}
#             data["Designation"].append(a)
#         return data
#     else:
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
 
# @app.get("/get/Country/List")
# def list2(token:str=Depends(oauth2_scheme)):
#     new=country_state3.objects(status="Active").to_json()
#     new1=json.loads(new)
#     data={"Error":"False","Message":"Data found","Country_List":[]}
#     for i in new1:
#         a={"Country_Name":i["Capital"],"Country_Code":i["Capital_code"],"status":i["status"]}
#         data["Country_List"].append(a)
# #             # data.append(de)
#         return data
#     else:
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# # @app.get("/get/Country/List")
# # def list2(token:str=Depends(oauth2_scheme)):
# #     # data={"Error":"False","message":"Data found","Country List":}
    
# #     # r=country_state.objects(country_name="North-East District").distinct()
# #     r=country_state.objects(country_status="Active").distinct(field="country_name")
# #     d=country_state.objects(country_status="Active").to_json()
# #     data_list=json.loads(d)
# #     if data_list:
# #         data={"Error":"False","Message":"Data found","Country_List":[]}
# #         for i,j in zip(r,data_list):
# #             de={"Country_Name":i,"Country_Code":j["country_code"],"Country_Status":j["country_status"],"id":j["id"]}
# #             data["Country_List"].append(de)
# #             # data.append(de)
# #         return data
# #     else:
# #         a={"Error":"True","Message":"Data not found"}
# #         return JSONResponse(content=a, status_code=400)
# @app.get("/get/State/List")
# def list1(token:str=Depends(oauth2_scheme)):
#     r=country_state2.objects(status="Active").to_json()
#     data_list=json.loads(r)
#     data={"Error":"False","Message":"Data found","State_List":[]}
#     if data_list:
#         for g in data_list:
#             ji={"State":g["StateName"],"Statecode":g["Statecode"],"Status":g["status"]}
#             data["State_List"].append(ji)
#         return data
#     else:
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.put("/update_user_master_details")
# def update_user_list(me:update_user_master_list_using_emp_id):
#     try:
#         new=Usercreate.objects(Employee_id=me.Employee_id).to_json()
#         new1=json.loads(new)
#         if new1:
#             try:
#                 b1= me.Branch[:1].upper() + me.Branch[1:]
#                 new=Usercreate.objects(Employee_id=int(me.Employee_id)).update_one(set__User_name=me.User_name,set__mobile_number=int(me.mobile_number),set__Desigination=me.Desigination,set__Email_id=me.Email_id,set__Country=me.Country,set__State=me.State,set__City=me.City,set__Pincode=int(me.Pincode),set__Allowance_Per_Day=int(me.Allowance_Per_Day),set__Multi_Branch_Access=me.Multi_Branch_Access,set__Department=me.Department,set__Reporting_Manager=me.Reporting_Manager,set__Bank_Account_No=int(me.Bank_Account_No),set__Bank_Name=me.Bank_Name,set__IFSC_Code=me.IFSC_Code,set__PAN_Number=me.PAN_Number,set__ID_Proof_No=me.ID_Proof_No,set__Role_Code=me.Role_Code,set__Branch=b1)
#                 b="Successfully Updated"
#                 if b:
#                         return {"Error":"False","Message":b}
#                 else:
#                     a={"Error":"True","Message":"Data not found"}
#                     return JSONResponse(content=a, status_code=400)
#             except ValidationError:
#                 a={"Error":"True","Message":"please enter valid email_Id"}
#                 return JSONResponse(content=a, status_code=400)
#         else:
#                 a={"Error":"True","Message":"please enter valid Employee_id"}
#                 return JSONResponse(content=a, status_code=400)
#     except ValueError:
#         a={"Error":"True","Message":"please enter valid Employe_id"}
#         return JSONResponse(content=a, status_code=400)

@app.put("/update/Bank/details")
def update(Employe_id:int,Bank_name:str,Bank_Account_No:int,IFSC_Code:str,token:str=Depends(oauth2_scheme)):
    a= Usercreate.objects(Employee_id=Employe_id).update_one(set__Bank_Name=Bank_name,set__Bank_Account_No=Bank_Account_No,set__IFSC_Code=IFSC_Code)
    b="Successfully Submited"
    if b:
            return {"Error":"False","Message":b}
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)

# @app.post("/ADD/USER/MASTER/NEW_UNIT")
# async def new_unit(me:addunitmaster,token:str=Depends(oauth2_scheme)):
#     b=me.unit_name[:1].upper()+me.unit_name[1:]
#     alr_unit = Addunitmaster.objects(unit_name=b).first()
#     if alr_unit:
#         if alr_unit.status == 'Inactive':
#             sno = alr_unit.sno
#             alr_unit.delete()
#             Addunitmaster.objects(sno__gt=sno).update(dec__sno=1)    
#         else:
#             data = {"Error":"True", "Message":"Unit name already exists."}
#             return JSONResponse(content=data, status_code=400)
#     img = Addunitmaster(sno=Addunitmaster.objects.count()+1,unit_name=b,cluster_name=me.cluster_name,address=me.address,status=me.status,file_name=me.file_name)
#     img.save()
#     b = "Successfully Submitted"
#     if b:
#         return {"Error":"False", "Message":b}
#     else:
#         a = {"Error":"True", "Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
   
# @app.get("/get/UnitMaster/Data")
# def get_all(token:str=Depends(oauth2_scheme)):
#     a=Addunitmaster.objects(status="Active").order_by("-sno").to_json() 
#     data1={"Error":"False","Message":"Data found","Unitmaster":[]}
#     data=json.loads(a)
#     if data:
#         for d in data:
#             sno=d["sno"]
#             unit_code=d["unit_code"]
#             unit_name=d["unit_name"]
#             cluster_name=d["cluster_name"]
#             address=d["address"]
#             status=d["status"]
#             f1=d["file_name"]
#             a2=str.encode(f1)
#             FILEPATH="./api/static/{}_unit.jpg".format(unit_name)
#             filepath="./api/static/{}_unit.jpg".format(unit_name)
#             return_filepATH = "http://13.127.133.6"+filepath[5:]
#             with open(FILEPATH,"wb") as fh:
#                 fh.write(base64.decodebytes(a2))
#             k={"SNO":sno,"Unit_Code":unit_code,"Unit_Name":unit_name,"Cluster_Name":cluster_name,"Address":address,"Status":status,"Image_path":return_filepATH}
#             data1["Unitmaster"].append(k)
#         return data1
#     else:
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
# @app.post("/search/UnitMaster/Data")
# def search_data(me:search_unit):
#     a=Addunitmaster.objects(unit_code=me.unit_code,status="Active").to_json() 
#     data1={"Error":"False","Message":"Data found","Unitmaster":[]}
#     data=json.loads(a)
#     if data:
#         for d in data:
#             sno=d["sno"]
#             unit_code=d["unit_code"]
#             unit_name=d["unit_name"]
#             cluster_name=d["cluster_name"]
#             address=d["address"]
#             status=d["status"]
#             try:
#                 f1=d["file_name"]
#                 a2=str.encode(f1)
#                 FILEPATH="./api/static/{}_unit.jpg".format(unit_name)
#                 filepath="./api/static/{}_unit.jpg".format(unit_name)
#                 return_filepATH = "http://13.127.133.6"+filepath[5:]
#                 with open(FILEPATH,"wb") as fh:
#                     fh.write(base64.decodebytes(a2))
#             except:
#                 return "Image Not found"
#             k={"SNO":sno,"Unit_Code":unit_code,"Unit_Name":unit_name,"Cluster_Name":cluster_name,"Address":address,"Status":status,"image_path":return_filepATH}
#             data1["Unitmaster"].append(k)
#         return data1
#     else:
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
            
# @app.get("/get/Unitmaster/Counts")
# def counts(token:str=Depends(oauth2_scheme)):
#      u=Addunitmaster.objects().count()
#      v=Addunitmaster.objects(status="Active").count()
#      w=Addunitmaster.objects(status="Inactive").count()
#      a={"Total_Units":u,"Active_Units":v,"Inactive_Units":w}
#      if a:
#          data1={"Error":"False","Message":"Data found","Counts":[]}
#          data1["Counts"].append(a)
#          return data1
#      else:
#         n={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=n, status_code=400)

# @app.put("/Update_unitmaster_data")
# def update_image(me:update_unitmaster):
#     new=Addunitmaster.objects(unit_name=me.unit_code).to_json()
#     new1=json.loads(new)
#     if new1:
#         if me.file_name not in ["", "string"]:
#             a= Addunitmaster.objects(unit_name=me.unit_code).update_one(set__unit_name=me.unit_name,set__cluster_name=me.cluster_name,set__address=me.address,set__file_name=me.file_name)
#         elif me.file_name == "":
#             a= Addunitmaster.objects(unit_name=me.unit_code).update_one(set__unit_name=me.unit_name,set__cluster_name=me.cluster_name,set__address=me.address)
#         elif me.file_name=="string":
#             a= Addunitmaster.objects(unit_name=me.unit_code).update_one(set__unit_name=me.unit_name,set__cluster_name=me.cluster_name,set__address=me.address)

#         b="Successfully Updated"
#         if b:
#                 return {"Error":"False","Message":b}
#         else:
#             # raise HTTPException(status_code=404, detail="data not found")
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
#     else:
#             # raise HTTPException(status_code=404, detail="data not found")
#             a={"Error":"True","Message":"please enter valid unit_code"}
#             return JSONResponse(content=a, status_code=400)
# @app.put("/Delete_unitmaster_data")
# def get_delete_data(me:delete_unitmaster):
#     new=Addunitmaster.objects(unit_code=me.unit_code).to_json()
#     new1=json.loads(new)
#     if new1:
#         a= Addunitmaster.objects(unit_code=me.unit_code).update_one(set__status=me.status)
#         b="Successfully Updated"
#         if b:
#                 return {"Error":"False","Message":b}
#         else:
#             # raise HTTPException(status_code=404, detail="data not found")
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
#     else:
#          a={"Error":"True","Message":"please enter valid Ucid"}
#          return JSONResponse(content=a, status_code=400)
# @app.get("/get_Inactive_unitmasterdata")
# def get_Inactive_data():
#     a=Addunitmaster.objects(status="Inactive").to_json() 
#     data1={"Error":"False","Message":"Data found","Unitmaster_Inactive":[]}
#     data=json.loads(a)
#     if data:
#         for d in data:
#             sno=d["sno"]
#             unit_code=d["unit_code"]
#             unit_name=d["unit_name"]
#             cluster_name=d["cluster_name"]
#             address=d["address"]
#             status=d["status"]
#             k={"SNO":sno,"Unit_Code":unit_code,"Unit_Name":unit_name,"Cluster_Name":cluster_name,"Address":address,"Status":status}
#             data1["Unitmaster_Inactive"].append(k)
#         return data1
#     else:
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
# @app.get("/get_unit_master_image")
# async def read_image(sno: int):
#     try:
#         image_obj = AddMaster1.objects(sno=sno).first()
#         if image_obj:
#             image_data = image_obj.pan_attach_path
#             decoded_image = base64.b64decode(image_data)
#             return Response(content=decoded_image, media_type="image/jpeg/pdf")
#         else:
#             return {"error":"image not found"}
#     except :
#         a={"Error":"True","Message":"Image not found"}
#         return JSONResponse(content=a, status_code=400)




# @app.delete("/Delete/unit")
# async def delete_image(me:don8,token:str=Depends(oauth2_scheme)):
#     image = Unit_Master.objects(unit_code=me.unit_code).first()
#     if image:
#         image.delete()
#         # return {"detail":"Unit deleted"}
#         b="Successfully Submited"
#         return {"Error":"False","Message":b}

#     else:
#         # raise HTTPException(status_code=404, detail="Unit not found")
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/Add/Master")
# async def master(me:addmaster1):
#     # in_tz = pytz.timezone('Asia/Kolkata')
#     # in_time = datetime.now(in_tz)
#     # in_time_str = in_time.strftime('%Y-%m-%d %H:%M')
#     b=me.branch[:1].upper()+me.branch[1:]
#     try:
#         geolocator = Nominatim(user_agent="geoapiExercises")
#         Latitude =me.Latitude
#         Longitude =me.Longitude
#         location = geolocator.reverse(Latitude+","+Longitude)
#         address = location.raw['address']
#         city=address["city"]
#         state=address["state"]
#         pincode=address["postcode"]
#         district=address["state_district"]
#         location=address["state_district"]
#     except ValueError:
#         # return "please enter Latitude and Longitude values"
#         data1={"Error":"True","Message":"GPS Singal Too Weak"}
#         return JSONResponse(content=data1, status_code=400)
#     now = datetime.now()
#     try: 
#         master=AddMaster1(sno=AddMaster1.objects.count()+1,Ucid_id="UC{:02d}".format(AddMaster1.objects.count()+1),Agent_name=me.Agent_name,mobile=me.mobile,Qualification=me.Qualification,Designation=me.Designation,Bank_Account_No=me.Bank_Account_No,Bank_Name=me.Bank_Name,IFSC_Code=me.IFSC_Code,PAN_Number=me.PAN_Number,Latitude=Latitude,Longitude=Longitude,area=location,city=city,district=district,state=state,pincode=pincode,created_by=me.created_by,status="Active",bank_attach_path=me.bank_attach_path,pan_attach_path=me.pan_attach_path,branch=b,created_on=now)
#         master.save()
#     except NotUniqueError:
# #         # return "Mobile Number is alredy Existed"
#         data1={"Error":"True","Message":"Mobile Number Already Existed"}
#         return JSONResponse(content=data1, status_code=400)
#     except  ValidationError:
#         data1={"Error":"True","Message":"Please Check Mobile Number"}
#         return JSONResponse(content=data1, status_code=400)
#     b="Successfully Submitted"
#     if b:
#         return {"Error":"False","Message":b}
#     else:
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/get/Master/List")
# def list1(me:getaddmaster):
#     data=AddMaster1.objects(created_by=me.emp_id,status="Active").order_by("-sno").to_json()
#     g=json.loads(data)
#     data1={"Error":"False","Message":"Data found","MasterList":[]}
#     if g:
#         for a in g:
#             a1=a["bank_attach_path"]
#             f = a["Agent_name"]
#             f1=a["pan_attach_path"]
#             a2=str.encode(a1)
#             a3=str.encode(f1)
#             FILEPATH="./api/static/{}_bank.jpg".format(f)
#             filepath="./api/static/{}_bank.jpg".format(f)
#             return_filepATH = "http://13.127.133.6"+filepath[5:]
#             with open(FILEPATH,"wb") as fh:
#                 fh.write(base64.decodebytes(a2))
#             FILEPATH="./api/static/{}pan.jpg".format(f)
#             filepath="./api/static/{}pan.jpg".format(f)
#             return_filepATH2 = "http://13.127.133.6"+filepath[5:]
#             with open(FILEPATH,"wb") as fh:
#                 fh.write(base64.decodebytes(a3))
#             g=a["created_on"]
#             timestamp = g['$date']
#             date_object = datetime.fromtimestamp(timestamp/1000).date()
#             formatted_date = date_object.strftime('%d-%b-%Y')
#             gt={"sno":a["sno"],"UCID":a["Ucid_id"],"Agent_name":a["Agent_name"],"Mobile":a["mobile"],"Qualification":a["Qualification"],"Designation":a["Designation"],"Location":a["area"],"Bank_Name":a["Bank_Name"],"Bank_Account_No":str(a["Bank_Account_No"]),"IFSC_Code":a["IFSC_Code"],"Created_on":formatted_date,"Branch":a["branch"],"PAN_Number":a["PAN_Number"],"bank_path":return_filepATH,"pan_path":return_filepATH2}
#             data1["MasterList"].append(gt)
#         return data1
#     else:
#         # return {"Error":"True","Message":"Data not found"}
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/search_master_list_mobile")
# def master_list(me:search_masterlist):
#     b = me.search[:2].upper() + me.search[2:]
#     c= me.search[:1].lower() + me.search[1:]
#     if me.search==b:
#         result = AddMaster1.objects(Q(Agent_name__icontains=b) | Q(Ucid_id__icontains=b) | Q(status="Active"),created_by=me.created_by).to_json()
#         result1=json.loads(result)
#         data1={"Error":"False","message":"Data found","MasterList":[]}
#         for a in result1:
#             a1=a["bank_attach_path"]
#             f = a["Agent_name"]
#             f1=a["pan_attach_path"]
#             a2=str.encode(a1)
#             a3=str.encode(f1)
#             FILEPATH="./api/static/{}_bank.jpg".format(f)
#             filepath="./api/static/{}_bank.jpg".format(f)
#             return_filepATH = "http://13.127.133.6"+filepath[5:]
#             with open(FILEPATH,"wb") as fh:
#                 fh.write(base64.decodebytes(a2))
#             FILEPATH="./api/static/{}pan.jpg".format(f)
#             filepath="./api/static/{}pan.jpg".format(f)
#             return_filepATH2 = "http://13.127.133.6"+filepath[5:]
#             with open(FILEPATH,"wb") as fh:
#                 fh.write(base64.decodebytes(a3))
#             g=a["created_on"]
#             timestamp = g['$date']
#             date_object = datetime.fromtimestamp(timestamp/1000).date()
#             formatted_date = date_object.strftime('%d-%b-%Y')
#             gt={"sno":a["sno"],"UCID":a["Ucid_id"],"Agent_name":a["Agent_name"],"Qualification":a["Qualification"],"Designation":a["Designation"],"Location":a["area"],"Created_on":formatted_date,"Branch":a["branch"],"bank_path":return_filepATH,"pan_path":return_filepATH2}
#             data1["MasterList"].append(gt)
#         return data1
#     elif me.search==c:
#         result = AddMaster1.objects(Q(Agent_name__icontains=c) | Q(Ucid_id__icontains=c) | Q(status="Active")).to_json()
#         result1=json.loads(result)
#         data1={"Error":"False","message":"Data found","MasterList":[]}
#         if result1:
#             for a in result1:
#                 a1=a["bank_attach_path"]
#                 f = a["Agent_name"]
#                 f1=a["pan_attach_path"]
#                 a2=str.encode(a1)
#                 a3=str.encode(f1)
#                 FILEPATH="./api/static/{}_bank.jpg".format(f)
#                 filepath="./api/static/{}_bank.jpg".format(f)
#                 return_filepATH = "http://13.127.133.6"+filepath[5:]
#                 with open(FILEPATH,"wb") as fh:
#                     fh.write(base64.decodebytes(a2))
#                 FILEPATH="./api/static/{}pan.jpg".format(f)
#                 filepath="./api/static/{}pan.jpg".format(f)
#                 return_filepATH2 = "http://13.127.133.6"+filepath[5:]
#                 with open(FILEPATH,"wb") as fh:
#                     fh.write(base64.decodebytes(a3))
#                 g=a["created_on"]
#                 timestamp = g['$date']
#                 date_object = datetime.fromtimestamp(timestamp/1000).date()
#                 formatted_date = date_object.strftime('%Y-%b-%d')
#                 gt={"sno":a["sno"],"UCID":a["Ucid_id"],"Agent_name":a["Agent_name"],"Qualification":a["Qualification"],"Designation":a["Designation"],"Location":a["area"],"Created_on":formatted_date,"Branch":a["branch"],"bank_path":return_filepATH,"pan_path":return_filepATH2}
#                 data1["MasterList"].append(gt)
#             return data1
#     else:
             
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/search/Master/List")
# def search_master_list(me:search_master_list):
#     data=AddMaster1.objects(sno=int(me.sno),status="Active").to_json()
#     g=json.loads(data)
#     data1={"Error":"False","Message":"Data found","MasterList":[]}
#     if g:
#         for a in g:
#             g=a["created_on"]
#             timestamp = g['$date']
#             a1=a["bank_attach_path"]
#             f = a["Agent_name"]
#             f1=a["pan_attach_path"]
#             a2=str.encode(a1)
#             a3=str.encode(f1)
#             FILEPATH="./api/static/{}_bank.jpg".format(f)
#             filepath="./api/static/{}_bank.jpg".format(f)
#             return_filepATH = "http://13.127.133.6"+filepath[5:]
#             with open(FILEPATH,"wb") as fh:
#                 fh.write(base64.decodebytes(a2))
#             FILEPATH="./api/static/{}pan.jpg".format(f)
#             filepath="./api/static/{}pan.jpg".format(f)
#             return_filepATH2 = "http://13.127.133.6"+filepath[5:]
#             with open(FILEPATH,"wb") as fh:
#                 fh.write(base64.decodebytes(a3))
#             date_object = datetime.fromtimestamp(timestamp/1000).date()
#             formatted_date = date_object.strftime('%Y-%b-%d')
#             gt={"sno":a["sno"],"UCID":a["Ucid_id"],"Agent_name":a["Agent_name"],"Qualification":a["Qualification"],"Designation":a["Designation"],"Location":a["area"],"Created_on":formatted_date,"bank_path":return_filepATH,"pan_path":return_filepATH2}
#             data1["MasterList"].append(gt)
#         return data1
#     else:
#         # return {"Error":"True","Message":"Data not found"}
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.put("/update_add_master_data")
# def update_master(me:update_addmaster):
#     try:
#         new=AddMaster1.objects(sno=me.sno).to_json()
#         new1=json.loads(new)
#         if new1:
#             if me.bank_attach_path !="" and me.pan_attach_path !="" :
#                 a= AddMaster1.objects(sno=me.sno).update_one(set__Agent_name=me.Agent_name,set__mobile=me.mobile,set__Qualification=me.Qualification,set__Designation=me.Designation,set__Bank_Account_No=int(me.Bank_Account_No),set__Bank_Name=me.Bank_Name,set__IFSC_Code=me.IFSC_Code,set__PAN_Number=me.PAN_Number,set__branch=me.branch,set__bank_attach_path=me.bank_attach_path,set__pan_attach_path=me.pan_attach_path)
#             elif me.bank_attach_path !="":
#                 a= AddMaster1.objects(sno=me.sno).update_one(set__Agent_name=me.Agent_name,set__mobile=me.mobile,set__Qualification=me.Qualification,set__Designation=me.Designation,set__Bank_Account_No=int(me.Bank_Account_No),set__Bank_Name=me.Bank_Name,set__IFSC_Code=me.IFSC_Code,set__PAN_Number=me.PAN_Number,set__branch=me.branch,set__bank_attach_path=me.bank_attach_path)
#             elif me.pan_attach_path !="":
#                 a= AddMaster1.objects(sno=me.sno).update_one(set__Agent_name=me.Agent_name,set__mobile=me.mobile,set__Qualification=me.Qualification,set__Designation=me.Designation,set__Bank_Account_No=int(me.Bank_Account_No),set__Bank_Name=me.Bank_Name,set__IFSC_Code=me.IFSC_Code,set__PAN_Number=me.PAN_Number,set__branch=me.branch,set__pan_attach_path=me.pan_attach_path)
#             elif me.bank_attach_path =="" and me.pan_attach_path =="":
#                 a= AddMaster1.objects(sno=me.sno).update_one(set__Agent_name=me.Agent_name,set__mobile=me.mobile,set__Qualification=me.Qualification,set__Designation=me.Designation,set__Bank_Account_No=int(me.Bank_Account_No),set__Bank_Name=me.Bank_Name,set__IFSC_Code=me.IFSC_Code,set__PAN_Number=me.PAN_Number,set__branch=me.branch)
#             # elif me.pan_attach_path=="string" or me.bank_attach_path=="string":
#             #     a= AddMaster1.objects(sno=me.sno).update_one(set__Agent_name=me.Agent_name,set__mobile=me.mobile,set__Qualification=me.Qualification,set__Designation=me.Designation,set__Bank_Account_No=int(me.Bank_Account_No),set__Bank_Name=me.Bank_Name,set__IFSC_Code=me.IFSC_Code,set__PAN_Number=me.PAN_Number,set__branch=me.branch)

#             b="Successfully Submited"
#             if b:
#              return {"Error":"False","Message":b}
#             else:
#              a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
#         else:
#             a={"Error":"True","Message":"please enter valid sno"}
#             return JSONResponse(content=a, status_code=400)
#     except ValueError:
#         a={"Error":"True","Message":"please enter valid sno"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/Create/Activity/Report")
# def act(me:active):
#     now = datetime.now()
#     k=str(now)
#     alr_unit = Active11.objects(camp=me.Activity_type).first()
#     if alr_unit:
#         if alr_unit.status == 'Inactive':
#             sno = alr_unit.sno
#             alr_unit.delete()
#             Active11.objects(sno__gt=sno).update(dec__sno=1)    
#         else:
#             data = {"Error":"True", "Message":"Unit name already exists."}
#             return JSONResponse(content=data, status_code=400)
#     try:
#         if me.Activity_type!=""and me.created_by!="":
#             data=Active11(sno=Active11.objects.count()+1,camp=me.Activity_type,status="Active",created_by=me.created_by,Modified_by="head2",Modified_on=k,created_on=now)
#             data.save()
#             a="Successfully Submitted"
#             if a:
#                     return {"Error":"False","Message":a}
#             else:
#                 # return {"Error":"True","Message":"Data not found"}
#                 a={"Error":"True","Message":"Data not found"}
#                 return JSONResponse(content=a, status_code=400)
#         else:
#             a={"Error":"True","Message":"please enter fileds"}
#             return JSONResponse(content=a, status_code=400)
#     except Exception:
#         a={"Error":"True","Message":"please enter correct fileds"}
#         return JSONResponse(content=a, status_code=400)
            

# @app.get("/get/Activity/Report")
# def Report():
#     d=Active11.objects(status="Active").order_by("-sno").to_json()
#     f=json.loads(d)
#     data={"Error":"False","Message":"Data found","ActivityReports":[]}
#     if f:
#         for c in f:
#             k=c["created_on"]
#             timestamp = k['$date']
#             date_object = datetime.fromtimestamp(timestamp/1000)
#             formatted_date = date_object.strftime('%d-%b-%Y')
#             re={"sno":c["sno"],"Camp":c["camp"],"Status":c["status"],"Created_on":formatted_date}
#             data["ActivityReports"].append(re)
#         return data
#     else:
#         # return {"Error":"True","Message":"Data not found"}
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/search/Activity/Report")
# def Report(me:search_activity_report):
#     d=Active11.objects(sno=int(me.sno),status="Active").to_json()
#     f=json.loads(d)
#     data={"Error":"False","Message":"Data found","ActivityReports":[]}
#     if f:
#         for c in f:
#             k=c["created_on"]
#             timestamp = k['$date']
#             date_object = datetime.fromtimestamp(timestamp/1000).date()
#             formatted_date = date_object.strftime('%Y-%b-%d')
#             re={"sno":c["sno"],"Camp":c["camp"],"Status":c["status"],"Created_on":formatted_date}
#             data["ActivityReports"].append(re)
#         return data
#     else:
#         # return {"Error":"True","Message":"Data not found"}
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.put("/update_activity_Report_data")
# def update_activity_report(me:update_activity_report):
#     try:
#         new=Active11.objects(sno=me.sno).to_json()
#         new2=json.loads(new)
#         if new2:
#                 a= Active11.objects(sno=me.sno).update_one(set__camp=me.Activity_type)
#                 a="Successfully Updated"
#                 if a:
#                  return {"Error":"False","Message":a}
#                 else:
#                             # return {"Error":"True","Message":"Data not found"}
#                         a={"Error":"True","Message":"Data not found"}
#                         return JSONResponse(content=a, status_code=400)
#         else:
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
#     except ValueError:
#         a={"Error":"True","Message":"please enter valid sno"}
#         return JSONResponse(content=a, status_code=400)

# @app.put("/delete_Activity_Report")
# def get_delete_activity_report(me:delete_activity):
#     try:
#         a= Active11.objects(sno=me.sno).update_one(set__status=me.status)
#         b="Successfully Deleted"
#         if a:
#             return {"Error":"False","Message":b}
#         else:
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
#     except ValueError:
#         a={"Error":"True","Message":"please enter valid sno"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/call/submit/details")
# async def call_sub(info:Request,me:callreport):
#     in_tz = pytz.timezone('Asia/Kolkata')
#     in_time = datetime.now(in_tz)
#     in_time_str = in_time.strftime('%Y-%m-%d %H:%M')
#     a=await info.json()
#     try:
#         Lattitide=a["Lattitide"]
#         Logitude=a["Logitude"]
#         geolocator = Nominatim(user_agent="geoapiExercises")
#         location = geolocator.reverse(Lattitide+","+Logitude)
#         address = location.raw['address']
#         city=address["city"]
#         state=address["state"]
#         pincode=address["postcode"]
#         district=address["state_district"]
#         location=address["city"]
#     except ValueError:
#         # return "please enter Lattitide and Logitude values"
#         data1={"Error":"True","Message":"GPS Signal too Weak"}
#         return JSONResponse(content=data1, status_code=400)
#     now = datetime.now().date()
#     start_time1= datetime.combine(now, time(0, 0))
#     end_time1= datetime.combine(now, time(23,59))
#     type=a["type"]
#     change= type[:1].upper() + type[1:]
#     u=me.Ucid_id
#     g=Callreport.objects(Ucid_id=u,created_on__gte=start_time1,created_on__lte=end_time1).to_json()
#     gg=json.loads(g)
#     tt=None
#     def ucid_valid():
#         for f in gg:
#             if f["Ucid_id"] is not None:
#                 tt =f["Ucid_id"]
#             else:
#                 tt=None

#             return tt
#     check=ucid_valid()    
#     if change=="Call":
        
#         if all([me.Ucid_id, me.name,me.mobilenumber,me.Designation]):
#             if me.Ucid_id!=check:
#                 fe=Callreport(sno=Callreport.objects.count()+1,Ucid_id=me.Ucid_id,name=me.name,Designation=me.Designation,mobilenumber=me.mobilenumber,catagery=me.catagery,remarks=me.remarks,groupcall=me.groupcall,branch=me.branch,camp=me.camp,campdetails=me.campdetails,Lattitide=Lattitide,Logitude=Logitude,city=city,pincode=pincode,district=district,state=state,location=location,station=me.station,created_by=me.created_by,status="Active",created_on=in_time_str)
#                 fe.save()
#                 a="Successfully Submitted"
#                 return {"Error":"False","Message":a}
#             else:
#                 data1={"Error":"True","Message":"UCID is Already Existed"}
#                 return JSONResponse(content=data1, status_code=400)
#         else:
#             # return {"message": "UCID and Name and mobile number and Designation is empty"}
#             data1={"Error":"True","Message":"UCID,Name,Mobile and Designation are Empty"}
#             return JSONResponse(content=data1, status_code=400)
#     elif change=="Camp":

#         if all([me.camp,me.campdetails]):
#             fe=Callreport(sno=Callreport.objects.count()+1,Ucid_id=me.Ucid_id,name=me.name,Designation=me.Designation,mobilenumber=me.mobilenumber,catagery=me.catagery,remarks=me.remarks,groupcall=me.groupcall,branch=me.branch,camp=me.camp,campdetails=me.campdetails,Lattitide=Lattitide,Logitude=Logitude,city=city,pincode=pincode,district=district,state=state,location=location,station=me.station,created_by=me.created_by,status="Active",created_on=in_time_str)
#             fe.save()
#             a="Successfully Submited"
#             return {"Error":"False","Message":a}
#         else:
#             # return {"message": "Camp and Campdetails is empty"}
#             data1={"Error":"True","Message":"Camp and Campdetails are Empty"}
#             return JSONResponse(content=data1, status_code=400)
#     else:
#             data1={"Error":"True","Message":"Please Enter Type"}
#             return JSONResponse(content=data1, status_code=400)
# @app.post("/get_call_submit_details")
# def get_call_submit(me:get_call_report):
#     for format in ["%Y-%m-%d","%Y/%m/%d","%Y.%m.%d","%d/%m/%Y","%d-%m-%Y","%d.%m.%Y","%m/%d/%Y","%m.%d.%Y","%d-%b-%Y","%Y-%b-%d"]:
#         try:
            
#             dto=datetime.strptime(me.date, format).date()
#             start_time1= datetime.combine(dto, time(0, 0))
#             end_time1= datetime.combine(dto, time(23,59))
#             f=Callreport.objects(Q(created_on__gte=start_time1) & Q(created_on__lte=end_time1) & Q(created_by=me.emp_id)   & Q(status="Active") & Q(Ucid_id__ne="")  & Q(name__ne="")).order_by("-sno").to_json()
#             # f=Callreport.objects(created_on=dto,status="Active").to_json()
#             g=json.loads(f)
#             data={"Error":"False","Message":"Data found","call_details":[]}
#             if g:
#                 for ff in g:
#                     k=ff["created_on"]
#                     timestamp = k['$date']
#                     date_object = datetime.fromtimestamp(timestamp/1000).date()
#                     formatted_date = date_object.strftime('%Y-%b-%d')
#                     a={"sno":ff["sno"],"Ucid_id":ff["Ucid_id"],"name":ff["name"],"Designation":ff["Designation"],"mobilenumber":ff["mobilenumber"],"city":ff["city"],"district":ff["district"],"state":ff["state"],"branch":ff["branch"],"station":ff["station"],"groupcall":ff["groupcall"],"catagery":ff["catagery"],"created_by":ff["created_by"],"created_on":formatted_date,"remarks":ff["remarks"]}
#                     data["call_details"].append(a)
#                 return data
#             else:
#             # return {"Error":"True","Message":"Data not found"}
#              data1={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=data1, status_code=400)
#         except ValueError:
#             pass
# @app.post("/get_activity_submit_details")
# def get_call_submit(me:get_call_report):
#     for format in ["%Y-%m-%d","%Y/%m/%d","%Y.%m.%d","%d/%m/%Y","%d-%m-%Y","%d.%m.%Y","%m/%d/%Y","%m-%d-%Y","%m.%d.%Y","%d-%b-%Y","%Y-%b-%d"]:
#         try:
            
#             dto=datetime.strptime(me.date, format).date()
#             start_time1= datetime.combine(dto, time(0, 0))
#             end_time1= datetime.combine(dto, time(23,59))
#             # f=Callreport.objects(Q(created_on__gte=start_time1) & Q(created_on__lte=end_time1)   & Q(status="Active")).order_by("-sno").to_json()
#             f=Callreport.objects(created_on__gte=start_time1,created_on__lte=end_time1,status="Active",camp__ne="",campdetails__ne="",created_by=me.emp_id).order_by("-sno").to_json()
#             # f=Callreport.objects(created_on=dto,status="Active").to_json()
#             g=json.loads(f)
#             data={"Error":"False","Message":"Data found","call_details":[]}
#             if g:
#                 for ff in g:
#                      ddd=ff["camp"]
#                      ddd4=ff["campdetails"]
#                      k=ff["created_on"]
#                      timestamp = k['$date']
#                      date_object = datetime.fromtimestamp(timestamp/1000).date()
#                      formatted_date = date_object.strftime('%Y-%b-%d')
#                      a={"sno":ff["sno"],"camp":ddd,"campdetails":ddd4,"created_by":ff["created_by"],"created_on":formatted_date,"remarks":ff["remarks"]}
#                      data["call_details"].append(a)
#                 return data
#             else:
#             # return {"Error":"True","Message":"Data not found"}
#              data1={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=data1, status_code=400)
#         except ValueError:
#             pass

# @app.post("/Search/call/report")
# def call(me:Se):
#     if type(me.search) == str:
#         b = me.search[:2].upper() + me.search[2:]
#         result = AddMaster1.objects(Q(mobile__contains=me.search) | 
#                                     Q(Ucid_id__regex=f'^{b}') | 
#                                     Q(Agent_name__icontains=me.search) ,created_by=me.created_by).to_json()
    
#         m=json.loads(result)
#         data={"Error":"False","message":"Data found","callreport":[]}
#         if m:
#             for f in m:
#                 de={"UCID":f["Ucid_id"],"Name":f["Agent_name"],"Designation":f["Designation"],"Mobilenumber":f["mobile"],"created_by":f["created_by"]}
#                 data["callreport"].append(de)
#             return data
#         else:
#             # return {"Error":"True","Message":"Data not found"}
#             data1={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=data1, status_code=400)
# @app.put("/update_call_submit_details")
# def update_call_sub(me:update_call):
#     new=Callreport.objects(sno=me.sno).to_json()
#     new1=json.loads(new)
#     if new1:
#         new=Callreport.objects(sno=me.sno).update_one(set__name=me.name,set__Designation=me.Designation,set__mobilenumber=me.mobilenumber,set__remarks=me.remarks,set__station=me.station,set__Ucid_id=me.Ucid_id)
#         b="Successfully Submitted"
#         if b:
#                 return {"Error":"False","Message":b}
#         else:
#             a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
#     else:
#             a={"Error":"True","Message":"please enter valid sno"}
#     return JSONResponse(content=a, status_code=400)

# @app.put("/update_call_status")
# def update_call_sub(me:update_status):
#     try:
#         new=Callreport.objects(sno=me.sno).to_json()
#         new1=json.loads(new)
#         if new1:
#             new=Callreport.objects(sno=me.sno).update_one(set__status=me.status)
#             b="Successfully Deleted"
#             if b:
#                     return {"Error":"False","Message":b}
#             else:
#                 a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
#         else:
#                 a={"Error":"True","Message":"please enter valid sno"}
#         return JSONResponse(content=a, status_code=400)
#     except ValueError:
#          a={"Error":"True","Message":"please enter valid sno"}
#          return JSONResponse(content=a, status_code=400)

# @app.post("/Delete_call_report_data_{sno}")
# def delete_userdetails(call_re:del_call_reort):
#     userdetail = Callreport.objects(sno=int(call_re.sno)).first()
#     if userdetail is None:
#         return {"Error": "True", "Message": "User not found"}
#     userdetail.delete()
#     Callreport.objects(sno__gt=call_re.sno).update(dec__sno=1)
#     return {"Error": "False", "Message":"Successfully Deleted"}

# @app.post("/ADD/Revenue/Target")
# def revenue(me:adre):
#     now = datetime.now()
#     k=str(now)
#     if me.unit_name!="" and me.month_year!="":
#         data=AddRe(sno=AddRe.objects.count()+1,unicode="UN{:002d}".format(AddRe.objects.count()+1),unit_name=me.unit_name,month_year=me.month_year,target=float(me.target),Incroces=float(me.Incores),Inlaks=float(me.Inlakhs),Inthousands=float(me.Inthousands),created_by=me.created_by,created_on=k,modified_by="None",modified_on=k,status="Active")
#         data.save()
#         b="Successfully Submitted"
#         if b:
#             return {"Error":"False","Message":b}
#         else:
#          a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
#     else :
#          a={"Error":"True","Message":"please enter valied fields"}
#          return JSONResponse(content=a, status_code=400)
# @app.post("/ADD/Revenue/Target")
# def revenue(me:adre11):
#     now = datetime.now()
#     change= me.unit_name[:1].upper() + me.unit_name[1:]
#     month_now=datetime.now().month
#     year_now=datetime.now().year
#     k2=str(now)
#     start_date = datetime(year_now, month_now, 1)
#     end_date = datetime(year_now, month_now + 1, 1)
#     b=me.month_year[0].upper()+me.month_year[1:]
#     f=AddRe11.objects(status="Active",created_on__gte=start_date,created_on__lt=end_date,unit_name=me.unit_name).order_by("-sno").to_json()
#     h=json.loads(f)
#     if h:
#         a={"Error":"True","Message":"Target Is Already Exist For This Month And Branch"}
#         return JSONResponse(content=a, status_code=400)
#     else:
#         data=AddRe11(sno=AddRe11.objects.count()+1,unicode="UN{:002d}".format(AddRe11.objects.count()+1),unit_name=change,month_year=str(b),target=float(me.target),Incroces=float(me.Incores),Inlaks=float(me.Inlakhs),Inthousands=float(me.Inthousands),created_by=me.created_by,modified_by="None",modified_on=k2,status="Active",created_on=now)
#         data.save()
#         b="Successfully Submitted"
#         if b:
#             return {"Error":"False","Message":b}
#         else:
#             a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.get("/get/revenue/Target")
# def get_rev():
#     f=AddRe11.objects(status="Active").order_by("-sno").to_json()
#     h=json.loads(f)
#     data={"Error":"False","message":"Data found","RevenueTarget":[]}
#     if h:
#         for g in h:
#             ff=g["month_year"]
#             for format in ["%Y-%m","%Y-%b","%b-%Y","%m-%Y"]:
#                 try:
#                     date_obj = datetime.strptime(ff, format)
#                     month_year_str = date_obj.strftime('%b-%Y')
#                 except ValueError:
#                     pass
#             b={"SNO":g["sno"],"UnitName":g["unit_name"],"Month_Year":month_year_str,"Target":str(g["target"]),"Incroces":str(g["Incroces"]),"Inlaks":str(g["Inlaks"]),"Inthousands":str(g["Inthousands"]),"status":g["status"]}
#             data["RevenueTarget"].append(b)
#         return data
#     else:
#         # return {"Error":"True","Message":"Data not found"}
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/search/revenue/Target")
# def get_revenue(me:search_revenue_web):
#     f=AddRe11.objects(sno=me.sno,status="Active").to_json()
#     h=json.loads(f)
#     data={"Error":"False","message":"Data found","RevenueTarget":[]}
#     if h:
#         for g in h:
#             ff=g["month_year"]
#             for format in ["%Y-%m","%Y-%b","%b-%Y","%m-%Y"]:
#                 try:
#                     date_obj = datetime.strptime(ff, format)
#                     month_year_str = date_obj.strftime('%b-%Y')
#                 except ValueError:
#                     pass
#             b={"SNO":g["sno"],"UnitName":g["unit_name"],"Month_Year":month_year_str,"Target":str(g["target"]),"Incroces":str(g["Incroces"]),"Inlaks":str(g["Inlaks"]),"Inthousands":str(g["Inthousands"])}
#             data["RevenueTarget"].append(b)
#         return data
#     else:
             
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# # if type(me.search) == str:
# #         b = me.search[:2].upper() + me.search[2:]
# #         result = AddMaster1.objects(Q(mobile__regex=f'^{me.search}') | Q(Ucid_id__regex=f'^{b}') | Q(Agent_name__regex=f'^{me.search}')).to_json()
# @app.post("/search_revenue_taget_mobile")
# def revenue_terget_search(me:search_revenue1):
#     result = AddRe11.objects(unit_name__icontains=me.search,status="Active",created_by=me.created_by).to_json()
#     result1=json.loads(result)
#     data={"Error":"False","message":"Data found","RevenueTarget":[]}
#     if result1:
#         for g in result1:
#             ff=g["month_year"]
#             for format in ["%Y-%m","%Y-%b","%b-%Y","%m-%Y"]:
#                 try:
#                     date_obj = datetime.strptime(ff, format)
#                     month_year_str = date_obj.strftime('%b-%Y')
#                 except ValueError:
#                     pass
#             b={"SNO":g["sno"],"UnitName":g["unit_name"],"Month_Year":month_year_str,"Target":str(g["target"]),"Incroces":str(g["Incroces"]),"Inlaks":str(g["Inlaks"]),"Inthousands":str(g["Inthousands"]),"status":g["status"]}
#             data["RevenueTarget"].append(b)
#     return data


# @app.put("/change/Revenue/target")
# def update(me:update_revenue_data):
#     try:
#         new=AddRe11.objects(sno=int(me.sno)).to_json()
#         new1=json.loads(new)
#         if new1:
#             a= AddRe11.objects(sno=int(me.sno)).update_one(set__target=float(me.target),set__Incroces=float(me.Incores),set__Inlaks=float(me.Inlakhs),set__Inthousands=float(me.Inthousands))
#             b="Successfully Updated"
#             if b:
#                     return {"Error":"False","Message":b}
#             else:
#                 # return {"Error":"True","Message":"Data not found"}
#                 a={"Error":"True","Message":"Data not found"}
#                 return JSONResponse(content=a, status_code=400)
#         else:
#             a={"Error":"True","Message":"please enter valid sno"}
#             return JSONResponse(content=a, status_code=400)
#     except ValueError:
#         a={"Error":"True","Message":"please enter valid sno"}
#         return JSONResponse(content=a, status_code=400)
# @app.put("/change/Revenue/target/unit/status")
# def update(me:upda):
#     try:
#         new=AddRe11.objects(sno=int(me.sno)).to_json()
#         new1=json.loads(new)
#         if new1:
#             a= AddRe11.objects(sno=int(me.sno)).update_one(set__status=me.status)
#             b="Successfully Updated"
#             if b:
#                     return {"Error":"False","Message":b}
#             else:
#                 # return {"Error":"True","Message":"Data not found"}
#                 a={"Error":"True","Message":"Data not found"}
#                 return JSONResponse(content=a, status_code=400)
#         else:
#             a={"Error":"True","Message":"please enter valid sno"}
#             return JSONResponse(content=a, status_code=400)
#     except ValueError:
#         a={"Error":"True","Message":"please enter valid sno"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/ADD/Addmission/Target")
# def addmission(me:add_adimision_data):
#     # in_tz = pytz.timezone('Asia/Kolkata')
#     # in_time = datetime.now(in_tz)
#     # in_time_str = in_time.strftime('%Y-%m-%d %H:%M')
#     b=me.unit_name[:1].upper()+me.unit_name[1:]
#     now = datetime.now()
#     now1= datetime.now().date()
#     k=str(now)
#     f=AddAD.objects(status="Active",created_on=now1).order_by("-sno").to_json()
#     h=json.loads(f)
#     if h:
#         a={"Error":"True","Message":"Addmission Is Already Exist For This Day And Branch"}
#         return JSONResponse(content=a, status_code=400)
#     else:
#             if me.unit_name!=""and me.Date!="":
#                 data=AddAD(sno=AddAD.objects.count()+1,unicode="UN{:002d}".format(AddAD.objects.count()+1),unit_name=b,Date=me.Date,target=int(me.target),created_by=me.created_by,modified_by="None",modified_on=k,status="Active",created_on=now1)
#                 data.save()
#                 b="Successfully Submitted"
#                 if b:
#                         return {"Error":"False","Message":b}
#                 else:
#                     # return {"Error":"True","Message":"Data not found"}
#                     a={"Error":"True","Message":"Data not found"}
#                     return JSONResponse(content=a, status_code=400)
#             else:
#                 a={"Error":"True","Message":"please enter unit_name and Date"}
#                 return JSONResponse(content=a, status_code=400)
# @app.get("/get/Addmission/Target")
# def get_adimission():
#     f=AddAD.objects(status="Active").order_by("-sno").to_json()
#     h=json.loads(f)
#     data={"Error":"False","Message":"Data found","AddmissionTarget":[]}
#     if h:
#         for g in h:
#             date=g["Date"]
#             for format in ["%Y-%m-%d","%Y/%m/%d","%Y.%m.%d","%d/%m/%Y","%d-%m-%Y","%d.%m.%Y","%m/%d/%Y","%m-%d-%Y","%m.%d.%Y","%d-%b-%Y","%Y-%b-%d"]:
#                 try:
                    
#                     dto=datetime.strptime(date, format).date()
#                 except ValueError:
#                     pass
#             ds=dto.strftime("%d-%b-%Y")
#             b={"SNO":g["sno"],"UnitName":g["unit_name"],"Date":ds,"Target":str(g["target"]),"status":g["status"]}
#             data["AddmissionTarget"].append(b)
#         return data
#     else:
#         # return {"Error":"True","Message":"Data not found"}
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/search_admission_mobile")
# def revenue_terget_search(me:search_adimission):
#         result = AddAD.objects(unit_name__icontains=me.search,status="Active",created_by=me.created_by).to_json()
#         result1=json.loads(result)
#         data={"Error":"False","message":"Data found","AddmissionTarget":[]}
#         if result1:
#             for g in result1:
#                 aaa=g["Date"]
#                 b={"SNO":g["sno"],"UnitName":g["unit_name"],"Date":g["Date"],"Target":str(g["target"]),"status":g["status"]}
#                 data["AddmissionTarget"].append(b)
#         return data
# @app.post("/search/Addmission/Target/data")
# def get_adimission_data(me:search_adimission_data):
#     f=AddAD.objects(sno=me.sno,status="Active").to_json()
#     h=json.loads(f)
#     data={"Error":"False","Message":"Data found","AddmissionTarget":[]}
#     if h:
#         for g in h:
#             # k=g["Date"]
#             # timestamp = k['$date']
#             # date_object = datetime.fromtimestamp(timestamp/1000).date()
#             b={"SNO":g["sno"],"UnitName":g["unit_name"],"Date":g["Date"],"Target":g["target"]}
#             data["AddmissionTarget"].append(b)
#         return data
#     else:
#         # return {"Error":"True","Message":"Data not found"}
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.put("/change/Addmission/target")
# def update(me:update_adimission_data):
#     try:
#         new=AddAD.objects(sno=int(me.sno)).to_json()
#         new1=json.loads(new)
#         if new1:
#             a= AddAD.objects(sno=int(me.sno)).update_one(set__target=float(me.target))
#             b="Successfully Updated"
#             if b:
#                     return {"Error":"False","Message":b}
#             else:
#                 # return {"Error":"True","Message":"Data nt found"}
#                 a={"Error":"True","Message":"Data not found"}
#                 return JSONResponse(content=a, status_code=400)
#         else :
#             a={"Error":"True","Message":"please enter valid sno"}
#             return JSONResponse(content=a, status_code=400)
#     except ValueError:
#         a={"Error":"True","Message":"please enter valid sno"}
#         return JSONResponse(content=a, status_code=400)

# @app.put("/change/Addmission/target/unit/status")
# def update(me:adiupda):
#     try:
#         new=AddAD.objects(sno=int(me.sno)).to_json()
#         new1=json.loads(new)
#         if new1:
#             a= AddAD.objects(sno=int(me.sno)).update_one(set__status=me.status)
#             b="Successfully Updated"
#             if b:
#                     return {"Error":"False","Message":b}
#             else:
#                 # return {"Error":"True","Message":"Data not found"}
#                 a={"Error":"True","Message":"Data not found"}
#                 return JSONResponse(content=a, status_code=400)
#         else :
#             a={"Error":"True","Message":"please enter valid sno"}
#             return JSONResponse(content=a, status_code=400)
#     except ValueError:
#         a={"Error":"True","Message":"please enter valid sno"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/Create/Camp/Data")
# def cam(me:camp):
#     now = datetime.now()
#     k=str(now)
#     # in_tz = pytz.timezone('Asia/Kolkata')
#     # in_time = datetime.now(in_tz)
#     # in_time_str = in_time.strftime('%Y-%m-%d %H:%M')
#     f=Camp.objects(Q(status="Start")  & Q(created_by=me.created_by)).to_json()
#     g=json.loads(f)
#     if g:
#         a={"Error":"True","Message":"Please Stop Already Existed Camp"}
#         return JSONResponse(content=a, status_code=400)
#     else :
#         da=Camp(sno=Camp.objects.count()+1,TransID="CAMP{:002d}".format(Camp.objects.count()+1),state=me.state,city=me.city,Area=me.Area,location=me.location,campname=me.campname,created_by=me.created_by,modified_by="head",modified_on=k,status="Start",created_on=now)
#         da.save()
#         ad=da.TransID
#         b="Successfully Created"
#         if b:
#             return {"Error":"False","Message":b,"CAMPID":ad}
#         else:
#             # return {"Error":"True","Message":"Data not found"}
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)

    
# @app.post("/Get/Camp")
# def empn(me:campdate):
#     da=me.from_date
#     da1=me.to_date
#     for format in ["%Y-%m-%d","%Y/%m/%d","%Y.%m.%d","%d/%m/%Y","%d-%m-%Y","%d.%m.%Y","%m/%d/%Y","%m-%d-%Y","%m.%d.%Y","%d-%b-%Y","%Y-%b-%d"]:
#             try:
#                 dto=datetime.strptime(da, format)
#                 dto1=str(dto)
#                 d=datetime.strptime(da1, format)
#                 d22=datetime.strptime(da1, format)
#                 d1=str(d)
#                 dto22=datetime.strptime(me.to_date,format)+timedelta(days=1)
#                 dto221=str(dto22)
#                 start_time1= datetime.combine(dto, time(0, 0))
#                 end_time1= datetime.combine(dto, time(23,59))
#                 if dto1!=dto22:
#                     f=Camp.objects(created_by=me.emp_id,created_on__gte=dto1,created_on__lte=dto22).order_by("-sno").to_json()
#                     g=json.loads(f)
#                 else:
#                      f=Camp.objects(created_by=me.emp_id,created_on__gte=start_time1,created_on__lte=end_time1).order_by("-sno").to_json()
#                      g=json.loads(f)
                
#                 data={"Error":"False","Message":"Data found","Campdetails":[]}
#                 if g:
#                     for k in g:
#                         g=k["created_on"]
#                         timestamp = g['$date']
#                         date_object = datetime.fromtimestamp(timestamp/1000).date()
#                         formatted_date = date_object.strftime('%d-%b-%Y')
#                         ds={"SNO":k["sno"],"CampID":k["TransID"],"State":k["state"],"City":k["city"],"Area":k["Area"],"Campname":k["campname"],"Date":formatted_date,"Status":k["status"]}
#                         data["Campdetails"].append(ds)
#                     return data
#                 else:
#                     # return {"Error":"True","Message":"Data not found"}
#                     a={"Error":"True","Message":"Data not found"}
#                     return JSONResponse(content=a, status_code=400)
#             except ValueError:
#                 pass

# @app.put("/update/Camp/status")
# def update(me:updatecamp):
#     b1= me.status[:1].upper() + me.status[1:]
#     f=Camp.objects(created_by=me.emp_id,TransID=me.TransID).to_json()
#     g=json.loads(f)
#     if g:
#         a= Camp.objects(created_by=me.emp_id,TransID=me.TransID).update_one(set__status=b1)
#         b="Successfully Updated"
#         if b:
#                 return {"Error":"False","Message":b}
#         else:
#             # return {"Error":"True","Message":"Data not found"}
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
#     else:
#         a={"Error":"True","Message":"Please check Details"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/Create/Enroll/Registration")
# def enroll(me:enrol):
#     # in_tz = pytz.timezone('Asia/Kolkata')
#     # in_time = datetime.now(in_tz)
#     # in_time_str = in_time.strftime('%Y-%m-%d %H:%M')
#     now = datetime.now()
#     k=str(now)
#     a=Camp.objects(TransID=me.TransID,status="Start").to_json()
#     b=json.loads(a)
#     ti={"Error":"False","Message":"Data found","Enroll":[]}
#     try:
#         for mn in b:
#             de=mn["status"]
#         if de=="Start":
#             if me.Patient_name!="" and me.Age!=0:
#                 en=Enrol(sno=Enrol.objects.count()+1,TransID=me.TransID,Patient_name=me.Patient_name,Age=int(me.Age),mobile=me.mobile,Remarks=me.Remarks,created_by=me.created_by,status="Active",created_on=now)
#                 en.save()
#                 b="Successfully Submitted"
#                 return {"Error":"False","Message":b}
#             else:
#                 b="please enter patient_name and age"
#                 return {"Error":"False","Message":b}
#         elif de=="Stop":
#             # return {"Error":"True","Message":"Data not found"}
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
            
#     except:ValueError
#     # return {"Error":"True","Message":"Campclosed"}
#     a={"Error":"True","Message":"Campclosed"}
#     return JSONResponse(content=a, status_code=400)
# @app.post("/get/Enroll/Registration")
# def Enroll(me:enrolme):
#     data={"Error":"False","Message":"Data found","Enroll":[]}
#     g=Enrol.objects(TransID=me.TransID,status="Active").order_by("-sno").to_json()
#     f=json.loads(g)
#     if f :
#         for fd in f:
#             # g=fd["created_on"]
#             # timestamp = g['$date']
#             # date_object = datetime.fromtimestamp(timestamp/1000).date()
#             # formatted_date = date_object.strftime('%Y-%b-%d')
#             a2=fd["mobile"]
#             g=fd["created_on"]
#             timestamp = g['$date']
#             date_object = datetime.fromtimestamp(timestamp/1000).date()
#             formatted_date = date_object.strftime('%d-%b-%Y')
#             formatted_number = a2[:1] + "*******" + a2[-2:]
#             a={"SNO":fd["sno"],"TransID":fd["TransID"],"Patientname":fd["Patient_name"],"Age":fd["Age"],"Mobile":formatted_number,"Remarks":fd["Remarks"],"created_by":fd["created_by"],"created_on":formatted_date}
#             data["Enroll"].append(a)
#         return data
#     else:
#         # return {"Error":"True","Message":"Data not found"}
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/search/Enroll/Registration")
# def Search_enrol_data(me:search_enrol_dta):
#     data={"Error":"False","Message":"Data found","Enroll":[]}
#     g=Enrol.objects(sno=me.sno).to_json()
#     f=json.loads(g)
#     if f :
#         for fd in f:
#             g=fd["created_on"]
#             timestamp = g['$date']
#             date_object = datetime.fromtimestamp(timestamp/1000).date()
#             formatted_date = date_object.strftime('%d-%b-%Y')
#             a2=fd["mobile"]
#             formatted_number = a2[:1] + "*******" + a2[-2:]
#             a={"SNO":fd["sno"],"TransID":fd["TransID"],"Patientname":fd["Patient_name"],"Age":fd["Age"],"Mobile":formatted_number,"Remarks":fd["Remarks"],"created_by":fd["created_by"],"created_on":formatted_date}
#             data["Enroll"].append(a)
#         return data
#     else:
#         # return {"Error":"True","Message":"Data not found"}
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.put("/update_enrol_registration")
# def change_enrol_reg(me:update_enrol_data):
#     try:
#         new=Enrol.objects(sno=int(me.sno)).to_json()
#         new1=json.loads(new)
#         if new1:
#             data=Enrol.objects(sno=int(me.sno)).update_one(set__Patient_name=me.Patient_name,set__mobile=me.mobile,set__Age=int(me.age),set__Remarks=me.Remarks)
#             b="Successfully Updated"
#             if b:
#                     return {"Error":"False","Message":b}
#             else:
#                 # return {"Error":"True","Message":"Data not found"}
#                 a={"Error":"True","Message":"Data not found"}
#                 return JSONResponse(content=a, status_code=400)
#         else:
#             a={"Error":"True","Message":"please enter valid sno"}
#             return JSONResponse(content=a, status_code=400)
#     except ValueError:
#          a={"Error":"True","Message":"please enter valid sno"}
#          return JSONResponse(content=a, status_code=400)
# @app.put("/update_enrol_registration_status")
# def change_enrol_reg(me:update_enrol_status):
#     try:
#         new=Enrol.objects(sno=me.sno).to_json()
#         new1=json.loads(new)
#         if new1:
#             data=Enrol.objects(sno=me.sno).update_one(set__status=me.status)
#             b="Successfully Updated"
#             if b:
#                     return {"Error":"False","Message":b}
#             else:
#                 # return {"Error":"True","Message":"Data not found"}
#                 a={"Error":"True","Message":"Data not found"}
#                 return JSONResponse(content=a, status_code=400)
#         else:
#             a={"Error":"True","Message":"please enter valid sno"}
#             return JSONResponse(content=a, status_code=400)
#     except ValueError:
#         a={"Error":"True","Message":"please enter valid sno"}
#         return JSONResponse(content=a, status_code=400)


# @app.post("/Create/area/names")
# def areas(me:area):
#     a=Areas(Location=me.Location,Pincode=me.Pincode,State=me.State,District=me.District,areacode=me.areacode)
#     a.save()
#     b="Successfully Updated"
#     return {"Error":"False","Message":b}
# @app.post("/get/area/lists")
# def area_list(me:Location):
#     if type(me.city) == str:
#         b = me.city[:1].upper() + me.city[1:]
#     d=Areas.objects.filter(Q(District=b)).to_json()
#     g=json.loads(d)
#     data={"Error":"False","Message":"Data found","Areas":[]}
#     if g:
#         for s in g:
#             a={"Area":s["Location"],"areacode":s["areacode"]}
#             data["Areas"].append(a)
#         return data
#     else:
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/add/city/names")
# def citys(me:city):
#     s=Cityes2(sno=Cityes2.objects.count()+1,State=me.State,City=me.City,city_code=me.city_code)
#     s.save()
#     b="Successfully Created"
#     if b:
#             return {"Error":"False","Message":b}
#     else:
#         # return {"Error":"True","Message":"Data not found"}
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/get/city")
# def cites(me:state):
#     a=Cityes2.objects(State=me.state).to_json()
#     f=json.loads(a)
#     data={"Error":"False","Message":"Data found","city":[]}
#     if f:
#         for g in f:
#             a=g["City"]
#             # data["city"].append(a)
#             a={"city":g["City"],"Citycode":g["city_code"]}
#             data["city"].append(a)
#         return data
#     else:
#         # return {"Error":"True","Message":"Data not found"}
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/create/cluster/data")
# def clusters(me:cluster):
#     b = me.cluster_name[:1].upper() + me.cluster_name[1:]
#     alr= Cluster1.objects(cluster_name=me.cluster_name).first()
#     if alr:
#         if alr.status == 'Inactive':
#             alr.status = 'Active'
#             alr.save()
#         else:
#             data = {"Error":"True", "Message":"Cluster name already exists."}
#             return JSONResponse(content=data, status_code=400)
#     else:
#         new=Cluster1(sno=Cluster1.objects.count()+1,cluster_code="CLU{:002d}".format(Cluster1.objects.count()+1),cluster_name=b,address=me.address,status="Active")
#         new.save()
#     b="Successfully Created"
#     if b:
#         return {"Error":"False","Message":b}
#     else:
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)

# @app.post("/create/cluster/data")
# b = me.cluster_name[:1].upper() + me.cluster_name[1:]
# def clusters(me:cluster):
#     if all([me.cluster_name, me.address]):
#         new=Cluster(sno=Cluster.objects.count()+1,cluster_code="CLU{:002d}".format(Cluster.objects.count()+1),cluster_name=me.cluster_name,address=me.address,status="Active")
#     else :
#         a={"Error":"True","Message":"please enter details"}
#         return JSONResponse(content=a, status_code=400)
#     new.save()
#     b="Successfully Created"
#     if b:
#             return {"Error":"False","Message":b}
#     else:
#         # return {"Error":"True","Message":"Data not found"}
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.get("/get/cluster/data")
# def clusters():
#     clu=Cluster1.objects(status="Active").order_by("-sno").to_json()
#     clus=json.loads(clu)
#     data={"Error":"False","Message":"Data found","Clusters":[]}
#     if clus:
#         for cl in clus:
#             a={"Sno":cl["sno"],"cluster_code":cl["cluster_code"],"cluster_name":cl["cluster_name"],"address":cl["address"],"status":cl["status"]}
#             data["Clusters"].append(a)
#         return data
#     else:
#         # return {"Error":"True","Message":"Data not found"}
#         a={"Error":"True","Message":"Data not found"}
#     return JSONResponse(content=a, status_code=400)
# @app.post("/search_cluster_mobile")
# def search_cluster_data(me:cluster_search_mobile):
#         result = Cluster1.objects(cluster_name__icontains=me.search,status="Active").to_json()
#         result1=json.loads(result)
#         data={"Error":"False","message":"Data found","Clusters":[]}
#         for cl in result1:
#             a={"Sno":cl["sno"],"cluster_code":cl["cluster_code"],"cluster_name":cl["cluster_name"],"address":cl["address"],"status":cl["status"]}
#             data["Clusters"].append(a)
#         return data
# @app.post("/search/cluster/data")
# def search_cluster_data(me:search_cluster):
#     clu=Cluster1.objects(sno=me.sno,status="Active").to_json()
#     clus=json.loads(clu)
#     data={"Error":"False","Message":"Data found","Clusters":[]}
#     if clus:
#         for cl in clus:
#             a={"Sno":cl["sno"],"cluster_code":cl["cluster_code"],"cluster_name":cl["cluster_name"],"address":cl["address"],"status":cl["status"]}
#             data["Clusters"].append(a)
#         return data
#     else:
#         # return {"Error":"True","Message":"Data not found"}
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.put("/update_cluster_data")
# def update_cluster(me:update_cluster_data):
#     try:
#         a= Cluster1.objects(sno=me.sno).update_one(set__cluster_name=me.cluster_name,set__address=me.address)
#         b="Successfully Updated"
#         if b:
#                 return {"Error":"False","Message":b}
#         else:
#             # return {"Error":"True","Message":"Data not found"}
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
#     except:
#         a={"Error":"True","Message":"please enter valid sno"}
#         return JSONResponse(content=a, status_code=400)

# @app.put("/delete_cluster_unit")
# def delete_cluster(me:delete_cluster_data):
#     new=Cluster1.objects(cluster_code=me.cluster_code).to_json()
#     new1=json.loads(new)
#     if new1:
#         a= Cluster1.objects(cluster_code=me.cluster_code).update_one(set__status=me.status)
#         b="Successfully Updated"
#         if b:
#                 return {"Error":"False","Message":b}
#         else:
#             # return {"Error":"True","Message":"Data not found"}
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
#     else:
#         a={"Error":"True","Message":"please enter valid code"}
#         return JSONResponse(content=a, status_code=400)

# @app.get("/get_cluster_counts")
# def get_cluster():
#      u=Cluster1.objects().count()
#      v=Cluster1.objects(status="Active").count()
#      w=Cluster1.objects(status="Inactive").count()
#      a={"Total_clusters":u,"Active_clusters":v,"Inactive_clusters":w}
#      if a:
#          data1={"Error":"False","Message":"Data found","Counts":[]}
#          data1["Counts"].append(a)
#          return data1
#      else:
#         n={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=n, status_code=400)

# @app.post("/create/refer/patient")
# def refer(me:referpatient):
#     # in_tz = pytz.timezone('Asia/Kolkata')
#     # in_time = datetime.now(in_tz)
#     # in_time_str = in_time.strftime('%Y-%m-%d %H:%M')
#     try:
#         id=int(me.emp_id)
#     except ValueError:
#         a={"Error":"True","Message":"Please Check Employe_id"}
#         return JSONResponse(content=a, status_code=400)

#     uc_id=me.Ucid
#     now = datetime.now().date()
#     k=str(now)
#     user=Usercreate.objects(Employee_id=id).to_json()
#     master=AddMaster1.objects(Ucid_id=uc_id).to_json()
#     ma1=json.loads(master)
#     user1=json.loads(user)
#     if user1 and ma1:
#         for u,v in zip(user1,ma1):
#             d=u["User_name"]
#             f1=u["mobile_number"]
#             f2=u["Branch"]
#             e=v["Agent_name"]
#             f=v["mobile"]
#             new=Referpatient(sno=Referpatient.objects.count()+1,patient_name=me.patient_name,patient_mobile=me.patient_mobile,executive_name=d,Ucid=me.Ucid,Ucid_name=e,conslutant=me.conslutant,speciality=me.speciality,remarks=me.remarks,Ipno="none",mapped_by="none",mapped_on="none",status="Pending",created_by=me.created_by,branch=f2,agent_mobile=f,executive_mobile=f1,created_on=now)
#             new.save()
#         a={"Error":"False","Message":"Successfully Submitted"}
#         return JSONResponse(content=a, status_code=200)
#     else:
#         # return {"Error":"True","Message":"Data not found"}
#         a={"Error":"True","Message":"Please Check Entered Ucid"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/get/the/refer/patient/data")
# def get_refer(me:reget):
#     da=me.from_date
#     da1=me.to_date
#     if da and da1 not in["","string"]:
#         for format in ["%Y-%m-%d","%Y/%m/%d","%Y.%m.%d","%d/%m/%Y","%d-%m-%Y","%d.%m.%Y","%m/%d/%Y","%m-%d-%Y","%m.%d.%Y","%d-%b-%Y","%Y-%b-%d"]:
#             try:
#                 dto=datetime.strptime(da, format).date()
#                 dto1=str(dto)
#                 d=datetime.strptime(da1, format).date()
#                 d=datetime.strptime(da1, format).date()
#                 d22=datetime.strptime(da1, format)
#                 d1=str(d)
#                 dto22=datetime.strptime(me.to_date,format)+timedelta(days=1)
#                 if dto!=d:
#                     f=Referpatient.objects(Q(created_on__gte=dto1) & Q(created_on__lte=d1) & Q(created_by=str(me.emp_id)) & Q(status="Pending")).order_by("-sno").to_json()
#                     g=json.loads(f)
#                 else:
#                     print("dd")
#                     f=Referpatient.objects(Q(created_on__gte=dto1) & Q(created_on__lt=dto22) & Q(status="Pending") & Q(created_by=str(me.emp_id))).order_by("-sno").to_json()
#                     g=json.loads(f)
#                 data1={"Error":"False","Message":"Data found","patient":[]}
#                 if g:
#                         for ff in g:
#                             g=ff["created_on"]
#                             timestamp = g['$date']
#                             date_object = datetime.fromtimestamp(timestamp/1000).date()
#                             formatted_date = date_object.strftime('%d-%b-%Y')
#                             a={"sno":ff["sno"],"patient_name":ff["patient_name"],"patient_mobile":ff["patient_mobile"],"executive_name":ff["executive_name"],"Agent_name":ff["Ucid_name"],"Ucid":ff["Ucid"],"conslutant":ff["conslutant"],"speciality":ff["speciality"],"remarks":ff["remarks"],"emp_id":ff["created_by"],"branch":ff["branch"],"executive_mobile":str(ff["executive_mobile"]),"agent_mobile":ff["agent_mobile"],"Ipno":ff["Ipno"],"mapped_by":ff["mapped_by"],"mapped_on":ff["mapped_on"],"created_by":ff["created_by"],"created_on":formatted_date,"status":ff["status"]}
#                             data1["patient"].append(a)
#                         return data1
#                 else:
#                     a={"Error":"True","Message":"Data not found"}
#                     return JSONResponse(content=a, status_code=400)
#             except ValueError:
#                 pass
#     # else:
#     #     a={"Error":"True","Message":"Please enter from_date and to_date "}
#     #     return JSONResponse(content=a, status_code=400)
# @app.post("/search/the/refer/patient/data")
# def get_refer(me:search_refer_patient):
#     f=Referpatient.objects(sno=me.sno).to_json()
#     g=json.loads(f)
#     data1={"Error":"False","Message":"Data found","patient":[]}
#     if g:
#         for ff in g:
#             g=ff["created_on"]
#             timestamp = g['$date']
#             date_object = datetime.fromtimestamp(timestamp/1000).date()
#             formatted_date = date_object.strftime('%d-%b-%Y')
#             a={"sno":ff["sno"],"patient_name":ff["patient_name"],"patient_mobile":ff["patient_mobile"],"executive_name":ff["executive_name"],"Agent_name":ff["Ucid_name"],"Ucid":ff["Ucid"],"conslutant":ff["conslutant"],"speciality":ff["speciality"],"remarks":ff["remarks"],"emp_id":ff["created_by"],"branch":ff["branch"],"executive_mobile":str(ff["executive_mobile"]),"agent_mobile":ff["agent_mobile"],"Ipno":ff["Ipno"],"mapped_by":ff["mapped_by"],"mapped_on":ff["mapped_on"],"created_by":ff["created_by"],"created_on":formatted_date,"status":ff["status"]}
#             data1["patient"].append(a)
#         return data1
#     else:
#      a={"Error":"True","Message":"Data not found"}
#     return JSONResponse(content=a, status_code=400)
# @app.post("/search_patient_data_mobile")
# def search_patient_data(me:search_patient):
#     result = Referpatient.objects(Q(patient_name__icontains=me.search) | Q(patient_mobile__icontains=me.search) | Q(Ucid__icontains=me.search),created_by=me.created_by).order_by("-sno").to_json()
#     result1=json.loads(result)
#     data1={"Error":"False","Message":"Data found","patient":[]}
#     if result1:
#         for ff in result1:
#             g=ff["created_on"]
#             timestamp = g['$date']
#             date_object = datetime.fromtimestamp(timestamp/1000).date()
#             formatted_date = date_object.strftime('%d-%b-%Y')
#             a={"sno":ff["sno"],"patient_name":ff["patient_name"],"patient_mobile":str(ff["patient_mobile"]),"executive_name":ff["executive_name"],"Agent_name":ff["Ucid_name"],"Ucid":ff["Ucid"],"conslutant":ff["conslutant"],"speciality":ff["speciality"],"remarks":ff["remarks"],"branch":ff["branch"],"executive_mobile":str(ff["executive_mobile"]),"agent_mobile":ff["agent_mobile"],"Ipno":ff["Ipno"],"mapped_by":ff["mapped_by"],"mapped_on":ff["mapped_on"],"created_by":ff["created_by"],"created_on":formatted_date,"status":ff["status"]}
#             data1["patient"].append(a)
#         return data1
    
#     else:
             
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)

# @app.put("/update_patient/data")
# def update_patient_data1(me:update_patient_data):
#     try:
#         new=Referpatient.objects(sno=int(me.sno)).to_json()
#         new1=json.loads(new)
#         if new1:
#             a= Referpatient.objects(sno=int(me.sno)).update_one(set__patient_name=me.patient_name,set__patient_mobile=me.patient_mobile,set__conslutant=me.conslutant,set__speciality=me.speciality,set__remarks=me.remarks)
#             b="Successfully Updated"
#             if b:
#                     return {"Error":"False","Message":b}
#             else:
#                 # return {"Error":"True","Message":"Data nt found"}
#                 a={"Error":"True","Message":"Data not found"}
#                 return JSONResponse(content=a, status_code=400)
#         else:
#             a={"Error":"True","Message":"please enter valid sno"}
#             return JSONResponse(content=a, status_code=400)
#     except ValueError:
#         a={"Error":"True","Message":"please enter valid sno"}
#         return JSONResponse(content=a, status_code=400)
# @app.put("/update_patient_status")
# def update_patient_data(me:update_refer_patient_status):
#     try:
#         new=Referpatient.objects(sno=me.sno).to_json()
#         new1=json.loads(new)
#         if new1:
#             a= Referpatient.objects(sno=me.sno).update_one(set__status=me.status)
#             b="Successfully Updated"
#             if b:
#                     return {"Error":"False","Message":b}
#             else:
#                 # return {"Error":"True","Message":"Data nt found"}
#                 a={"Error":"True","Message":"Data not found"}
#                 return JSONResponse(content=a, status_code=400)
#         else:
#             a={"Error":"True","Message":"please enter valid sno"}
#             return JSONResponse(content=a, status_code=400)
#     except ValueError:
#         a={"Error":"True","Message":"please enter valid sno"}
#         return JSONResponse(content=a, status_code=400)

# @app.get("/get/department")
# def consul():
#     a=Consultant.objects().to_json()
#     b=json.loads(a)
#     data1={"Error":"False","Message":"Data found","Department":[]}
#     if b:
#         for ff in b:
#             a1={"department":ff["department"]}
#             data1["Department"].append(a1)
#         return data1
#     else:
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/ADD/consultant/")
# def consul(me:consultant):
#     new=Consultant(sno=Consultant.objects.count()+1,consultant=me.consultant,department=me.department)
#     new.save()
#     a={"Error":"False","Message":"Successfully Submitted"}
#     if a:
#         return JSONResponse(content=a, status_code=200)
#     else:
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/get/consultant")
# def consul(me:department):
#     a=Consultant.objects(department=me.department_name).to_json()
#     b=json.loads(a)
#     data1={"Error":"False","Message":"Data found","Consultant":[]}
#     if b:
#         for ff in b:
#             a1={"consultant":ff["consultant"]}
#             data1["Consultant"].append(a1)
#         return data1
#     else:
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)


# @app.post("/get/my/team/report")
# async def add_records(me:myteamre):
#         date_only=me.date
#         for format in ["%Y-%m-%d","%Y/%m/%d","%Y.%m.%d","%d/%m/%Y","%d-%m-%Y","%d.%m.%Y","%m/%d/%Y","%m-%d-%Y","%m.%d.%Y","%d-%b-%Y","%Y-%b-%d"]:

#             try:
#                 dto=datetime.strptime(me.date,format)
#                 # dto1=datetime.strptime(dd,format).datetime()
#                 date_only = datetime.combine(dto, datetime.min.time())
#             except ValueError:
#                 pass
#         gg=Usercreate.objects(Reporting_Manager=me.reporting_manager).to_json()
#         ggg=json.loads(gg)
#         if ggg:
#             data1={"Error":"False","Message":"Data found","Teamreports":[]}
#             for ff in ggg:
#                 dan=ff["Employee_id"]
#                 dan2=ff["Reporting_Manager"]
#                 dan3=ff["User_name"]
#                 start_time1= datetime.combine(dto, time(0, 0))
#                 end_time1= datetime.combine(dto, time(16,00))
#                 start_time2= datetime.combine(dto, time(16, 1))
#                 end_time2= datetime.combine(dto, time(23, 59))
#                 start_time3= datetime.combine(dto, time(0, 0))
#                 end_time3= datetime.combine(dto, time(23, 59))
#                 rr=Callreport.objects(created_on__gte=start_time1,created_on__lte=end_time1,created_by=str(dan)).count()
#                 r=Callreport.objects(created_on__gte=start_time2,created_on__lte=end_time2,created_by=str(dan)).count()
#                 # pipeline = [{"$match": {"camp": {"$ne": "String","$ne":""}}},{"$group": {"_id": "$camp", "count": {"$sum": 1}}},{"$group": {"_id": None, "total_count": {"$sum": 1}}}]
#                 #call count ucid
#                 r1=Callreport.objects(created_on__gte=start_time3,created_on__lte=end_time3,created_by=str(dan),Ucid_id__ne="").count()
#                 r2=Callreport.objects(created_on__gte=start_time3,created_on__lte=end_time3,created_by=str(dan),camp__ne="").count()
#                 aaa={"EMP_id":dan,"Name":dan3,"Reporting_manager":dan2,"First_Half":rr,"Second_Half":r,"Callcount":r1,"Activitycount":r2}
#                 data1["Teamreports"].append(aaa)
#             return data1
#         else:
#                 a={"Error":"True","Message":"Data not found"}
#                 return JSONResponse(content=a, status_code=400)

        

# @app.post("/get/Team/coverage")
# def gf(me:getre):
#     id=me.Reporting_manager_id
#     for format in ["%Y-%m","%Y/%m","%m-%Y","%m.%Y","%m/%Y","%b-%Y","%Y-%b"]:

#             try:
#                 dto1=datetime.strptime(me.month_year,format)
#                 dto2=datetime.strptime(me.month_year,format).year
#                 dto3=datetime.strptime(me.month_year,format).month
#                 # end_date = (datetime(dto2, dto3 + 1, 1) - timedelta(days=1))
#                 if dto3<=11:
#                     end_date = (datetime(dto2, dto3 + 1, 1) - timedelta(days=1))
#                 else:
#                     end_date = (datetime(dto2, 1, 1) - timedelta(days=1))

#             except ValueError:
#                 pass
#     a=Usercreate.objects(Reporting_Manager=str(id),Role_Code="Executive",Active_Status="Active").to_json()
#     a1=json.loads(a)
#     data2={"Error":"False","Message":"Data found","Teamreport":[]}
#     if a1:
#         for d in a1:
#             dd=d["Employee_id"]
#             dd1=d["User_name"]
#             a=Callreport.objects(created_by=str(dd),created_on__gte=dto1,created_on__lte=end_date,Ucid_id__ne="").count()
#             new1=AddMaster1.objects(created_by=str(dd),created_on__gte=dto1,created_on__lte=end_date,Ucid_id__ne="").count()
#             new3=Callreport.objects(created_by=str(dd),created_on__gte=dto1,created_on__lte=end_date,Ucid_id__ne="").distinct('Ucid_id')
#             call_count=len(new3)
#             Not_visit=new1-call_count
#             af={"Emp_id":dd,"Name":dd1,"call_count":a,"Master_count":new1,"unique_call_count_ucid":call_count,"Not_visit":Not_visit,"v1":a,"v2":0,"v3":0}
#             data2["Teamreport"].append(af)
#         return data2
#     else:
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)

# @app.post("/get_my_team_report_mkh")
# def mar(me:marketing):
#     for format in ["%Y-%m-%d","%Y/%m/%d","%Y.%m.%d","%d/%m/%Y","%d-%m-%Y","%d.%m.%Y","%m/%d/%Y","%m-%d-%Y","%m.%d.%Y","%d-%b-%Y","%Y-%b-%d"]:

#             try:
#                 dto=datetime.strptime(me.from_date,format).date()
#                 dto1=datetime.strptime(me.to_date,format).date()
#                 date_only = datetime.combine(dto, datetime.min.time())
#                 start_time1= datetime.combine(dto, time(0, 0))
#                 end_time1= datetime.combine(dto, time(16,00))
#             except ValueError:
#                 pass
#     bre=me.Branch
#     change= bre[:1].upper() + bre[1:]
#     a=Usercreate.objects(Branch=change,Role_Code__in=["Manager", "Executive"],Active_Status="Active").to_json()
#     b=json.loads(a)
#     if b :
#         data1={"Error":"False","Message":"Data found","Marketing":[]}
#         for c in b:
#             h=c["Employee_id"]
#             gg=c["User_name"]
#             mm=c["Reporting_Manager"]
#             rc=c["Role_Code"]
#             if dto!=dto1:
#                 vv=Camp.objects(created_by=str(h),created_on__gte=dto,created_on__lte=dto1).count()
#                 uu=Enrol.objects(created_by=str(h),created_on__gte=str(dto),created_on__lte=str(dto1)).count()
#             else:
#                 vv=Camp.objects(created_by=str(h),created_on__gte=start_time1,created_on__lte=end_time1).count()
#                 uu=Enrol.objects(created_by=str(h),created_on__gte=str(start_time1),created_on__lte=str(end_time1)).count()
#             aaa={"Emp_id":h,"Name":gg,"Camp_counts":vv,"Reporting_Manager":mm,"Enrol_counts":uu,"Role":rc}
#             data1["Marketing"].append(aaa)
#         return data1
#     else:
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
# # @app.post("/get_my_team_report_mkh_list")
# # def mar(me:marketing):
# #     dto = datetime.strptime(me.from_date, "%Y-%m-%d")
# #     dto1 = datetime.strptime(me.to_date, "%Y-%m-%d") + timedelta(days=1)
# #     bre = me.Branch
# #     change = bre[:1].upper() + bre[1:]
# #     manager_data = Usercreate.objects(Branch=change, Role_Code__in=["Manager", "Executive"], Active_Status="Active").as_pymongo()
# #     if not manager_data:
# #         return {"Error": "True", "Message": "No data found"}
# #     result = {"Error": "False", "Message": "Data found", "Marketing": []}
# #     for manager in manager_data:
# #         employee_id = manager["Employee_id"]
# #         User_name=manager["User_name"]
# #         camp_data = Camp.objects(created_by=str(employee_id), created_on__gte=dto, created_on__lt=dto1).order_by("-sno").as_pymongo()
# #         enrol_data = Enrol.objects(created_by=str(employee_id), created_on__gte=dto, created_on__lt=dto1).order_by("-sno").as_pymongo()
# #         for camp in camp_data:
            
# #             for enrol in enrol_data:
# #                 if camp and enrol_data:
# #                     camps_str = camp["TransID"]
# #                     camp_names_str = camp["campname"]
# #                     Enroll = enrol["Patient_name"]
# #                 else:
# #                     camps_str = "Null"
# #                     camp_names_str = "Null"
# #                     Enroll = "Null"
# #                 result["Marketing"].append({
# #                     "Employee_id": employee_id,
# #                     "User_name": User_name,
# #                     "camps": camps_str,
# #                     "Date": camp["created_on"],
# #                     "camp_names": camp_names_str,
# #                     "patients": Enroll
# #                 })

# #     if not result["Marketing"]:
# #         a={"Error":"True","Message":"Data not found"}
# #         return JSONResponse(content=a,status_code=400)
# #     else:
# #         return result





# @app.post("/get/Team/camp/registration/list")
# def mar(me:marketing1):
#     for format in ["%Y-%m-%d","%Y/%m/%d","%Y.%m.%d","%d/%m/%Y","%d-%m-%Y","%d.%m.%Y","%m/%d/%Y","%m-%d-%Y","%m.%d.%Y","%d-%b-%Y","%Y-%b-%d"]:

#             try:
#                 dto=datetime.strptime(me.from_date,format)
#                 dto1=datetime.strptime(me.to_date,format)
#                 start_time1= datetime.combine(dto, time(0, 00))
#                 end_time1= datetime.combine(dto, time(23,59))
#                 date_only = datetime.combine(dto, datetime.min.time())
#             except ValueError:
#                 pass
#     # bre=me.Branch
#     # change= bre[:1].upper() + bre[1:]
#     # a=Usercreate.objects(Branch=change).to_json()
#     # b=json.loads(a)
#     # if b :
#     #     data1={"Error":"False","Message":"Data found","Registration_list":[]}
#     #     for c in b:
#     #         d=c["Reporting_Manager"]
#     #         e=Usercreate.objects(Reporting_Manager=d).to_json()
#     #         f=json.loads(e)
#     #         for g in f:
#     #             h=g["Employee_id"]
#     #             # vv=Camp.objects(created_by=str(h),created_on__gte=dto,created_on__lte=dto1).count()
#     if dto!=dto1:
#         uu=Enrol.objects(created_by=me.emp_id,created_on__gte=str(dto),created_on__lte=str(dto1)).to_json()
#         vv=json.loads(uu)
#     else:
#          uu=Enrol.objects(created_by=me.emp_id,created_on__gte=str(start_time1),created_on__lte=str(end_time1)).to_json()
#          vv=json.loads(uu)
#     data1={"Error":"False","Message":"Data found","Registration_list":[]}
#     if vv:
#         for v in vv:
#             a22=v["mobile"]
#             formatted_number = a22[:1] + "*******" + a22[-2:]
#             m={"Patient_name":v["Patient_name"],"Age":v["Age"],"Mobile":formatted_number}
#             data1["Registration_list"].append(m)
#         return data1       
#     else:
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)           
       

# @app.post("/creating/personlized/greetings")
# def gree(me:greet):
#     # in_tz = pytz.timezone('Asia/Kolkata')
#     # in_time = datetime.now(in_tz)
#     # in_time_str = in_time.strftime('%Y-%m-%d %H:%M')
#     now = datetime.now()
#     k=str(now)
#     now1= datetime.now().date()
#     dum=str(now1)
#     type1=me.catagory
#     cat=type1[:1].upper()+type1[1:]
#     if cat=="Video":
#         if all([me.image,me.target_link]):
#             d=Greet(sno=Greet.objects.count()+1,Greet_id="GRT{:002d}".format(Greet.objects.count()+1),title=me.title,message=me.message,catagory=me.catagory,image=me.image,target_link=me.target_link,share=me.share,employe_name=me.employe_name,desigation=me.desigation,status="Active",created_by=me.created_by,created_on=now,modified_by="head",modified_on=k)
#             f=d.image_name="image"+str(d.sno)+str(dum)
#             d.save()
#             a={"Error":"False","Message":"Successfully Submitted"}
#             if a:
#              return JSONResponse(content=a, status_code=200)
#         else:
#             a={"Error":"True","Message":"please import image and video link"}
#             return JSONResponse(content=a, status_code=400)
#     elif cat=="Image":
#         if all([me.image]):
#                 d=Greet(sno=Greet.objects.count()+1,Greet_id="GRT{:002d}".format(Greet.objects.count()+1),title=me.title,message=me.message,catagory=me.catagory,image=me.image,target_link=me.target_link,share=me.share,employe_name=me.employe_name,desigation=me.desigation,status="Active",created_by=me.created_by,created_on=now,modified_by="head",modified_on=k)
#                 f=d.image_name="image"+str(d.sno)+str(dum)
#                 d.save()
#                 a={"Error":"False","Message":"Successfully Submitted"}
#                 if a:
#                     return JSONResponse(content=a, status_code=200)
#         else :
#                 a={"Error":"True","Message":"please upload image"}
#                 return JSONResponse(content=a, status_code=400)
#     else:
#         a={"Error":"True","Message":"Please enter category"}
#         return JSONResponse(content=a, status_code=400)


# @app.get("/get/personlized/greetings/data")
# def greets():
#     d=Greet.objects(status='Active').order_by("-sno").to_json()
#     # return json.loads(d)
#     dd=json.loads(d)
#     data1={"Error":"False","Message":"Data found","Greet":[]}
#     if dd:
#         for g in dd:
#             m=g["created_on"]
#             f1=g["Greet_id"]
#             timestamp = m['$date']
#             f=g["image"]
#             a2=str.encode(f)
#             FILEPATH="./api/static/{}_greet.jpg".format(f1)
#             filepath="./api/static/{}_greet.jpg".format(f1)
#             return_filepATH = "http://13.127.133.6"+filepath[5:]
#             with open(FILEPATH,"wb") as fh:
#                 fh.write(base64.decodebytes(a2))
#             date_object = datetime.fromtimestamp(timestamp/1000).date()
#             a={"SNO":g["sno"],"Greet_id":g["Greet_id"],"Title":g["title"],"Message":g["message"],"Image_name":g["image_name"],"Target_link":g["target_link"],"Catagory":g["catagory"],"Status":g["status"],"Created_by":g["created_by"],"Created_on":date_object,"Share":g["share"],"Employe_name":g["employe_name"],"Desigation":g["desigation"],"Image_path":return_filepATH}
#             data1["Greet"].append(a)
#         return data1
#     else:
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
# @app.post("/search/get/personlized/greetings/data")
# def search_greet(me:search_greet_id):
#     d=Greet.objects(Greet_id=me.Greet_id,status='Active').order_by("-sno").to_json()
#     # return json.loads(d)
#     dd=json.loads(d)
#     data1={"Error":"False","Message":"Data found","Greet":[]}
#     if dd:
#         for g in dd:
#             m=g["created_on"]
#             f1=g["Greet_id"]
#             timestamp = m['$date']
#             f=g["image"]
#             a2=str.encode(f)
#             FILEPATH="./api/static/{}_greet.jpg".format(f1)
#             filepath="./api/static/{}_greet.jpg".format(f1)
#             return_filepATH = "http://13.127.133.6"+filepath[5:]
#             with open(FILEPATH,"wb") as fh:
#                 fh.write(base64.decodebytes(a2))
#             date_object = datetime.fromtimestamp(timestamp/1000).date()
#             a={"SNO":g["sno"],"Greet_id":g["Greet_id"],"Title":g["title"],"Message":g["message"],"Image_name":g["image_name"],"Target_link":g["target_link"],"Catagory":g["catagory"],"Status":g["status"],"Created_by":g["created_by"],"Created_on":date_object,"Share":g["share"],"Employe_name":g["employe_name"],"Desigation":g["desigation"],"Image_path":return_filepATH}
#             data1["Greet"].append(a)
#         return data1
#     else:
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
# @app.put("/update_greeting_data")
# def update_greet_data(me:update_greet):
#     new=Greet.objects(Greet_id=me.Greet_id).to_json()
#     new1=json.loads(new)
#     if new1:
#         if me.image not in ["", "string"]:
#             data=Greet.objects(Greet_id=me.Greet_id).update_one(set__title=me.title,set__message=me.message,set__employe_name=me.employe_name,set__desigation=me.desigation,set__image=me.image)
#         elif me.image=="":
#             data=Greet.objects(Greet_id=me.Greet_id).update_one(set__title=me.title,set__message=me.message,set__employe_name=me.employe_name,set__desigation=me.desigation)
#         elif me.image=="string":
#             data=Greet.objects(Greet_id=me.Greet_id).update_one(set__title=me.title,set__message=me.message,set__employe_name=me.employe_name,set__desigation=me.desigation)

#         a={"Error":"False","Message":"Successfully Updated"}
#         return JSONResponse(content=a, status_code=200)

#     else:
#         a={"Error":"True","Message":"please enter valid Greet_id"}
#         return JSONResponse(content=a, status_code=400)

# @app.put("/update/creating/personlized/status")
# def update(me:upgre):
#     try:
#         new=Greet.objects(sno=int(me.sno)).to_json()
#         new1=json.loads(new)
#         if new1:
#             b1= me.status[:1].upper() + me.status[1:]
#             a= Greet.objects(sno=int(me.sno)).update_one(set__status=b1)
#             b="Successfully Updated"
#             if b:
#                     return {"Error":"False","Message":b}
#             else:
#                 # return {"Error":"True","Message":"Data not found"}
#                 a={"Error":"True","Message":"Data not found"}
#                 return JSONResponse(content=a, status_code=400)
#     except ValueError:
#         a={"Error":"True","Message":"please enter valid sno"}
#         return JSONResponse(content=a, status_code=400)
# @app.post("/News/upload")
# def add_news(me:news):
#     # in_tz = pytz.timezone('Asia/Kolkata')
#     # in_time = datetime.now(in_tz)
#     # in_time_str = in_time.strftime('%Y-%m-%d %H:%M')
#     now = datetime.now()
#     k=str(now)
#     now1= datetime.now().date()
#     dum=str(now1)
#     if me.title!="" and me.message!="":
#         mat=News(sno=News.objects.count()+1,news_id="NEW{:002d}".format(Greet.objects.count()+1),title=me.title,message=me.message,Attachment=me.Attachment,share=me.share,status="Active",created_by=me.created_by,created_on=now,modified_by="head",modified_on=k)
#         f=mat.Attachment_name="attach"+str(mat.sno)+str(dum)
#         mat.save()
#         a={"Error":"False","Message":"Successfully Submitted"}
#         if a:
#             return JSONResponse(content=a, status_code=200)
#         else:
#                 a={"Error":"True","Message":"Data not found"}
#                 return JSONResponse(content=a, status_code=400)
#     else:
#         a={"Error":"True","Message":"please enter details"}
#         return JSONResponse(content=a, status_code=400)
# @app.get("/get/new/data")
# def get_news():
#     ff=News.objects(status="Active").order_by("-sno").to_json()
#     f1=json.loads(ff)
#     data1={"Error":"False","Message":"Data found","news":[]}
#     if f1:
#         for d in f1:
#             m=d["created_on"]
#             f1=d["news_id"]
#             timestamp = m['$date']
#             f=d["Attachment"]
#             a2=str.encode(f)
#             FILEPATH="./api/static/{}_news.jpg".format(f1)
#             filepath="./api/static/{}_news.jpg".format(f1)
#             return_filepATH = "http://13.127.133.6"+filepath[5:]
#             with open(FILEPATH,"wb") as fh:
#                 fh.write(base64.decodebytes(a2))
#             date_object = datetime.fromtimestamp(timestamp/1000).date()
#             d1={"Sno":d["sno"],"News_id":d["news_id"],"Title":d["title"],"Message":d["message"],"Attach_name":d["Attachment_name"],"Share":d["share"],"Status":d["status"],"Created_by":d["created_by"],"Created_on":date_object,"Image_path":return_filepATH}
#             data1["news"].append(d1)
#         return data1
#     else:
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
# @app.post("/search/get/news/data")
# def search_get_news(me:search_news_data):
#     ff=News.objects(news_id=me.News_id,status="Active").order_by("-sno").to_json()
#     f1=json.loads(ff)
#     data1={"Error":"False","Message":"Data found","news":[]}
#     if f1:
#         for d in f1:
#             m=d["created_on"]
#             f1=d["news_id"]
#             timestamp = m['$date']
#             f=d["Attachment"]
#             a2=str.encode(f)
#             FILEPATH="./api/static/{}_news.jpg".format(f1)
#             filepath="./api/static/{}_news.jpg".format(f1)
#             return_filepATH = "http://13.127.133.6"+filepath[5:]
#             with open(FILEPATH,"wb") as fh:
#                 fh.write(base64.decodebytes(a2))
#             date_object = datetime.fromtimestamp(timestamp/1000).date()
#             d1={"Sno":d["sno"],"News_id":d["news_id"],"Title":d["title"],"Message":d["message"],"Attach_name":d["Attachment_name"],"Share":d["share"],"Status":d["status"],"Created_by":d["created_by"],"Created_on":date_object,"Image_path":return_filepATH}
#             data1["news"].append(d1)
#         return data1
#     else:
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
# @app.put("/update/news/status")
# def update(me:newupd):
#     try:      
#         new=News.objects(sno=int(me.sno)).to_json()
#         new1=json.loads(new)
#         if new1:
#             b1= me.status[:1].upper() + me.status[1:]
#             a= News.objects(sno=int(me.sno)).update_one(set__status=b1)
#             b="Successfully Updated"
#             if b:
#                     return {"Error":"False","Message":b}
#             else:
#                 a={"Error":"True","Message":"Data not found"}
#                 return JSONResponse(content=a, status_code=400)
#     except:
#         a={"Error":"True","Message":"please enter valid sno"}
#         return JSONResponse(content=a, status_code=400)
# @app.put("/update_news_details")
# def update(me:update_news):
#     try:
#         new=News.objects(sno=me.sno).to_json()
#         new1=json.loads(new)
#         if new1:
#             if me.image not in ["", "string"]:
#                 a= News.objects(sno=me.sno).update_one(set__title=me.title,set__message=me.message,set__share=me.share,set__Attachment=me.Attachment)
#             elif me.Attachment=="":
#                 a= News.objects(sno=me.sno).update_one(set__title=me.title,set__message=me.message,set__share=me.share)
#             elif me.Attachment=="string":
#                 a= News.objects(sno=me.sno).update_one(set__title=me.title,set__message=me.message,set__share=me.share)
#             b="Successfully Updated"
#             if b:
#                     return {"Error":"False","Message":b}
#             else:
#                 a={"Error":"True","Message":"Data not found"}
#                 return JSONResponse(content=a, status_code=400)
#     except:
#          a={"Error":"True","Message":"please enter valid sno"}
#          return JSONResponse(content=a, status_code=400)

# @app.put("/location-update-api")
# def loc(me:Cordi):
#     try:
#         coordinates = me.coordinates
#         add=[]
#         latitude,longitude = map(float, coordinates.split(","))
#         Lattitide=str(latitude)
#         Logitude=str(longitude)
#         geolocator = Nominatim(user_agent="geoapiExercises")
#         location = geolocator.reverse(Lattitide+","+Logitude)
#         address = location.raw['address']
#         g=address["state_district"]
#         add.append(g)
#         f=address["city"]
#         add.append(f)
#         h=address["state"]
#         add.append(h)
#         i=address["postcode"]
#         add.append(i)
#         i=address["country"]
#         add.append(i)
#         # da=str(address)
#         # print(type(address))
#         a= Usercreate.objects(Employee_id=int(me.emp_id)).update_one(set__Location=str(coordinates),set__Location_address=str(add))
#         b="Successfully Updated"
#         if b:
#                 return {"Error":"False","Message":b}
#         else:
#             a={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=a, status_code=400)
#     except:
#          a={"Error":"True","Message":"please enter valid emp_id and coordinates"}
#          return JSONResponse(content=a, status_code=400)
# @app.post("/location_coverage_report")
# def coverage(me:loccoverage):
#     now = datetime.now().date()
#     k=now
#     b1= me.Branch[:1].upper() + me.Branch[1:]
#     data1={"Error":"False","Message":"Data found","location_coverage":[]}
#     new=Usercreate.objects(Branch=b1,Active_Status="Active",Role_Code__in=["Manager", "Executive"]).to_json()
#     new1=json.loads(new)
#     if new1:
#         for n in new1:
#             id=n["Employee_id"]
#             na=n["User_name"]
#             loc=n["Location"]
#             loca=n["Location_address"]
#             phone=n["mobile_number"]
#             role=n["Role_Code"]
#             data=Callreport.objects(created_on__gt=k,created_by=str(id)).to_json()
#             dss=json.loads(data)
#             if dss:
#                 status="present"
#             else:
#                 status="absent"
#             r1=Callreport.objects(created_on__gt=k,created_by=str(id),Ucid_id__ne="").count()
#             r2=Callreport.objects(created_on__gt=k,created_by=str(id),camp__ne="").count()
#             a={"emp_id":id,"emp_name":na,"status":status,"Role_code":role,"calls":r1,"activites":r2,"location":loc,"location_address":loca,"phonenumber":phone}
#             data1["location_coverage"].append(a)
#         return data1
#     else:
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)

# @app.post("/get_location_emp_coverage_report")
# def get_location_emp(me:get_location_cov):
#     now = datetime.now().date()
#     print(now)
#     k=now
#     start_time1= datetime.combine(now, time(0, 00))
#     end_time1= datetime.combine(now, time(23,59))
#     data1={"Error":"False","Message":"Data found","emp_coverage":[]}
#     new=AddMaster1.objects(created_by=me.emp_id,created_on__gte=start_time1,created_on__lte=end_time1).count()
#     new1=len(Callreport.objects(created_by=me.emp_id,created_on__gte=start_time1,created_on__lte=end_time1,Ucid_id__ne='').distinct(field="Ucid_id"))
#     total=new+new1
#     new5=Callreport.objects(created_by=me.emp_id,created_on__gte=start_time1,created_on__lte=end_time1).to_json()
#     new6=json.loads(new5)
#     if new6:
#         for data in new6:
#             a=data["Ucid_id"]
#         nn=len(new6)
#         if nn==1:
#             v1=nn
#         elif nn>1:
#             v2=nn
#         elif nn>3:
#             v3=nn
#         a={"total_counts":total,"meet":new1,"not_meet":new,"v1":v1,"v2":0,"v3":0}
#         data1["emp_coverage"].append(a)
#         return data1
#     else:
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
# @app.get("/image_floder")
# def image_floder(sno:str):
#     d=AddMaster1.objects(sno=sno).to_json()
#     d1=json.loads(d)
#     for d2 in d1:
#         a=d2["bank_attach_path"]
#         f = d2["Agent_name"]
#         a2=str.encode(a)
#         FILEPATH="./api/static/{}_pan.jpg".format(f)
#         with open(FILEPATH,"wb") as fh:
#             fh.write(base64.decodebytes(a2))
#         b=d2["pan_attach_path"]
#         b2=str.encode(b)
#         with open("to_pan_attach.jpeg","wb") as fn:
#             fn.write(base64.decodebytes(b2))
@app.get("/static/{file_path:path}")
async def serve_static(file_path: str):
    return FileResponse(f"./static/{file_path}")


    
# @app.get("/image floder")
# def image_floder(sno:str):
#     d=AddMaster1.objects(sno=sno).to_json()
#     d1=json.loads(d)
#     for d2 in d1:
#         a=d2["bank_attach_path"]
#         a2=str.encode(a)
#         FILEPATH="./api/static/bank_attach.jpeg"
#         with open(FILEPATH,"wb") as fh:
#             fh.write(base64.decodebytes(a2))
#         b=d2["pan_attach_path"]
#         b2=str.encode(b)
#         with open("to_pan_attach.jpeg","wb") as fn:
#             a=fn.write(base64.decodebytes(b2))
#     return StreamingResponse(a, media_type="image/jpeg")


    # new2=Callreport.objects(created_by=emp_id,Ucid_id__ne='').to_json()
    # new3=json.loads(new2)
    # aa=[]
    # for f in new3:
    #     a=f["Ucid_id"]
    #     b=f["created_by"]
    #     new4=Callreport.objects(Ucid_id=a).count()
    #     aa.append(new4)
    

    # not_meet=new-new1
    # return new,new1,not_meet


    



# @app.get("/get/greet/image/{image_id}")
# async def read_image(sno: int):
#     image_obj = AddMaster1.objects(sno=sno).first()
#     if image_obj:
#         image_data = image_obj.bank_attach_path
#         decoded_image = base64.b64decode(image_data)
#         image_stream = io.BytesIO(decoded_image)
#         a=StreamingResponse(image_stream, media_type="image/jpeg")
#         print(a)
#         return a
#     else:
#         return {"error":"image not found"}




 

        




    
# def area_list(me:Location):
#     d=Areas.objects(District=me.area).to_json()
#     g=json.loads(d)
#     # g=Enrol.objects(TransID=me.TransID).to_json()
#     # f=json.loads(g)
#     # data={"Error":"False","Message":"Data found","Areas":[]}
#     # if g:
#     #     for s in g:
#     #         a={"Location":s["Location"]}
#     #         data["Areas"].append(a)
#     #     return data
#     # else:
#     #     a={"Error":"True","Message":"Data not found"}
#     #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=a)



# @app.post("/upload file")
# def upload(az:don5,data:UploadFile=File(...)):
#     aa=uploa(name=az.name)
#     a=data.filename
#     print(type(a))
#     with open(a,'rb') as fd:
#         aa.bank.put(fd,content_type='image/jpeg')
#         aa.save()

    

# #static files
# app.mount("/static",StaticFiles(directory="static"),name="static")
# @app.post("/Bank Attachment")
# async def create_upload_file(file:UploadFile=File(...),token:str=Depends(oauth2_scheme)):
#     FILEPATH="./static/images"
#     filename=file.filename
#     extension=filename.split(".")[1]
#     if extension not in ["png","jpg"]:
#         return {"status":"error","detail":"File extension not allowed"}
#     token_name=secrets.token_hex(10)+"."+extension
#     generate_name=FILEPATH+token_name
#     file_content=await file.read()
#     with open(generate_name,"wb")as file:
#         file.write(file_content)
#     img=Image.open(generate_name)
#     img=img.resize(size=(200,200))
#     img.save(generate_name)
#     file.close()
# app.mount("/static",StaticFiles(directory="static"),name="static")
# @app.post("/pan attach")
# async def create_upload_file(file:UploadFile=File(...),token:str=Depends(oauth2_scheme)):
#     FILEPATH="./static/pan_attach"
#     filename=file.filename
#     extension=filename.split(".")[1]
#     if extension not in ["png","jpg"]:
#         return {"status":"error","detail":"File extension not allowed"}
#     token_name=secrets.token_hex(10)+"."+extension
#     generate_name=FILEPATH+token_name
#     file_content=await file.read()
#     with open(generate_name,"wb")as file:
#         file.write(file_content)
#     img=Image.open(generate_name)
#     img=img.resize(size=(200,200))
#     img.save(generate_name)
#     file.close()
# @app.post("/id_proof_attach")
# async def create_upload_file(file:UploadFile=File(...),token:str=Depends(oauth2_scheme)):
#     FILEPATH="./static/id_proof_attach"
#     filename=file.filename
#     extension=filename.split(".")[1]
#     if extension not in ["png","jpg"]:
#         return {"status":"error","detail":"File extension not allowed"}
#     token_name=secrets.token_hex(10)+"."+extension
#     generate_name=FILEPATH+token_name
#     file_content=await file.read()
#     with open(generate_name,"wb")as file:
#         file.write(file_content)
#     img=Image.open(generate_name)
#     img=img.resize(size=(200,200))
#     img.save(generate_name)
#     file.close()
# @app.post("/profile_image_path")
# async def create_upload_file(file:UploadFile=File(...),token:str=Depends(oauth2_scheme)):
#     FILEPATH="./static/profile_image_path"
#     filename=file.filename
#     extension=filename.split(".")[1]
#     if extension not in ["png","jpg"]:
#         return {"status":"error","detail":"File extension not allowed"}
#     token_name=secrets.token_hex(10)+"."+extension
#     generate_name=FILEPATH+token_name
#     file_content=await file.read()
#     with open(generate_name,"wb")as file:
#         file.write(file_content)
#     img=Image.open(generate_name)
#     img=img.resize(size=(200,200))
#     img.save(generate_name)
#     file.close()

  
    

    # User._get_collection_name(),
# @app.get("/the geo code")
# def geo():
#     geolocator = Nominatim(user_agent="my_user_agent")
#     city ="delhi"
#     country ="india"
#     loc = geolocator.geocode(city+','+ country)
#     print("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)
#     # a=loc.latitude
#     # b=loc.longitude
#     # print(a,b)
