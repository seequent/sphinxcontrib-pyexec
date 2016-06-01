# PyExec

A sphinx extension for running python code and displaying both the input and
output [sphinx documentation](http://www.sphinx-doc.org/). 

In the conf.py add `PyExec` to your extensions.

In the ReStructuredText file, use the `exec` environment

```
  .. exec::
    print 2 + 2
```

To output python code & the results in your documentation. 

```
  >> print 2 + 2
  4
```

Note that you need to include the `print` statement for the output to be shown. To see it in action, checkout the [Properties documentation](http://propertiespy.readthedocs.io/). 

Based on

- https://github.com/sphinx-doc/sphinx/blob/master/sphinx/directives/code.py
- http://stackoverflow.com/a/18143318/6086999



