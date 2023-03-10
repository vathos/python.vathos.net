<!-- markdownlint-disable -->

<a href="../vathos/products.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `products`
Product creation and administration. 

**Global Variables**
---------------
- **BASE_URL**
- **ALLOWED_UNITS**

---

<a href="../vathos/products.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_product`

```python
create_product(
    name,
    model_file_name,
    unit,
    projection_matrix,
    image_size,
    image_range,
    token
)
```

Creates a product and attaches a 3d model file and camera to it. 



**Args:**
 
 - <b>`name`</b> (str):  human-readable name for the new product 
 - <b>`model_file_name`</b> (str):  path to a CAD model file on disk. Currently, the only  supported format is Wavefront OBJ. 
 - <b>`unit`</b> (str):  unit in which the CAD model is meaured. Must be one of  `['m', 'dm', 'cm', 'mm']`. 
 - <b>`projection_matrix`</b> (numpy.ndarray):  a $3\times 3$ projection matrix of the   used camera 
 - <b>`image_size`</b> (tuple):  image width and height in number of pixels 
 - <b>`image_range`</b>:  (tuple): minimal and maximal depths captured with the camera in  meters 
 - <b>`token`</b> (str):  API access token 



**Returns:**
 
 - <b>`str`</b>:  identifier of the created product 


---

<a href="../vathos/products.py#L112"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_product`

```python
get_product(product_id, token)
```

Downloads product data. 



**Args:**
 
 - <b>`product_id`</b> (str):  product id 
 - <b>`token`</b> (str):  API access token 



**Returns:**
 
 - <b>`dict`</b>:  product data 


---

<a href="../vathos/products.py#L130"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `list_products`

```python
list_products(token, verbose=False)
```

Lists all exisiting products 



**Args:**
 
 - <b>`token`</b> (str):  API access token 
 - <b>`verbose`</b> (bool):  whether to return all fields (or just name+id) 



**Returns:**
 
 - <b>`list`</b>:  product data 


