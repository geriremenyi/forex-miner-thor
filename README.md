# forex-miner-thor

Trading engine implementation for forex-miner.com. 

The repo's name is coming from the Norse mythology, in which [Thor](https://en.wikipedia.org/wiki/Thor) is a hammer-wielding god associated with thunder, lightning, storms, sacred groves and trees, strength and the protection of mankind.

## Getting started

This chapter guides you through how to quickly setup your development environment.

### Prerequisites

- [Python 3.8.x](https://www.python.org/) to build, run etc.
- [pip](https://pip.pypa.io/en/stable/) to install dependencies
- [PyCharm](https://www.jetbrains.com/pycharm/) (optional) as the IDE.
- [Docker](https://www.docker.com/products/docker-desktop) (optional) to contenarize the engine
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) (optional) to deploy the engine to a kubernetes cluster

### Local setup

1. Clone this repo
```bash
# HTTPS
https://github.com/geriremenyi/forex-miner-asgard.git
# SSH
git@github.com:geriremenyi/forex-miner-asgard.git
```

2. Navigate to the root of the project and create a python virtual environment to handle dependencies for this project in an isolated way
```bash
python -m venv my-environment-name
```

3. Activate the virtual environment created in step 2.
```bash
# Windows
my-environment-name\Scripts\activate.bat
# Unix
source my-environment-name/bin/activate
```

4. Install project dependencies
```bash
pip install -r requirements.txt
```

5. Setup PYTHONPATH
```bash
# Windows
set PYTHONPATH=<root folder of the project on your hard disk>
# Unix
export PYTHONPATH=<root folder of the project on your hard disk>
```

### Run

To run the engine you just have to start the `Flask` server which will listen on the `localhost:31001`.

```bash
python forex_miner_thor/api/api.py
```

### Notebooks

There are some Jupyter notebooks defined under the [notebooks](notebooks) folder. Using these ones, the sample data and backtesting results can be discovered.

To start the jupyter notebook execute the following command.
```bash
jupyter notebook
```

It will open a browser where you can navigate to the folder and see the notebooks.

:warning: It makes sense to comment out or limit the cases of the backtesting based optimization as it runs for around 20 hours.

### Tests

Unit tests can be found under the [unittests folder](tests/unittests). To run the tests just run the following command.
```bash
python -m unittest discover ./tests/unittests
```

## Deployment

This chapter guides you through the CI/CD setup and the deployment steps for the engine.

### GitHub Actions

There are continuous integration and deployment steps setup as GitHub actions to be able to test on every pull-request and to be able to deliver fast. 

#### Continuous integration

All pull request opened against any branches triggers a continuous integration workflow to run.

The steps are defined in the [`continuous_integration.yaml` file](.github/workflows/continuous_integration.yaml).

Recently ran integrations can be found [here](https://github.com/geriremenyi/forex-miner-thor/actions?query=workflow%3A"Continuous+Integration").

#### Continuous deployment

All changes on the [master branch](https://github.com/geriremenyi/forex-miner-thor/tree/master) triggers a deployment to the [kubernetes cluster behind the `forex-miner.com` domain](https://github.com/geriremenyi/forex-miner-asgard).

The steps are defined in the [`continuous_deployment.yaml` file](.github/workflows/continuous_deployment.yaml).

Recently ran deployments can be found [here](https://github.com/geriremenyi/forex-miner-thor/actions?query=workflow%3A"Continuous+Deployment").

To create and deploy a new version of the service run the following:

1. Checkout from [develop branch](https://github.com/geriremenyi/forex-miner-thor/tree/master) and create a new release branch
```shell script
git checkout -b releases/x.y.z
```

2. Bump the version
```shell script
# Bump patch version (x.y.z -> x.y.z+1)
./scripts/bump_version patch
# Bump minor version (x.y.z -> x.y+1.z)
./scripts/bump_version minor
# Bump major version (x.y.z -> x+1.y.z)
./scripts/bump_version minor
```

3. Commit changes
```shell script
git add .
git commit -m "Release x.y.z"
```

4. Checkout, update master and merge it to the release branch
```shell script
git checkout master
git pull
git checkout releases/x.y.z
git merge master --strategy-option ours
```

5. Push it to GitHub
```shell script
git push --set-upstream origin releases/x.y.z
```

6. Open a PR against the [master](https://github.com/geriremenyi/forex-miner-thor/tree/master) and the [develop](https://github.com/geriremenyi/forex-miner-thor/tree/develop) branch

7. After completing the PR against the master branch the CD workflow kicks in and will deploy the new version

### Kubernetes Cluster

The kubernetes deployments are defined under the [k8s folder](k8s).

There is no external resources required for the engine to run, so it is enough to run the following commands to deploy the engine to any kubernetes cluster.
1. If not yet created, create a namespace called `forex-miner`
```bash
kubectl create namespace forex-miner
```
2. Deploy persistent volume
```bash
kubectl apply -f ./k8s/volume.yaml
```
3. Deploy app
```bash
kubectl apply -f ./k8s/app.yaml
```
4. Deploy service (to expose engine API)
```bash
kubectl apply -f ./k8s/service.yaml
```