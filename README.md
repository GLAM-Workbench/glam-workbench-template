# GLAM Workbench repository template

This is a template to create a new repository for the GLAM Workbench. 

## Setup

### Create a repository from this template

1. Click the big green **Use this template** button.
2. Enter a name for your new repository and click **Create repository from template**
3. Head over to the created repository and complete the setup.

### Configure authentication

In order to complete the process you'll need to create a personal access token and attach it to the new repository.

1. From your GitHub account's dropdown menu (top right of screen) go to **Settings** > **Developer settings** > **Personal access tokens**.
2. Click on the **Generate new token** button.
3. In the 'Note' field, give your key a meaningful label.
4. Check the box next to 'Workflow'.
5. Click on the green **Generate token** buttom at the bottom of the screen.
6. Your new token will be displayed – copy it!
7. Go to the new repository you created above.
8. From the repository's **Settings** menu, select **Secrets** > **Actions**.
9. Click on the **New repository secret** button.
10. In the 'Name' field enter `REPO_SETUP_TOKEN`.
11. In the 'Value' field paste your token from above.
12. Click on the green **Add secret** button.

That's it. The set up process will use the token, then delete the secret when it's finished.

### Complete repository setup

1. In the new repository, click on the `cookiecutter.json` file to open it, then click on the pencil icon to start editing.
2. Add the necessary configuration settings (see below) to `cookiecutter.json`.
3. When you've finished, click on the green **Commit changes** button.
4. The 'Setup Repository Action' will be triggered to complete the configuration of your repository. Click on the 'Actions' tab to see what's happening.
5. Once the action completes, you're ready to go!

This template is based on @stefanbuck's [cookiecutter-template](https://github.com/stefanbuck/cookiecutter-template).

### Configuration settings

There's a few values that you need to set in `cookiecutter.json`.

* `project_name` – this will be the name of the corresponding section in the GLAM Workbench and will probably be either the name of a GLAM organisation, or a specific collection, eg: 'Trove newspapers', 'National Museum of Australia'.
* `project_description` – a brief description for the README
* `creators` – add your name and ORCID id to the nested `creators_list`. This is used to pre-populate the `.zenodo.json` metadata file and can be changed later.

The other values can be left as they are.

## Your new repository

Your new repository will contain the following files, updated by `cookiecutter` to use the config values you supplied via `cookiecutter.json`:

* `README.md` – a README template, edit as required
* `LICENSE`
* `CONTRIBUTING.md` – guidelines for developing your new repository
* `requirements.in` – a list of Python packages needed to run notebooks
* `dev-requirements.in` – additional packages needed for development
* `runtime.txt` – set Python version
* `sample_notebook.ipynb` – a basic example notebook
* `jupyter_config.json` – configuration for Voilá
* `.zenodo.json` – metadata for integration with Zenodo
* `reclaim-manifest.jps` – config file to allow one-click installation on Reclaim Cloud
* `.github/cache_pull_request.yml` – GitHub action that runs when a pull request is created, and builds and caches an image for testing on Binder
* `.github/docker_push.yml` – GitHub action that runs on merge/push, generates a Docker image and uploads it to Quay.io
* `update_version.sh` – development utility script to update version numbers (see below for usage)
* `pyproject.toml` – configuration for development environment
* `.pre-commit-config.yaml` – configuration for development environment
* `list_imports.py` – development utility script (see below for usage)
* `test_and_lint.sh` – development utility script (see below for usage)

Make sure you have a look at `CONTRIBUTING.md` for more information on developing your new repository.

