# Contributing

Changes come through PRs that TJ reviews.

1. Branch from the latest `main`.
2. Make one change per PR, and title it `type(scope): summary`, such as `fix(main): handle an empty category`.
3. Open the PR. `PR Title`, the three `Lint` checks and `Docker Build` run on it, and a dry run of the release names the version the merge would ship ([docs/CICD.md](docs/CICD.md)).
4. Update the `docs/` page that owns the topic in the same PR, and add a decision record when the PR makes a decision.

Every merge to `main` releases the image to Docker Hub, and the PR title sets the bump.

Build and run it in Docker, so nothing installs on your machine:

```shell
docker build -t better-lighter-pack:dev .
docker run --rm better-lighter-pack:dev
docker run --rm better-lighter-pack:dev python main.py trips/Wonderland.csv
```

There are no tests yet, so run the script against the files in `trips/` and compare the output with what you expect.
