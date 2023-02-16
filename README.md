# webtorch

All 21MB of Python in PyTorch shimmed to at least *load* on the web (check out everything in this [file](https://github.com/bwasti/webtorch/blob/main/torch/_C/__init__.py), and these [minimal changes](https://github.com/bwasti/webtorch/blob/main/changes.diff) to the baseline source).  Nothing works and the only (broken) function can be found in index.html (`randn`):

```javascript
  pyodide.registerJsModule('torch_shim', {
    js_global_shim: pyodide.toPy({
      randn: (...args) => { return pyodide.toPy({shape: [...args]}) }
    })
  })
```

then in the browser:

```python
import torch
torch.randn(128, 128)
```

Theoretically this could be used to shim all the native ops in PyTorch while preserving things like `fx`, `functorch` and full execution of generic scripts in the browser.
`jit` would be immensely difficult to shim, as well as `cuda` related functionality.
