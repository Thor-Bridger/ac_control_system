from pwm_control import run_duty_cycle

# Based on your system output, this is the ONLY chip that controls the header pins.


if __name__ == "__main__":
    try:
        usr_input = input("Enter duty cycle (0.0 to 1.0): ")
        usr_duty_cycle = 1.0-float(usr_input.strip())

        run_duty_cycle(duty_cycle=usr_duty_cycle, freq_hz=500, pin_num=21) 
    except KeyboardInterrupt:
        print("\nStopped.")
    except TypeError:
        print("Invalid input. Please enter a number between 0.0 and 1.0.")