# Extending MkDocs

I found a couple of ways to extend MKDocs but not much documentation.

## mkdocs-simple-hooks

!!! mkdocs-simple-hooks
    You can use this plugin to create simple hooks for mkdocs without having to create a separate plugin package.
    Just define a function and register it as a hook in the mkdocs.yml. The function shall have the same API as the desired hook. 
    
    [mkdocs-simple-hooks](https://github.com/aklajnert/mkdocs-simple-hooks)
e.g. "Hello world!" can be added to every page by hooking MkDoc's `on_page_markdown` [Global Event](https://www.mkdocs.org/dev-guide/plugins/)  callback.

Simply make a file `page_markdown.py` and add the following to `mkdocs.yml`
```yaml
plugins:
    - search
    - mkdocs-simple-hooks:
          hooks:
              on_env: "on_env:print_env"
              on_page_markdown: "on_page_markdown:hello_world"
```


```python
def hello_world(markdown,page,config,files):
    return markdown + "\n*Hello world!*"
```


## mkdocs-macros

!!! mkdocs-macros
    mkdocs-macros-plugin is a plugin/framework that makes it easy for contributors of an MkDocs website to produce richer and more beautiful pages. It can do two things:

    Transforming the markdown pages into Jinja2 templates that:
     * Use environment or custom variables,
     * Call pre-defined or custom macros,
     * Exploit standard or custom filters
     * Replacing MkDocs plugins for a wide range of tasks: e.g. manipulating the navigation, adding files after the html pages have already been generated etc.
    
    [mkdocs-macros](https://mkdocs-macros-plugin.readthedocs.io/en/latest/)
{{ mymacro() }}

This code is added to the page using this code in text of the page:

```
{% raw %} 
{{ mymacro() }}
{% endraw %}
```


## Reference

### Global Events
https://www.mkdocs.org/dev-guide/plugins/


