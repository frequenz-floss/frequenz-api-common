# Frequenz Common API Release Notes

## Summary

Added versioning to the API, added new component category variants, and split
sensors out of components.

## Upgrading

- The package names have been changed from `frequenz.api.common.<package>` to
  `frequenz.api.common.v1.<package>`. `v1` is the API's major version, and will
  be incremented for breaking changes.

- Added `frequenz.api.common.sensors` package, containing the enums
  `SensorCategory` and `SensorType`. Removed the component category variant
  `COMPONENT_CATEGORY_SENSOR` and the enum `SensorType` from
  `frequenz.api.common.components`.

- The component category variant `PRECHARGE_MODULE` has been renamed to
  `PRECHARGER`.

## New Features

- Added a new component category variant: `COMPONENT_CATEGORY_FUSE`.

- Added a new component category variant:
  `COMPONENT_CATEGORY_VOLTAGE_TRANSFORMER`.
