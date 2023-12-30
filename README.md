# fantasy-front
A streamlit frontend for fantasy NWSL

# TODOs

- read from rosters sheet to populate dropdown lists for each week (would make it so much easier to set lineups without needing multiple tabs open!)
- actually implement the functionality to add new weeks     
    - will have to check that there is no break, i.e. we need the calendar
    - have it name the sheets automatically 
    - format can be created using dataframes
- add way to add players from the pool to a managers roster and viceversa
    - could eventually add way for players to trade
- would be cool to eventually add OAuth so we can validate that managers are who they say they are
    - since we are all friends and this is 100% a toy I am happy to start with a simple passphrase

# learnings + things to research

- the streamlit connection does not allow one to view the list of spreadsheets apparently. Not a huge fan of my current implementation but I wanted to get basic read/write functionality done quickly
