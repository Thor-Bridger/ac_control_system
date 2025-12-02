from pwm_control import run_duty_cycle, turn_off
import threading
import time
import queue

# Based on your system output, this is the ONLY chip that controls the header pins.


def main():

    duty_queue = queue.Queue()
    fan_control_thread = threading.Thread(target=run_duty_cycle, args=(duty_queue, 500, 21))
    fan_control_thread.start()


    while True:
        try:
            usr_input = input("Enter duty cycle (0.0 to 1.0): ")
            usr_duty_cycle = 1.0-float(usr_input.strip())
            duty_queue.put(usr_duty_cycle)
            time.sleep(1)
        except KeyboardInterrupt:
            print("Exiting...")
            break


main()