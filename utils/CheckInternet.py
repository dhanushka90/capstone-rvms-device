# pip install requests
import requests


class CheckInternet:

    def is_cnx_active(timeoutVar):
        try:
            requests.head("http://www.google.com/", timeout=timeoutVar)
            print("The internet connection is active")
            return True
        except requests.ConnectionError:
            print("The internet connection is not active")
            return False

    def wait_till_cnx_is_active(timeout):
        while True:
            if obj.is_cnx_active(timeout) is True:
                # Do somthing
                print("The internet connection is active")
                break
            else:
                pass


obj = CheckInternet
