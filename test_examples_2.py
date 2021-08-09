import requests

class TestExamples2:
    def test_dz_12(self):

        r = requests.request("get","https://playground.learnqa.ru/api/homework_header")

        assert r.status_code == 200, "Wrong response code"

        assert r.headers["x-secret-homework-header"] == "Some secret value", "Incorrect header in the responce"