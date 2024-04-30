# Inheritance

By default, [JSON Type Definition][jsontypedef.com] does not support inheritance.

But by using `jtd-codebuild`, you can define inheritance between type definitions.
You can do this by using `extends` keyword like below.

```yaml
Person:
  properties:
    id:
      type: string
    name:
      type: string

Chef:
  extends: Person
  properties:
    restaurant:
      type: string

HeadChef:
  extends: Chef
  properties:
    sousChef:
      ref: Chef
```

You can also extend multiple types like below.

```yaml
Person:
  properties:
    id:
      type: string
    name:
      type: string

MyRestaurantMixin:
  properties:
    restaurant:
      type: string

Chef:
  extends: [Person, MyRestaurantMixin]
```

If a class or classes are given in the `extends` keyword, the properties of the parent classes are merged into the child class.

> [!IMPORTANT]
> Note that this feature does not programatically inherit the classes in the generated code.
> It only merges the properties of the parent schemas into the child schema.

[jsontypedef.com]: https://jsontypedef.com/docs/
[jtd-codegen]: https://jsontypedef.com/docs/jtd-codegen/
