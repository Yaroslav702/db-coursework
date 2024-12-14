INSERT INTO User (user_name, user_lastname, user_password) 
VALUES 
('John', 'Doe', 'hashed_password_1'),
('Jane', 'Smith', 'hashed_password_2'),
('Alice', 'Johnson', 'hashed_password_3');

INSERT INTO Role (role_name, user_role, role_description) 
VALUES 
('Admin', 1, 'Administrator role with full permissions'),
('Editor', 2, 'Editor role with content management permissions'),
('Viewer', NULL, 'Viewer role with read-only access');

INSERT INTO Permission (name_of_permission, description_of_permission, role_permission) 
VALUES 
('View Content', 'Allows viewing of all content', 3),
('Edit Content', 'Allows editing existing content', 2),
('Manage Users', 'Allows managing user accounts', 1),
('Delete Content', 'Allows deletion of content', 1);

INSERT INTO Result (result_name, result_description) 
VALUES 
('Completed', 'The survey was successfully completed'),
('In Progress', 'The survey is still being filled out'),
('Failed', 'The survey submission failed');

INSERT INTO Survey (survey_name, survey_description, survey_result, survey_user) 
VALUES 
('Customer Satisfaction Survey', 'Survey about customer satisfaction', 1, 1),
('Employee Feedback Survey', 'Collecting feedback from employees', 2, 2),
('Website Usability Survey', 'Survey to evaluate website usability', NULL, 3);
