# License: MIT
# Copyright © 2023 Frequenz Energy-as-a-Service GmbH

"""Tests for the frequenz.api.common package."""


def test_package_import() -> None:
    """Test that the package can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common import v1alpha7

    assert v1alpha7 is not None


def test_module_import_decimal() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.type import decimal_pb2

    assert decimal_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.type import decimal_pb2_grpc

    assert decimal_pb2_grpc is not None


def test_module_import_metrics_bounds() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.metrics import bounds_pb2

    assert bounds_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.metrics import bounds_pb2_grpc

    assert bounds_pb2_grpc is not None


def test_module_import_metrics_metrics() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.metrics import metrics_pb2

    assert metrics_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.metrics import metrics_pb2_grpc

    assert metrics_pb2_grpc is not None


def test_module_import_grid() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7 import grid

    assert grid is not None


def test_module_import_grid_delivery_area() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.grid import delivery_area_pb2

    assert delivery_area_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.grid import delivery_area_pb2_grpc

    assert delivery_area_pb2_grpc is not None


def test_module_import_microgrid() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7 import microgrid

    assert microgrid is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.microgrid import microgrid_pb2

    assert microgrid_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.microgrid import microgrid_pb2_grpc

    assert microgrid_pb2_grpc is not None


def test_module_import_microgrid_lifetime() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.microgrid import lifetime_pb2

    assert lifetime_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.microgrid import lifetime_pb2_grpc

    assert lifetime_pb2_grpc is not None


def test_module_import_microgrid_electrical_components() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.microgrid import electrical_components

    assert electrical_components is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.microgrid.electrical_components import (
        electrical_components_pb2,
    )

    assert electrical_components_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.microgrid.electrical_components import (
        electrical_components_pb2_grpc,
    )

    assert electrical_components_pb2_grpc is not None


def test_module_import_microgrid_communication_components() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.microgrid import communication_components

    assert communication_components is not None

    from frequenz.api.common.v1alpha7.microgrid.communication_components import (
        communication_components_pb2,
    )

    assert communication_components_pb2 is not None

    from frequenz.api.common.v1alpha7.microgrid.communication_components import (
        communication_components_pb2_grpc,
    )

    assert communication_components_pb2_grpc is not None


def test_module_import_location() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.type import location_pb2

    assert location_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.type import location_pb2_grpc

    assert location_pb2_grpc is not None


def test_module_import_pagination() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7 import pagination

    assert pagination is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.pagination import pagination_info_pb2

    assert pagination_info_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.pagination import pagination_info_pb2_grpc

    assert pagination_info_pb2_grpc is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.pagination import pagination_params_pb2

    assert pagination_params_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1alpha7.pagination import pagination_params_pb2_grpc

    assert pagination_params_pb2_grpc is not None
