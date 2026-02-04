# Frequenz Common API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

<!-- Here goes notes on how to upgrade from previous versions, including deprecations and what they should be replaced with -->

## New Features

- The following new messages have been added:
  - `TransformerRatio`: Represents a single transformer ratio with primary and secondary values.
  - `TransformerRatioThreePhase`: Represents a three-phase transformer ratio, containing individual `TransformerRatio` messages for each phase.
  - `MeterTransformerRatio`: Represents a meter's transformer ratio (either CT or VT) along with its operational lifetime.
  - `Meter`: Represents a meter with lists of current and voltage transformer ratios. Each list contains `MeterTransformerRatio` entries to allow tracking historical configurations.

- The `ElectricalComponentCategorySpecificInfo` message has been updated to include the new `Meter` component category.

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
