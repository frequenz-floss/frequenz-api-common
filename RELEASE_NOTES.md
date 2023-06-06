# Frequenz Common API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

* The submodule URL was changed to use HTTPS instead of SSH (to avoid problems trying to unlock SSH keys to do updates, etc.).

  Make sure you sync your submodules to the new URL:

  ```console
  $ git submodule sync
  Synchronizing submodule url for 'submodules/api-common-protos'
  ```

* [`EVChargerType` enum refactored](https://github.com/frequenz-floss/frequenz-api-common/pull/21)

  The enum with the oder variants was compiled into the following rust enum
  (by prost):
  ```rust
  pub enum EvChargerType {
      /// Default type.
      EvchargerTypeUnspecified = 0,
      /// The EV charging station supports AC charging only.
      EvchargerTypeAc = 1,
      /// The EV charging station supports DC charging only.
      EvchargerTypeDc = 2,
      /// The EV charging station supports both AC and DC.
      EvchargerTypeHybrid = 3,
  }
  ```
  Here the enum variants were unnecessarily prefixed with `EvchargerType`.
  This lead to accessing the enum variants in a very verbose manner, e.g.,
  `EvChargerType::EvchargerTypeHybrid`.

  The changed version of the enum in this commit results in the following
  rust enum:
  ```rust
  pub enum EvChargerType {
      /// Default type.
      Unspecified = 0,
      /// The EV charging station supports AC charging only.
      Ac = 1,
      /// The EV charging station supports DC charging only.
      Dc = 2,
      /// The EV charging station supports both AC and DC.
      Hybrid = 3,
  }
  ```
  Here the unnecessary prefix `EvchargerType` is absent. This reduces the
  verbosity while accessing the enum variants, making the resulting rust code
  more readable, e.g., as `EvChargerType::Hybrid`.

  This change also leads to renaming the enum from `EVChargerType` to
  `EvChargerType`, to satisfy protolint requirements.
## New Features

<!-- Here goes the main new features and examples or instructions on how to use them -->

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
