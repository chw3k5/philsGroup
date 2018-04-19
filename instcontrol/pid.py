"""
PID (proportional integral and derivative) functions can be use to control systems by
changing the system's inputs based on measured systems outputs to reach some goal value
for the output. There is considerable literature on the subject in the field of engineering.

The proportional term can be understood simply, it is the
difference between the measured output value and the goal value

The derivative term compares the difference between the measures output
and the goal value changes between measurements as a function of time.
This can be an instantaneous change comparing the difference on the Nth measurement
to the (N - 1)th, or it can be averaged derivative over aa time period.

The integral term, the context of present function, can be considered an average
of the promotional terms oven a moving window of measurements, the sum of N through N - 20,
for example. Sometimes it may be useful (though not implemented in this code)
 to have a PID function with an integral term that
is a running sum from 0 to N. This is useful when something for something like a positional
PID function that is tracking a moving object such as an asteroid.

"""
import time
import numpy as np



class PID:
    def __init__(self, goal_output, zone1_difference, zone1_pid, zone2_pid,
                 time_difference_integral, time_difference_derivative):
        """
        :param goal_output (float): The value you want the PID function to reach.
        :param zone1_difference (float): Once the difference between the goal and the measured value
                                         is less than this value, the code will use the PID parameters
                                         in zone1_pid.
        :param zone1_pid (3-tuple of floats): The first entry in the tuple is the proportional constant,
                                              the second entry is the integral constant, and
                                              the third entry is the derivative constant when in zone 1.
        :param zone2_pid (float): When the difference between the goal and the measured value
                                  is GREATER than the zone1_difference, then
                                  the first entry in the tuple is the proportional constant,
                                  the second entry is the integral constant, and
                                  the third entry is the derivative constant.
        """
        self.goal_output = float(goal_output)
        self.zone1_difference = np.abs(float(zone1_difference))
        self.zone1_pid = (float(zone1_pid[0]), float(zone1_pid[1]), float(zone1_pid[2]))
        self.zone2_pid = (float(zone2_pid[0]), float(zone2_pid[1]), float(zone2_pid[2]))
        self.time_difference_integral = float(time_difference_integral)
        self.time_difference_derivative = float(time_difference_derivative)

        self.time_measurements = []
        self.input_measurements = []
        self.output_measurements = []

        self.running_sum = 0.0
        self.start_time = None

    def re_init(self):
        pass

    def record_measured_data(self, input, output, max_length=1000):
        self.time_measurements.append(time.time())
        self.input_measurements.append(float(input))
        self.output_measurements.append(float(output))
        data_length = len(self.time_measurements)
        if max_length < data_length:
            self.time_measurements = self.time_measurements[-max_length:]
            self.input_measurements = self.input_measurements[-max_length:]
            self.output_measurements = self.output_measurements[-max_length:]
            self.data_length = max_length
        else:
            self.data_length = data_length

        if self.start_time is None:
            self.start_time = self.time_measurements[0]

    def get_new_set_point(self, y_current, y_last, x_last, x_current, error_sum, error_last, Ki, Kp, Kd):
        time_of_latest_measurement = self.time_measurements[-1]
        output_of_latest_measurement = self.output_measurements[-1]
        input_of_latest_measurement = self.input_measurements[-1]
        time_array = np.array(self.time_measurements)
        time_difference_array = time_array[1:] - time_array[:-2]
        input_array = np.array(self.input_measurements)
        output_difference_array = np.array(self.output_measurements) - self.goal_output

        if self.data_length < 2:
            raise Exception("The record_measured_data method must be call twice before " +
                            "using the method getNewSetPoint.")

        # Calculate proportional term
        output_difference = self.goal_output - output_of_latest_measurement

        # select the PID constants
        if np.abs(output_difference) <= self.zone1_difference:
            proportional_constant = zone1_pid[0]
            integral_constant = zone1_pid[1]
            derivative_constant = zone1_pid[2]
        else:
            proportional_constant = zone2_pid[0]
            integral_constant = zone2_pid[1]
            derivative_constant = zone2_pid[2]

        # in units of output
        proportional_term = proportional_constant * output_difference

        # Calculate integral terms
        self.running_sum += output_difference * time_difference_array[-1]
        if self.time_difference_integral == float("inf"):
            # in output units, this
            integral_term = integral_constant * self.running_sum / (time_of_latest_measurement - self.start_time)
        else:
            for start_integral_index in range(self.data_length - 1, 0, -1):
                time_difference = time_of_latest_measurement - self.time_measurements[start_integral_index]
                if self.time_difference_integral < time_difference:
                    start_integral_index -= 1
                    break
            output_differences_to_use_for_integral_term = output_difference_array[start_integral_index + 1:]


            # in output units, and should be comparable to the output_difference / integral_constant
            # due to the mean. This is not a true integral, but rather a running average of the output_difference
            integral_term = integral_constant * np.mean(output_differences_to_use_for_integral_term
                                                        * time_difference_array[start_integral_index])

        # Calculate derivative term
        if self.time_difference_derivative == float("inf"):
            start_derivative_index = 0
        else:
            for start_derivative_index in range(self.data_length - 1, 0, -1):
                time_difference = time_of_latest_measurement - self.time_measurements[start_derivative_index]
                if self.time_difference_integral < time_difference:
                    start_derivative_index -= 1
                    break
        output_differences_to_use_for_derivative_term = np.array(self.output_measurements[start_derivative_index:])







        x_diff = float(x_current-x_last)
        # only needed for moving setpoints, mA_set
        der_error = (output_difference-error_last)/x_diff
        # below is ideal derivative term for a fixed set point, mA_set
        der_error_simple = y_last - y_current

        # the function
        pterm =  * output_difference
        iterm = error_sum
        dterm = Kd*der_error_simple
        # print "pterm:",pterm,'   iterm:',iterm,'   dterm:',dterm
        pid_function_y = pterm + iterm + dterm
        pid_function_x = pid_function_y/der_error
        return pid_function_x, pid_function_y, output_difference, error_sum

# This only runs if executing pid.py directionly and not when importing this class into another scrips or file
if __name__ == "__main__":
    # Example PID code #
    goal_output = 20.0
    zone1_difference = 1.0
    zone1_pid = (0.0 , 1.0, 1.0)
    zone2_pid = (1.0, 0.0, 0.0)
    my_pid =  PID(goal_output, zone1_difference, zone1_pid, zone2_pid)