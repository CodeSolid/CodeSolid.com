.. _embedded_systems_essentials_with_arm_notes:


Notes for `Embedded Systems Essentials with ARM <https://www.edx.org/learn/embedded-systems/arm-education-embedded-systems-essentials-with-arm-getting-started?index=product&objectID=course-65433bff-efc4-4e62-8a91-af05dc37802a&webview=false&campaign=Embedded+Systems+Essentials+with+Arm%3A+Getting+Started&source=edX&product_category=course&placement_url=https%3A%2F%2Fwww.edx.org%2Flearn%2Fembedded-systems>`_.
------------------------------------------------

`ARM <https://arm.com>`_ designed `Mbed <https://os.mbed.com>`_ an open-source C++ framework for
doing IOT development on Cortex-M microcontrollers.  Cortex-M processor are (see `wikipedia <https://en.wikipedia.org/wiki/ARM_Cortex-M>`_) 32-bit processor cores licensed by ARM, but manufactured by many manufacturers.  

Common to embedded systems:
===========================

This is based on `this video <https://www.youtube.com/watch?v=IXFcSDif2Mw>`_.

* Usually have computation processing.
* Do specific tasks that repeat either on timer or in response to triggers.
* Benefits:
	* Low power
	* High Performance
	* Low Cost
* Often subject to real-time constraints.
* Fault handling code is usually larger than other code, because fault handling important.
* Parts:
	* Microprocessor / aka CPU 
	* Arithmetic Logic Unit (ALU)
	* Peforms fetching of instructions / decoding of them / execution
	* Has a memory interface:
		* From which instructions are fetched
		* Which can also be interacted with.
* MCU = Microprocessor plus additional components e.g. Program memory, data memory, digital I/O, Analog I/O, Timers, Other peripherals
* CPU usually single core.
* Enormous range of applications:
	* Closed loop control systems
	* Maintain a set point, e.g. temperature
	* Specialized functions within larger system.
Example is bike computer:
	* Sense wheel rotation
	* Cacluates speed, distance, time.
	* Constraints are size / cost / battery life.
	* Low cost CPU
Example Engine Control Unit:
	* real-time
	* reliable in harsh environments
	* Networking to rest of constraints
	* High demand - powerful MCU

A recommended book is Fast and Effective Embedded System Design; Applying the ARM Mbed

... Skip several videos of notes, all good.  Now working on the good stuff, the lab, the video for which is `here <https://www.youtube.com/watch?v=BD0C3Awlhf0>`_.

Here are the Docker  command for the mbed simulator:

.. code-block:: bash

	docker pull armedu/mbed_sim
	docker run -p 7829:7829 armedu/mbed_sim

An example `supported board <https://www.mouser.com/ProductDetail/STMicroelectronics/NUCLEO-F401RE?qs=fK8dlpkaUMvGeToFJ6rzdA%3D%3D&utm_source=digipart&utm_medium=aggregator&utm_campaign=NUCLEO-F401RE&utm_term=NUCLEO-F401RE&utm_content=STMicroelectronics>`_ mentioned in the course.

Here's a bit of fun I had doing the phi phenomenon on a row of LEDs

.. code-block:: C++

	#include "mbed.h"

	int main() {
		DigitalOut leds [] = {
			DigitalOut(LED1),
			DigitalOut(LED2),
			DigitalOut(LED3),
			DigitalOut(LED4),
		};
		const int NUM_LEDS = sizeof(leds) / sizeof(leds[0]);
		int i = 0;
		
		const int off_ms = 10, on_ms = 40;
		
		while (true) {
			
			if (leds[i]) {
				leds[i] = false;
				// Run through array and loop to beginning
				i = i == NUM_LEDS - 1  ? 0 : i + 1;			
				wait_ms(off_ms);
			}
			else {
				leds[i] = true;				
				wait_ms(on_ms);
			}
		
		}
	}

Independent Progress:
=====================

Here are some other things I've done:

* Tried to install mbed studio using ~/Downloads/MbedStudio-1.4.5.pkg -- but it fails. I asked about it in forums.mbed.com, `here <https://forums.mbed.com/t/mbed-studio-mac-installation-fails-apple-silicon/21333>`_.
* Found `keil studio <https://studio.keil.arm.com/>`_, an online IDE that looks like a VS Code thinger, which also led me to find the `VS Code Extension <https://marketplace.visualstudio.com/items?itemName=Arm.keil-studio-pack>`, which I haven't yet installed.  Oh hell, let's try it.  OK, it's installed, now what with that thingie.  Well, even the online keil studio says it can't find any devices to add, so lest I spend too much on shipping for the one board I need, I...
* Ordered 2 units of the mbed-supported `STMicroelectronics NUCLEO-F401RE <https://www.mouser.com/ProductDetail/STMicroelectronics/NUCLEO-F401RE?qs=fK8dlpkaUMvGeToFJ6rzdA%3D%3D&utm_source=digipart&utm_medium=aggregator&utm_campaign=NUCLEO-F401RE&utm_term=NUCLEO-F401RE&utm_content=STMicroelectronics>`_.
* Installed stlink on a guess using brew install stlink.  This added a bunch of utilities to  /opt/homebrew/Cellar/stlink/1.7.0/bin/ (not yet on path) -- most of which to-date complain that they can't find any ST-LINK devices.



	


