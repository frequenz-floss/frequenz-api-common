# Frequenz Common API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

<!-- Here goes notes on how to upgrade from previous versions, including deprecations and what they should be replaced with -->

## New Features

- The following new entities have been added to the package `v1alpha8`:
  - Enum `microgrid.electrical_components.ElectricalComponentOperationalMode`: Enumeration of the possible operational modes of an electrical component - inactive, telemetry-only, control-only, and control-and-telemetry.
  - Field `microgrid.electrical_components.ElectricalComponent.operational_mode`: Defines if an electrical component is active, if it provides telemetry data, and if it accepts control commands.

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
