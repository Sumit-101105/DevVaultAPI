\# DevVaultAPI



A developer-focused REST API built with Python and FastAPI for managing and organizing reusable code snippets.



\## Overview



DevVaultAPI is a backend development project designed to provide a structured way to store, retrieve, update, delete, and search code snippets.



The project is being developed incrementally through multiple development sprints, with an emphasis on REST API design, backend architecture, data management, and security.



\## Tech Stack



\- \*\*Language:\*\* Python

\- \*\*Framework:\*\* FastAPI

\- \*\*Data Validation:\*\* Pydantic

\- \*\*ASGI Server:\*\* Uvicorn

\- \*\*Current Storage:\*\* In-memory Python dictionary



\## Implemented Features



\### Sprint 1 – Core CRUD API



\- Create new code snippets.

\- Retrieve all available snippets.

\- Retrieve individual snippets using their IDs.

\- Update existing snippets.

\- Delete snippets.

\- Search snippets by title, programming language, and ID.

\- Validate incoming requests using Pydantic.

\- Handle invalid requests and missing resources using HTTP exceptions.

\- Interactive API documentation through Swagger UI.



\## Getting Started



\### Prerequisites



\- Python 3.10 or later

\- pip



\### Installation



Clone the repository:



```bash

git clone https://github.com/Sumit-101105/DevVaultAPI.git

```



Navigate into the project directory:



```bash

cd DevVaultAPI

```



Install dependencies:



```bash

pip install -r requirements.txt

```



\### Run the Application



```bash

python -m uvicorn app.main:app --reload

```



The API will be available at:



`http://127.0.0.1:8000`



\### API Documentation



Once the application is running, access the interactive Swagger documentation:



`http://127.0.0.1:8000/docs`



You can also access the ReDoc documentation at:



`http://127.0.0.1:8000/redoc`



\## Development Roadmap



| Sprint | Planned Development | Status |

|---|---|---|

| Sprint 1 | Core CRUD operations and snippet management | Completed |

| Sprint 2 | Database integration and persistent storage | Planned |

| Sprint 3 | User authentication and authorization | Planned |

| Sprint 4 | Security improvements and advanced functionality | Planned |

| Sprint 5 | Automated testing, documentation, and deployment | Planned |



\## Current Limitations



\- Data is currently stored in memory and is lost when the application restarts.

\- User authentication has not yet been implemented.

\- Database persistence is planned for a future sprint.



\## Project Status



\- \*\*Current Version:\*\* v0.1.0

\- \*\*Current Milestone:\*\* Sprint 1 Completed



This project is actively under development.



\## Author



\*\*Sumit\*\*



GitHub: \[Sumit-101105](https://github.com/Sumit-101105)

