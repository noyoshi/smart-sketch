### Development

run `yarn start` to start the development server

run `yarn sass` to start the sass daemon

Note: if VS code is not picking up on your virtual enviornment, then change
`python.pythonPath` in your `settings.json` to the location of python in the virtual enviornment.

### Production

run `yarn build` to build the project

run `serve -s build/` to run the built project on a simple server. If you do not
have `serve` installed, install it with yarn: `yarn global add serve`.

---

#### Notes

- If one component should modify another - they should both be underneat the same prop, which passes a function to the prop that is triggering the modify. Then, when that function is called, the top most pop can pass down new props to the component that should be getting modified.
