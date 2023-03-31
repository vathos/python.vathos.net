<!-- markdownlint-disable -->

<a href="../vathos/services/depalletizing.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `services.depalletizing`
Methods to train and run models for depalletizing. 

**Global Variables**
---------------
- **BASE_URL**

---

<a href="../vathos/services/depalletizing.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `train_product`

```python
train_product(product_id, calibration_image, token, device_id=None)
```

Starts a training. 



**Args:**
 
 - <b>`product_id`</b> (str):  id of the product to start the training for. A product  is created with the function `create_product()` from the module  `vathos.products`. 
 - <b>`calibration_image`</b> (np.ndarray):  Depth image of the plane the detected  objects will rest upon during inference in meters and floating-point  precision. 
 - <b>`token`</b> (str):  API access token 



**Returns:**
 
 - <b>`str`</b>:  id of the training task 


---

<a href="../vathos/services/depalletizing.py#L76"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `run_inference`

```python
run_inference(
    product_id,
    test_image,
    token,
    score_threshold=0.9999,
    refine_detections=True
)
```

Runs an inference request. 



**Args:**
 
 - <b>`product_id`</b> (str):  id of the product to start the training for. A product  is created with the function `create_product()` from the module  `vathos.products`. 
 - <b>`test_image`</b> (np.ndarray):  float32 image representing the depth in meters 
 - <b>`token`</b> (str):  API access token 



**Returns:**
 
 - <b>`list`</b>:  detected objects 


