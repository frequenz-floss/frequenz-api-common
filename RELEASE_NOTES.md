# Frequenz Common API Release Notes

## Summary

This release introduces several breaking changes, new features, and improvements to the existing API. The most significant changes include renaming and restructuring of the `components` package to `electrical_components`, the introduction of new diagnostic codes, and the addition of new messages for communication components and streaming events.

## Upgrading

- Removed:

    + `microgrid.components.ComponentStatus`, use `microgrid.electrical_components.ElectricalComponentControlMode` instead
    + `ComponentErrorCode.UNDERVOLTAGE_SHUTDOWN`, use `ElectricalComponentDiagnosticCode.UNDERVOLTAGE` instead
    + `microgrid.sensors.SensorMetric`, use `metrics.Metric` instead
    + `microgrid.sensors.SensorMetricSample`, use `metrics.MetricSample` instead
    + `microgrid.sensors.SensorCategory`, since it was not useful and potentially confusing

        Sensors can report different sensor metrics, and they could belong to several of these categories simultaneously. This defeats the purpose of having singular categories for sensors. Some more useful categorization may be introduced again in the future.

- Renamed several symbols to increase consistency and clarity:

    + `microgrid.components`:

        * The whole package and all proto files, messages, field, enums were renamed to `electrical_components`
        * `ComponentCategoryMetadataVariant` to `ElectricalComponentCategorySpecificInfo`
        * `ComponentCategory` to `ElectricalComponentCategory`
        * `Component.category_type` to `ElectricalComponent.category_specific_info`
        * `ComponentCategoryMetadataVariant.metadata` to `ElectricalComponentCategorySpecificInfo.kind`
        * `ComponentErrorCode` to `ElectricalComponentDiagnosticCode`
        * `ComponentState` to `ElectricalComponentStateSnapshot`
        * `ComponentState.sampled_at` to `ElectricalComponentStateSnapshot.origin_time`
        * `ComponentData` to `ElectricalComponentTelemetry` (to better specify its purpose of encapsulating general telemetry data from electrical components)
        * `ComponentData.states` to `ElectricalComponentTelemetry.state_snapshots`
        * Grid-related terms to clarify their meaning and purpose:

            + `COMPONENT_CATEGORY_GRID` to `ELECTRICAL_COMPONENT_CATEGORY_GRID_CONNECTION_POINT`
            + `ComponentCategoryMetadataVariant.metadata.grid` to `ElectricalComponentCategorySpecificInfo.kind.grid_connection_point`
        * `InverterType.INVERTER_TYPE_SOLAR` to `InverterType.INVERTER_TYPE_PV` (to align with the more colloquial term "PV inverter")
        * `ComponentCategory.COMPONENT_CATEGORY_RELAY` to `ElectricalComponentCategory.ELECTRICAL_COMPONENT_CATEGORY_BREAKER` (to better align with the common terminology used in electrical engineering).
        * All contents of all the files in the `electrical_components` directory (previously `components`) are now moved into the `electrical_components.proto` file.

    + `microgrid.sensors`:

        * `SensorErrorCode` to `SensorDiagnosticCode`
        * `SensorData` to `SensorTelemetry` (to better specify its purpose of encapsulating general telemetry data from sensors)
        * `SensorState` to `SensorStateSnapshot`
        * `SensorData.states` to `SensorTelemetry.state_snapshots`
        * `SensorState.sampled_at` to `SensorStateSnapshot.origin_time`
        * `SensorStateCode.SENSOR_STATE_CODE_ON` to `SensorStateCode.SENSOR_STATE_CODE_OK` (to better indicate that we do not control on/off state of sensors)

    + `metrics`:

        * The file `metric_sample.proto` to `metrics.proto`
        * `MetricSample.source` to `MetricSample.connection`
        * `MetricSample.sampled_at` to `sample_time`

    + `metrics.Metric`:

       * The enum variants to follow a more consistent naming scheme of core-concept to modifier.
       * `METRIC_AC_APPARENT_POWER*` to `METRIC_AC_POWER_APPARENT*`
       * `METRIC_AC_ACTIVE_POWER*` to `METRIC_AC_POWER_ACTIVE*`
       * `METRIC_AC_REACTIVE_POWER*` to `METRIC_AC_POWER_REACTIVE*`
       * `METRIC_AC_APPARENT_ENERGY*` to `METRIC_AC_ENERGY_APPARENT*`
       * `METRIC_AC_ACTIVE_ENERGY*` to `METRIC_AC_ENERGY_ACTIVE*`
       * `METRIC_AC_REACTIVE_ENERGY*` to `METRIC_AC_ENERGY_REACTIVE*`

    + `types`:

        * The whole package has been renamed to `type`.

- Renumbered some enum values to remove unnecessary gaps:

    + `microgrid.components.ComponentCategory` (`microgrid.electrical_components.ElectricalComponentCategory`)
    + `microgrid.components.ComponentErrorCode` (`microgrid.electrical_components.ElectricalComponentDiagnosticCode`)
    + `metrics.Metric`

- The minimum allowed version of `protobuf` and `grpcio` has been updated to 6.31.1 and 1.72.1 respectively, you might also need to bump your dependencies accordingly.

- The file `location.proto` has been moved to the `types` package, moving the message `Location` to `types.Location`.

- The type of the field `metrics.MetricSample.connection` has been changed from `string` to `metrics.MetricConnection`. The latter is a newly added message that provides a better categorization of the connection type.

- The `v1` package has been renamed to `v1alpha7`. The current `v1` package now consists of the contents the same directory from the v0.6.x branch, which is the latest stable version of the API.

- The enum `ComponentCategory` (now `ElectricalComponentCategory`) has been extended with new variants.

## New Features

Added many new messages and enum values:

- `microgrid.communication_components`: Package with message definitions for communication components

    + `CommunicationComponentDiagnostic`: Message to represent warnings and errors in microgrid communication components
    + `CommunicationComponentStateSnapshot`: Message to represent the state of communication components

- `microgrid.electrical_components` (previously `microgrid.components`)

    + `ElectricalComponentDiagnostic`: Message to represent warnings and errors in microgrid electrical components
    + `ElectricalComponentDiagnosticCode` (previously `ComponentErrorCode`): New diagnostic codes to cover more cases, especially for inverters
    + `InverterType.INVERTER_TYPE_WIND_TURBINE`: Enum value to represent wind turbine inverters

- `microgrid.ElectricalComponentCategory` (previously `microgrid.ComponentCategory`) has been extended with new enum values:
    + `ELECTRICAL_COMPONENT_CATEGORY_PLC`
    + `ELECTRICAL_COMPONENT_CATEGORY_STATIC_TRANSFER_SWITCH`
    + `ELECTRICAL_COMPONENT_CATEGORY_UNINTERRUPTIBLE_POWER_SUPPLY`
    + `ELECTRICAL_COMPONENT_CATEGORY_CAPACITOR_BANK`
    + `ELECTRICAL_COMPONENT_CATEGORY_SMART_LOAD`
    + `ELECTRICAL_COMPONENT_CATEGORY_WIND_TURBINE`

- `microgrid.sensors`

    + Message linking microgrid and sensor IDs
    + `SensorDiagnostic`: Message to represent warnings and errors in microgrid sensors
    + Added warnings to sensor `SensorState`

- `streaming`: Package with message definitions for streaming events

    + `Event`: Enum to represent different types of streaming events (Created, Deleted, Updated)

- `types`

    + `Interval`: Message to standardize time interval filtering across APIs

        This uses `start_time` (inclusive) and `end_time` (exclusive) fields, aligning with ISO 8601 and common programming conventions.

