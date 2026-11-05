TIL how to organize dependencies in large codebases with UV.
--
Imagine a vast Python project. And at the top level it is broken into many interconnected components.

[UV workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces/) allow each component to be managed more independently but tied together by a shared dependency `project.toml` file.

so in the top level project.toml:

```toml
[project]
...
[tool.uv.workspace]
members = ["packages/*"]
```

Alternatively, for more well define sub-projects, they can be included as independent projects:

```toml
[tool.uv.sources]
bird-feeder = { path = "packages/bird-feeder" }
```

& looks like '[tach'](https://github.com/tach-org/tach?tab=readme-ov-file) is a good tool to track dependency graphs. 