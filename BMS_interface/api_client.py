from requests import post
server="http://127.0.0.1:8000"

def customer_entry(usrid,usrpwd):
    response = post(
        server+"/login/customer",
        json={
            "log_id":usrid,
            "pwd":usrpwd
            }
        )
    return response.json().get("access_token")

def admin_entry(usrid,usrpwd):
    response = post(
        server+"/login/admin",
        json={
            "log_id":usrid,
            "pwd":usrpwd
            }
        )
    return response.json().get("access_token")
