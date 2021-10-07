# image_bg_removal
Remove background form given set of images

**The virtual environment is managed by Pipenv**

* Install Pipenv https://pipenv.pypa.io/en/latest/
    ```powershell
        pip install pipenv
    ```

* Initialize the environment from the repository(This will install the python 3.8 with the required dependencies from the Pipefile.lock)
    ```powershell
        pipenv install
    ```

    ![Environment Initialization](https://github.com/dragonfoxsl/image_bg_removal/blob/main/readme/install_env.png)

* Run the script
    ```powershell
        pipenv run python .\remove_bg.py
    ```

    ![Script Execution](https://github.com/dragonfoxsl/image_bg_removal/blob/main/readme/script_run.png)