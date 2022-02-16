import logging
import cv2

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

LOG = logging.getLogger(__name__)
router = APIRouter()

"""
########################################################################################
####                                     ENDPOINTS                                  ####
########################################################################################
"""


@router.get("/")
async def match(request: Request):
    try:
        return JSONResponse(content={"status": "OK", "opencv": cv2.__version__})
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=500, detail=exc.args)
