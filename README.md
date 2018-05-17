# Limits

Calculates the theoretical limits of detecting NAEs given target and device variables

## Requirements

* `python2.7`
* `virtualenv`
* `bash`
* `pip`

## Setup

1. Run `virtualenv venv` to setup a virtual environment
2. Activate via `source venv/bin/activate`
3. Run `main.py`

## Usage

Inside `main.py`, you can configure two objects and their parameters. Here's a quick example:

```python
mythical_creature = Target({
	'pupil_radius': 0.75,
	'pupil_inter_distance': mm_to_m(5),
	'tl_efficiency': 1.0,
})

latest_iphone = Device({
	'lens_focal_length': mm_to_m(4.15),
	'lens_aperture_width': mm_to_m(1.86),
	'spotlight_power': 1,
	'spotlight_radius': 1,
	'spotlight_spread_angle': 0.0,
	'spotlight_median_wavelength': nm_to_m(555.0),
	'sensor_width': mm_to_m(4.8),
})
```

Then assign the `target` and `device` for calculation via:

```python
target = mythical_creature.data
device = latest_iphone.data
```

And then calculate via `python main.py`!