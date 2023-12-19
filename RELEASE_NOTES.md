# Frequenz Common API Release Notes

## Summary

This release adds new features, and fixes the documentation of a few messages.

## Upgrading

- This release does not contain breaking changes in terms of protobuf definitions.
  However, when upgrading, applications may need to be adjusted to work with the new additions.

## New Features

- Adds ability to specify static bounds in the `Component` message.

- Adds protobuf definition necessary for Electricity Trading (and for Ancillary Services Market).

## Bug Fixes

- Fixes `SensorData` and `ComponentData` doc examples to correctly reflect differences in respective values.
