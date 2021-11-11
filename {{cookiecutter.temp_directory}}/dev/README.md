# GLAM Workbench development

This directory contains information and tools for people developing their own GLAM Workbench repositories.

## Configuring the GitHub repository

To allow GitHub actions to push Docker images to quay.io, you need to create the follow GitHub secrets:

* `QUAY_USERNAME`: user name of the quay.io robot account
* `QUAY_PASSWORD`: password of the quay.io robot account

See the [repo2Docker GitHub Action](https://github.com/marketplace/actions/repo2docker-action) documentation for more information on setting up a robot account.

To write the repository description (extracted from the `README`) to quay.io, you also need to set the following secret:

* `API_KEY__QUAY_IO`: quay.io API token

See the [Update Container Description](https://github.com/christian-korneck/update-container-description-action ) documentation for more informatio.

## Setting up your local environment

* Create and activate a Python virtual environment (Python >= 3.8 should be ok). I use [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv).
* Clone this repository
* Run `pip install pip-tools`
* Run `pip-compile requirements.in` – generates `requirements.txt`
* Run `pip-compile dev-requirements.in` – generates `dev-requirements.txt`
* Run `pip-sync requirements.txt dev-requirements.txt` – installs latest versions of required packages
* Run `jupyter lab` – start Jupyter
* Make notebooks!

## Adding new requirements

As you develop your notebooks, you'll probably want to add some addition Python packages.

* Add required package to `requirements.in`
* Run `pip-compile requirements.in` – to update `requirements.txt`
* Run `pip-sync requirements.txt` – to install new packages

If you've been using `pip` to install things directly rather than `pip-tools`, you might have lost track of which packages you've imported into your notebooks. The `list_imports.py` script looks for imports in notebooks and creates a `requirements-tocheck.in` file that you can check and copy into `requirements.in` as required. This won't include packages that aren't directly imported, and others where the package name is different to the import.

## Updating packages

Every now and then you'll want to update your Python packages to keep everything up-to-date.

* Run `pip-compile --upgrade`
* Run `pip-sync`

## Pushing to GitHub

* Best to work in a new branch – `git checkout -b update`
* Delete the contents of the `.binder` directory if it exists – this is a pointer to the latest Docker image, if you don't delete it, you won't be able to test your changes on Binder. It gets generated automatically when a new Docker image is created.
* Make changes...
* Add and commit your changes.
* `git push origin update` – push changes to 'update' branch on Github
* Go to GitHub repository > Pull requests, and create a pull request based on commits to update branch.
* A Github Action will run that uses `repo2docker` to build and cache an image on Binder. A button will be added as a comment on the pull requests that points Binder to the current branch/commit. This enables you to test your changes using Binder before merging them into the master branch.
* If it's all ok, then merge the pull request.
* A GitHub action runs that uses `repo2docker` to generate a Docker image and upload it to quay.io. A tag pointing to the image is added to the repo so that Binder will use the pre-built image. The action also creates an `index.ipynb` notebook from `README.md`.

## Preparing for release

See these [notes on version numbering](https://github.com/GLAM-Workbench/glam-workbench.github.io/discussions/11). 

To have versions automatically archived in Zenodo, you have to [give Zenodo access to your GitHub account](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content), and configure it to listen for any new releases from the repository.

The `update_versions.sh` script in the `dev` directory helps you update various files so that you're ready to create a new release on GitHub. Just give it the name of the new version, eg: `./update_versions v0.1.0.`.

* Make sure notebooks are listed in `README.md`
* Run the `update_versions.sh` script, supplying the tag of the new version. This will update `README.md` and `zenodo.json` with the new version details.
* Push changes to GitHub as above.
* Go to GitHub and create a new release, using the version name as the release name and the tag.