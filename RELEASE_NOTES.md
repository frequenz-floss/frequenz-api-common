# Frequenz Common API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

- The dependency on `googleapis-common-protos` / `googleapis/googleapis` was
  removed, now the built-in `frequenz.api.common.v1.types.Decimal` is used
  internally instead. This is compatible with Google's type, but if you
  depended indirectly on Google's submodule or python packages, you may need to
  update your dependencies.

  Nevertheless it is strongly recommended to remove the dependency on Google
  repos and use the built-in `frequenz.api.common.v1.types.Decimal` instead if
  your project only uses the `Decimal` type from it too.

- Voltage metrics have been renamed from `METRIC_VOLTAGE_PHASE_[1|2|3]` to
  `METRIC_VOLTAGE_PHASE_[1|2|3]_N`.

## New Features

- Added a `Frequenz.api.common.v1.types.Decimal` type, compatible with
  `google.type.Decimal`.

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
