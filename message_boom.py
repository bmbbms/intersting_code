import requests
import  time
import json

class SMS_boom(object):
    """
    数码之家短信接口
    """
    def __init__(self, number):
        self.number = number
        self.url = "http://bbs.mydigit.cn/registe.php"
        self.header = {
            "Referer": "http://bbs.mydigit.cn/registe.php",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/70.0.3538.102 Safari/537.36"

        }


    def get_respose(self):
        data = {
            "action": "auth",
            "step" : "1",
            "mobile": self.number
        }

        try :
            respose = requests.post(self.url,data =data,headers= self.header)
            print("fasongchenggong")
        except Exception :
            print("fasongshibai")

    def run(self):
        self.get_respose()

if __name__ == "__main__":
    one = SMS_boom("15623444629")
    one.run()