Claude Project Naming Convention
==============================================================================


Why Naming Convention is Important
------------------------------------------------------------------------------
When you use Claude AI intensively in your day-to-day life, it’s common to accumulate many Claude Projects (>= 100). A good project name helps you quickly locate the right project.

Claude Project name search uses **Prefix Search**, which differs from N-Gram Search. It cannot match letters in the middle of a word. Additionally, the tokens in your query are treated as logical **OR**, not **AND**, which may lead to too many results in the search output.

Now, let’s move on to the next section to explore some naming convention tricks.


Naming Convention tricks
------------------------------------------------------------------------------
A naming convention should be designed to be effective for both **humans** and **search functionality**. Based on my best practices, I recommend including two key parts in the project name:

1. **Keywords**: A collection of abbreviations or tags that provide context. For example, if you have an AI designed for your work at the company "ABC," focusing on the "EFG" project, you can use "ABC EFG" as the prefix of the project name.
2. **Title**: A concise description to help humans quickly understand the purpose of the project.

For instance, `"ABC EFG | Meeting Assistant"` is an effective name for a project that assists with preparing meeting invites, emails, summaries, and actionable items for the "EFG" project at "ABC" company.


My Favorite Keyword System
------------------------------------------------------------------------------
Here is a list of my preferred keywords:

- **ABC work**: Projects related to work at ABC company.
- **EFG proj**: related to EFG project.
- **GitHub**: ``gh``
- **GitLab**: ``gl``
- **BitBucket**: ``bb``
- **Tool**: ``tool``


My Favorite Project Naming Convention
------------------------------------------------------------------------------
Depending on the type of Claude Project, here are some naming conventions I follow:


For a Specific Job-Related Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you are working on a specific job at a company, such as **ABC Corp**, on a project called **XYZ Project** (optional), and the Claude Project performs a specific task like **Code Review** (optional), the name format should be::

    ``${Job Keyword} ${Project Keyword} | ${Project Name} | ${Task}``.

Example (efg = Bank Portal Project)::

    abc work efg proj | Bank Portal Project | code review

Color Code: :orange:`Work`


For Git Repository Specific Development Assistants
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If the Claude Project assists with work in a GitHub repository, such as writing code, creating documentation, writing pull requests, code review, the name format is::

    gh or gl or bb | ${GitHub Account Name}/${Repo Name} | ${Task}

For this ``learn_claude`` project, I use::

    gh | MacHu-GWU/learn_claude | everything

Color Code: :green:`Git Repository`


For General Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If the Claude Project is a standalone utility not tied to a specific job or project, use the format::

    tool | ${Tool Name and Description}

For example::

    tool | text summary

Color Code: :blue:`Tool`
