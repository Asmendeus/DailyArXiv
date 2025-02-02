import time
import pytz
from datetime import datetime

from utils import get_daily_papers_by_keyword, generate_table, back_up_files, remove_backups, get_daily_date, parse_date


beijing_timezone = pytz.timezone('Asia/Shanghai')

# NOTE: arXiv API seems to sometimes return an unexpected empty list.

# get current beijing time date in the format of "2021-08-01"
current_date = datetime.now(beijing_timezone).strftime("%Y-%m-%d")
# get last update date from DailyPapers.md
with open("DailyPapers.md", "r") as f:
    while True:
        line = f.readline()
        if "Last update:" in line: break
    last_update_date = line.split(": ")[1].strip()
    # if last_update_date == current_date:
        # sys.exit("Already updated today!")

keyword_groups = ["Superconductivity", "Hubbard", "t-J", "LaNiO", "Tensor Network", "QMC"]
keywords = {
    "Superconductivity": ["superconduct",],
    # "Superconductivity": ["superconductivity", "superconductor", "superconduction", "superconducting"],
    "Hubbard": ["Hubbard",],
    "t-J": ["t-J",],
    "LaNiO": ["LaNiO", "La3Ni2O7", "La4Ni3O10", "La_3Ni_2O_7", "La_4Ni_3O_\{10\}", "La$_3$Ni$_2$O$_7$", "La$_4$Ni$_3$O$_\{10\}$"],
    "Tensor Network": ["tensor network", "tensor-network", "dmrg"],
    "QMC": ["quantum monte carlo", "AFQMC", "CPQMC", "CPMC"],
}

for group in keyword_groups:
    assert group in keywords, f"'{group}' is not a key in keywords"

max_result = 100 # maximum query results from arXiv API for each keyword
issues_result = 15 # maximum papers to be included in the issue

# all columns: Title, Authors, Abstract, Link, Tags, Comment, Date
# fixed_columns = ["Title", "Link", "Date"]

column_names = ["Title", "Link", "Abstract", "Date", "Comment"]

back_up_files() # back up DailyPapers.md and ISSUE_TEMPLATE.md

# write to DailyPapers.md
f_dp = open("DailyPapers.md", "w") # file for DailyPapers.md
f_dp.write("# Daily Papers\n")
f_dp.write("Last update: {0}\n\n".format(current_date))

# write to ISSUE_TEMPLATE.md
f_is = open(".github/ISSUE_TEMPLATE.md", "w") # file for ISSUE_TEMPLATE.md
f_is.write("---\n")
f_is.write("title: Latest {0} Papers - {1}\n".format(issues_result, get_daily_date()))
f_is.write("labels: documentation\n")
f_is.write("---\n")
f_is.write("**Please check the [Github](https://github.com/Asmendeus/DailyArXiv) page for a better reading experience and more papers.**\n\n")

for keyword_group in keyword_groups:
    f_dp.write("## {0}\n".format(keyword_group))
    f_is.write("## {0}\n".format(keyword_group))

    papers = []
    for keyword in keywords[keyword_group]:
        if len(keyword.split()) == 1: link = "AND" # for keyword with only one word, We search for papers containing this keyword in both the title and abstract.
        else: link = "OR"
        papers += get_daily_papers_by_keyword(keyword, column_names, max_result, link)
        time.sleep(5) # avoid being blocked by arXiv API

    unique_papers = {}
    for paper in papers:
        unique_papers[paper['Link']] = paper
    papers = list(unique_papers.values())
    papers = sorted(papers, key=lambda x: parse_date(x['Date']), reverse=True)
    if len(papers) == 0: continue
    if len(papers) > issues_result: papers = papers[:issues_result]

    rm_table = generate_table(papers)
    is_table = generate_table(papers[:issues_result], ignore_keys=["Abstract"])
    f_dp.write(rm_table)
    f_dp.write("\n\n")
    f_is.write(is_table)
    f_is.write("\n\n")
    time.sleep(5) # avoid being blocked by arXiv API

f_dp.close()
f_is.close()
remove_backups()
