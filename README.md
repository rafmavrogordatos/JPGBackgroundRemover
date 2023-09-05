<h1 align="center">🎨 JPG Background Remover 🎨</h1>

<p align="center">
  <b>Remove the background from JPG images with ease using Python, Tkinter, and RemBG!</b>
</p>

<h2>📋 Requirements</h2>
<ul>
  <li>Python 3</li>
  <li>Tkinter (included in Python)</li>
  <li>Rembg</li>
</ul>

<h2>💻 Usage</h2>
<p>
  To use the background remover, simply run the following command:
  <pre>
python remove_bg.py
  </pre>
  This will launch the GUI, where you can select the input and output images and click the "Process" button to remove the background.
</p>

<h2>⭐ Features</h2>
<ul>
  <li>Intuitive GUI for easy use</li>
  <li>Fast and accurate background removal</li>
  <li>Support for JPG images</li>
</ul>

<h2>🤔 How it works</h2>
<p>
  The background remover uses a combination of image processing techniques to identify the regions of the image that correspond to the background and remove them. This includes converting the image to grayscale, applying thresholding to create a binary image, and finding the contours in the image. The contours that correspond to the background are then removed, leaving only the foreground objects in the image.
</p>

<h2>🙏 Credits</h2>
<p>
  The background removal algorithm was developed by <a href="https://github.com/rafmavrogordatos">Raf Mavrogordatos</a>.
</p>
