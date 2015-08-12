# Reading Barcode with Webcam in Python
The sample demonstrates how to create a simple Webcam Barcode reader in Python.

![image](http://www.codepool.biz/wp-content/uploads/2015/08/webcam_barcode_result.png)

Installation
-------------
* Dynamsoft Barcode SDK: http://www.dynamsoft.com/Downloads/Dynamic-Barcode-Reader-Download.aspx
* Python: https://www.python.org/ftp/python/
* NumPy: http://sourceforge.net/projects/numpy/files/NumPy/
* SciPy: http://sourceforge.net/projects/scipy/files/scipy/
* OpenCV: http://sourceforge.net/projects/opencvlibrary/files/opencv-win/

How to Run
-----------
1. Copy **\<opencv_installation_dir\>\build\python\2.7\x86\cv2.pyd** to **\<Python27\>\Lib\site-packages\cv2.pyd**
1. Build Dynamsoft Barcode Reader library for Python. Please refer to https://github.com/Dynamsoft/Dynamsoft-Barcode-Reader/tree/master/samples/Python
2. Copy **DynamsoftBarcodeReader.pyd** and **DynamsoftBarcodeReaderx64.dll** / **DynamsoftBarcodeReaderx86.dll** to the project folder.
3. Connect a Webcam to your PC. Make sure you have installed the Webcam driver.
4. Open **cmd.exe**, locate your project folder and type in ``python webcam_barcode_reader.py``
5. Press **Enter** to capture a frame and then recognize Barcodes.
6. Press **ESC** to close the program.

Blog
----
[Reading Barcode with Webcam in OpenCV and Python][1]

[1]:http://www.codepool.biz/opencv-python-webcam-barcode-reader.html
