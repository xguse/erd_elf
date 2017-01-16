Commands
========

The Makefile contains the central entry points for common tasks related to this project.



* `make github_remote` launches a script to create and syncronize a remote github repository for this project.

* `make environment` uses the project's `requirements.txt` file to create and provision a conda environment for this project. Then it registers the conda environment with your local jupyter set up as an ipython kernel with the same name as the conda environment.

* `make clean_env` undoes everything that `make environment` sets up.

* `make serve_nb` starts a jupyter notebook with this project's `notebooks` directory as the root.

* `make clean_bytecode` removes all `__pycache__` directories and leftover `*.pyc` files from the project.
