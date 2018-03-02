# Python virtual environment install

## Install virtual environment

`$ sudo -H pip2 install virtualenv virtualenvwrapper`

`$ sudo -H pip3 install virtualenv virtualenvwrapper`

`$ echo "# Virtual Environment Wrapper"  >> ~/.bashrc`

`$ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc`

`$ source ~/.bashrc`

## create a virtual environment (for python2)

`$ mkvirtualenv ve-py2 -p python2`

`$ workon ve-py2`
  
now install python libraries within this virtual environment

`$ pip install numpy scipy matplotlib scikit-image scikit-learn ipython`
  
quit virtual environment

`$ deactivate`

## create a virtual environment (for python3)

`$ mkvirtualenv ve-py3 -p python3`

`$ workon ve-py3`
  
now install python libraries within this virtual environment

`$ pip install numpy scipy matplotlib scikit-image scikit-learn ipython`
  
quit virtual environment

`$ deactivate`


# Create symlink in virtual environment after OpenCV installed
Depending upon Python version you have, paths would be different. 
OpenCV’s Python binary (`cv2.so`) can be installed either in directory site-packages or dist-packages. 
Use the following command to find out the correct location on your machine.

`$ find /usr/local/lib/ -type f -name "cv2*.so"`

It should output paths similar to one of these (or two in case OpenCV was compiled for both Python2 and Python3).
For Python 2 (note the version could be different than this):

`/usr/local/lib/python2.7/dist-packages/cv2.so`

For Python 3 (note the version could be different than this):

`/usr/local/lib/python3.5/dist-packages/cv2.cpython-35m-x86_64-linux-gnu.so`

To link the library for Python 2:

`$ cd ~/.virtualenvs/ve-py2/lib/python2.7/site-packages`

`$ ln -s /usr/local/lib/python2.7/dist-packages/cv2.so cv2.so`
  
To link the library for Python 3:

`$ cd ~/.virtualenvs/ve-py3/lib/python3.6/site-packages`

`$ ln -s /usr/local/lib/python3.6/dist-packages/cv2.cpython-36m-x86_64-linux-gnu.so cv2.so`


