# Travel Planner API

A robust travel management system built with **Django REST Framework**. This application allows travelers to plan trips, import locations from the **Art Institute of Chicago API**, and track their progress with built-in business logic constraints.

##  Key Features

- **Project Management**: Full CRUD operations for managing travel projects.
- **Third-Party API Integration**: Real-time validation of `external_id` against the Art Institute of Chicago API.
- **Advanced Business Logic**:
  - **Auto-Completion**: Projects are automatically marked as `is_completed` when all associated places are visited.
  - **Deletion Protection**: Projects with at least one visited place cannot be deleted (returns `400 Bad Request`).
  - **Smart Constraints**: Maximum of 10 places per project.
  - **Duplicate Prevention**: Prevents adding the same `external_id` to the same project.
- **Bonus Features**:
  - Full **Docker** & **Docker Compose** configuration for easy deployment.
  - Filtering for projects (e.g., `?is_completed=true`).
  - Pagination for list endpoints.

##  Tech Stack

- **Backend**: Python 3.13, Django 4.2, Django REST Framework
- **Database**: SQLite
- **Containerization**: Docker, Docker Compose
- **Third-party API**: Art Institute of Chicago

##  Getting Started with Docker

To run the project locally in a few seconds:

1. Clone this repository.
2. Ensure you have Docker and Docker Compose installed.
3. Run the following command in the project root:
   ```bash
   docker-compose up --build
4. The API will be available at: `http://localhost:8000/api/projects/`
5. Admin Panel: `http://localhost:8000/admin/`

The API can be tested directly in the browser using the **Django REST Framework Browsable API**:
1. Open `http://localhost:8000/api/projects/` to view the list and use the POST form.
2. Use the **Raw data** tab to send JSON payloads for nested objects.
3. Use the URL parameters like `?is_completed=true` to test filtering.