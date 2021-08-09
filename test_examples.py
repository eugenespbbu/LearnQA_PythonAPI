import requests

class TestExamples:
    def test_dz_11(self):

        r = requests.request("get", "https://playground.learnqa.ru/api/homework_cookie")

        assert r.status_code == 200, "Wrong response code"

        assert 'Cookie HomeWork=hw_value for .playground.learnqa.ru/' in str(r.cookies), "Incorrect cookies in the responce"

