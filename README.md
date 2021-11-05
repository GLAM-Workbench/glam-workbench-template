# GLAM Workbench repository template

This is a template to create a new repository for the GLAM Workbench. 

## Setup

### Create a repository from this template

1. Click the big green button `Use this template` or click <a href="../../generate">here</a>.
2. Enter a name for your new repository and click `Create repository from template`
3. Head over to the created repository and complete the setup.

### Complete setup

1. In the a new repository, <a href="../../edit/main/cookiecutter.json">complete the project setup</a> by editing the `cookiecutter.json` file. (See below for config details.) 
1. Hit <kbd>cmd</kbd> + <kbd>S</kbd> and then <kbd>Enter</kbd> to perform a commit (the commit message doesn't really matter).
1. Wait <a href="../../actions">Setup Repository Action</a> to complete.

This template is based on @stefanbuck's [cookiecutter-template](https://github.com/stefanbuck/cookiecutter-template).

### Configuration settings

There's a few values that you need to set in `cookiecutter.json`.

* `project_name` – this will be the name of the corresponding section in the GLAM Workbench and will probably be either the name of a GLAM organisation, or a specific collection, eg: 'Trove newspapers', 'National Museum of Australia'.
* `project_description` – a brief description for the README
* `creators` – add your name and ORCID id to the nested `creators_list`. This is used to pre-populate the `.zenodo.json` metadata file and can be changed later.

The other values can be left as they are.

## Your new repository

Your new repository will contain the following files, updated by `cookiecutter` to use the config values you supplied via `cookiecutter.json`:

* `README.md`
* `LICENSE`
* `requirements.in`
* `dev-requirements.in`
* `runtime.txt`
* `reclaim-manifest.jps`
* `sample_notebook.ipynb`

There's also a `dev` directory that contains useful documentation and scripts for setting up and magaing your repository. Have a look at the `README.md` in the `dev` directory for instructions on getting your new repository running.


