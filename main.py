from filter import filter_user_data

# URLs for GET requests
postsURL = "https://jsonplaceholder.typicode.com/posts"
todosURL = "https://jsonplaceholder.typicode.com/todos"
usersURL = "https://jsonplaceholder.typicode.com/users"
    
filter_user_data(postsURL, todosURL, usersURL)
