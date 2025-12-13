from flask import Flask
from flask_restful import Resource,Api


app=Flask(__name__)

api=Api(app)

employee=[]
class Employee(Resource):

    def get(self,name):
        for i in employee:
            if name in list(i.keys()):
                return i

        return {"message":f"{name} not found"}


    def post(self,name):
        emp={"name":name}
        employee.append(emp)
        return {"message":"added","employee":emp}


    def delete(self,name):

        for i in employee:
            if name in list(i.keys()):
                employee.remove(i)
                return {"message":f"{name} is deleted"}

        return {"message":f"{name} does not exists"},404


class AllEmployee(Resource):

    def get(self):
        return {"employees":employee}


api.add_resource(Employee,"/emp/<string:name>")

api.add_resource(AllEmployee,"/All")

app.run()