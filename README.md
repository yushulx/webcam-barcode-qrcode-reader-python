# Reading Barcode and QR Code Using Webcam, Python and OpenCV
The sample demonstrates how to create a simple Webcam Barcode and QR code reader in Python. OpenCV stitcher API is used to stitch multiple barcode and QR code results.

## License Activation
Get a desktop license key from [here](https://www.dynamsoft.com/customer/license/trialLicense?product=dbr) to activate [Dynamsoft Barcode Reader SDK](https://www.dynamsoft.com/barcode-reader/sdk-desktop-server/):

```python
BarcodeReader.init_license("DLS2eyJoYW5kc2hha2VDb2RlIjoiMjAwMDAxLTE2NDk4Mjk3OTI2MzUiLCJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSIsInNlc3Npb25QYXNzd29yZCI6IndTcGR6Vm05WDJrcEQ5YUoifQ==")
```

## Installation

```
pip install opencv-python dbr
```

## Try Example

- [scanner.py](https://github.com/yushulx/webcam-barcode-reader-python/blob/master/scanner.py)
    
    Use webcam to scan barcode and QR code in real-time.

    ![Python barcode and QR code reader](https://www.dynamsoft.com/codepool/img/2022/04/multiple-barcode-qrcode-scan.png)

- [stitcher.py](https://github.com/yushulx/webcam-barcode-reader-python/blob/master/stitcher.py)
    
    Get camera closer to scan more barcode and QR code precisely and then stitch them together as a panorama image.

    ![Python barcode and QR code reader with panorama stitching](https://www.dynamsoft.com/codepool/img/2022/04/panorama-barcode-qr-code.png)

- [barcode_based_panorama.py](https://github.com/yushulx/webcam-barcode-qrcode-reader-python/blob/master/barcode_based_panorama.py)
    
    Concatenate images based on barcode and QR code detection results. No image processing algorithm used.
    
    ![concatenate barcode and QR code images](./output.png)
    
- [barcode_reader.py](https://github.com/yushulx/webcam-barcode-qrcode-reader-python/blob/master/barcode_reader.py)
    
    Used to read barcode and QR code from image files.
    
    ```bash
    python barcode_reader.py <image-file>
    ```

## Blog
[Scanning Barcode and QR Code Using Webcam, OpenCV and Python](https://www.dynamsoft.com/codepool/opencv-python-webcam-barcode-reader.html)

