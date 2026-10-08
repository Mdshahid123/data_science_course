from fastapi import FastAPI,Path
import uvicorn  # 1. Import the server wrapper
import json 

app=FastAPI() # it will give the object of class


# register the all routes 


# register the get request for the "/patient/{patient_id}" routes

@app.get("/patient/{patient_id}")
def view_patient(patient_id:str=Path(..., description="id of the patient in the db",example="p001")):
    print("pid",patient_id)
    # load all patient
    with open("patients.json","r") as file:
        data=json.load(file)

        if patient_id in data:
            return data[patient_id]

        return {"error":"patitent not found"}
    


if __name__ == "__main__":
    uvicorn.run("path_query_params:app", host="127.0.0.1", port=8000,reload=True) # it will create a http server(means it can understand the http request and send http response as well)





