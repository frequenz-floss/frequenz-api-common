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

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
