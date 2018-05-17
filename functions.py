import math

def max_resolvable_distance(target, device):
	# Returns max resolvable distance via angular resolution in meters
	inter_distance = target['pupil_inter_distance']
	aperture_width = device['lens_aperture_width']
	median_wavelength = device['spotlight_median_wavelength']
	return (inter_distance * aperture_width) / (1.22 * median_wavelength)

def max_viewing_angle(target, device):
	# Returns max viewing angle in degrees
	focal_length = device['lens_focal_length']
	resolution_width = device['sensor_width']
	rad = 2 * math.atan(resolution_width / (2 * focal_length))
	return math.degrees(rad)

def max_scanning_width(target, device):
	# Returns max scanning width via max viewing angle and max distance in meters
	max_distance = max_resolvable_distance(target, device)
	viewing_angle = max_viewing_angle(target, device)
	half_viewing_angle = math.radians(viewing_angle / 2)
	half_width = max_distance * math.tan(half_viewing_angle)
	return 2 * half_width

def area_circle(radius):
	# Returns the area of a circle given radius
	return math.pi * (radius ** 2)

def area_after_divergence(angle, radius, distance):
	# Returns beam projected area after distance
	delta_radius = distance * math.tan(math.radians(angle))
	projected_radius = radius + delta_radius
	return math.pi * (projected_radius ** 2)

def max_sensor_irradiance(target, device):
	# Returns max irradiance (assumes reflection beam is parallel)
	power_spotlight = device['spotlight_power']
	area_pupil = area_circle(target['pupil_radius'])
	distance = max_resolvable_distance(target, device)
	area_spotlight_projected = area_after_divergence(
		device['spotlight_spread_angle'],
		device['spotlight_radius'],
		distance
	)
	coefficient = target['tl_efficiency']
	return (coefficient * power_spotlight * area_pupil) / area_spotlight_projected