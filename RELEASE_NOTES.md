# Frequenz Common API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

<!-- Here goes notes on how to upgrade from previous versions, including deprecations and what they should be replaced with -->

## New Features

- Renamed `components` to `electrical_components` and related messages, fields, enums.
- Added message linking microgrid and sensor IDs.
- Added new message definitions for communication components.
- Added new message `ElectricalComponentDiagnostic` to represent warnings and errors in microgrid electrical components.
- The enum `ComponentErrorCode` has now been renamed to `ElectricalComponentDiagnosticCode` to better reflect its shared usage with warnings and errors.

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
