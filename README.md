# InMoov Mini 

InMoov Mini is a scaled down (60%) version of [InMoov](http://inmoov.fr)

The Web Based User Interface is based on the [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

## Usage

Install Operating System pre-requisites
```
sudo apt update
sudo apt install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libatlas-base-dev gfortran git python3-dev python3-pip
```

Make python3 the default python interpreter
```
sudo rm /usr/bin/python
sudo ln -s /usr/bin/python3 /usr/bin/python
```

Install NumPy
```
sudo pip install numpy
```

Compile OpenCV
#### Instructions modified from [pyimagesearch.com](https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/)
```
sudo git clone https://github.com/opencv/opencv.git
sudo git clone https://github.com/opencv/opencv_contrib.git
cd opencv
sudo mkdir build
cd build
sudo cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
    -D BUILD_EXAMPLES=ON ..
```

Clone this repo
```
git clone https://github.com/bcarroll/inmoov_mini.git
```

Change to the inmoov_mini directory
```
cd inmoov_mini
```

Install the Python pre-requisite modules
```
sudo pip install -r requirements.txt
```

Setup Flask
```
export FLASK_APP=main.py
```

Setup the database
```
flask db init
flask db migrate
flask db upgrade
```

Start the Web User Interface
```
flask run
```

Open a web browser and navigate to http://inmoov_mini:5000
