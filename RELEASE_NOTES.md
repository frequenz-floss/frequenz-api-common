# Frequenz Common API Release Notes

## Summary

Added `model` and `operational_mode` fields to electrical components and sensors, deprecating separate `manufacturer` and `model_number` fields.

## Upgrading

- The following fields have been deprecated in the package `v1alpha8`, and will be removed in a future release:
  - `microgrid.electrical_components.ElectricalComponent.manufacturer` (string): The manufacturer of the electrical component.
  - `microgrid.electrical_components.ElectricalComponent.model_number` (string): The model number of the electrical component.
  - `microgrid.sensors.Sensor.manufacturer` (string): The manufacturer of the sensor.
  - `microgrid.sensors.Sensor.model_number` (string): The model number of the sensor.

## New Features

- The following new entities have been added to the package `v1alpha8`:
  - Enum `microgrid.electrical_components.ElectricalComponentOperationalMode`: Enumeration of the possible operational modes of an electrical component - inactive, telemetry-only, control-only, and control-and-telemetry.
  - Field `microgrid.electrical_components.ElectricalComponent.operational_mode`: Defines if an electrical component is active, if it provides telemetry data, and if it accepts control commands.
  - Field `microgrid.electrical_components.ElectricalComponent.model`: The model name of the electrical component, including the manufacturer and model number.
  - Field `microgrid.sensors.Sensor.model`: The model name of the sensor, including the manufacturer and model number.

## Bug Fixes

- None
