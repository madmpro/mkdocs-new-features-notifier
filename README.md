# mkdocs-new-features-notifier


✚ This plugin enables you to notify users of new features in your product. It does this by identifying new documentation files, and having these listed under a blinking navigation entry

✏️ [Blog Post]() | 🐍 [Python Package](https://pypi.org/project/mkdocs-new-features-notifier/) | ✚ [Demo]() | 📕 [Docs]()

## Features

- **Identification of new features in documentation** 

## Install

It's easy to get started using [PyPI] and `pip` using Python:

```terminal
$ pip install mkdocs-new-features-notifier
```

## Usage

Look at [the sample project]() for an example implementation, or see [what it looks like after running `mkdocs build`]().

As of this release, a `new-features.md` file has to exist in the directory structure, similar to an `extra.css`, where the styling for the glowing effect will be placed.

`new-features.md` need not have any content, as it will be overwritten with each documentation release, should new documentation files be detected
Below is a sample mkdocs.yml file
```yaml
# /mkdocs.yml
site_name: Sample Docs

nav:
  - Home: 'index.md'
  - Sample Item: 'item.md'
  - Updates: 'new-features.md'

plugins:
  - mkdocs-new-features-notifier

extra-css: [css/extra.css]

theme:
  name: 'material'
  custom_dir: assets/

```

#### Example Source Filetree

```terminal
$ tree .

├── docs
│   ├── item.md.md
│   ├── index.md
|   └── new-features.md 
├── mkdocs.yml
└── assets
    └── css
        └── extra.css

3 directories, 5 files
```

#### Example extra.css file

```css
@keyframes glowing {
0% { background-color: #98d4ff; box-shadow: 0 0 5px #fff; }
10% { background-color: #92cdf7; box-shadow: 0 0 20px #fff; }
20% { background-color: #8cc7f2; box-shadow: 0 0 20px #fff; }
30% { background-color: #85c0eb; box-shadow: 0 0 20px #fff; }
40% { background-color: #7fb9e4; box-shadow: 0 0 20px #fff; }
50% { background-color: #78b1dc; box-shadow: 0 0 20px #fff; }
60% { background-color: #7fb9e4; box-shadow: 0 0 20px #fff; }
70% { background-color: #85c0eb; box-shadow: 0 0 20px #fff; }
80% { background-color: #8cc7f2; box-shadow: 0 0 20px #fff; }
90% { background-color: #92cdf7; box-shadow: 0 0 20px #fff; }
100% { background-color: #98d4ff; box-shadow: 0 0 5px #fff; }
}

.new_update {
animation: glowing 1500ms infinite;
}
```

## Supported Versions

- Python 3 &mdash; 3.5, 3.6, 3.7
- [Mkdocs] 1.0.4 and above.

## License

Released under the Apache 2.0 License. See [here](./LICENSE) for more details.

