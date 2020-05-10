## Summary
- [Windows](#for-windows)
- [Linux](#for-linux)

## For Windows
- ### Prerequisites
  - `python 3.6 or above`
- ### Installation
  1. First clone the repository
    ```
    git clone https://github.com/sumagnadas/graph-plotter.git
    ```
  2. Install all the dependencies
    ```
    python -m pip install -r requirements_windows.txt
    ```
  3. Install pycairo
    ```
    cd resources
    pip install pycairo-1.19.1-cp38-cp38-win_amd64.whl
    ```
  4. Now run the script
    ```
    python main.py
    ```

## For Linux
  - ### Prerequisites
    - `python 3.6 or above`
  - ### Installation
    1. First clone the repository
    ```
    git clone https://github.com/sumagnadas/graph-plotter.git
    ```
    2. Install libcairo2-dev<br>
    ##### For Ubuntu/Debian derivatives:
    ```
    sudo apt-get install libcairo2-dev
    ```
    ##### For Fedora:
    ```
    sudo yum install cairo-devel
    ```
    ##### For openSUSE:
    ```
    zypper install cairo-devel
    ```
    3. Install all the other dependencies
    ```
    python -m pip install -r requirements_linux.txt
    ```
    4. Now run the script
    ```
    ./main.py
    ```
