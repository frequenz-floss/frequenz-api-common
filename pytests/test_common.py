# License: MIT
# Copyright © 2023 Frequenz Energy-as-a-Service GmbH

"""Tests for the frequenz.api.common package."""


def test_package_import() -> None:
    """Test that the package can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common import v1

    assert v1 is not None


def test_module_import_metrics_bounds() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.metrics import bounds_pb2

    assert bounds_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.metrics import bounds_pb2_grpc

    assert bounds_pb2_grpc is not None


def test_module_import_metrics_metric_sample() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.metrics import metric_sample_pb2

    assert metric_sample_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.metrics import metric_sample_pb2_grpc

    assert metric_sample_pb2_grpc is not None


def test_module_import_grid() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1 import grid

    assert grid is not None


def test_module_import_grid_delivery_area() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.grid import delivery_area_pb2

    assert delivery_area_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.grid import delivery_area_pb2_grpc

    assert delivery_area_pb2_grpc is not None


def test_module_import_microgrid() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1 import microgrid

    assert microgrid is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.microgrid import microgrid_pb2

    assert microgrid_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.microgrid import microgrid_pb2_grpc

    assert microgrid_pb2_grpc is not None


def test_module_import_microgrid_lifetime() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.microgrid import lifetime_pb2

    assert lifetime_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.microgrid import lifetime_pb2_grpc

    assert lifetime_pb2_grpc is not None


def test_module_import_microgrid_components() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.microgrid import components

    assert components is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.microgrid.components import battery_pb2

    assert battery_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.microgrid.components import battery_pb2_grpc

    assert battery_pb2_grpc is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.microgrid.components import components_pb2

    assert components_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.microgrid.components import components_pb2_grpc

    assert components_pb2_grpc is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.microgrid.components import ev_charger_pb2

    assert ev_charger_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.microgrid.components import ev_charger_pb2_grpc

    assert ev_charger_pb2_grpc is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.microgrid.components import fuse_pb2

    assert fuse_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.microgrid.components import fuse_pb2_grpc

    assert fuse_pb2_grpc is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.microgrid.components import grid_pb2

    assert grid_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.microgrid.components import grid_pb2_grpc

    assert grid_pb2_grpc is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.microgrid.components import inverter_pb2

    assert inverter_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.microgrid.components import inverter_pb2_grpc

    assert inverter_pb2_grpc is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.microgrid.components import transformer_pb2

    assert transformer_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.microgrid.components import transformer_pb2_grpc

    assert transformer_pb2_grpc is not None


def test_module_import_location() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1 import location_pb2

    assert location_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1 import location_pb2_grpc

    assert location_pb2_grpc is not None


def test_module_import_pagination() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1 import pagination

    assert pagination is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.pagination import pagination_info_pb2

    assert pagination_info_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.pagination import pagination_info_pb2_grpc

    assert pagination_info_pb2_grpc is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.pagination import pagination_params_pb2

    assert pagination_params_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common.v1.pagination import pagination_params_pb2_grpc

    assert pagination_params_pb2_grpc is not None
