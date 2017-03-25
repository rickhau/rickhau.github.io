# python make_entry.py "New Post title"
# This will generate a date_title.md under content

import sys
from datetime import datetime
import os

TEMPLATE = """
---
{title}
date: {year}-{month:02d}-{day} {hour}:{minute:02d}
category:
slug: {slug}
---

"""


def make_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    filename = "{}_{:0>2}_{:0>2}_{}.md".format(
        today.year, today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title,
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    target_folder = 'content/{}/{:02d}/{:02d}'.format(today.year, today.month, today.day)
    print("{}".format(target_folder))
    if not os.path.exists(target_folder):
        try:
            os.makedirs(target_folder)
        except:
            raise OSError("Unable to create destinaion directory: (%s)!!!".format(target_folder))
        else:
            print("Target folder: (%s) is created.".format(target_folder))
    f_create = "{}/{}".format(target_folder, filename)
    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> {}".format(f_create))


if __name__ == '__main__':

    if len(sys.argv) > 1:
        make_entry(sys.argv[1])
    else:
        print "No title given"