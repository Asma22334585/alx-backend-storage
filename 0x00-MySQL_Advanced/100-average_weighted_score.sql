--creates a stored procedure 
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
     SET weight_average_score = (
	SELECT SUM(score * weight) / SUM(weight)
	FROM users AS user
	JOIN corrections AS corr 
	ON user.id = corr.user_id
	JOIN projects AS pro
	On corr.project_id = pro.id
	WHERE user.id = user_id
    );
    UPDATE users
    SET average_score = weight_average_score
    WHERE id = user_id;
END //
DELIMITER ;
