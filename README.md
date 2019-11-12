# SmartSketch

## Supercharge your creativity with state of the art image synthesis

![promo.png](docs/promo.png)

Video Demo below!

[![](http://img.youtube.com/vi/HfsO59TCnq8/0.jpg)](http://www.youtube.com/watch?v=HfsO59TCnq8 "AI Background Landscape Painting Using SmartSketch XYZ")

## Credits

- https://nvlabs.github.io/SPADE/
- https://arxiv.org/abs/1903.07291
- https://github.com/nvlabs/spade/
- Special thanks to @AndroidKitKat for helping us host this!

## Set Up

- You'll need to install the pretrained generator model for the COCO dataset into `checkpoints/coco_pretrained/`. Instructions for this can be found on the `nvlabs/spade` repo.

- Make sure you need to install all the Python requirements using `pip3 install -r requirements.txt`. Once you do this, you should be able to run the server using `python3 server.py`. It will run it on `0.0.0.0` on port 80. Unfortunately these are hardcoded into the server and right now you cannot pass CLI arguments to the server to specify the port and host, as the PyTorch stuff also reads from the command line (will fix this soon).

### TODOS

- [ ] Change how we run the model, make it easier to use (don't use their options object)
- [ ] Make a seperate frontend server and a backend server (for scaling)
- [ ] Try to containerize at least the bacckend components
