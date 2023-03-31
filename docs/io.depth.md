<!-- markdownlint-disable -->

<a href="../vathos/io/depth.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `io.depth`
Reading depths image from various file formats. 


---

<a href="../vathos/io/depth.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `read_volumetric_tiff`

```python
read_volumetric_tiff(filename)
```

Reads a point map from a volumetric TIFF. 

This is for example exported by the MechMind viewer.  


---

<a href="../vathos/io/depth.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `write_volumetric_tiff`

```python
write_volumetric_tiff(filename, point_map)
```

Writes a point map to a volumetric TIFF. 


---

<a href="../vathos/io/depth.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `read_from_png_uint8`

```python
read_from_png_uint8(filename)
```

Reads a depth map packed into the RG channels of a PNG-compressed image. 

This is the preferred way of storing depth images in all Vathos services. 


---

<a href="../vathos/io/depth.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `write_to_png_uint8`

```python
write_to_png_uint8(filename, depth)
```

Writes a depth map into the RG channels of a PNG-compressed image. 


---

<a href="../vathos/io/depth.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `write_to_png_uint8_buffer`

```python
write_to_png_uint8_buffer(depth)
```

Packs a float depth image into a PNG-compressed byte buffer. 


---

<a href="../vathos/io/depth.py#L65"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `read_from_png_uint16`

```python
read_from_png_uint16(filename)
```

Reads a depth map from a 16-bit monochrome image in PNG format. 

Used in academic [datasets](http://redwood-data.org/3dscan/index.html).    


---

<a href="../vathos/io/depth.py#L75"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `write_to_png_uint16`

```python
write_to_png_uint16(filename, depth)
```

Reads a depth map from a 16-bit monochrome image in PNG format. 

Used in academic [datasets](http://redwood-data.org/3dscan/index.html).    


