INSERT INTO departments (name, description) VALUES
('Department of Computer Science', 'Offers undergraduate and master degrees in software engineering, networks, distributed systems, and artificial intelligence.'),
('Department of Mathematics', 'Focuses on pure and applied mathematics, probability, statistics, and operational research.'),
('Department of Physics', 'Covers fundamental physics, energetics, materials science, and radiation physics.'),
('Department of Process Engineering', 'Specializes in chemical engineering, pharmaceutical processes, environmental engineering, and polymers.'),
('Department of Electrical and Electronic Engineering', 'Provides training in automation, telecommunications, power systems, and embedded electronics.');

INSERT INTO announcements (title, the_content, pubmication_date) VALUES
('2026/2027 Academic Year Registration', 'Pedagogical and administrative registration for Licence and Master students at the Faculty of Sciences is now open via the Progres platform.', '2026-09-10'),
('First Semester Exam Schedule', 'The official timetable for the first semester exams has been published. Students are required to check their assigned amphitheaters and bring their student ID cards.', '2026-11-18'),
('Call for PFE Graduation Project Proposals', 'Final-year L3 and M2 students must submit their graduation project themes signed by their academic supervisors before the end of the month.', '2026-11-12'),
('Scientific Workshop on Artificial Intelligence', 'The Department of Computer Science is hosting a hands-on seminar on distributed AI and big data next Tuesday at the main auditorium.', '2026-11-15');

INSERT INTO admins (username, password_hash) VALUES
    ('admin', 'scrypt:32768:8:1$gGgXaQO6YsIRnC6J$6a1b27b504db64bcfca7d8f41d6cad5da736afa3322a28d7458e66fab000016455cdc7a5e134a6b008d9b7656eaac9e993f645d4bfbc8f90c25f28c6ffe352f6');