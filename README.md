What is it
==========

A Python Markdown extension that allows you to create special tables with 2 items per thing. I use these similar to definition lists, but where I need them to be inline, and lined-up. The table itself would be hidden in css.

It requires PHP style tables to be enabled.

# Installation

    $ pip install git+git://github.com/Saevon/markdown-defn-table.git

# Usage

Activate the `defn_table` extension and use the following markup:

```
!defn_table!
`ENABLE`: **enables** the app
`DEBUG`: turns on debug mode
```

Would generate the following

```
<div class="defn-table" markdown=1>
 |
-|-
`ENABLE` | **enables** the app
`DEBUG` | turns on debug mode
</div>
```



# Troubleshooting

Please consider using [Github issues tracker](http://github.com/Saevon/markdown-defn-table/issues) to submit bug reports or feature requests.


# License

[MIT License](http://www.opensource.org/licenses/mit-license.php)
