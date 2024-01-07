import sys 
import html
import os

MARKDOWN_CODE="\n`"+"`"+"`\n"

def define_env(env):
    "Hook function"

    @env.macro
    def mymacro():
      with open("main.py") as this_python_file:
          lines="".join(this_python_file.readlines())

      return "You can extend MkDocs with code like:\n"+MARKDOWN_CODE+lines+MARKDOWN_CODE


    @env.macro
    def code_from_file(path: str, flavor: str = ""):
        """
        Load code from a file and save as a preformatted code block.
        If a flavor is specified, it's passed in as a hint for syntax highlighters.

        Example usage in markdown:

            {{code_from_file("code/myfile.py", "python")}}

        """
        docs_dir ="includes"
        path = os.path.abspath(os.path.join(docs_dir, path))
        if not os.path.exists(path):
            return f"""<b>File not found: {path}</b>"""
        with open(path, "r") as f:
            return (
                #f"""<pre><code class="{flavor}">{html.escape(f.read())}</code></pre>"""
                f"```{flavor}\n"+f.read()+"\n```"
            )

    @env.macro
    def external_markdown(fn: str):
        """
        Load markdown from files external to the mkdocs root path.
        Example usage in markdown:

            {{external_markdown("../../README.md")}}

        """
        docs_dir = env["project_dir"]+"/includes"
        fn = os.path.abspath(os.path.join(docs_dir, fn))
        if not os.path.exists(fn):
            return f"""<b>File not found: {fn}</b>"""
        with open(fn, "r") as f:
            return f.read()
