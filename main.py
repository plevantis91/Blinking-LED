"""
MicroPython LED Blinking Project
Makes an LED blink at a fixed interval using MicroPython
"""

import machine
import time
from time import sleep

class BlinkingLED:
    def __init__(self, pin_number=2, blink_interval=1.0):
        """
        Initialize the blinking LED
        
        Args:
            pin_number (int): GPIO pin number for the LED (default: 2)
            blink_interval (float): Blink interval in seconds (default: 1.0)
        """
        self.pin_number = pin_number
        self.blink_interval = blink_interval
        self.led = machine.Pin(pin_number, machine.Pin.OUT)
        self.is_running = False
        
    def blink_once(self):
        """Blink the LED once (on then off)"""
        self.led.on()
        sleep(self.blink_interval / 2)
        self.led.off()
        sleep(self.blink_interval / 2)
        
    def start_blinking(self):
        """Start continuous blinking"""
        self.is_running = True
        print(f"Starting LED blinking on pin {self.pin_number} with {self.blink_interval}s interval")
        
        while self.is_running:
            self.blink_once()
            
    def stop_blinking(self):
        """Stop blinking and turn off LED"""
        self.is_running = False
        self.led.off()
        print("LED blinking stopped")
        
    def set_interval(self, new_interval):
        """Change the blink interval"""
        self.blink_interval = new_interval
        print(f"Blink interval changed to {new_interval}s")
        
    def get_status(self):
        """Get current status"""
        return {
            'pin': self.pin_number,
            'interval': self.blink_interval,
            'running': self.is_running
        }

def main():
    """Main function to run the LED blinking program"""
    print("MicroPython LED Blinking Project")
    print("=" * 40)
    
    # Create LED instance (adjust pin number as needed for your board)
    # Common pins: ESP32/ESP8266 - pin 2, Raspberry Pi Pico - pin 25
    led = BlinkingLED(pin_number=2, blink_interval=1.0)
    
    try:
        # Start blinking
        led.start_blinking()
        
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\nStopping LED blinking...")
        led.stop_blinking()
        print("Program terminated by user")
        
    except Exception as e:
        print(f"Error occurred: {e}")
        led.stop_blinking()

# Run the program if this file is executed directly
if __name__ == "__main__":
    main()
