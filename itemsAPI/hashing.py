from passlib.context import CryptContext



pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")



class Hash():

    #Method to convert the password into hass password

    def bcrypt(password: str):
        return pwd_cxt.hash(password)


    #Method to verify the password

    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)