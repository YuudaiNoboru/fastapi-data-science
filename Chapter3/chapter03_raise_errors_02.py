from fastapi import FastAPI, Body, status, HTTPException

app = FastAPI()

@app.post("/password")

async def check_password(password: str = Body(...), password_confirm: str = Body(...)):
    if password != password_confirm:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail={
                "message": "Password don't match.",
                "hints": [
                    "Check the caps lock on your keyboard",
                    "Try to make the password visibre by clicking on the eye icon to check you typing",
                ]
            },
        )
    return {"message": "Passwords match."}