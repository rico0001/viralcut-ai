from fastapi import APIRouter, UploadFile, File, HTTPException
from services.storage import save_file
from services.authz import check_user_permission

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), user_id: int):
    # Check if the user has permission to upload files
    if not check_user_permission(user_id):
        raise HTTPException(status_code=403, detail="Permission denied")

    # Save the uploaded file
    try:
        file_path = await save_file(file)
        return {"filename": file.filename, "file_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))