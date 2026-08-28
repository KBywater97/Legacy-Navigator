# Legacy Navigator

Legacy Navigator is a Python project I'm building as I learn software development, debugging, automation, APIs, and eventually AI-assisted developer tools.

The long-term goal is to create a platform that helps developers and learners diagnose errors, search previous solutions, navigate technical resources, and build a reusable knowledge base from problems they've encountered.

## Current Version

**v0.0.1 — Ticketing System Prototype**

The current version is a command-line Python application that can:

- Create error tickets
- Assign unique ticket IDs
- Store ticket creation timestamps
- Save tickets persistently using JSON
- View previously created tickets
- Update ticket status
- Search tickets by error message
- Exit through an interactive menu

Ticket data is stored locally in `data/tickets.json`.

The real ticket data file is excluded from Git using `.gitignore`. A sample structure is provided in:

`data/tickets.example.json`


## Planned Features

Future versions may include:

- Improved ticket searching and filtering
- Notes and solutions attached to tickets
- Stack Overflow / Stack Exchange API integration
- Automatic error lookup
- SQLite database storage
- Web interface
- Documentation and knowledge-base search
- Automated error ticket creation
- AI-assisted troubleshooting with source citations
- Coding exercises based on recurring errors

## Why I'm Building This

Legacy Navigator is both a learning project and an attempt to build something useful.

Instead of learning programming only through isolated exercises, I'm using the project to practice Python, Git, APIs, databases, web development, automation, debugging, and software architecture while gradually turning those skills into a larger working application.

The project will evolve as my understanding grows.

## Status

 **Early Development**

Legacy Navigator is currently a functional command-line prototype and is under active development.