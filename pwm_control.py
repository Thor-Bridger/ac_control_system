import gpiod
from gpiod.line import Direction, Value
import time

CHIP_PATH = "/dev/gpiochip0" 

def run_duty_cycle(duty_cycle, freq_hz, pin_num):
    PIN_NUM = pin_num

    period = 1.0 / freq_hz
    """Run a simple duty cycle on the specified GPIO pin."""
    print(f"Running duty cycle on GPIO {PIN_NUM} with {duty_cycle*100}% duty cycle...")

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
            # Turn ON
            request.set_value(PIN_NUM, Value.ACTIVE)
            time.sleep(on_time)
            
            # Turn OFF
            request.set_value(PIN_NUM, Value.INACTIVE)
            time.sleep(off_time)