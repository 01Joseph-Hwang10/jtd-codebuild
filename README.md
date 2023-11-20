# JSON Type Definition Code Build

jtd-codebuild is a tool for generating language specific schemas and interfaces code from JSON Type Definition IDL files in yaml format.

This tool is built on top of [`jtd-codegen`](https://jsontypedef.com/) so check out the documentation if you don't have a clue about JSON Type Definition.

## Prerequisites

- Python
  - [pyyaml](https://pyyaml.org/)
- [jtd-codegen](https://jsontypedef.com/docs/jtd-codegen/)

## Installation

```bash
pip install jtd-codebuild
```

## Usage

```bash
jtd-codebuild path/to/the/folder/where/jtd-codebuild.json/is/located
```


## Required conventions

### Configuration

The script will find `jtd-codebuild.json` which is the configuration file of this tooling.

#### `root-schema-path`

The path to the root schema file. 
Root schema file will be the entry point of the code generation, 
where every definition files will be merged into.

Defaults to `schema.jtd.yaml`

#### `definitions-path`

The path to the definitions directory.
This directory will be recursively searched for definition files.

Definition file is a file that contains a single or multiple definitions.
Checkout the documentation below for more information.

Defaults to `definitions`

#### `output-schema-path`

The path for the merged schema file converted in json format.

Defaults to `gen/schema.jtd.json`

#### `includes`

Array of JTD package paths to include.

The path should have `jtd-codegen.json` file in it 
so that this tool can find the codegen configuration.

If you specifiy a package path,
it will reference the package's schema definitions 
when generating schema file you are working on.

Defaults to `[]`

#### `targets`

Compile targets.

It's a JSONRecord contains the object having following properties:
  - `language (string)`: The language of the target.
                We essentially inject this value to `jtd-codegen` as target language option
                which is provided as a flag which is like `--{language}-out`.
                Available languages can be found in the documentation of `jtd-codegen`. 
                (See: https://jsontypedef.com/)
  - `path (string)`: The path to the directory where the generated code will be placed.

##### `targets` - Language Specific Options - Python

- `use-pydantic (boolean)`: Whether to use pydantic as a `dataclass` decorator provider.
                            If this is set to true, the generated code will use `pydantic.dataclasses.dataclass` as a `dataclass` decorator so that you can use pydantic's validation features.
                            Otherwise, the generated code will be plain python dataclasses.
                            Defaults to `false`.

##### `targets` - Language Specific Options - TypeScript

- `tsconfig-path (string)`: The path to the tsconfig file.
                   This will be used to compile typescript code 
                   to javascript code and type declarations.
                   If you want to generate plain javascript artifact with type declarations, 
                   you should also provide this option.


### Configuration Example

Example congfiguration file is provided below. Copy it and modify it to your needs.

```jsonc
{
  "root-schema-path": "schema.jtd.yaml",
  "definitions-path": "definitions",
  "output-schema-path": "gen/schema.jtd.json",
  "targets": [
    {
      "language": "python",
      "path": "gen/python"
    },
    {
      "language": "typescript",
      "path": "gen/typescript",
      "tsconfig-path": "tsconfig.build.json"
    }
  ]
}
```

### Root Schema File

Root schema file is the entry point of the code generation. 

It will be the file where every definition files will be merged into.

If you don't need a root `Schema` type, you can just create an empty file.

### Definition files

Definition files are sharable files of which each of them contains a single or multiple definitions.

Each declared keys as a root key in the definition file will be merged as a key of `definitions` object in the root schema file, and those symbols can be shared across the other definition files.

For example, let's say you have a definition file whose code is like below.

```yaml
book:
  properties:
    id:
      type: string
    title:
      type: string
```

This can be referenced in other definition files like below.

```yaml
user:
  properties:
    id:
      type: string
    name:
      type: string
    books:
      elements:
        ref: book
```

This will be merged as a single schema like below.

```json
{
  "definitions": {
    "book": {
      "properties": {
        "id": {
          "type": "string"
        },
        "title": {
          "type": "string"
        }
      }
    },
    "user": {
      "properties": {
        "id": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "books": {
          "elements": {
            "ref": "book"
          }
        }
      }
    }
  }
}
```

Checkout more about `ref` if you don't have a clue about it. https://jsontypedef.com/docs/jtd-in-5-minutes/#ref-schemas

### Manual dependency management

Since IDL files are basically just a bunch of JSON objects,
we need to manually manage the dependency between the definition files.

For example, assume you have a folder structure like the below:

```
definitions
├── book
│   └── book.jtd.yaml
└── user
    └── user.jtd.yaml
```

And assume that `book.jtd.yaml` and `user.jtd.yaml` are the root definition files of each module.

In this case, you need to annotate that `user.jtd.yaml` depends on `book.jtd.yaml` like below.

```yaml
# user.jtd.yaml
#
# Depends on:
#   - book (at ../book/book.jtd.yaml)
user:
  properties:
    id:
      type: string
    name:
      type: string
    books:
      elements:
        ref: book
```
