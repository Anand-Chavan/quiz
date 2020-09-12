DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Question;
DROP TABLE IF EXISTS Question_choices;
DROP TABLE IF EXISTS User_question_answer;


CREATE TABLE Users
	(
		user_id    integer ,
   		regtime    datetime,
   		username   varchar(100),
   		useremail  varchar(100),
   		userpass   varchar(100),
		PRIMARY KEY (user_id)
   	);

CREATE TABLE Question
	(
   		question_id   integer,
   		question      varchar(20),
   		is_active     integer,
		PRIMARY KEY (question_id)
   	);



CREATE TABLE  Question_choices
	(
		choice_id    integer,
		question_id  integer,
		is_right_choice  integer,		
		choice           varchar(20),
		PRIMARY KEY (choice_id),
		FOREIGN KEY (question_id) REFERENCES Question(question_id)
    );


CREATE TABLE User_question_answer
	(
		user_id      integer,
		question_id  integer,
		choice_id    integer,
		is_right     integer,
		answer_time  datetime,
		FOREIGN KEY (question_id) REFERENCES Question(question_id),
		FOREIGN KEY (user_id) REFERENCES Users(user_id),
		FOREIGN KEY (choice_id) REFERENCES Question_choices(choice_id)


   	)