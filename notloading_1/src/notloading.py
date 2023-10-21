

#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
left_motor_a = Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)
left_motor_b = Motor(Ports.PORT18, GearSetting.RATIO_6_1, True)
left_motor_c = Motor(Ports.PORT17, GearSetting.RATIO_6_1, True)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b, left_motor_c)
right_motor_a = Motor(Ports.PORT10, GearSetting.RATIO_6_1, False)
right_motor_b = Motor(Ports.PORT9, GearSetting.RATIO_6_1, False)
right_motor_c = Motor(Ports.PORT8, GearSetting.RATIO_6_1, False)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b, right_motor_c)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 299.24, 323.84999999999997, 260.731, MM, 0.75)
hugger = DigitalOut(brain.three_wire_port.a)
hanger = DigitalOut(brain.three_wire_port.b)
controller_1 = Controller(PRIMARY)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")


def when_started1():
    global myVariable
    drivetrain.set_stopping(HOLD)
    drivetrain.set_drive_velocity(80, PERCENT)
    pass


# define variables used for controlling motors based on controller inputs
drivetrain_l_needs_to_be_stopped_controller_1 = False
drivetrain_r_needs_to_be_stopped_controller_1 = False

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global drivetrain_l_needs_to_be_stopped_controller_1, drivetrain_r_needs_to_be_stopped_controller_1, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            
            # calculate the drivetrain motor velocities from the controller joystick axies
            # left = axis3 + axis1
            # right = axis3 - axis1
            drivetrain_left_side_speed = controller_1.axis3.position() + controller_1.axis1.position()
            drivetrain_right_side_speed = controller_1.axis3.position() - controller_1.axis1.position()
            
            # check if the value is inside of the deadband range
            if drivetrain_left_side_speed < 5 and drivetrain_left_side_speed > -5:
                # check if the left motor has already been stopped
                if drivetrain_l_needs_to_be_stopped_controller_1:
                    # stop the left drive motor
                    left_drive_smart.stop()
                    # tell the code that the left motor has been stopped
                    drivetrain_l_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the left motor next
                # time the input is in the deadband range
                drivetrain_l_needs_to_be_stopped_controller_1 = True
            # check if the value is inside of the deadband range
            if drivetrain_right_side_speed < 5 and drivetrain_right_side_speed > -5:
                # check if the right motor has already been stopped
                if drivetrain_r_needs_to_be_stopped_controller_1:
                    # stop the right drive motor
                    right_drive_smart.stop()
                    # tell the code that the right motor has been stopped
                    drivetrain_r_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the right motor next
                # time the input is in the deadband range
                drivetrain_r_needs_to_be_stopped_controller_1 = True
            
            # only tell the left drive motor to spin if the values are not in the deadband range
            if drivetrain_l_needs_to_be_stopped_controller_1:
                left_drive_smart.set_velocity(drivetrain_left_side_speed, PERCENT)
                left_drive_smart.spin(FORWARD)
            # only tell the right drive motor to spin if the values are not in the deadband range
            if drivetrain_r_needs_to_be_stopped_controller_1:
                right_drive_smart.set_velocity(drivetrain_right_side_speed, PERCENT)
                right_drive_smart.spin(FORWARD)
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)

#endregion VEXcode Generated Robot Configuration

# Begin project code
1.57

#endregion VEXcode Generated Robot Configuration
myVariable = 0

def when_started1():
    global myVariable
    pass

def onevent_controller_1buttonA_pressed_0():
    global myVariable
    if hugger.value():
        hugger.set(False)
    else:

        hugger.set(True)


def onevent_controller_1buttonL2_pressed_0():
    global myVariable
    if hanger.value():
        hanger.set(False)
    else:
        hanger.set(True)


# system event handlers
controller_1.buttonA.pressed(onevent_controller_1buttonA_pressed_0)
controller_1.buttonL2.pressed(onevent_controller_1buttonL2_pressed_0)

# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

when_started1()
    

def autonomous():
    
    drivetrain.drive_for(FORWARD, 48, INCHES)
    for i in range(5):

        drivetrain.turn_for(LEFT, 9, DEGREES)
        drivetrain.drive_for(FORWARD, 5, INCHES)
    
    


def driver_control():
    drivetrain.set_stopping(HOLD)
    drivetrain.set_drive_velocity(100, PERCENT)