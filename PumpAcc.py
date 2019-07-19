import Output

class PumpAcc(Output):
    
    def __init__(self, pin):
        super.__init__(pin)

    def on():
        GPIO.output(super.PIN, GPIO.LOW)

    def off():
        GPIO.output(super.PIN, GPIO.HIGH)
    