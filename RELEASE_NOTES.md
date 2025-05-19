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

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
