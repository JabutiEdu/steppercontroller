#-----------------------------------
# Name: Stepper Motor
#
# Author: matt.hawkins
# Author: Pedro Henrique Kopper
#
# Created: 11/07/2012
# Updated: 15/08/2014
#
#Copyright: (c) matt.hawkins 2012
#-----------------------------------
#!/usr/bin/env python
 
# Import required libraries
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

StepCount1 = 4
Seq1 = []
Seq1 = range(0, StepCount1)
Seq1[0] = [1,0,0,0]
Seq1[1] = [0,1,0,0]
Seq1[2] = [0,0,1,0]
Seq1[3] = [0,0,0,1]

StepCount2 = 8
Seq2 = []
Seq2 = range(0, StepCount2)
Seq2[0] = [1,0,0,0]
Seq2[1] = [1,1,0,0]
Seq2[2] = [0,1,0,0]
Seq2[3] = [0,1,1,0]
Seq2[4] = [0,0,1,0]
Seq2[5] = [0,0,1,1]
Seq2[6] = [0,0,0,1]
Seq2[7] = [1,0,0,1]

class Stepper(object):
    def __init__(self, pins, speed, stepcount):
        self.pins = pins
        self.speed = speed
        self.stepcount = stepcount
        if self.stepcount == 4:
            self.sequence = Seq1
        if self.stepcount == 8:
            self.sequence = Seq2
        for pin in pins:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin, False)
    def spin(self, steps):
        i = 0
        total = 0
        while total < steps:
            for pin in range(0, 4):
                xpin = self.pins[pin]
                if self.sequence[i][pin]!=0:
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)
            time.sleep(self.speed)
            i += 1
            total += 1
            if (i == self.stepcount):
                i = 0
            if (i < 0):
                i = self.stepcount
    def cleanup(self):
        for pin in self.pins:
            GPIO.output(pin, False)
        GPIO.cleanup()
