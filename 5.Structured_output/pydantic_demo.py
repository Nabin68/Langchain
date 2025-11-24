from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from pydantic import BaseModel,EmailStr,Field
from typing import Optional

load_dotenv()

Model = ChatCohere(model="command-a-03-2025")

class Student(BaseModel):
    name:str="Nabin"  #keeping name here,mean its default value if non of the name is passed then it will be there we can remove this too
    age:Optional[int]=None    #Keeping age optional  and put it as None if not present in the output
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,default=5,description="A decimal value representing the cgpa of the student")

new_student={"name":"SRK","email":"nabin12@gmail.com","age":12,"cgpa":"8.9"}  #even if we keep float as string it will automaticlly convert it 

student=Student(**new_student)

"""now the output is in Pydantic object format
to convert the output in dictionaires format we do"""
student_dict=student.model_dump()
print(student_dict["age"])

"""to convert in JSON format"""

student_json=student.model_dump_json()


