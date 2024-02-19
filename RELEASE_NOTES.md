# Frequenz Common API Release Notes

## Summary

This release contains minor updates to the API, including new metric variants,
and a new field in `MetricSample` to identify the source of the metric.

## New Features

- Added a field named `source` to `MetricSample` to allow the user to identify
  the source of the metric, in case different sensors in component report
  metrics with the same `Metric` variant.

- Added 3 new metric variants for inverter temperatures:
  - `METRIC_INVERTER_TEMPERATURE_CABINET`
  - `METRIC_INVERTER_TEMPERATURE_HEATSINK`
  - `METRIC_INVERTER_TEMPERATURE_TRANSFORMER`
