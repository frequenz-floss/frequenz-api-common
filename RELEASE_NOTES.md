# Frequenz Common API Release Notes

## Summary

This release adds types for describing aggregated telemetry, for choosing how metrics are resampled, and for reporting on the power of pools of electrical components.

## Upgrading

<!-- Here goes notes on how to upgrade from previous versions, including deprecations and what they should be replaced with -->

## New Features

- `microgrid.pools.PoolPowerReport` reports how a service sets the power of a pool of electrical components, as seen from a priority: the target power, the power the components are set to now and when they are expected to reach the target, the power the proposals at that priority got, the bounds still available to them, and the power of components the service can't control. Its `ElectricalComponentPowerReport` entries give each component's setpoints and `PowerOutcome`, or the `ExclusionReason` it is left out for.
- `microgrid.telemetry.AggregateExpression` describes a value computed from the telemetry of several electrical components: aggregates a service computes from the component graph (`NamedAggregate`), single metrics of single components (`ElectricalComponentMetric`), formulas (`Formula`) and constants, combined with sum, difference, scale, min, max and coalesce.
- `metrics.ResamplingFunction` names how the values of a metric within one resampling interval are combined: average, minimum, maximum, latest value, or sum.

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
