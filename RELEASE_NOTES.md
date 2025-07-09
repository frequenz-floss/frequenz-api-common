# Frequenz Common API Release Notes

## Summary

This release introduces the new `v1alpha8` version of the API, which includes several breaking changes compared to `v1alpha7`. The changes focus on improving consistency and clarity by renaming several symbols and removing unused components.

## Upgrading

- A new package `frequenz.api.common.v1alpha8` has been introduced, containing the following breaking changes from `v1alpha7`.

- Removed:

    + `electrical_components.Fuse`
    + `InverterType.INVERTER_TYPE_WIND_TURBINE`

- Renamed several symbols to increase consistency and clarity:

    + `microgrid`:

        * `MicrogridComponentIds` to `MicrogridElectricalComponentIds`
        * `MicrogridComponentIDs.component_ids` to `MicrogridElectricalComponentIds.electrical_component_ids`

    + `electrical_components`:

        * `ElectricalComponentConnections.source_component_id` to `ElectricalComponentConnections.source_electrical_component_id`
        * `ElectricalComponentConnections.destination_component_id` to `ElectricalComponentConnections.destination_electrical_component_id`
        * `ElectricalComponentStateSnapshot.component_id` to `ElectricalComponentStateSnapshot.electrical_component_id`
        * Transformer-related terms are renamed to align them with power transformers, which are more commonly used in electrical engineering:
            * `electrical_components.VoltageTransformer` to `electrical_components.PowerTransformer`
            * `ElectricalComponentCategorySpecificInfo.kind.voltage_transformer` to `ElectricalComponentCategorySpecificInfo.kind.power_transformer`
            * `ElectricalComponentCategory.ELECTRICAL_COMPONENT_CATEGORY_VOLTAGE_TRANSFORMER` to `ElectricalComponentCategory.ELECTRICAL_COMPONENT_CATEGORY_POWER_TRANSFORMER`

    + `types`:

        * The whole package has been renamed to `types` to avoid using reserved keywords in programming languages.
