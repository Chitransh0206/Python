# Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Enter your post: ")
# Check if the post contains the word "Harry"


# if ("Harry" or "harry" in post):
#     print("The post is talking about Harry.")

if ("Harry".lower() in post.lower()):      #THIS IS SAME AS ABOVE COMMENTED ONE
    print("The post is talking about Harry.")

else:
    print("The post is not talking about Harry.")    