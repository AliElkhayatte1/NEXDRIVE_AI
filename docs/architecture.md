# Architecture

NEXDRIVE AI is designed as a set of importable Python modules with explicit
interfaces.

- `app.capture` obtains screen frames. It does not perform inference or control.
- `app.perception` defines object-detection and road-segmentation contracts.
- `app.decision` converts a frame or future perception result into driving
  commands.
- `app.control` applies approved commands to a vehicle controller. Real input
  integrations are out of scope for this initial foundation.
- `app.evaluation` will contain future latency and reliability metrics.
- `app.ui` will contain a future desktop interface.

The application should use dependency injection: real models and controllers
can replace mocks without changing the interfaces.
