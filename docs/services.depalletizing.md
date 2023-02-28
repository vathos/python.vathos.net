<!-- markdownlint-disable -->

<a href="../vathos/services/depalletizing.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `services.depalletizing`




**Global Variables**
---------------
- **BASE_URL**

---

<a href="../vathos/services/depalletizing.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `train_product`

```python
train_product(product_id, calibration_image_path, token, device_id=None)
```

Starts a training. 



**Args:**
 
 - <b>`product_id`</b> (str):  id of the product to start the training for. A product  is created with the function `create_product()` from the module  `vathos.products`. 
 - <b>`calibration_image_path`</b> (str):  path of an image for extrinsic calibration. The image must be a depth image of the plane the detected objects will rest upon during inference. It is converted to millimeters, then cast to a short integer array whose LSB and MSB are put into the red respectively green channel of an 8-bit RGB image before storing it as a PNG-compressed file. 
 - <b>`token`</b> (str):  API access token 



**Returns:**
 
 - <b>`str`</b>:  id of the training task 




---

<a href="../vathos/services/depalletizing.py#L73"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `run_inference`

```python
run_inference(product_id, test_image_path, token)
```

Runs an inference request. 



**Args:**
 
 - <b>`product_id`</b> (str):  id of the product to start the training for. A product  is created with the function `create_product()` from the module  `vathos.products`. 
 - <b>`test_image_path`</b> (str):  path of image to run inference on. This image must measure the depth of each pixe in millimeters, where each pixel is stored as a short integer, whose LSB and MSB are packed into the red respectively green channel of an 8-bit RGB image before storing it as a PNG-compressed file. 
 - <b>`token`</b> (str):  API access token 



**Returns:**
 
 - <b>`list`</b>:  detected objects   


