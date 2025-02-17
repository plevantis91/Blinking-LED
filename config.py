"""
Configuration file for LED Blinking Project
Modify these settings to customize the LED behavior
"""

# LED Configuration
LED_PIN = 2  # GPIO pin number for the LED
BLINK_INTERVAL = 1.0  # Blink interval in seconds

# Board-specific configurations
# Uncomment the configuration for your specific board:

# ESP32/ESP8266 Configuration
# LED_PIN = 2  # Built-in LED on most ESP boards
# BLINK_INTERVAL = 0.5

# Raspberry Pi Pico Configuration
# LED_PIN = 25  # Built-in LED on Pico
# BLINK_INTERVAL = 1.0

# Arduino Nano 33 IoT Configuration
# LED_PIN = 13  # Built-in LED
# BLINK_INTERVAL = 0.8

# Custom LED Configuration
# LED_PIN = 5  # Custom pin for external LED
# BLINK_INTERVAL = 2.0

# Advanced Settings
ENABLE_DEBUG = True  # Enable debug output
SAVE_ENERGY = False  # Enable power saving mode (slower blinking)

# Power saving mode settings (when SAVE_ENERGY = True)
POWER_SAVE_INTERVAL = 5.0  # Blink interval when in power save mode
POWER_SAVE_CYCLES = 3  # Number of blinks before entering power save
