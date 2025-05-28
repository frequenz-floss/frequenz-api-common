# Frequenz Common API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

- The `ElectricalComponentStatus` enum has ben removed in favour of the `ElectricalComponentControlMode` enum.

## New Features

- Renamed `components` to `electrical_components` and related messages, fields, enums.
- Added message linking microgrid and sensor IDs.
- Added new message definitions for communication components.
- Added new message `ElectricalComponentDiagnostic` to represent warnings and errors in microgrid electrical components.
- The enum `ComponentErrorCode` has now been renamed to `ElectricalComponentDiagnosticCode` to better reflect its shared usage with warnings and errors.
- Added new message `SensorDiagnostic` to represent warnings and errors in microgrid sensors.
- The enum `SensorErrorCode` has now been renamed to `SensorDiagnosticCode` to better reflect its shared usage with warnings and errors.
- Added warnings to sensor `SensorState`.
- Added a common `TimeIntervalFilter` message in `frequenz.api.common.v1.types` to standardize time interval filtering across APIs. This uses `start_time` (inclusive) and `end_time` (exclusive) fields, aligning with ISO 8601 and common programming conventions.
- Added new message `CommunicationComponentDiagnostic` to represent warnings and errors in microgrid communication components.
- Added new message `CommunicationComponentStateSnapshot` to represent the state of communication components.
- Added new message definitions for streaming events (Deleted, Created, Updated)
- Remove unnecessary gap in numbering in the `ElectricalComponentCategory` enum.
- Renumber variants in the `Metric` enum to remove unnecessary gaps.
- Added a new enum `ElectricalComponentControlMode` to define control modes for electrical components.
- Renamed `metric_sample.proto` to `metrics.proto` to better reflect its content.
- Renamed electrical component category `COMPONENT_CATEGORY_GRID` to `ELECTRICAL_COMPONENT_CATEGORY_GRID_CONNECTION_POINT` to clarify its meaning. Note that the change in the enum change is a part of a larger refactoring of the electrical component category enum.
- The oneof variant `ComponentCategoryMetadataVariant.metadata.grid` has been renamed to `ElectricalComponentCategorySpecificInfo.info.grid_connection_point` to better reflect its purpose.
- A new inverter type `INVERTER_TYPE_WIND_TURBINE` has been added to the `InverterType` enum.
- Renamed `ComponentCategoryMetadataVariant` to `ElectricalComponentCategorySpecificInfo`.
- Renamed field `ElectricalComponent.category_type` to `ElectricalComponent.category_specific_info` to better reflect its purpose.
- Renamed `ElectricalComponentState` to `ElectricalComponentStateSnapshot` to better reflect its purpose.
- Renamed `SensorState` to `SensorStateSnapshot` to better reflect its purpose.
- Renamed `sampled_at` timestamps for state snapshots to `origin_time`.
- Renamed `sampled_at` timestamps for metric samples to `sample_time`.
- Remove `SensorMetricSample` in favour of using `MetricSample` for sensors.
- Remove `SensorMetric` enum, since it was unused and redundant.
- Renamed `MetricSample.source` to `MetricSample.connection` to make it more specific as to what it refers to.
- Rename `SensorStateCode.SENSOR_STATE_CODE_ON` to `SensorStateCode.SENSOR_STATE_CODE_OK`, to better indicate that we do not control on/off state of sensors.
- Rename `ComponentData` to `ElectricalComponentTelemetry` to better specify its purpose of encapsulating general telemetry data from electrical components.
- Rename `SensorData` to `SensorTelemetry` to better specify its purpose of encapsulating general telemetry data from sensors.
- The following changes have been made to the `ElectricalComponentDiagnosticCode` enum (previously `ComponentErrorCode`):
    - The code `UNDERVOLTAGE_SHUTDOWN` has been removed in favour of `UNDERVOLTAGE`.
    - New diagnostic codes have been added to cover more cases, especially for inverters.
    - The codes have been renumbered.
- Removed `SensorCategory` enum, since it was not useful and potentially confusing. Sensors can report different sensor metrics, and they could belong to several of these categories simultaneously. This defeats the purpose of having singular categories for sensors. We need to rethink how to categorize sensors. Until then, having it does not add any value, and therefore it has been removed.

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
