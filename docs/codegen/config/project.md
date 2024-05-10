# Project Configuration

`jtd-codebuild <path>` CLI finds the configuration file in the given path and generates the code based on the configuration.

The path should be a folder that contains the configuration file, named `jtd-codebuild.json`.

> [!NOTE]
> The file name should be `jtd-codebuild.json`. No other file name is allowed.

## Configuration Options

### `include`

> - Optional
> - Default: `[]`

The `include` field is an array of files or directories
that contain the JSON Type Definition IDL files.

Glob is supported in the `include` field.

The program will recursively search for given globs and 
include all the files that match the globs.

Note that it will not include the files that are not `.yml`, `.yaml`, or `.json` files
even if they match the globs.

### `references`

> - Optional
> - Default: `[]`

The `references` field is similar to the [include](#include) field.

The difference is that the program treats the files included from the `references`
as an external dependency.

For example, schemas included from the `references` field are allowed to have name conflicts with the schemas in the [include](#include) field, if [duplicate](#duplicate) is set to `allow`.

But in contrast, schemas included from the [include](#include) field are not allowed to have name conflicts at any time.

Note that glob is not supported in the `references` field.

### `jtdBundlePath`

> - Optional
> - Default: `gen/schema.jtd.json`

`jtd-codebuild` program basically merges every json schemas from [include](#include) and [references](#references) fields into one JSON Type Definition file.

The `jtdBundlePath` field is a path to the bundled JSON Type Definition file that is used 
as an intermediate step to generate language-specific code.


### `duplicate`

> - Optional
> - Default: `error`
> - Possible values: `error`, `allow`

`duplicate` field is an option to handle the case 
when there are duplicate schemas in the [references](#references) fields.

If `duplicate` is set to `error`, the program will throw an error when there are duplicate schemas.

If `duplicate` is set to `allow`, the program will overwrite the existing schema with the new schema when there are duplicate schemas.

Here, schemas in [include](#include) fields have precedence over schemas in [references](#references) fields, and references in back have precedence over the references in front.

### `targetProcessingStrategy`

> - Optional
> - Default: `parallel`
> - Possible values: `parallel`, `serial`

`targetProcessingStrategy` field is an option to specifiy the method of processing the targets.

As `serial` option exists for debugging purposes, it is recommended to use `parallel` option for the best performance.

### `targets`

The `targets` field is an array of objects 
that specify the language and the path to generate the code.

Currently, `jtd-codebuild` supports the following targets.
Check each language's configuration for more details.

- [C#](./csharp.md)
- [Go](./go.md)
- [Java](./java.md)
- [Python](./python.md)
- [Ruby](./ruby.md)
- [Rust](./rust.md)
- [Typescript](./typescript.md)

## Substitutes

`jtd-codebuild.json` supports the following substitutes.

- `<projectRoot>`: The root directory of the project. It is same as the directory that `jtd-codebuild.json` is in.
- `<workspaceRoot>`: The root directory of the workspace. `jtd-codebuild` searches for the closest parent which contains `jtd-codebuild-workspace.json` file, and uses that directory as the workspace root. If `jtd-codebuild` fails to find the workspace root, it uses the project root as the workspace root.
