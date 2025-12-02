from pwm_control import run_duty_cycle, turn_off
import threading
import time

# Based on your system output, this is the ONLY chip that controls the header pins.

global duty_cycle

def fan_control(duty_cycle, freq_hz, pin_num):
    run_duty_cycle(duty_cycle, freq_hz, pin_num)    

def main_code():
    while True:
        time.sleep(1)

if __name__ == "__main__":
    print("PWM Control Started. Press Ctrl+C to stop.")

    try:
        usr_input = input("Enter duty cycle (0.0 to 1.0): ") #Frequency is fixed at 500Hz, pin 21
        usr_duty_cycle = 1.0-float(usr_input.strip())
        fan_control_thread = threading.Thread(target=fan_control, args=(usr_duty_cycle, 500, 21))
        fan_control_thread.start()

        main_thread = threading.Thread(target=main_code)
        main_thread.start()

    except KeyboardInterrupt:
        print("\nPWM Control Stopped.")
        turn_off(21)
