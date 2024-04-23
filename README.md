```
The RFID sheild is a sheild I made for a class in my senior year of high school. I am uploading the code here and writing documentation for the library so that others can use it in the future.

---------DOCUMENTATION---------
Start by importing RFIDsheild. After you can do a few things:
- Reprogram the RFID chip
- Use the two buttons
- Use the LED grid

--==REPROGRAM THE RFID==--
You don't need to pass any paramiters to init.
rfid_chip = RFIDsheild.rfid()

--rfid_chip.write()--
Required:
rfid_chip.write(to_write)
Optional:
rfid_chip.write(to_write, head)

to_write
  This paramiter will encode a link starting with https:// to the RFID chip
head
  This is optional. 0x04 by default. Changes the head from https:// to another
                      Value    Protocol
                      -----    --------
                      0x00     No prepending is done
                      0x01     http://www.
                      0x02     https://www.
                      0x03     http://
                      0x04     https://
--EXAMPLE--

import RFIDsheild
chip = RFIDsheild.rfid()
chip.write('connorlayson.github.io')





--==USE THE BUTTONS==--
You need to pass which button is being defined as either a 1 or a 0. Button 0 is the top button, closest to the LEDs
bottom_button = RFIDsheild.button(1)

--bottom_button.get_press()--
Returns True if the button is being pressed. No paramiters needed

--EXAMPLE--

import RFIDsheild
buttonA = RFIDsheild.button(0)
buttonB = RFIDsheild.button(1)
if buttonA.get_press():
  print('Button A clicked!')
if buttonB.get_press():
  print('Button B clicked!')





--==USE THE LED GRID==--
You don't need any paramiters to init
leds = RFIDsheild.led_array()

--leds.fill()--
Turns on all the LEDs. No paramiters needed.

--leds.clear()--
Turns off all the LEDs. No paramiters needed.

--leds.activate(led)--
Turns on a specific LED or LEDs. Needs 1 paramiter (see below)

--leds.deactivate(led)--
Turns off a specific LED or LEDs. Needs 1 paramiter (see below)

--leds.toggle(led)--
Toggles specific LED or LEDs on or off, whichever it isn't already. Needs 1 paramiter (see below)

PARAMITERS:
The led paramiter is the same for all 3 functions it is refrenced in. 










