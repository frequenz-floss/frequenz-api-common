# Frequenz Common API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

<!-- Here goes notes on how to upgrade from previous versions, including deprecations and what they should be replaced with -->

## New Features

- `microgrid.pools.PoolPowerReport` reports how a service sets the power of a pool of electrical components, as seen from a priority: the target power, the power the components are set to now and when they are expected to reach the target, the power the proposals at that priority got, the bounds still available to them, and the power of components the service can't control. Its `ElectricalComponentPowerReport` entries give each component's setpoints and `PowerOutcome`, or the `ExclusionReason` it is left out for.
- `metrics.ResamplingFunction` names how the values of a metric within one resampling interval are combined: average, minimum, maximum, latest value, or sum.

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
