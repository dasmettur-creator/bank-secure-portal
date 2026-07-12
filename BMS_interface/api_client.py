from requests import post
server="http://127.0.0.1:8000"

def customer_entry(usrid,usrpwd):
    response = post(
        server+"/login/customer",
        json={
            "userid":usrid
            "userpassword":usrpwd
            }
        )
        return reponse.json()

def admin_entry(usrid,usrpwd):
    response = post(
        server+"/login/admin",
        json={
            "userid":usrid
            "userpassword":usrpwd
            }
        )
        return reponse.json()
