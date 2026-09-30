# asreview-minimal

This package allows you to install specific features of [asreview](https://github.com/asreview/asreview).
At this moment, only models will be installed.
This package cannot be installed at the same time as asreview.

The model code under `src/asreview/models`, `src/asreview/utils.py`, and
`src/asreview/_deprecated.py` is vendored from
[asreview v1.6.6](https://github.com/asreview/asreview/tree/v1.6.6) (Apache 2.0),
with local patches for compatibility with newer scikit-learn releases.

To extend this package, you can use
asreview's [extensions](https://asreview.readthedocs.io/en/latest/extensions_dev.html#model-extensions) framework.

## Building

```bash
# build the package
pw run build
```
