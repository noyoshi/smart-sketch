[![Build Status](https://travis-ci.com/noyoshi/webapp-bootstrap.svg?token=9Vq7GRbMm7sqmhG1UdvM&branch=master)](https://travis-ci.com/noyoshi/webapp-bootstrap)

- We are using `nodenv` and `pyenv` to manage the versions - I suggest you install and use them. Python version is `3.6.0` to be compatible with Tensor Flow.

### Helpful Stuff?

- https://tomchentw.github.io/react-google-maps/
- https://firebase.google.com/
- https://github.com/noyoshi/yldus

### Docs

- https://react-icons.netlify.com/#/
- https://react-bootstrap.netlify.com/
- https://favicon.io/emoji-favicons

### Google Cloud SDK

- https://cloud.google.com/sdk/docs/

.. If you use CloudRun, it might not be good for demos because there could be 0 instances up at the time. Make sure to see if you can set a minimum number of instances to prevent this.


## TODOS
- [x] Everyone should be able to run the models on their computers
- [x] Function that takes two image files, and runs the model with them
- [x] Function that uploads a file to a remote server
- [x] The client can update the image in the browser with a new image it recieves

Once those are done...
- The server receives the image from the client and writes it to disk
- The server takes the image from somewhere and runs the model with it (function #1 from above)
- The server takes the generated image and sends it to the client
- Make the drawer for the client that uses the HTML canvas to draw an image, and upload it as a PNG to some endpoint
- Sets up the stack for google cloud

#### Credits
- https://github.com/LukasMarx/react-file-upload
- https://nvlabs.github.io/SPADE/
- https://arxiv.org/abs/1903.07291
- https://github.com/nvlabs/spade/
