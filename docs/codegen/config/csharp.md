# CSharpTarget

The `CSharpTarget` class is a subclass of `Target` 
that is used to configure the code generation for CSharp.

## Configuration Options

### `language`

> - Required

Set the `language` field to `"csharp"` to generate CSharp code.

### `path`

> - Required

The `path` field is a string that specifies the path to generate the code.

### `namespace`

> - Required

The `namespace` specifies namespace of the generated classes.

### `typingBackend`

> - Optional
> - Default: `System.Text.Json`
> - Possible values: `System.Text.Json`

The `typingBackend` field specifies the implementation of the typing system.

Currently, only `System.Text.Json` is supported. (See <https://jsontypedef.com/docs/csharp-codegen/> for more information)
