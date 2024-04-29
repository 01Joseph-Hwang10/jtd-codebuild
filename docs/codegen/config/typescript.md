# TypescriptTarget

The `TypescriptTarget` class is a subclass of `Target` 
that is used to configure the code generation for Typescript.

## Configuration Options

### `language`

> - Required

Set the `language` field to `"typescript"` to generate Typescript code.

### `path`

> - Required

The `path` field is a string that specifies the path to generate the code.

### `propertyFormat`

> - Optional
> - Possible values: `snake`, `camel`, `pascal`

The `propertyFormat` field is a string that specifies the format of the property names.

If not given, [jtd-codegen] will handle the property names as they are.

[jtd-codegen]: https://jsontypedef.com/docs/jtd-codegen/