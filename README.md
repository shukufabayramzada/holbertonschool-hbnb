# holbertonschool-hbnb
# HBnB Evolution Project: Part 1 Guide 🏠

Welcome to the HBnB Evolution Project, where we embark on creating a web application inspired by AirBnB using Python and Flask!

## Project Overview 🌟

HBnB Evolution aims to replicate the functionality of AirBnB, allowing users to list places for rent, write reviews, and search for accommodations. This first part focuses on laying the foundation for our application's backend, including data modeling, API development, and testing.

## What’s Cooking in Part 1? 🍳

### Sketching with UML:
Start by sketching out the application's backbone using UML (Unified Modeling Language) to create a blueprint for how our classes and components will interact. This step is crucial for visualizing the structure and relationships between different parts of our application.

### Our UML diagram
  [UML diagram](https://lucid.app/lucidchart/b0c8979c-33fd-4881-91bd-46c56fea7709/edit?viewport_loc=-1692%2C1310%2C4348%2C1970%2C0_0&invitationId=inv_538f1d49-4af1-4f3e-9614-af9b030738a7)

### If you want to check is as image:
![UML diagram for_our project](https://github.com/shukufabayramzada/holbertonschool-hbnb/blob/main/UML%20diagram%20for%20hbnb%20project.jpeg)

### Testing Our Logic:
Ensure everything works smoothly by creating comprehensive tests for the API endpoints and business logic. We utilize tools like `unittest` in Python to automate testing and ensure reliability throughout the development process.

### Building the API:
Implement the API using Flask, a lightweight and versatile web framework for Python. The API will serve as the interface for our application, handling HTTP requests and responses. Routes will be designed to support CRUD operations (Create, Read, Update, Delete) for entities such as places, users, reviews, and amenities.

### File-Based Data Storage:
Begin with a file-based system to store data, choosing between text, JSON, XML, or other formats. While this approach simplifies initial development and testing phases, future iterations will transition to a more robust database solution (e.g., PostgreSQL, MySQL) to handle scalability and data integrity requirements.

### Packaging with Docker:
Wrap up the project by packaging everything into a Docker image. Docker containers provide a consistent environment for running applications, ensuring portability and ease of deployment across different platforms and environments.

## The Three Layers of Our API Cake 🍰

- **Services Layer:** Handles incoming requests and outgoing responses via the API. It acts as the interface between the client and the application's core logic.
  
- **Business Logic Layer:** Core processing and decision-making component of the application. Here, rules such as user authentication, data validation, and business workflows are implemented.
  
- **Persistence Layer:** Initially file-based, storing and retrieving data for the application. This layer interacts directly with the storage mechanism (e.g., files) to manage the application's data.

## The Data Model: Key Entities 📝

### Places:
Places are the core entities of our application, representing accommodations available for rent. Each place includes attributes such as:
- Name, description
- Address, city, latitude, longitude
- Host (owner)
- Number of rooms, bathrooms
- Price per night, max guests
- Amenities (features like Wi-Fi, pools)
- Reviews (user feedback and ratings)

### Users:
Users are individuals interacting with the application, categorized as hosts (owners of places) or reviewers (users leaving reviews). Key attributes include:
- Email (unique identifier)
- Password
- First name, last name

### Reviews:
User-generated feedback and ratings for places. Each review contains:
- Rating (e.g., 1-5 stars)
- Comment
- Date of submission

### Amenities:
Features available in places, such as Wi-Fi, pools, etc. Users can select from a predefined catalog or add new amenities as needed.

### Country and City:
Places are associated with cities, and each city belongs to a country. This hierarchical structure facilitates categorization and search functionalities within the application.

## Business Logic: Rules to Live By 📏

- **Unique Users:** Each user is uniquely identified by their email address.
  
- **One Host per Place:** Every place must have exactly one designated host.
  
- **Flexible Hosting:** A user can be a host for multiple places or none at all.
  
- **Open Reviewing:** Users can submit reviews for places they do not own.
  
- **Amenity Options:** Places can have multiple amenities from a predefined catalog, and users can contribute new amenities to expand the catalog.
  
- **City-Country Structure:** Places are categorized under cities, and cities are associated with countries. This hierarchical organization supports efficient categorization and searching of places.

## Essential Attributes for Every Entity 🌟

- **Unique ID (UUID4):** Globally unique identifier for each entity, ensuring no overlap or ambiguity in data identification.
  
- **Creation Date (`created_at`):** Timestamp indicating when an object was created, essential for auditing and data lifecycle management.
  
- **Update Date (`updated_at`):** Timestamp recording the last modification made to an object, aiding in tracking data changes and maintaining accuracy over time.

## Why These Attributes Matter? 🧩

- **Uniqueness:** UUID4 ensures each entity is distinct, crucial for scalable and reliable data management.
  
- **Traceability:** `created_at` and `updated_at` timestamps provide a clear audit trail of entity lifecycle, facilitating debugging, auditing, and user interaction analysis.

## Testing 🧪

- Comprehensive testing is conducted using tools such as `curl` and HTTP methods (`PUT`, `GET`, `POST`, `DELETE`) to verify API functionality and behavior.
  
- Unit testing with `unittest` ensures individual components of the application like models function correctly, maintaining reliability and stability throughout development.

## Team 👥

  **Members:**
[Shukufa Bayramzada](https://github.com/shukufabayramzada)
[Simara Rustam](https://github.com/simararustam)
  
  **Collaboration:**
  Our team works collaboratively to design, develop, and test the HBnB Evolution Project, ensuring a cohesive and effective implementation.

## Data Storage 🗄️

- **Type:**
  File-based (initially)

- **Storage Format:**
  Utilizes text, JSON, or XML files to store application data during early development stages. Future iterations will incorporate database solutions for enhanced scalability and performance.

## Contributing 🤝

We welcome contributions to the HBnB Evolution Project! To contribute, follow these steps:

1. **Clone the repository:**
`git clone https://github.com/shukufabayramzada/holbertonschool-hbnb.git`
`cd holbertonschool-hbnb`

2. **Create a new branch:**
`git checkout -b feature/your-feature-name`

3. **Make your changes and commit:**
`git add .`
`git commit -m "Your commit message here"`

4. **Push to your branch:**
`git push origin feature/your-feature-name`

5. **Submit a pull request:** 
Go to the repository on GitHub and submit a pull request from your branch to `main`. Provide a clear description of your changes, why they are needed, and any considerations for reviewers.

6. **Discuss and iterate:** 
Participate in discussions and address any feedback or changes requested by the maintainers. Once approved, your pull request will be merged, and your contributions 
will be part of HBnB Evolution!

## Requirements 📋

- **Dependencies:**
- All required packages are listed in `requirements.txt`. Install these dependencies using
  ```
  pip install -r requirements.txt
  ```
to set up the development environment.

