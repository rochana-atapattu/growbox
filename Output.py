import IO

class Output(IO):

    def __init__(self,pin):
        super.__init__()
        GPIO.setup(pin, GPIO.OUT) 