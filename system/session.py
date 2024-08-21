sessions = {}

def start_session(ip, user:dict):
    sessions[ip] = {'page':'main','user':user}

def stop_session(ip):
    sessions.pop(ip)

def get_sessions():
    return sessions


