from secrets import token_hex

def login(level,userid,pwd):
    if level=='admin':
        exist=check_admin_table(userid,pwd)
        if exist:
            return 'adm-'+token_hex(16)+''
    elif level=='customer':
        exist=check_customer_table(userid,pwd)
        if exist:
            return 'cus-'+token_hex(16)+''
    return False
