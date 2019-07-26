import sys
from json import dumps as serializer
import time
from requests.sessions import Session
from simplejson import loads as deserializer


IBS_URI = "http://127.0.0.1:1237/"
USERNAME = "system"
PASSWORD = "OXedEtYp6h9w#"

# common HTTP-headers which will be sent with all IBSng requests
DEFAULT_HEADERS = {
    "Content-type": "application/json",
    "Accept": "application/json",
    "User-Agent": "ibs-jsonrpc",
    "Accept-Charset": "utf-8",
    "Cache-Control": "no-cache",
}

# cache first session object for all IBSng interaction in one
# request-response lifecycle
_session = None


# load _session or create a new Session object
def _get_session():
    global _session
    if _session is None:
        _session = Session()
        _session.headers.update(DEFAULT_HEADERS)
    return _session


def send_request(handler, method, parameters):
    """Send a HTTP request to IBSng with specified parameters and auth data

    :param handler: IBSng handler name
    :type handler: str
    :param method: IBSng method name
    :type method: str
    :param parameters: parameters to send for the method
    :type parameters: dict
    :return: IBSng response in a dict
    :rtype: dict
    """
    session = _get_session()
    method_to_call = ".".join((handler, method,))
    response_object = session.post(url=IBS_URI, data=serializer(dict(method=method_to_call, params=parameters)))
    return deserializer(response_object.text)


def login():
    method = "login"
    handler = "login"
    params = {
        "auth_remoteaddr": "127.0.0.1",
        "auth_type": "ANONYMOUS",
        "auth_name": "ANONYMOUS",
        "auth_pass": "ANONYMOUS",
        "login_auth_pass": PASSWORD,
        "create_session": True,
        "login_auth_name": USERNAME,
        "login_auth_type": "ADMIN"
    }

    resp = send_request(handler, method, params)
    return resp


def updateUserAttrs(session_id, user_info, user_id):
    user_name = str(user_info[0])
    serial = str(user_info[1])
    group = str(user_info[2])
    handler = "user"
    method = "updateUserAttrs"
    params = {
        "auth_remoteaddr": "127.0.0.1",
        "auth_session": session_id,
        "auth_name": USERNAME,
        "auth_type": "ADMIN",
        "user_id": str(user_id),
        "attrs": {'group_name': group , 'normal_user_spec': {'normal_username': user_name, 'normal_password': ''}, 'serial': serial},
        "to_del_attrs": []
    }

    resp = send_request(handler, method, params)
    return resp

def addNewUsers(session_id, count, group):
    handler = "user"
    method = "addNewUsers"
    params = {
        "auth_remoteaddr": "127.0.0.1",
        "auth_session": session_id,
        "auth_name": USERNAME,
        "auth_type": "ADMIN",
        "count": count,
        "group_name": str(group),
        "credit":{1:1, 2:0, 3:0, 4:0, 5:0, 6:0},
        "isp_name": "Main",
        "credit_comment": ""
    }

    resp = send_request(handler, method, params)
    return resp

def main():
    count = 3
    group = "test"
    session_id = login()
    if session_id['error']:
        print(session_id['error'])
        exit
    user_ids = addNewUsers(session_id['result'], count, group)
    ids = user_ids["result"]
    if user_ids["error"]:
        print(user_ids["error"])
    for id in ids:
        print(id)
        print('\n')

if __name__ == "__main__":
    main()
