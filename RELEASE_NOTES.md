# Frequenz Common API Release Notes

## Summary

- Removed dependency on `googleapis-common-protos` in favor of internal
`frequenz.api.common.v1.types.Decimal`, advising updates to dependencies for
users previously relying on Google's types.
- Renamed voltage and current metrics for clarity and introduced new metrics,
including line-to-line voltages and Total Harmonic Distortion (THD) metrics,
with updated naming conventions for simplicity and precision.

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

- The variants in the enum `Metric` have been renumberd due to the addition of
  line-to-line voltages.

- Current metrics have been renamed:
  `METRIC_AC_APPARENT_CURRENT` -> `METRIC_AC_CURRENT`
  `METRIC_AC_APPARENT_CURRENT_PHASE_[1|2|3]` -> `METRIC_AC_CURRENT_PHASE_[1|2|3]`

- Metrics for Total Harmonic Distortion have been un-abbreviated:
  `METRIC_AC_THD_CURRENT` -> `METRIC_AC_TOTAL_HARMONIC_DISTORTION_CURRENT`
  `METRIC_AC_THD_CURRENT_PHASE_[1|2|3]` -> `METRIC_AC_TOTAL_HARMONIC_DISTORTION_CURRENT_PHASE_[1|2|3]`

- Renamed `SimpleMetricSample` to `SimpleMetricValue`, because it does not
  contain a timestamp, so it does not represent a sample but a value.

- Renamed `AggregatedMetricSample` to `AggregatedMetricValue`, because it does not
  contain a timestamp, so it does not represent a sample but a value.

- Renamed `MetricSampleVariant` to `MetricValueVariant`.

- Rename `MetricSample.sample` to `MetricSample.value`.

- Rename `SensorMetricSample.sample` to `SensorMetricSample.value`.

## New Features

- Added a `Frequenz.api.common.v1.types.Decimal` type, compatible with
  `google.type.Decimal`.

- The following new metrics have been added:
  - `METRIC_VOLTAGE_PHASE_1_PHASE_2`
  - `METRIC_VOLTAGE_PHASE_2_PHASE_3`
  - `METRIC_VOLTAGE_PHASE_3_PHASE_1`
