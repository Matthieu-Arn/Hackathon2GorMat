<h1 align="center">Lost and Found</h1>

The Campus Lost & Found platform aims to help students and staff easily report, search for, and recover lost items on campus. The platform streamlines the process of connecting individuals who have lost belongings with those who may have found them, ensuring quick and effective item recovery.

Target Audience:
- Students: Those who have lost items and want to report them or search for found items.
- Finders: Individuals who have found items and want to report them to return to the rightful owner.
- Campus Administration: Admins can monitor reports, moderate activity, and assist in the recovery of valuable or sensitive items.


[Live project](https:///)

Admin Username: 

Password: 

[Project Board](https://)

## User Experience (UX)

### User Stories

#### User Story 1:  

- As a student, I want to create an account so I can report lost or found items.

- Acceptance Criteria:

  1. The user can fill out a form with details about the lost item (description, date, location) and submit it. 

#### User Story 2: 

- As a student, I want to report a lost item so I can try to recover it quickly.

- Acceptance Criteria:

  1. The user can fill out a form with details about the lost item (description, date, location) and submit it.

#### User Story 3: 

- As a student, I want to report a found item so that it can be returned to the owner.

- Acceptance Criteria:

  1. The user can submit details about the found item (item_name, date, location) via a form.
 
#### User Story 4: 

- As a student, I want to search for lost or found items so I can see if my lost item has been reported (nice-to-have feature).

- Acceptance Criteria:

  1. The user can search and filter items by keyword.

#### User Story 5:

- As a student, I want to receive a notification when an item matching my lost item description is reported as found (nice-to-have feature).

- Acceptance Criteria:

  1. The user receives an email notification or platform notification when an item with similar characteristics is reported.

#### User Story 6: 

- As a user, I want to message the finder of a reported item so I can coordinate returning the lost item.
  
- Acceptance Criteria:

  1. The user can send and receive private messages to the person who posted a lost or found report.

#### User Story 7: 

- As a student, I want to mark my lost item as recovered once it has been found.
  
- Acceptance Criteria:

  1. The user can update the status of their lost item report to “recovered” once they’ve gotten it back.

#### User Story 8: 

- As an admin, I want to moderate posts so that inappropriate or false reports are removed.

- Acceptance Criteria:

  1. Admins can view, edit, or delete reports to ensure quality control and prevent misuse of the platform.


### Accessibility 

## Design

### Colour Scheme 

### Typography

### Imagery

### Wireframes

### Existing Features 

#### Home Page

- Hero Section: 

- Navigation Bar: 

- Footer: Contains links to  social media profiles.
  
#### Other pages

### Future Features

## Data Models

### Item Model:

<img width="319" alt="Item_Model_Table" src="https://github.com/user-attachments/assets/eb64eb9a-98e8-4bf1-9694-93b71eafd149">

### Comment Model:

<img width="317" alt="Comment_Model_Table" src="https://github.com/user-attachments/assets/f2cc923f-22ac-4553-95dc-9d7574bef8e6">

### User Model:

<img width="476" alt="User_Model_Table" src="https://github.com/user-attachments/assets/3725fd94-1f40-48cb-99c3-89c983378691">

- The User model is provided by Django.

### Relationships:

#### User <-> Item:

- A one-to-many relationship where a user can report multiple items (either lost or found).

- id in the User model references user_id in the Item model.

#### User <-> Comment:

- A one-to-many relationship where a user can post multiple comments, but each comment is associated with only one user.

- 	id in the User model references user_id in the Comment model.

 #### Item <-> Comment:

- A one-to-many relationship where each item can have multiple comments, stored in the comment-content field in the Item model. Each item (identified by item_id) can have multiple comments stored in comment_content.

- id in the Item model references item_id in the Comment model

### ER Diagram

![ERD](https://github.com/user-attachments/assets/bca66b30-91f3-4826-87a8-65385c85d83d)

## Technologies Used 

## Agile Methodology 

[Project Board](https://)

Agile methodology was implemented throughout the development of this project, providing an iterative and flexible approach to software development.

The process was structured using GitHub’s Project Board, which employed a Kanban-style system to manage the user stories and their progress.

## Deployment

## Testing

### Validation of HTML, CSS, JS, and Python Code
Validation tools used are [Nu HTML Checker](https://validator.w3.org/nu/), [Jigsaw](https://jigsaw.w3.org/css-validator/), [JSHint](https://jshint.com/), [PEP8 codeInst](https://pep8ci.herokuapp.com) and [Python Syntax Checker](https://extendsclass.com/python-tester.html).

#### HTML Validation

#### CSS Validation

#### Javascript Validation

#### Python Validation

### Manual Testing 

### Responsive Design

### Cross-Browser Compatibility Testing

The website was tested across multiple web browsers, including Chrome, Edge, and Firefox, to ensure cross-browser compatibility. All features, including navigation, user interactions, and responsiveness, performed as expected, with no display or functionality issues observed. This confirms that the website delivers a consistent user experience across these major browsers.

## Credits 




