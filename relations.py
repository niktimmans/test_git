#Не лучшее решение из-за хранения иформации о тарифе в классе клиента
#Правильное решение в файле correct_relation.py

class Customer:

    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    def __str__(self):
        return "Имя {0.name}, баланс {0._balance}".format(self)

    @property
    def balance(self):
        return self._balance

    def record_payment(self, amount_paid):
        assert amount_paid > 0, "Пополнить можно на ненулевое значение"
        self._balance += amount_paid

    def record_call(self, call_type, minutes):
        if(call_type == "Г"):
            self._balance -= 5 * minutes
        elif(call_type == "М"):
            self._balance -= minutes

class CustomerFree2ndAfter10(Customer):

    def record_call(self, call_type, minutes):
        if(call_type == "Г" and minutes > 10):
            bonus_minutes = (minutes - 10) // 2
        else:
            bonus_minutes = 0

        super().record_call(call_type, minutes - bonus_minutes)

class CustomerCheaperFirst5(Customer):

    def record_call(self, call_type, minutes):
        if (minutes > 5):
            expensive_minutes = (minutes - 5) * 2 + minutes
        else:
            expensive_minutes = minutes // 2

        super().record_call(call_type, expensive_minutes)

ivan = Customer("Иван Петров", 150)
elena = Customer("Елена Миронова", 100)

ivan.record_call("Г", 20)
ivan.record_call("М", 5)
elena.record_call("М", 10)

ivan.record_payment(155)

print(ivan)
print(elena)