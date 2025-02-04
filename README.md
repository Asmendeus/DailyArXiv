# DailyArXiv

This project is forked from [zezhishao/DailyArXiv](https://github.com/zezhishao/DailyArXiv) in fact.

🔒 *An unknown error caused the project not to run after directly forking it.* 🔒

## Original Project Introduction

The project automatically fetches the latest papers from arXiv based on keywords.

The subheadings in the DailyPapers file represent the search keywords.

Only the most recent articles for each keyword are retained, up to a maximum of 100 papers.

You can click the 'Watch' button to receive daily email notifications.

## Revised

- **Changes to article information storage files**: Store updated article information in file `DailyPapers.md` instead of `README.md`. Now `README.md` will no longer be automatically updated daily.
- **Improvement of Keyword system**: Support for keyword grouping, `DailyPapers.md` and `ISSUE_TEMPLATE.md` will put the same group of keywords in the same table, to accommodate the existence of similar keywords.

## Tags and Keywords

```python
tags = ["cond-mat", "quant-ph", "math-ph"]
```

```python
keywords = {
    "Superconductivity": ["superconduct",],
    "Hubbard": ["Hubbard",],
    "t-J": ["t-J", "$t$-$J$", "t-t'-J", "$t$-$t'$-$J$"],
    "LaNiO": ["LaNiO", "La3Ni2O7", "La4Ni3O10", "La_3Ni_2O_7", "La_4Ni_3O_\{10\}", "La$_3$Ni$_2$O$_7$", "La$_4$Ni$_3$O$_\{10\}$"],
    "Tensor Network": ["tensor network", "tensor-network", "dmrg"],
    "QMC": ["quantum monte carlo", "AFQMC", "CPQMC", "CPMC"],
}
```

> **WARNING**: The arXiv API does not support fuzzy search capabilities, for example the wildcard“*” is not available. A tip is that some proper nouns can perform a fuzzy search function by entering the root word, such as "superconduct".

> **WARNING**: Too many keywords in a group may trigger the arXiv site's defenses against frequent requests. If the error is triggered, please rerun the file `main.py` or adjust the sleep time in `main.py`

## How to use

- If your area of interest and keywords are included in this project, you can watch the project and GitHub will alert you via email with each update
- If you need to customize some of the field tags and keywords, please download the full code for this project. (**NOT FORK!** Some errors in the FORK cause ACTION to be unable to be triggered normally.)
  Then change tags (i.e. the parameter `target_fileds` of `filter_tags` in `utils.py`) and keywords (i.e. `keyword_groups` and `keywords` in `main.py`) according to your needs.
  Finally, push the project into your repository, and make sure that the ACTION is available.
