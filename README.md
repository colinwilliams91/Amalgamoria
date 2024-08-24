# Amalgamoria
It's Wordle except you're trying not to die

## Develop
Use Python 3.12

### Activate the Virtual Environment (Windows)
- Create your Virtual Environment in the root directory of the project
  - `py -3 -m venv .venv`
- Activate your Environment
  - `.venv\Scripts\activate`

### Activate the Virtual Environment (Mac and Linux)
- Create your Virtual Environment in the root directory of the project
  - `python3 -m venv .venv`
- Activate your Environment
  - `source .venv/bin/activate`

### Installing Dependencies
- Ensure you're in the Virtual Environment
- `pip install -r requirements.txt`

### Run the App
- Run the app
  - `fastapi dev Amalgamoria\main.py`

### Update Dependencies List
`pip freeze > requirements.txt`

### Workflow
- clone this repo
- create or pick up a ticket [from Amalgamoria Task Board](https://github.com/users/colinwilliams91/projects/11)
  - assign yourself to the ticket
  - comment any changes or divergences from the original ticket body (most recent comment is most relevant)
- make a branch directly from the ticket (lower right section "create a branch" hyperlink)
- open a PR from your branch to this remote `origin` -> https://github.com/colinwilliams91/Amalgamoria.git

### Commit Standard
- please use [Gitmoji Specification](https://gitmoji.dev/) for commit conventions
- 6 most popular:

| purpose | emoji | shortcode | unicode |
| ------- | ----- | --------- | ------- |
| feat    | ✨ | `:sparkles:` | U+2728 |
| fix     | 🐛 | `:bug:` | U+1F41B |
| refactor | ♻ | `:recycle:` |  U+267B-FE0F |
| chore | 💻 | `:computer:` | U+1F4BB |
| test | 🧪 | `:test_tube:` | U+1F9EA |
| docs | 📝 | `:memo:` | U+1F4DD |

```
# emoji-data master json
https://raw.githubusercontent.com/iamcal/emoji-data/master/emoji.json
```

