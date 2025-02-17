# MicroPython LED Blinking Project

A simple MicroPython project that makes an LED blink at a fixed interval. This project is designed to work with various MicroPython-compatible microcontrollers.

## Features

- 🚀 Simple LED blinking with configurable intervals
- 🔧 Easy configuration through `config.py`
- 📱 Compatible with ESP32, ESP8266, Raspberry Pi Pico, and other MicroPython boards
- 🛡️ Graceful error handling and keyboard interrupt support
- ⚡ Object-oriented design for easy customization

## Hardware Requirements

- MicroPython-compatible microcontroller (ESP32, ESP8266, Raspberry Pi Pico, etc.)
- LED (built-in or external)
- Resistor (220Ω-1kΩ) if using external LED
- Breadboard and jumper wires (for external LED setup)

## Quick Start

1. **Upload the code to your microcontroller:**
   ```bash
   # Using ampy (Adafruit MicroPython Tool)
   ampy --port /dev/ttyUSB0 put main.py
   ampy --port /dev/ttyUSB0 put config.py
   
   # Or using rshell
   rshell -p /dev/ttyUSB0
   cp main.py /pyboard/
   cp config.py /pyboard/
   ```

2. **Run the program:**
   ```python
   import main
   main.main()
   ```

3. **Or run directly:**
   ```python
   exec(open('main.py').read())
   ```

## Configuration

Edit `config.py` to customize the LED behavior:

```python
# LED Configuration
LED_PIN = 2  # GPIO pin number for the LED
BLINK_INTERVAL = 1.0  # Blink interval in seconds

# Enable debug output
ENABLE_DEBUG = True
```

### Board-Specific Pin Configurations

| Board | Built-in LED Pin | Notes |
|-------|------------------|-------|
| ESP32/ESP8266 | 2 | Most ESP boards |
| Raspberry Pi Pico | 25 | Built-in LED |
| Arduino Nano 33 IoT | 13 | Built-in LED |

## Usage Examples

### Basic Usage
```python
from main import BlinkingLED

# Create LED instance
led = BlinkingLED(pin_number=2, blink_interval=1.0)

# Start blinking
led.start_blinking()
```

### Advanced Usage
```python
from main import BlinkingLED

# Create LED with custom settings
led = BlinkingLED(pin_number=5, blink_interval=0.5)

# Change interval while running
led.set_interval(2.0)

# Check status
status = led.get_status()
print(f"LED status: {status}")

# Stop blinking
led.stop_blinking()
```

## Project Structure

```
BlinkingLed/
├── main.py          # Main LED blinking program
├── config.py        # Configuration settings
├── requirements.txt # Project dependencies
└── README.md        # This file
```

## Hardware Setup

### Using Built-in LED
Most microcontrollers have a built-in LED that can be used without additional hardware.

### Using External LED
If you want to use an external LED:

1. Connect the positive leg (anode) of the LED to the GPIO pin
2. Connect the negative leg (cathode) of the LED to a resistor (220Ω-1kΩ)
3. Connect the other end of the resistor to ground (GND)

```
GPIO Pin → LED(+) → LED(-) → Resistor → GND
```

## Troubleshooting

### Common Issues

1. **LED not blinking:**
   - Check the pin number in `config.py`
   - Verify the LED connections
   - Ensure the microcontroller is powered

2. **Wrong blink interval:**
   - Modify `BLINK_INTERVAL` in `config.py`
   - Restart the program after changes

3. **Import errors:**
   - Ensure all files are uploaded to the microcontroller
   - Check that MicroPython is properly installed

### Debug Mode

Enable debug output by setting `ENABLE_DEBUG = True` in `config.py` to see detailed information about the LED status.

## Customization

### Adding Multiple LEDs
```python
from main import BlinkingLED

# Create multiple LED instances
led1 = BlinkingLED(pin_number=2, blink_interval=1.0)
led2 = BlinkingLED(pin_number=3, blink_interval=0.5)

# Run them in sequence or parallel
```

### Adding Patterns
You can extend the `BlinkingLED` class to add custom blinking patterns:

```python
def blink_pattern(self, pattern):
    """Blink with a custom pattern (list of on/off durations)"""
    for duration in pattern:
        self.led.on()
        sleep(duration)
        self.led.off()
        sleep(duration)
```

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project!
