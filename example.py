import time
import RFIDsheild

#Initalize each part of the RFID sheild
leds = RFIDsheild.led_array()
chip = RFIDsheild.rfid()
top = RFIDsheild.button(0)
bot = RFIDsheild.button(1)

selection = 0

#Handle what to write, then write it
def write_chip():
    if selection == 0:
        chip.write('connorlayson.github.io')
    if selection == 1:
        chip.write('wikipedia.org')
    if selection == 2:
        chip.write('google.com')
    if selection == 3:
        chip.write('adafruit.com')
    if selection == 4:
        chip.write('connorlayson.github.io/pyJay')
    if selection == 5:
        chip.write('youtube.com')
    if selection == 6:
        chip.write('dndbeyond.com')
    if selection == 7:
        chip.write('heroforge.com')

#Code loop
while True:
    #Turn all LEDs off
    leds.clear()
    #Turn on what's selected
    leds.activate(selection)

    #Test for button presses
    if bot.get_press():
        #Advance selection, then loop it around if you get to the end
        selection += 1
        if selection == 8:
            selection = 0
    if top.get_press():
        write_chip()
    
    #Buffer
    time.sleep(0.2)