from parametric_simulation import run_two_parameter_parametric
from post_processor import get_2D_results
import numpy as np

eplus_run_plus = './energyplus9.5/energyplus'
idf_path = './1ZoneUncontrolled_win_1.idf'
this_output_dir = './param_exp_2'
parameter_key_0 = ['WindowMaterial:SimpleGlazingSystem',
					'SimpleWindow:DOUBLE PANE WINDOW',
					'solar_heat_gain_coefficient']
parameter_vals_0 = np.arange(0.25, 0.76, 0.1)
parameter_key_1 = ['WindowMaterial:SimpleGlazingSystem',
                   'SimpleWindow:DOUBLE PANE WINDOW',
                   'u_factor']
parameter_vals_1 = np.arange(1.0, 2.6, 0.3)

output_paths = run_two_parameter_parametric(eplus_run_plus, idf_path, this_output_dir,
								parameter_key_0, parameter_vals_0,
								parameter_key_1, parameter_vals_1)
print(output_paths)
p_o, max_y = get_2D_results(output_paths)
print(parameter_key_0, p_o.split('_')[0])
print(parameter_key_1, p_o.split('_')[1])