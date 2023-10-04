class CallPlan:

    def __init__(self, name):
        self.name = name

    def record_call(self, call_type, minutes):
        if (call_type == "Г"):
            return self.record_call_g(minutes)
        elif (call_type == "М"):
            return self.record_call_m(minutes)

    def record_call_g(self, minutes):
        raise NotImplementedError

    def record_call_m(self, minutes):
        raise NotImplementedError

class CallPlanSimple(CallPlan):

    def __init__(self):
        self.name = "Повременный"

    def record_call_g(self, minutes):
        return minutes * 5

    def record_call_m(self, minutes):
        return minutes

class CallPlanFree2ndAfter10(CallPlanSimple):

    def __init__(self):
        self.name = "После 10 в 2 раза дешевле"

    def record_call_g(self, minutes):
        if(minutes > 10):
            bonus_minutes = (minutes - 10) // 2
        else:
            bonus_minutes = 0

        return super().record_call_g(minutes - bonus_minutes)


class CallPlanTwiceFreeBefore5(CallPlanSimple):

    def __init__(self):
        self.name = "До 5 в 2 раза дешевле"

    def record_call(self, call_type, minutes):

        LIMIT_CHEAP = 5
        if minutes > LIMIT_CHEAP:
            cheap_minutes = LIMIT_CHEAP
            expensive_minutes = minutes - LIMIT_CHEAP
        else:
            cheap_minutes = minutes
            expensive_minutes = 0


        return super().record_call(call_type, cheap_minutes / 2 + expensive_minutes * 2)


class Customer:

    def __init__(self, name, balance, call_plan):
        self.name = name
        self._balance = balance
        self.call_plan = call_plan
        if(self.call_plan is None):
            self.call_plan = CallPlan

    def __str__(self):
        return "Имя {0.name}, баланс {0._balance}".format(self)

    @property
    def balance(self):
        return self._balance

    def record_payment(self, amount_paid):
        assert amount_paid > 0, "Пополнить можно на ненулевое значение"
        self._balance += amount_paid

    def record_call(self, call_type, minutes):
        costs = self.call_plan.record_call(call_type, minutes)
        self._balance -= costs



ivan = Customer("Иван Петров", 150, CallPlanFree2ndAfter10)
elena = Customer("Елена Миронова", 100, CallPlanTwiceFreeBefore5)

ivan.record_call("Г", 20)
ivan.record_call("М", 5)
elena.record_call("М", 10)

ivan.record_payment(155)

print(ivan)
print(elena)