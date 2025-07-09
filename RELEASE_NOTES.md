# Frequenz Common API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

<!-- Here goes notes on how to upgrade from previous versions, including deprecations and what they should be replaced with -->

## New Features

- A new package `frequenz.api.common.v1alpha8` has been added. It has the following changes when compared to `frequenz.api.common.v1alpha7`:
  - `electrical_components.Fuse` has been removed.
  - `InverterType.INVERTER_TYPE_WIND_TURBINE` has been removed.
  - `ElectricalComponentConnections.source_component_id` has been renamed to `ElectricalComponentConnections.source_electrical_component_id`
  - `ElectricalComponentConnections.destination_component_id` has been renamed to `ElectricalComponentConnections.destination_electrical_component_id`
  - `ElectricalComponentStateSnapshot.component_id` has been renamed to `ElectricalComponentStateSnapshot.electrical_component_id`
  - `microgrid.MicrogridComponentIds` has been renamed to `microgrid.MicrogridElectricalComponentIds`.
  - `MicrogridComponentIDs.component_ids` has been renamed to `MicrogridElectricalComponentIds.electrical_component_ids`.
  - `electrical_components.VoltageTransformer` has been renamed to `electrical_components.PowerTransformer`, to make the name more consistent with the underlying concept.
  - `ElectricalComponentCategorySpecificInfo.kind.voltage_transformer` has been renamed to `ElectricalComponentCategorySpecificInfo.kind.power_transformer`, to make the name more consistent with the underlying concept.
  - `ElectricalComponentCategory.ELECTRICAL_COMPONENT_CATEGORY_VOLTAGE_TRANSFORMER` has been renamed to `ElectricalComponentCategory.ELECTRICAL_COMPONENT_CATEGORY_POWER_TRANSFORMER`, to make the name more consistent with the underlying concept.
  - The `type` package has been renamed to `types`, to avoid using reserved keywords in programming languages.


## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
