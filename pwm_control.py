import gpiod
from gpiod.line import Direction, Value
import time
import queue


CHIP_PATH = "/dev/gpiochip0"

def turn_off(pin_num):
    PIN_NUM = pin_num
    with gpiod.request_lines(
        CHIP_PATH,
        consumer="turn-off",
        config={
            PIN_NUM: gpiod.LineSettings(
                direction=Direction.OUTPUT,
                output_value=Value.INACTIVE
            )
        }
    ) as request:   

        request.set_value(PIN_NUM, Value.INACTIVE)

def run_duty_cycle(duty_cycle_queue, freq_hz, pin_num):
    
    duty_cycle = 0.0
    PIN_NUM = pin_num
    period = 1.0 / freq_hz

    
    

    with gpiod.request_lines(
        CHIP_PATH,
        consumer="duty-cycle-test",
        config={
            PIN_NUM: gpiod.LineSettings(
                direction=Direction.OUTPUT,
                output_value=Value.INACTIVE
            )
        }
    ) as request:
        on_time = period * duty_cycle
        off_time = period - on_time

        while True:
            
            if not duty_cycle_queue.empty():
                duty_cycle = duty_cycle_queue.get()
                duty_cycle_queue.task_done()
                on_time = period * duty_cycle
                off_time = period - on_time
                print("Real duty cycle:", duty_cycle)

            else:
                pass

            try:

                # Turn ON
                request.set_value(PIN_NUM, Value.ACTIVE)
                time.sleep(on_time)
                
                # Turn OFF
                request.set_value(PIN_NUM, Value.INACTIVE)
                time.sleep(off_time)

            except KeyboardInterrupt:
                request.set_value(PIN_NUM, Value.INACTIVE)