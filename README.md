# SmartSketch

## Supercharge your creativity with state of the art image synthesis

![promo.png](docs/promo.png)

**Video Demo below!**

[![](http://img.youtube.com/vi/HfsO59TCnq8/0.jpg)](http://www.youtube.com/watch?v=HfsO59TCnq8 "AI Background Landscape Painting Using SmartSketch XYZ")

## Credits

- See project page here: https://nvlabs.github.io/SPADE/
- Read paper here: https://arxiv.org/abs/1903.07291
- See source code here: https://github.com/nvlabs/spade/
- Special thanks to @AndroidKitKat for helping us host this!

## Set Up

- You'll need to install the pretrained generator model for the COCO dataset into `checkpoints/coco_pretrained/`. Instructions for this can be found on the `nvlabs/spade` repo.

- Make sure you install all the Python requirements using `pip3 install -r requirements.txt` (in `/backend` folder).     

- Once you do so, you should be able to run the server using `python3 server.py`. It will run it on `0.0.0.0` on port 80 (on `127.0.0.1` for Windows users). Unfortunately, these are hardcoded into the server and right now you cannot pass CLI arguments to the server to specify the port and host, as the PyTorch stuff also reads from the command line (will fix this soon). If you would like to change this, locate line 195 in `backend/server.py`.



### TODOS

- [ ] Change how we run the model, make it easier to use (don't use their options object)
- [ ] Make a seperate frontend server and a backend server (for scaling)
- [ ] Try to containerize at least the backend components
