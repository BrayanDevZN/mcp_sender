from pydantic import BaseModel, field_validator

class ValidSender(BaseModel):

    email:str 
    subject:str 
    body:str 


    @field_validator("email")
    def valid(cls, email:str):

        if not "@gmail.com" in email:
            raise ValueError(f"Expeted '@gmail.com' in {email}")


        return email