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
                 time_difference_for_integral, time_difference_for_derivative,
                 time_difference_for_input_units,
                 max_array_length=1000,
                 verbose=False):
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
        self.time_difference_for_integral = float(time_difference_for_integral)
        self.time_difference_for_derivative = float(time_difference_for_derivative)
        self.time_difference_for_input_units = float(time_difference_for_input_units)
        self.max_array_length = int(max_array_length)
        self.verbose = bool(verbose)

        self.time_measurements = []
        self.input_measurements = []
        self.output_measurements = []

        self.running_sum = 0.0
        self.start_time = None

        self.running_derivative = 0.0
        self.derivative_counter = 0

        self.data_length = 0

    def record_measured_data(self, input, output):
        self.time_measurements.append(time.time())
        self.input_measurements.append(input)
        self.output_measurements.append(output)
        data_length = len(self.time_measurements)
        if self.max_array_length < data_length:
            self.time_measurements = self.time_measurements[-1 * self.max_array_length:]
            self.input_measurements = self.input_measurements[-1 * self.max_array_length:]
            self.output_measurements = self.output_measurements[-1 * self.max_array_length:]
            self.data_length = self.max_array_length
        else:
            self.data_length = data_length
        if self.start_time is None:
            self.start_time = self.time_measurements[0]
        if self.verbose:
            print("Input:", input, " Output:", output)

    def get_new_set_point(self):
        input_measurements = np.array(self.input_measurements, dtype="float")
        output_measurements = np.array(self.output_measurements, dtype="float")
        input_of_latest_measurement = input_measurements[-1]
        time_array = np.array(self.time_measurements)

        time_of_latest_measurement = time_array[-1]
        # The arrays below need to all be the same length, N - 1, where N is the length of the time_array
        time_difference_array = time_array[1:] - time_array[:-1]
        output_difference_array = self.goal_output - np.array(output_measurements[1:])
        input_change_array = np.array(input_measurements[1:]) - np.array(input_measurements[:-1])
        output_change_array = np.array(output_measurements[1:]) - np.array(output_measurements[:-1])
        if self.data_length < 2:
            raise Exception("The record_measured_data method must be call twice before " +
                            "using the method getNewSetPoint.")

        """
        Calculate proportional term
        """
        output_difference = output_difference_array[-1]

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

        """
        Calculate integral terms
        """
        self.running_sum += output_difference * time_difference_array[-1]
        if self.time_difference_for_integral == float("inf"):
            running_sum_in_output_units = self.running_sum / (time_of_latest_measurement - self.start_time)
            # in output units
            integral_term = integral_constant * running_sum_in_output_units
        else:
            # start with the M - 1 index where M is the length of the output_difference_array
            integral_time_sum = 0.0
            for index_for_integral_calculation in reversed(range(len(time_difference_array))):
                # count the time backwards from the last measurement
                # until self.time_difference_for_integral is less than integral_time_sum
                integral_time_sum += time_difference_array[index_for_integral_calculation]
                if self.time_difference_for_integral < integral_time_sum:
                    # this stops the loop and saves the index where
                    # self.time_difference_for_integral is less than integral_time_sum
                    break
            output_differences_to_use_for_integral_term = output_difference_array[index_for_integral_calculation:]
            time_differences_to_use_for_integral_term = time_difference_array[index_for_integral_calculation:]
            # calculate the integral array
            integral_in_output_and_time_units = np.sum(output_differences_to_use_for_integral_term
                                                       * time_differences_to_use_for_integral_term)
            # normalize the integral to be comparable to the proportional terms
            # (this is a mean instead of a sum on N points)
            norm_integral_in_output_and_time_units = integral_in_output_and_time_units \
                                                     / float(len(output_differences_to_use_for_integral_term))



            # convert out of output times time units
            norm_integral_in_output_units = norm_integral_in_output_and_time_units / np.mean(time_differences_to_use_for_integral_term)
            # in output units, and should be comparable to the output_difference / integral_constant
            # due to the mean. This is not a true integral, but rather a running average of the output_difference
            integral_term = integral_constant * norm_integral_in_output_units

        """
        Calculate derivative term
        """
        # used when self.time_difference_derivative == float("inf")
        self.running_derivative += output_difference_array[-1] / time_difference_array[-1]
        self.derivative_counter += 1
        if self.time_difference_for_derivative == float("inf"):
            average_derivative = self.running_derivative / float(self.derivative_counter)
            average_time_difference = (time_of_latest_measurement - self.start_time) / float(self.derivative_counter)
            average_derivative_in_output_units = average_derivative * average_time_difference
            # in output units
            derivative_term = derivative_constant * average_derivative_in_output_units
        else:
            derivative_time_sum = 0.0
            for index_for_derivative_calculation in reversed(range(len(time_difference_array))):
                # count the time backwards from the last measurement
                # until self.time_difference_for_derivative is less than derivative_time_sum
                derivative_time_sum += time_difference_array[index_for_derivative_calculation]
                if self.time_difference_for_derivative < derivative_time_sum:
                    # this stops the loop and saves the index where
                    # self.time_difference_for_derivative is less than integral_time_sum
                    break
            output_differences_to_use_for_derivative_term = output_difference_array[index_for_derivative_calculation:]
            time_differences_to_use_for_derivative_term = time_difference_array[index_for_derivative_calculation:]
            # calculate the derivative
            mean_derivative_in_output_divided_by_time_units = np.sum(output_differences_to_use_for_derivative_term) \
                                                                / np.sum(time_differences_to_use_for_derivative_term)
            # convert to output units
            derivative_in_output_units = mean_derivative_in_output_divided_by_time_units \
                                         * np.mean(time_differences_to_use_for_derivative_term)
            derivative_term = derivative_constant * derivative_in_output_units

        set_term_change_in_output_units = proportional_term + integral_term + derivative_term

        """
        Convert to input units
        """
        input_time_sum = 0.0
        for index_for_input_calculation in reversed(range(len(time_difference_array))):
            # count the time backwards from the last measurement
            # until self.time_difference_for_input is less than input_time_sum
            input_time_sum += time_difference_array[index_for_input_calculation]
            if self.time_difference_for_input_units < input_time_sum:
                # this stops the loop and saves the index where
                # self.time_difference_for_input_units is less than integral_time_sum
                break
        dinput_by_doutput = np.sum(input_measurements[index_for_input_calculation:]) \
                            / np.sum(output_measurements[index_for_input_calculation:])
        # dinput_by_doutput = 1000.
        # convert the set_term_change to the input units
        set_term_change_in_input_units = set_term_change_in_output_units * dinput_by_doutput
        # get the new set term
        set_term = set_term_change_in_input_units + input_of_latest_measurement
        if self.verbose:
            print("set_term:", set_term,
                  "\nchange in set_term input units:", set_term_change_in_input_units,
                  "\nchange in set_term output units:", set_term_change_in_output_units,
                  "\n input to output conversion:", dinput_by_doutput)
            print("(constant_P, constant_I, constant_D) (" +
                  str(proportional_constant) + ", " +
                  str(integral_constant) + ", " +
                  str(derivative_constant) + ")")
            print("(preconstant_P, preconstant_I, preconstant_D) output units (" +
                  str(output_difference) + ", " +
                  str(norm_integral_in_output_units) + ", " +
                  str(derivative_in_output_units) + ")")
            print("(P_term, I_term, D_term) output units (" +
                  str(proportional_term) + ", " +
                  str(integral_term) + ", " +
                  str(derivative_term) + ")")
            print("(P_term, I_term, D_term) input units (" +
                  str(proportional_term * dinput_by_doutput) + ", " +
                  str(integral_term * dinput_by_doutput) + ", " +
                  str(derivative_term * dinput_by_doutput) + ")\n")
        return set_term


# This only runs if executing pid.py directly and not when importing this class into another scripts or file
if __name__ == "__main__":
    import random
    from matplotlib import pyplot as plt
    """
    Example PID code
    """
    # set parameters for the PID function
    goal_output = 17.0
    zone1_difference = 1.2
    zone1_pid = (0.0, 0.2, 0.03)
    zone2_pid = (0.2, 0.0, 0.0)
    # averaging times
    time_difference_for_integral = 1.0  # in seconds
    time_difference_for_derivative = 1.  # in seconds
    time_difference_for_input_units = 1.0  # in seconds
    # initialize the class that holds the pid function
    my_pid =  PID(goal_output, zone1_difference, zone1_pid, zone2_pid,
                  time_difference_for_integral,
                  time_difference_for_derivative,
                  time_difference_for_input_units, verbose=True)
    # time between measurements
    meas_time = 0.1  # in seconds
    """
    Make some fake test data
    """
    # This something that changes the system output that you cannot control
    # like heating from the sun or mass water in a lake from evaporation and rain.
    sine_wave = 10.0 * np.sin(np.arange(0.0, 100.0, 0.01))
    noise = (np.array([random.random() for n in range(len(sine_wave))]) - 0.5)
    externalFunction = sine_wave + noise

    # this is the thing you can control, like the voltage on a resistor or valve on a pipe
    the_device = 10.0 * np.arange(-1.0, 3.0, 0.0001)
    device_max_input = len(the_device) - 1
    device_min_input = 0

    # this is used a lot so I make definition here
    def measurement_loop(counter, my_pid, inputVal):
        externalVal = externalFunction[counter]
        counter += 1
        # wait a some time for the input to take effect
        time.sleep(meas_time)
        """
        This of where a real device will need to be controlled
        """
        # my "device" requires a discrete input value
        discrete_inputVal = int(np.round(inputVal))
        # some error checking to keep the device in the bounds of it's operation
        if discrete_inputVal < 0:
            discrete_inputVal = device_min_input
        elif device_max_input < discrete_inputVal:
            discrete_inputVal = device_max_input
        # In this example the output is a simple function of the inputVal and externalVal
        # but this could be a much more complex relationship.
        outputVal = the_device[discrete_inputVal] + externalVal
        my_pid.record_measured_data(input=discrete_inputVal, output=outputVal)
        return counter, my_pid

    # make a guess at the initial input
    # Example: how much voltage to use, how far to turn a knob
    inputVal = len(the_device) / 2

    # get the first value from the external forcing function
    # Example: how much it rained, how much heat was absorbed
    counter = 0
    # the first measurement loop
    counter, my_pid = measurement_loop(counter, my_pid, inputVal)

    # Change the inputVal by some amount to train the the PID function
    # this action can be repeat a few times but has no benefit after time greater than
    # that of time_difference_for_integral, time_difference_for_derivative, time_difference_for_input_units
    for n in range(5):
        inputVal -= 1000
        counter, my_pid = measurement_loop(counter, my_pid, inputVal)

    # get a new set value from the PID function
    inputVal = my_pid.get_new_set_point()

    counter, my_pid = measurement_loop(counter, my_pid, inputVal)

    # repeat to let the PID function control your input
    for n in range(900):
        # get a new set value from the PID function
        inputVal = my_pid.get_new_set_point()
        counter, my_pid = measurement_loop(counter, my_pid, inputVal)

    leglines = []
    leglabels = []
    leglines.append(plt.Line2D(range(10), range(10),
                               color='green'))
    leglabels.append('Goal')
    leglines.append(plt.Line2D(range(10), range(10),
                               color='firebrick'))
    leglabels.append('External Forces')
    leglines.append(plt.Line2D(range(10), range(10),
                               color='dodgerblue'))
    leglabels.append('Internal Forces')
    leglines.append(plt.Line2D(range(10), range(10),
                               color='darkOrchid'))
    leglabels.append('Total output')
    legendLoc = 0
    legendNumPoints = 3
    legendHandleLength = 4

    plt.plot(my_pid.time_measurements, np.array(my_pid.output_measurements) * 0.0 + goal_output, color='green')
    plt.plot(my_pid.time_measurements, externalFunction[:counter], color='firebrick')
    device_output = []
    for n in my_pid.input_measurements:
        one_device_output = the_device[n]
        device_output.append(one_device_output)
    plt.plot(my_pid.time_measurements, device_output, color='dodgerblue')
    plt.plot(my_pid.time_measurements, my_pid.output_measurements, color='darkOrchid')

    plt.legend(leglines, leglabels, loc=legendLoc, numpoints=legendNumPoints, handlelength=legendHandleLength)

    plt.show()






