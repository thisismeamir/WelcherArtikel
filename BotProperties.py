def wordRequestCheck(message):
    condition = False
    for i in message:
        if i in '1234567890=+-_\|]}[{'";:/?.>,<!@#$%^&*()":
            condition=False
        else:
            condition=True
    return condition

def TruePasser(message):
    return True