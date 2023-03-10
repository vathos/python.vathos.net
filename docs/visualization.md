<!-- markdownlint-disable -->

<a href="../vathos/visualization.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `visualization`
Visualization. 

**Global Variables**
---------------
- **VISUALIZATION_ENABLED**
- **UNIT_CONVERSION_FACTOR**

---

<a href="../vathos/visualization.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `unpack_short`

```python
unpack_short(rgb)
```

Unpacks two byte channels into a single channel of type short. 


---

<a href="../vathos/visualization.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `backproject`

```python
backproject(depth, K)
```

Backprojects a depth image into a point cloud. 


---

<a href="../vathos/visualization.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `visualize_detections`

```python
visualize_detections(detections, test_image_path, token, fitness_threshold=0.7)
```

Visualizes a point cloud and detections. 

This function is only executed if mayavi and trimesh are installed. 



**Args:**
 
 - <b>`model_file_name`</b> (str):  path to a CAD model file on disk. Currently, the only  supported format is Wavefront OBJ. 
 - <b>`unit`</b> (str):  unit in which the CAD model is meaured. Must be one of  `['m', 'dm', 'cm', 'mm']`. 
 - <b>`test_image_path`</b> (str):  path of the depth image used in inference 
 - <b>`projection_matrix`</b> (numpy.ndarray):  a $3\times 3$ projection matrix of the   used camera 
 - <b>`detections`</b> (list):  inferred object poses       


