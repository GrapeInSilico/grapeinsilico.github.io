+++
title ='Introduction'
slug = 'post8'
description = 'Development'
disableComments = true
image = '/images/window/grape-vine-tunnel-archway-passage-garden-autumn-near-douro-river-portugal-93621530.jpg'
+++

+--------------+
| Development  |
+==============+
|              |
+--------------+
| ::: contents |
| Contents     |
| :::          |
+--------------+
| > local      |
| >            |
| > :          |
+--------------+
| Contributing |
+--------------+

# Introduction

[OpenAlea](https://github.com/openalea) is open-source. Everyone is
welcome to contribute.

::: note
::: title
Note
:::

All the packages are separated on two [Github](https://github.com) pages

-   the official and stable packages on
    [OpenAlea](https://github.com/openalea)
-   the unofficial, WIP and *to be reviewed* packages on
    [OpenAlea-Incubator](https://github.com/openalea-incubator)
:::

There are many ways to contribute to
[OpenAlea](https://github.com/openalea). The most common ways of
contributing are coding or documenting different parts of the project.
One may improve documentation which is as much important as improving
the code itself. One could also create their own package, see [How to
contribute](#how-to-contribute).

Another way to contribute to the project is to report bugs ans issues
you are facing.

# How to contribute

The main way to contribute is to fork the package repository you are
interested in on [GitHub](https://github.com)

::: note
::: title
Note
:::

Remember, the packages are found on different
[GitHub](https://github.com) pages. The following steps describe a
tutorial for an [OpenAlea](https://github.com/openalea) package. Make
the good changes if you want to use
[OpenAlea-Incubator](https://github.com/openalea-incubator) packages.
:::

1.  [Create an account](https://github.com/join) on GitHub if you do not
    already have one. You will choose your [GitHub](https://github.com)
    login \<your_login\>.

2.  [Fork](https://help.github.com/en/articles/fork-a-repo) the package
    repository of your choice (for instance, [MTG
    repository](https://github.com/openalea/mtg)) and click on the
    \'[Fork](https://help.github.com/en/articles/fork-a-repo)\' button
    near the top of the page. It generates a copy of the repository
    under your account on the [GitHub](https://github.com) user account.
    For more details on how to fork a repository see [this
    guide](https://help.github.com/articles/fork-a-repo/).

3.  [Clone](https://help.github.com/en/articles/cloning-a-repository)
    your fork of the package repo from your [GitHub](https://github.com)
    account to your local disk :

        git clone https://github.com/<your_login>/<package_name>.git
        cd <package_name>

4.  Create a branch \<branch_name\> to hold your development changes :

        git checkout -b <branch_name>

    and start making changes. Always use a `feature` branch. It\'s good
    practice to never work on the `master` branch!

    ::: note
    ::: title
    Note
    :::

    In the above setup, your `origin` remote repository points to
    `<your_login>/.git`. If you wish to fetch/merge from the main
    repository instead of your forked one, you will need to add another
    remote to use instead of `origin`. It\'s good practice to choose the
    name `upstream` for it, and the command will be:

        git remote add upstream https://github.com/openalea/<package_name>.git

    If the package you chose come from OpenAlea-Incubator, the command
    will be:

        git remote add upstream https://github.com/openalea_incubator/<package_name>.git

    And in order to fetch the new remote and base your work on the
    latest changes of it you can:

        git fetch upstream
        git checkout -b <your_name> upstream/master
    :::

5.  Develop the feature on your feature branch on your computer, using
    Git to do the version control. When you\'re done editing, add
    changed files using `git add` and then `git commit` files:

        git add <modified_files>
        git commit -m "description of what you've done"

    to record your changes in Git, then push the changes to your
    [GitHub](https://github.com) account with:

        git push -u origin <branch_name>

6.  Once you\'ve finished, you can create a **pull request** on the
    corresponding [GitHub](https://github.com). Follow
    [these](https://help.github.com/articles/creating-a-pull-request-from-a-fork)
    instructions to create a pull request from your fork.

# How to make a proper bug report

# Documentation

You can also contribute to the documentation. If you find some parts
that are not explained enough or uncleared, you can complete or improve
the documentation.

Once you have forked the package on your device, you have to install
[Sphinx](https://www.sphinx-doc.org/en/master/) to generate the HTML
output :

    pip install sphinx

In each package repository, it must be a `docs/` directory in which the
reStructuredText documents are. You can modify or create these and
generate the HTML output in the `docs/` directory :

    make html 

::: note
::: title
Note
:::

If you are creating your own package, you can build the
[Sphinx](https://www.sphinx-doc.org/en/master/) environment directly in
the `docs/` directory :

    sphinx-quickstart
:::

Once you are finished, you can add, commit and push what you have done
on [GitHub](https://github.com) and then create a **pull request** (see
[How to contribute](#how-to-contribute)).

As we want all the documentation to look the same way, configure your
Sphinx like us:

1.  The theme we are using is the [Read the Docs Sphinx
    Theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/). The
    theme can be installed like this :

        pip install sphinx_rtd_theme

    Once you\'ve installed the theme, write in your `conf.py` file :

        html_theme = "sphinx_rtd_theme"

    Then write in the same file :

        html_theme_options = {
         'logo_only': True
        }

2.  Download the OpenAlea logo and put it your `_static` directory and
    then write in your `conf.py` file :

        html_static_path = ['_static']
        html_logo = "_static/openalea_web.svg"

3.  Mention the main website \"openalea.rtfd.io\"

## Moving from Python 2 to Python 3
