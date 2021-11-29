HEADER_SIZE=8
NAME_SIZE=8
SURNAME_SIZE=8
UNAME_SIZE = 8
PASSW_SIZE = 8
SIGNAL_SIZE=6
MSG_SIZE = 8
UID_LENGTH = 8
def format_message(message,msgType):
    if not message:
        return None
    header = f'{len(message):<{HEADER_SIZE}}'
    signal = f'{msgType:<{SIGNAL_SIZE}}'
    return f'{header}{signal}{message}'
def format_register_message(name, surname, uname, password,msgType):
    header = f'{len(name+surname+uname+password):<{HEADER_SIZE}}'
    signal = f'{msgType:<{SIGNAL_SIZE}}'
    len_name = f'{len(name):<{NAME_SIZE}}'
    len_surname = f'{len(surname):<{SURNAME_SIZE}}'
    len_Uname = f'{len(uname):<{UNAME_SIZE}}'
    len_pw = f'{len(password):<{PASSW_SIZE}}'
    return f'{header}{signal}{len_name}{len_surname}{len_Uname}{len_pw}{name}{surname}{uname}{password}'
def format_login_message(uname, password, msgType):
    header = f'{len(uname+password):<{HEADER_SIZE}}'
    signal = f'{msgType:<{SIGNAL_SIZE}}'
    len_Uname = f'{len(uname):<{UNAME_SIZE}}'
    len_pw = f'{len(password):<{PASSW_SIZE}}'
    return f'{header}{signal}{len_Uname}{len_pw}{uname}{password}'
def format_return_message(msgType, sucess):
    if sucess:
        return format_message("sucess", msgType + 30)
    else:
        return format_message("failed", msgType + 50)
def format_create_chat(uname, msgType):
    return format_message(uname,msgType)
def fromat_uid_chatUser(uid,msgType):
    if not uid:
        return None
    header = f'{len(uid):<{HEADER_SIZE}}'
    signal = f'{msgType:<{SIGNAL_SIZE}}'
    return f'{header}{signal}{uid}'
def format_chatMessage(uid, msg, msgType):
    header = f'{len(uid+msg):<{HEADER_SIZE}}'
    signal = f'{msgType:<{SIGNAL_SIZE}}'
    len_uid = f'{len(uid):<{UID_LENGTH}}'
    len_msg = f'{len(msg):<{MSG_SIZE}}'
    return f'{header}{signal}{len_uid}{len_msg}{uid}{msg}'
