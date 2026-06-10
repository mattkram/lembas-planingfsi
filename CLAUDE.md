# lembas-planingfsi

Lembas plugin for planingfsi hydrodynamic simulations.

## Development

### Environment setup

This project uses [pixi](https://pixi.sh) for environment management. All environments are locked via `pixi.lock`.

```bash
# Install dependencies and create environment
pixi install

# Run commands in the environment
pixi run python ...
pixi run pytest
pixi run <task>

# Enter a shell with the environment activated
pixi shell
```

**Never install packages via `pip install` directly.** Add dependencies to `pixi.toml` and run `pixi install`.

### Running tests

```bash
pixi run test
```

## Git conventions

See [commit-conventions.md](https://github.com/lembas-project/lembas-dev/blob/main/conventions/commit-conventions.md) and [pr-conventions.md](https://github.com/lembas-project/lembas-dev/blob/main/conventions/pr-conventions.md).

**Summary:**
- Commits: `<type>: <description>` (feat, fix, docs, refactor, test, chore)
- PRs: Atomic, incremental changes; squash merge via merge queue
- Stack PRs when changes depend on each other

## Build and publish

See [build-publish.md](https://github.com/lembas-project/lembas-dev/blob/main/conventions/build-publish.md) for the standard build and publish workflow.

Key points:
- Conda packages built with `pixi run -e build build`
- Published to `anaconda.org/lembas-project`
- Tagged releases go to `main` label, main branch pushes go to `dev` label

## Architecture

### Case handler

`PlaningPlateCase` in `src/lembas_planingfsi/flat_plate.py`:
- Subclasses `lembas.Case`
- Input parameters: `froude_num`, `angle_of_attack`
- Steps: `create_input_files` → `generate_mesh` → `run_solver`
- Results: `forces()` returns drag, lift, moment via `@result` decorator

### Plugin entry point

Registered in `pyproject.toml`:
```toml
[project.entry-points."lembas.plugins"]
planingfsi = "lembas_planingfsi:Plugin"
```

## Dependencies

Runtime dependencies are specified in `conda.recipe/recipe.yaml`, NOT in `pyproject.toml`. This prevents pip from overriding conda packages during editable installs.

The pixi.toml `[dependencies]` section specifies what's needed for development.
