from classes import *
from functions import *
from converters import *

def main():
	
	# Set human parameters
	human = Target({
		'pupil_radius': 0.75,
		'pupil_inter_distance': mm_to_m(5),
		'tl_efficiency': 1.0,
	})

	# Set iphone parameters
	iphone = Device({
		'lens_focal_length': mm_to_m(4.15),
		'lens_aperture_width': mm_to_m(1.86),
		'spotlight_power': 1,
		'spotlight_radius': 1,
		'spotlight_spread_angle': 0.0,
		'spotlight_median_wavelength': nm_to_m(555.0),
		'sensor_width': mm_to_m(4.8),
	})

	# Assign target and device
	target = human.data
	device = iphone.data

	# Run calculations
	L = max_resolvable_distance(target, device)
	E = max_sensor_irradiance(target, device)
	W = max_scanning_width(target, device)

	# Print results
	print("THEORETICAL LIMITS:")
	print("---------------------------")
	print("MAX SENSOR IRRADIANCE {:.2f} W/m^2".format(E))
	print("MAX RESOLVABLE DISTANCE {:.2f} m".format(L))
	print("MAX SCANNING WIDTH {:.2f} m".format(W))


# Start the show
# -----------------------------
if __name__ == '__main__':
	main()