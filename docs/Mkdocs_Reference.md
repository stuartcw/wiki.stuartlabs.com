
| site_name: Stuart's Brain                                      |   |   |
| -------------------------------------------------------------- | - | - |
| site_url: http://wiki.stuartlabs.com/                          |  blah | test  |
|                                                                |   |   |
| theme: material                                                |   |   |
|                                                                |   |   |
|                                                                |   |   |
| plugins:                                                       |   |   |
|     - search                                                   |   |   |
|     - macros                                                   |   |   |
|     - mkdocs-simple-hooks:                                     |   |   |
|           hooks:                                               |   |   |
|               on_env: "on_env:print_env"                       |   |   |
|               on_page_markdown: "on_page_markdown:hello_world" |   |   |
|     - rss                                                      |   |   |
| nav:                                                           |   |   |
|     - Home: index.md                                           |   |   |
|     - About: about.md                                          |   |   |
|     - MkDocs Help: help.md                                     |   |   |
|     - Info: info.md                                            |   |   |
|                                                                |   |   |
| extra:                                                         |   |   |
|   status:                                                      |   |   |
|       - new : new                                              |   |   |
|                                                                |   |   |
| markdown_extensions:                                           |   |   |
|     - pymdownx.highlight                                       |   |   |
|     - pymdownx.superfences                                     |   |   |
|     - smarty                                                   |   |   |
|     - toc:                                                     |   |   |
|         permalink: True                                        |   |   |
|     - sane_lists                                               |   |   |
|     - wikilinks                                                |   |   |
|     - admonition                                               |   |   |
|     - pymdownx.critic                                          |   |   |
|     - pymdownx.inlinehilite                                    |   |   |
|     - pymdownx.highlight                                       |   |   |
|     - pymdownx.emoji:                                          |   |   |
|           emoji_generator: !!python/name:pymdownx.emoji.to_svg |   |   |
