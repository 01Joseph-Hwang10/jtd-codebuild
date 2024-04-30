# `jtd-codebuild <path> init [--preset <preset>]`

This command initializes a `jtd-codebuild.json` file in the given path.

## Usage

```bash
jtd-codebuild <path> init [--preset <preset>]
```

### Arguments

- `<path>`: The path to initialize the `jtd-codebuild.json` file. If this is not provided, the current directory is used.

### Options

- `--preset <preset>`: The preset to use for the initialization. If this is not provided, the `config` preset is used by default. See [Presets](#presets) for available presets.


## Presets

Presets are predefined configurations that can be used to quickly initialize a `jtd-codebuild.json` configuration file and related files.

Currently, 3 presets are available:

- `config`: Initializes a configuration file with default values. If `--preset` is not provided, this preset is used by default.
- `project`: Initializes a configuration file with a project structure.
- `workspace`: Initializes a workspace configuration file.
