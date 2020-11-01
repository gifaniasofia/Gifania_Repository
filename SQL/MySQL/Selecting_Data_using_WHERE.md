This guide indicates that whenever the data we select need to meet certain criteria (specified using a "WHERE" clause), we specify those criteria after we have specified where the data come from.   

Let's say we want to know which Dognition customers received access to Dognition's first four tests for free.  These customers have a 1 in the "free_start_user" column of the users table.  The syntax you would use to select the data for these customers would be:

```mySQL
SELECT user_guid
FROM users
WHERE free_start_user=1;
```
(Note: user_guid is the field that specifies the unique User ID number of each customer in the users table)

If you wanted to double-check that the outputted data indeed met the criteria you specified, you could include a second column in your output that would give you the value in the free_start_user field for each row of the output: 

```mySQL
SELECT user_guid, free_start_user
FROM users
WHERE free_start_user=1;
```

Try this on your own below.  Remember to use %%sql to indicate that your query will span multiple lines, and consider whether you would like to limit the number of results you ouput using the syntax we learned last lesson.  If you do use a LIMIT statement, remember that it has to be the last item in your query, so this time you will place it after your WHERE statement instead of after your FROM statement.
