from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
import pandas as pd
from io import BytesIO

from schemas.schema import SalesData
import use_case.incentive as incentive

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/read-file")
def read_file(file: UploadFile):
    if not file:
        raise HTTPException(
                status_code=400,
                detail=f"File is required",
            )
    else:
        allowed_mime_types = [
            "application/vnd.ms-excel",  # For .xls files
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",  # For .xlsx files
        ]
        
        if file.content_type not in allowed_mime_types:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid file type. Expected an Excel file, got {file.content_type}",
            )
        contents = file.file.read()
        data = BytesIO(contents) 
        df = pd.read_excel(data, sheet_name = 'Sheet1', skiprows=1)

        arr = list()
        for i, r in df.iterrows():
            arr.append(SalesData(so=r['SO'], sp=r['SP'], sm=r['SM'], gm=r['GM'], item=r['Item'].lower()))
        file.file.close 
        return {"data": arr}
    
@app.post("/calculate-incentives")
def calculate_incentives(req: list[SalesData]):
    return {"data": incentive.calculate(req)}

app.mount('/', StaticFiles(directory='frontend/dist', html=True))