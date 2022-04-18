
class SchemaValidator(object):
    def __init__(self, response={}):
        self.response = response

    def isTrue(self):

        error_message = []
        try:
            name = self.response.get("name", None)
            if name is None:
                raise Exception("error")
        except Exception as ex:
            error_message.append("Field name is required")

        try:
            acc_no = self.response.get("acc_no", None)
            if acc_no is None:
                raise Exception("error")
        except Exception as ex:
            print("Error: {}", format(ex))
            error_message.append("Field acc_no is required")

        try:
            balance = self.response.get("balance", None)
            if balance is None or type(balance) is not int:
                raise Exception("error")
        except Exception as ex:
            print("Error: {}", format(ex))
            error_message.append("Field banlance is required")

        return error_message