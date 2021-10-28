# EasyCaptureFLIR

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

# REFERENCES 
* [EasyPySpin](https://github.com/elerac/EasyPySpin)
* [simple_pyspin](https://github.com/klecknerlab/simple_pyspin)

Script developed to acquire RGB image from a FLIR Camera

##  Thanks to simple_pyspin
A Pythonic class-based wrapper for the FLIR PySpin Library.

More documentation can be found on [Github Pages](https://klecknerlab.github.io/simple_pyspin/), and the source can be found on [Github](https://github.com/klecknerlab/simple_pyspin).

**Note: Please do not contact me with support issues.  I do not have time to troubleshoot installation issues -- if there are bugs feel free to post an issue on Github, but it is unlikely I will resolve it.**

## Why?
Why does this even exist, as the PySpin module already exists?  Because it's a pain to use, and difficult to wrap your head around basic operations.  For example, on some camera manually setting frame rate requires accessing methods by finding nodes, which is quite complicated.  This library makes it incredibly simple, and can also auto-document all the features of your *specific* cameras for easy reference.  

## Installation
1. If you don't already have them, I would recommend installing Numpy and the Python Imaging Library.  The easiest way to do this is to install a scientific Python distribution like [Anaconda](https://www.anaconda.com/distribution/).
2. [Install Spinnaker and PySpin from FLIR.](https://www.flir.com/products/spinnaker-sdk/)  
    - You will likely need to follow several manual steps after the Spinnaker installation to get PySpin ([Mac Instructions](https://www.flir.com/support-center/iis/machine-vision/application-note/getting-started-with-spinnaker-sdk-on-macos/,))
3. Install simple_pyspin module:
    - Install from PyPi: `pip install simple-pyspin`.
    - Download source from GitHub and use `setup.py`.
   
## External Links
Here are some external links that are useful for using Spinnaker SDK.
* [Spinnaker® SDK Programmer's Guide and API Reference (C++)](http://softwareservices.ptgrey.com/Spinnaker/latest/index.html)
* [Getting Started with Spinnaker SDK on MacOS Applicable products](https://www.flir.com/support-center/iis/machine-vision/application-note/getting-started-with-spinnaker-sdk-on-macos/)
* [Spinnaker Nodes](https://www.flir.com/support-center/iis/machine-vision/application-note/spinnaker-nodes/)
* [Configuring Synchronized Capture with Multiple Cameras](https://www.flir.com/support-center/iis/machine-vision/application-note/configuring-synchronized-capture-with-multiple-cameras)

