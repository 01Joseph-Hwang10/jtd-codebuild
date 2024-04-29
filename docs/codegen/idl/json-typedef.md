# IDL: JSON Type Definition

From [jsontypedef.com],

> JSON Type Definition, aka [RFC 8927][rfc8927], is an easy-to-learn, standardized way to define a schema for JSON data. You can use JSON Typedef to portably validate data across programming languages, create dummy data, generate code, and more.

This tool is based on [jtd-codegen] which is a code generator for JSON Type Definition.

You can find out how to write JSON Type Definition IDL files in the [jsontypedef.com] documentation.

## YAML support

Unlike the original [JSON Type Definition][jsontypedef.com] toolings,
`jtd-codebuild` supports YAML format for writing JSON Type Definition IDL files.

You can either write JSON Type Definition IDL files in JSON or YAML format.

[jsontypedef.com]: https://jsontypedef.com/docs/
[rfc8927]: https://datatracker.ietf.org/doc/html/rfc8927
[jtd-codegen]: https://jsontypedef.com/docs/jtd-codegen/