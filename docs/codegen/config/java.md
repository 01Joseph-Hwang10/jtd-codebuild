# JavaTarget

The `JavaTarget` class is a subclass of `Target` 
that is used to configure the code generation for Java.

## Configuration Options

### `language`

> - Required

Set the `language` field to `"csharp"` to generate Java code.

### `path`

> - Required

The `path` field is a string that specifies the path to generate the code.

### `package`

> - Required

The `package` specifies package name of the generated classes.

### `typingBackend`

> - Optional
> - Default: `jackson`
> - Possible values: `jackson`

The `typingBackend` field specifies the implementation of the typing system.

Currently, only `jackson` is supported. (See <https://jsontypedef.com/docs/java-codegen/> for more information)
