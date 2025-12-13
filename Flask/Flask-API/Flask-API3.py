from flask import Flask
from flask_restful import Resource, Api

app=Flask(__name__)

api=Api(app)

employee=[]

class Employee(Resource):

    def get(self,name):
        for i in employee:
            if(i["name"]==name):
                return i

        return {"name":None}

    def post(self,name):

        newemp={"name":name}

        employee.append(newemp)

        return {"message":"Added","employee":newemp}

    def delete(self,name):

        for i in employee:
            if i["name"]==name:
                employee.remove(i)
                return {"message":"Deleted","employee":i},200

        return {"message":"Not found", "employee":name},404

class AllEmployee(Resource):

    def get(self):
        return {"Employees":employee}

api.add_resource(Employee,"/emp/<string:name>")
api.add_resource(AllEmployee,"/AllEmp")

app.run()
