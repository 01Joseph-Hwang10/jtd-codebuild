# PythonTarget

The `PythonTarget` class is a subclass of `Target` 
that is used to configure the code generation for Python.

## Configuration Options

### `language`

> - Required

Set the `language` field to `"python"` to generate Python code.

### `path`

> - Required

The `path` field is a string that specifies the path to generate the code.

### `propertyFormat`

> - Optional
> - Possible values: `snake`, `camel`, `pascal`

The `propertyFormat` field is a string that specifies the format of the property names.

If not given, [jtd-codegen] will handle the property names as they are.

### `removeRootSchema`

> - Optional
> - Default: `true`

As this tool uses [jtd-codegen] under the hood, it always generates a root schema, named `Schema`.

But there's a case where you don't want the root schema to be generated.

In this case, set the `removeRootSchema` field to `true`.

### `typingBackend`

> - Optional
> - Default: `dataclass`
> - Possible values: `dataclass`, `pydantic`, `pydantic-dataclass`, `typed-dictionary`

The `typingBackend` field specifies the implementation of the typing system.

If not given, `dataclass` typing system will be used, which is used from [jtd-codegen] by default.

### `subscriptable`

> - Optional
> - Default: `false`

The `subscriptable` field is a boolean that specifies whether the generated classes are subscriptable.

This means that schemas can be accessed by index. (e.g. `schema["key"]`)

This option cannot be `true` if `typingBackend` is set to `typed-dictionary`.

[jtd-codegen]: https://jsontypedef.com/docs/jtd-codegen/