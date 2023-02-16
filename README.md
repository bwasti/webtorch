# webtorch

All 21MB of Python in PyTorch shimmed to at least *load* on the web.  Nothing works and the only (broken) function can be found in index.html (`randn`):

```javascript
  pyodide.registerJsModule('torch_shim', {
    js_global_shim: pyodide.toPy({
      randn: (...args) => { return pyodide.toPy({shape: [...args]}) }
    })
  })
```

Theoretically this could be used to shim all the native ops in PyTorch while preserving things like `fx`, `functorch` and full execution of generic scripts in the browser.
`jit` is almost certainly broken, as well as `cuda` related functionality.
