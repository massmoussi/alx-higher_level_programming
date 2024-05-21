-- compute the nmber of occurence of certain scre
SELECT score, count(*) AS number FROM second_table GROUP BY score ORDER by number DESC;
