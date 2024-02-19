# Frequenz Common API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

<!-- Here goes notes on how to upgrade from previous versions, including deprecations and what they should be replaced with -->

## New Features

- Added a field named `source` to `MetricSample` to allow the user to identify
  the source of the metric, in case different sensors in component report
  metrics with the same `Metric` variant.

- Added 3 new metric variants for inverter temperatures:
  - `METRIC_INVERTER_TEMPERATURE_CABINET`
  - `METRIC_INVERTER_TEMPERATURE_HEATSINK`
  - `METRIC_INVERTER_TEMPERATURE_TRANSFORMER`

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
