# day-01 creating a rest api using python fast api framework 


from fastapi import FastAPI
import uvicorn  # 1. Import the server wrapper
import json 


app = FastAPI()


#register the  all  api routes 

# / routes 
@app.get("/")
def hello():
    return {"message": "you are sending  get request at  / routes "} # here we are sending dictinary to the server and server will send a http response to the client by specifiing the content type json


# /view routes 
@app.get("/view")
def vew():

    # method 1
    #  file=open(f"patient.json","r") #open the file in read mode
    #  json_data=file.read() # read the data 
    #  file.close()
    #  data=json.loads(json_data) 


    # method 2
    # with open("patient.json", "r") as file:
    #     data = json.load(file)  # json.load works directly on the file object
    #     return data



# method 3
    with open("patients.json", "r") as file:
        json_data = file.read()

    data = json.loads(json_data)  # json.loads parses a JSON string
    return data



if __name__ == "__main__":
    uvicorn.run("creating_rest_api:app", host="127.0.0.1", port=8000,reload=True) # it will create a http server(means it can understand the http request and send http response as well)


