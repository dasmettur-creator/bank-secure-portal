from fastapi import FastAPI

app=FastAPI()

@app.get("/login/customer") #post
def cust_login():
    return login()

@app.get("/login/admin") #post
def admin_login():
    return "Hi admin"
